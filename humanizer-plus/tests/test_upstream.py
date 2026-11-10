"""Pin, citations, layout and size budgets for humanizer-plus."""
import hashlib
import importlib.util
import json
import os
import re
import subprocess
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
CAPS = {
    'SKILL.md': 8 * 1024,
    'overrides/khang.md': 4 * 1024,
    'languages/vi.md': 24 * 1024,
}
CARD_CAP = 5 * 1024
CARD_HEADINGS = ['## Reader and purpose', '## Structure', '## Length and format',
                 '## Medium tells', '## Vietnamese notes', '## Review checklist', '## Sources']


def load_sync():
    spec = importlib.util.spec_from_file_location('sync_upstream', SKILL / 'scripts' / 'sync-upstream.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def frontmatter(text):
    match = re.match(r'---\n(.*?)\n---\n', text, re.S)
    return match.group(1) if match else ''


def tracked_files():
    """Files git tracks under the skill, or every file when git is unavailable."""
    try:
        result = subprocess.run(['git', '-C', str(SKILL), 'ls-files', '-z', '--', '.'],
                                capture_output=True, check=True)
        names = [n for n in result.stdout.decode('utf-8').split('\0') if n]
        if names:
            return [SKILL / n for n in names]
    except (OSError, subprocess.CalledProcessError):
        pass
    return [p for p in SKILL.rglob('*')
            if p.is_file() or p.is_symlink()
            if '__pycache__' not in p.parts and not p.name.endswith('.pyc')]


class UpstreamTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sync = load_sync()
        cls.pin = json.loads((SKILL / 'UPSTREAM.json').read_text('utf-8'))
        cls.router = (SKILL / 'SKILL.md').read_text('utf-8')

    def test_pin_hashes(self):
        for rel, meta in self.pin['files'].items():
            digest = hashlib.sha256((SKILL / rel).read_bytes()).hexdigest()
            self.assertEqual(digest, meta['sha256'], rel)
        self.assertRegex(self.pin['commit'], r'^[0-9a-f]{40}$')

    def test_check_passes(self):
        self.assertEqual(self.sync.check(SKILL), [])

    def test_citations_resolve(self):
        upstream = (SKILL / 'upstream/humanizer.md').read_text('utf-8')
        self.assertEqual(self.sync.resolve_all(SKILL, upstream), [])

    def test_resolver_catches_bad_citations(self):
        index = self.sync.upstream_index((SKILL / 'upstream/humanizer.md').read_text('utf-8'))
        bad = '[upstream §1 Wrong title] [upstream: No such heading] §99'
        self.assertEqual(len(self.sync.anchor_failures(bad, 'x', index)), 3)
        good = '[upstream §1 Not X but Y] [upstream: How to work] [upstream: File mode] §26'
        self.assertEqual(self.sync.anchor_failures(good, 'x', index), [])

    def test_override_replaces_how_to_work_sentence(self):
        text = (SKILL / 'overrides/khang.md').read_text('utf-8')
        self.assertIn('[upstream: How to work]', text)
        sentence = 'Where the text is generic, add a specific detail you know to be true.'
        self.assertIn(sentence, (SKILL / 'upstream/humanizer.md').read_text('utf-8'))
        self.assertIn(sentence, text)

    def test_single_skill_md(self):
        found = [p for p in SKILL.rglob('SKILL.md')]
        self.assertEqual(found, [SKILL / 'SKILL.md'])

    def test_frontmatter(self):
        meta = frontmatter(self.router)
        self.assertRegex(meta, r'(?m)^name: humanizer-plus$')
        self.assertEqual(SKILL.name, 'humanizer-plus')
        description = re.search(r'(?m)^description: (.+)$', meta).group(1)
        self.assertLessEqual(len(description), 300)
        self.assertIn(f'upstream: "blader/humanizer {self.pin["version"]}"', meta)

    def test_medium_table_matches_cards(self):
        rows = set(re.findall(r'^\| `domains/([\w-]+)\.md` \|', self.router, re.M))
        cards = {p.stem for p in (SKILL / 'domains').glob('*.md')}
        self.assertTrue(rows)
        self.assertEqual(rows, cards)

    def test_card_headings(self):
        for card in sorted((SKILL / 'domains').glob('*.md')):
            lines = card.read_text('utf-8').splitlines()
            self.assertTrue(lines[0].startswith('# '), card.name)
            self.assertTrue(lines[1].startswith('Applies to: '), card.name)
            self.assertTrue(lines[2].startswith('Not for: '), card.name)
            headings = [line for line in lines if line.startswith('## ')]
            self.assertEqual(headings, CARD_HEADINGS, card.name)

    def test_size_caps(self):
        for rel, cap in CAPS.items():
            size = (SKILL / rel).stat().st_size
            self.assertLessEqual(size, cap, f'{rel} is {size} bytes, cap {cap}')
        for card in (SKILL / 'domains').glob('*.md'):
            self.assertLessEqual(card.stat().st_size, CARD_CAP, card.name)

    def test_files_are_utf8_without_symlinks_or_bytecode(self):
        for path in tracked_files():
            rel = path.relative_to(SKILL).as_posix()
            self.assertFalse(path.is_symlink(), rel)
            self.assertNotIn('__pycache__', path.parts, rel)
            self.assertFalse(rel.endswith('.pyc'), rel)
            path.read_bytes().decode('utf-8')

    def test_corpus_not_shipped(self):
        names = {p.name for p in tracked_files()}
        self.assertFalse({n for n in names if re.match(r'^n\d+\.txt$', n)})
        self.assertNotIn('mining-notes.md', names)


if __name__ == '__main__':
    unittest.main()
