#!/usr/bin/env python3
"""Check, diff and apply the vendored blader/humanizer copy.

Usage:
  sync-upstream.py check
  sync-upstream.py diff  --source PATH --ref REF [--out FILE]
  sync-upstream.py apply --source PATH --ref REF

The script has no network code. Fetch tags in the local clone first:
  git -C PATH fetch --tags
"""
import argparse
import difflib
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
PIN = 'UPSTREAM.json'
FILES = {'upstream/humanizer.md': 'SKILL.md', 'upstream/LICENSE': 'LICENSE'}
LAYER_GLOBS = ('SKILL.md', 'overrides/*.md', 'languages/*.md', 'domains/*.md')
PATTERNS = 'patterns/vi-tells.json'

ANCHOR_RE = re.compile(r'\[upstream(?: §(\d+) ([^\]]+)|: ([^\]]+))\]')
BARE_SECTION_RE = re.compile(r'(?<!\[upstream )§(\d+)')
HEADING_RE = re.compile(r'^#{1,6}\s+(.+?)\s*$')
NUMBERED_RE = re.compile(r'^(\d+)\.\s+(.+)$')
BOLD_LABEL_RE = re.compile(r'^(?:\d+\.\s+|[-*]\s+)?\*\*(.+?)\*\*')
VERSION_RE = re.compile(r'^\s*version:\s*"?([^"\s]+)"?', re.M)
WATCH_RE = re.compile(
    r'invent|make (anything|something) up|add(s|ing)? (a |an )?(specific )?(detail|fact)'
    r'|publish|send|post|commit|push|curl|https?://|install|run |execute|token|password',
    re.I)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def strip_code(text):
    """Remove fenced and inline code so syntax examples are not resolved."""
    text = re.sub(r'```.*?```', '', text, flags=re.S)
    return re.sub(r'`[^`\n]*`', '', text)


def upstream_index(text):
    """Return ({number: title}, {heading text}, {bold label}) for upstream text."""
    numbered, headings, labels = {}, set(), set()
    in_code = False
    for line in text.splitlines():
        if line.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        match = HEADING_RE.match(line)
        if match:
            title = match.group(1)
            headings.add(title)
            num = NUMBERED_RE.match(title)
            if num:
                numbered[int(num.group(1))] = num.group(2)
            continue
        match = BOLD_LABEL_RE.match(line)
        if match:
            labels.add(match.group(1).rstrip('.:'))
    return numbered, headings, labels


def anchor_failures(text, where, index):
    """List citations in text that do not resolve against index."""
    numbered, headings, labels = index
    failures = []
    for match in ANCHOR_RE.finditer(text):
        num, title, label = match.groups()
        if num:
            if numbered.get(int(num)) != title.strip():
                failures.append(f'{where}: {match.group(0)} (upstream has '
                                f'§{num} {numbered.get(int(num), "nothing")})')
        else:
            label = label.strip()
            if '<' in label:
                continue
            if label not in headings and label not in labels:
                failures.append(f'{where}: {match.group(0)} not found upstream')
    for match in BARE_SECTION_RE.finditer(text):
        if int(match.group(1)) not in numbered:
            failures.append(f'{where}: §{match.group(1)} is not an upstream section')
    return failures


def layer_texts(skill_dir):
    """Yield (relative path, text) for every file that cites upstream."""
    for pattern in LAYER_GLOBS:
        for path in sorted(skill_dir.glob(pattern)):
            yield path.relative_to(skill_dir).as_posix(), strip_code(path.read_text('utf-8'))
    catalogue = skill_dir / PATTERNS
    if catalogue.exists():
        data = json.loads(catalogue.read_text('utf-8'))
        for entry in data.get('patterns', []) + data.get('manual', []):
            if entry.get('maps_to'):
                yield f'{PATTERNS}#{entry["id"]}', entry['maps_to']


def resolve_all(skill_dir, upstream_text):
    index = upstream_index(upstream_text)
    failures = []
    for where, text in layer_texts(skill_dir):
        failures.extend(anchor_failures(text, where, index))
    return failures


def load_pin(skill_dir):
    return json.loads((skill_dir / PIN).read_text('utf-8'))


def check(skill_dir=SKILL_DIR):
    failures = []
    pin = load_pin(skill_dir)
    for rel, meta in pin['files'].items():
        path = skill_dir / rel
        if not path.exists():
            failures.append(f'{rel}: missing')
        elif sha256(path.read_bytes()) != meta['sha256']:
            failures.append(f'{rel}: sha256 differs from {PIN}')
    upstream = skill_dir / 'upstream/humanizer.md'
    if upstream.exists():
        failures.extend(resolve_all(skill_dir, upstream.read_text('utf-8')))
    return failures


def git_blob(source, commit, name):
    result = subprocess.run(['git', '-C', str(source), 'cat-file', 'blob', f'{commit}:{name}'],
                            capture_output=True)
    return result.stdout if result.returncode == 0 else None


def git_commit(source, ref):
    result = subprocess.run(['git', '-C', str(source), 'rev-parse', '--verify', f'{ref}^{{commit}}'],
                            capture_output=True, text=True)
    if result.returncode != 0:
        raise SystemExit(f'cannot resolve {ref} in {source}: {result.stderr.strip()}')
    return result.stdout.strip()


def sections(text):
    """Split text into {heading: [lines]} with '(preamble)' first."""
    out, current = {'(preamble)': []}, '(preamble)'
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            current = match.group(1)
            out.setdefault(current, [])
        else:
            out[current].append(line)
    return out


def version_of(text):
    match = VERSION_RE.search(text)
    return match.group(1) if match else 'unknown'


def version_key(value):
    return tuple(int(x) for x in re.findall(r'\d+', value)[:3])


def changelog_between(changelog, old, new):
    if not changelog:
        return []
    entries, keep = [], False
    for line in changelog.splitlines():
        match = re.match(r'^##\s+\[?v?(\d+\.\d+\.\d+)', line)
        if match:
            ver = version_key(match.group(1))
            keep = version_key(old) < ver <= version_key(new)
        if keep:
            entries.append(line)
    return entries


def watch_excerpt(line, width=240):
    """Show a long diff line around its first watchlist match."""
    if len(line) <= width:
        return line
    match = WATCH_RE.search(line)
    start = max(1, match.start() - width // 2) if match else 1
    return line[0] + ' ...' + line[start:start + width] + '...'


def diff(skill_dir, source, ref, out=None):
    commit = git_commit(source, ref)
    pin = load_pin(skill_dir)
    old = (skill_dir / 'upstream/humanizer.md').read_text('utf-8')
    new_bytes = git_blob(source, commit, 'SKILL.md')
    if new_bytes is None:
        raise SystemExit(f'SKILL.md not found at {commit}')
    new = new_bytes.decode('utf-8')
    license_new = git_blob(source, commit, 'LICENSE')
    changelog = git_blob(source, commit, 'CHANGELOG.md')

    print(f'old: {pin["version"]} {pin["commit"]}')
    print(f'new: {version_of(new)} {commit}')
    old_license = (skill_dir / 'upstream/LICENSE').read_bytes()
    print('LICENSE: ' + ('unchanged' if license_new == old_license else 'CHANGED, review it'))

    print('\nCHANGELOG entries:')
    for line in changelog_between(changelog.decode('utf-8') if changelog else '',
                                  pin['version'], version_of(new)) or ['(none found)']:
        print('  ' + line)

    old_num, old_heads, _ = upstream_index(old)
    new_num, new_heads, _ = upstream_index(new)
    print('\nHeadings:')
    for num in sorted(set(old_num) | set(new_num)):
        a, b = old_num.get(num), new_num.get(num)
        if a != b:
            print(f'  §{num}: {a or "(none)"} -> {b or "(removed)"}')
    for head in sorted(new_heads - old_heads):
        if not NUMBERED_RE.match(head):
            print(f'  added: {head}')
    for head in sorted(old_heads - new_heads):
        if not NUMBERED_RE.match(head):
            print(f'  removed: {head}')

    print('\nAnchors that would break:')
    for line in resolve_all(skill_dir, new) or ['(none)']:
        print('  ' + line)

    print('\nChanged lines per section:')
    old_sec, new_sec = sections(old), sections(new)
    for head in list(dict.fromkeys(list(old_sec) + list(new_sec))):
        delta = [l for l in difflib.unified_diff(old_sec.get(head, []), new_sec.get(head, []),
                                                 lineterm='', n=0)
                 if l[:1] in '+-' and not l.startswith(('+++', '---'))]
        if delta:
            print(f'  {head}: {len(delta)}')

    print('\nWatchlist (check each against overrides/khang.md):')
    diff_lines = list(difflib.unified_diff(old.splitlines(), new.splitlines(),
                                           'old/SKILL.md', 'new/SKILL.md', lineterm=''))
    hits = [l for l in diff_lines
            if l[:1] in '+-' and not l.startswith(('+++', '---')) and WATCH_RE.search(l)]
    for line in hits or ['(none)']:
        print('  ' + watch_excerpt(line))
    if out:
        Path(out).write_text('\n'.join(diff_lines) + '\n', 'utf-8')
        print(f'\nFull diff written to {out}')
    return 0


def apply(skill_dir, source, ref):
    commit = git_commit(source, ref)
    pin = load_pin(skill_dir)
    blobs = {}
    for rel, name in FILES.items():
        data = git_blob(source, commit, name)
        if data is None:
            raise SystemExit(f'{name} not found at {commit}')
        blobs[rel] = data
    for rel, data in blobs.items():
        (skill_dir / rel).write_bytes(data)
        pin['files'][rel] = {'source': FILES[rel], 'sha256': sha256(data)}
    pin['commit'] = commit
    pin['ref'] = ref
    pin['version'] = version_of(blobs['upstream/humanizer.md'].decode('utf-8'))
    (skill_dir / PIN).write_text(json.dumps(pin, indent=2) + '\n', 'utf-8')
    failures = check(skill_dir)
    for line in failures:
        print(line)
    return 1 if failures else 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('check')
    for name in ('diff', 'apply'):
        cmd = sub.add_parser(name)
        cmd.add_argument('--source', required=True, help='local clone of blader/humanizer')
        cmd.add_argument('--ref', required=True, help='tag or commit to compare')
        if name == 'diff':
            cmd.add_argument('--out', help='also write the full unified diff here')
    args = parser.parse_args(argv)
    if args.command == 'check':
        failures = check()
        for line in failures:
            print(line)
        if not failures:
            print('ok: pin hashes match and every upstream citation resolves')
        return 1 if failures else 0
    if args.command == 'diff':
        return diff(SKILL_DIR, Path(args.source), args.ref, args.out)
    return apply(SKILL_DIR, Path(args.source), args.ref)


if __name__ == '__main__':
    sys.exit(main())
