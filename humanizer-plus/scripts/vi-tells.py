#!/usr/bin/env python3
"""Flag Vietnamese AI-writing tells listed in languages/vi.md.

Usage: vi-tells.py [--json] [--patterns PATH] [--doctype DOCTYPE] [--include-quotes] FILE... | -

A finding is a prompt to reread the passage, never an order to delete it.
Exit codes: 0 no findings, 1 findings, 2 usage or catalogue error.
Standard library only; Python 3.9 or later.
"""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

DEFAULT_PATTERNS = Path(__file__).resolve().parent.parent / 'patterns' / 'vi-tells.json'
DOCTYPES = ('prose', 'ui', 'handoff', 'marketing')
KINDS = ('regex', 'density', 'manual')
STRENGTHS = ('strong', 'medium', 'weak')
REQUIRED = ('id', 'name', 'kind', 'scope', 'strength', 'regex', 'why', 'fix', 'examples', 'source')
ID_RE = re.compile(r'^VI-\d\d[a-z]?$')

MASKS = [
    re.compile(r'\A---\n.*?\n---[ \t]*(?:\n|\Z)', re.S),          # YAML frontmatter
    # fenced code: up to 3 spaces of indent (list items too); the closing fence uses
    # the same character and is at least as long; an unclosed fence runs to the end;
    # a backtick in the info string means inline code, not a fence (CommonMark)
    re.compile(r'^ {0,3}(?P<f>(?P<c>[`~])(?P=c){2,})[^`\n]*(?:\n.*?)??'
               r'(?:\n {0,3}(?P=f)(?P=c)*[ \t]*$|\Z)', re.S | re.M),
    # inline code: the closing run of backticks matches the opening run's length
    re.compile(r'(?<!`)(?P<t>`+)(?!`)(?:(?!\n[ \t]*\n).)+?(?<!`)(?P=t)(?!`)', re.S),
    re.compile(r'(?:https?://|www\.)[^\s<>()]+'),                 # URLs
    re.compile(r'(?<![\w/])(?:~|\.{1,2})?/(?:[\w.-]+/)*[\w.-]+'),  # absolute or ./ paths
    re.compile(r'(?<![\w/])[\w.-]+/[\w./-]*\.\w{1,6}\b'),         # relative paths with extension
    re.compile(r'<[^>\n]+>'),                                     # HTML tags
]
QUOTE_MASKS = [
    re.compile(r'^[ \t]*>[^\n]*$', re.M),                         # blockquote lines
    re.compile(r'“[^“”]*”'),                                      # quoted speech, any length
]


FILL = '\u2591'  # masked text: not a letter, digit, space or punctuation mark


class CatalogueError(Exception):
    pass


def nfc(text):
    return unicodedata.normalize('NFC', text)


def compile_entry(entry):
    flags = 0
    if entry.get('ignore_case'):
        flags |= re.IGNORECASE
    if entry.get('multiline'):
        flags |= re.MULTILINE
    regex = entry['regex'] if entry.get('raw') else nfc(entry['regex'])
    return re.compile(regex, flags)


def load_catalogue(path=DEFAULT_PATTERNS):
    """Load and validate the catalogue; raise CatalogueError on any problem."""
    try:
        data = json.loads(Path(path).read_text('utf-8'))
    except (OSError, ValueError) as exc:
        raise CatalogueError(f'cannot read {path}: {exc}')
    scopes = data.get('scopes', {})
    seen, compiled, errors = set(), [], []
    for entry in data.get('patterns', []):
        pid = entry.get('id', '?')
        missing = [key for key in REQUIRED if key not in entry]
        if missing:
            errors.append(f'{pid}: missing {", ".join(missing)}')
            continue
        if not ID_RE.match(pid):
            errors.append(f'{pid}: id must look like VI-NN or VI-NNa')
        if pid in seen:
            errors.append(f'{pid}: duplicate id')
        seen.add(pid)
        if entry['kind'] not in ('regex', 'density'):
            errors.append(f'{pid}: kind must be regex or density in patterns')
        if entry['strength'] not in STRENGTHS:
            errors.append(f'{pid}: strength must be one of {STRENGTHS}')
        if entry['scope'] not in scopes:
            errors.append(f'{pid}: unknown scope {entry["scope"]}')
        if entry['kind'] == 'density' and not isinstance(entry.get('per_1000_words'), (int, float)):
            errors.append(f'{pid}: density pattern needs per_1000_words')
        examples = entry['examples']
        if not isinstance(examples, dict) or not all(
                isinstance(examples.get(key, []), list) for key in ('hit', 'miss')):
            errors.append(f'{pid}: examples must hold hit and miss lists')
        try:
            compiled.append((entry, compile_entry(entry)))
        except re.error as exc:
            errors.append(f'{pid}: regex does not compile: {exc}')
    for entry in data.get('manual', []):
        if entry.get('kind') != 'manual' or not ID_RE.match(entry.get('id', '')):
            errors.append(f'{entry.get("id", "?")}: manual entries need kind manual and a VI id')
        if entry.get('id') in seen:
            errors.append(f'{entry.get("id")}: duplicate id')
        seen.add(entry.get('id'))
    if errors:
        raise CatalogueError('\n'.join(errors))
    data['_compiled'] = compiled
    data['_weights'] = data.get('scoring', {}).get('weights', {'strong': 3, 'medium': 2, 'weak': 1})
    data['_threshold'] = data.get('scoring', {}).get('cluster_threshold', 3)
    return data


def mask(text, include_quotes=False):
    """Replace regions that are not prose with FILL, keeping offsets and line breaks.

    FILL instead of spaces keeps a masked quote or code span from looking like
    a stray space before the punctuation that follows it.

    Each pattern runs on the text already masked by the ones before it, so a
    backtick or quote inside code cannot open a span that reaches into prose.
    """
    chars = list(text)
    for pattern in MASKS + ([] if include_quotes else QUOTE_MASKS):
        for match in pattern.finditer(''.join(chars)):
            for i in range(match.start(), match.end()):
                if chars[i] != '\n':
                    chars[i] = FILL
    return ''.join(chars)


def paragraph_starts(text):
    starts = [0]
    for match in re.finditer(r'\n[ \t]*\n\s*', text):
        starts.append(match.end())
    return starts


def locate(text, offset):
    line = text.count('\n', 0, offset) + 1
    col = offset - (text.rfind('\n', 0, offset) + 1) + 1
    return line, col


def lint(text, catalogue, doctype='prose', include_quotes=False, path='-'):
    """Return {"file", "findings", "clusters", "summary"} for one text."""
    raw = text
    text = nfc(raw)
    masked = mask(text, include_quotes)
    masked_raw = mask(raw, include_quotes)
    words = len(re.findall(r'[^\s' + FILL + r']+', masked))
    enabled = {'any', doctype}
    starts = paragraph_starts(text)
    findings = []
    for entry, regex in catalogue['_compiled']:
        if entry['scope'] not in enabled:
            continue
        source = masked_raw if entry.get('raw') else masked
        matches = list(regex.finditer(source))
        if not matches:
            continue
        if entry['kind'] == 'density':
            rate = len(matches) * 1000 / max(words, 1)
            if rate < entry['per_1000_words']:
                continue
            matches = matches[:1]
        for match in matches:
            if entry.get('raw'):
                line = raw.count('\n', 0, match.start()) + 1
                col = match.start() - (raw.rfind('\n', 0, match.start()) + 1) + 1
                offset = len(nfc(raw[:match.start()]))
                snippet = nfc(raw[match.start():match.end() + 1]).strip()
            else:
                line, col = locate(text, match.start())
                offset = match.start()
                snippet = text[match.start():match.end()]
            para = sum(1 for s in starts if s <= offset) - 1
            findings.append({
                'path': path, 'line': line, 'col': col, 'id': entry['id'],
                'strength': entry['strength'], 'match': snippet[:120],
                'why': entry['why'], 'fix': entry['fix'], 'paragraph': para,
                'weight': catalogue['_weights'][entry['strength']],
            })
    findings.sort(key=lambda f: (f['line'], f['col'], f['id']))
    by_para = {}
    for item in findings:
        by_para.setdefault(item['paragraph'], []).append(item)
    clusters = []
    for para, items in sorted(by_para.items()):
        score = sum(item['weight'] for item in items)
        if score >= catalogue['_threshold']:
            clusters.append({'paragraph': para, 'line': items[0]['line'], 'score': score,
                             'ids': sorted({item['id'] for item in items})})
    clusters.sort(key=lambda c: -c['score'])
    summary = {
        'words': words,
        'paragraphs': len(starts),
        'findings': len(findings),
        'clusters': len(clusters),
        'by_strength': {s: sum(1 for f in findings if f['strength'] == s) for s in STRENGTHS},
        'doctype': doctype,
    }
    return {'file': path, 'findings': findings, 'clusters': clusters, 'summary': summary}


def print_text(result, out):
    for item in result['findings']:
        out.write(f'{item["path"]}:{item["line"]}:{item["col"]} {item["id"]} {item["strength"]} '
                  f'"{item["match"]}" {item["why"]}\n')
    summary = result['summary']
    out.write(f'{result["file"]}: {summary["clusters"]} cluster(s), {summary["findings"]} finding(s), '
              f'{summary["words"]} words\n')
    for cluster in result['clusters']:
        out.write(f'  cluster {result["file"]}:{cluster["line"]} score {cluster["score"]}: '
                  f'{", ".join(cluster["ids"])}\n')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('files', nargs='+', help='files to lint, or - for stdin')
    parser.add_argument('--json', action='store_true', help='print JSON')
    parser.add_argument('--patterns', default=str(DEFAULT_PATTERNS), help='catalogue path')
    parser.add_argument('--doctype', choices=DOCTYPES, default='prose',
                        help='enables that scope in addition to "any" (default prose)')
    parser.add_argument('--include-quotes', action='store_true',
                        help='also lint blockquotes and text inside “ ”')
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        return 2 if exc.code else 0
    try:
        catalogue = load_catalogue(args.patterns)
    except CatalogueError as exc:
        sys.stderr.write(f'catalogue error:\n{exc}\n')
        return 2
    results = []
    for name in args.files:
        try:
            text = sys.stdin.read() if name == '-' else Path(name).read_text('utf-8')
        except (OSError, UnicodeDecodeError) as exc:
            sys.stderr.write(f'cannot read {name}: {exc}\n')
            return 2
        results.append(lint(text, catalogue, args.doctype, args.include_quotes, name))
    if args.json:
        payload = results[0] if len(results) == 1 else results
        json.dump(payload, sys.stdout, ensure_ascii=False, indent=2)
        sys.stdout.write('\n')
    else:
        for result in results:
            print_text(result, sys.stdout)
    return 1 if any(r['findings'] for r in results) else 0


if __name__ == '__main__':
    sys.exit(main())
