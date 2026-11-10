"""Catalogue schema and linter behaviour for scripts/vi-tells.py."""
import importlib.util
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import unicodedata
import unittest
from contextlib import redirect_stdout
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
SCRIPT = SKILL / 'scripts' / 'vi-tells.py'
CATALOGUE = SKILL / 'patterns' / 'vi-tells.json'
CORPUS_ENV = 'HUMANIZER_PLUS_VI_CORPUS'

AGENT_SAMPLE = (
    'Trong bối cảnh công nghệ phát triển không ngừng, việc quản lý tài liệu đóng vai trò '
    'quan trọng. Hơn nữa, hệ thống xử lý yêu cầu một cách nhanh chóng.\n\n'
    'Tóm lại, có thể thấy rằng đây là lựa chọn đáng cân nhắc. Hy vọng bài viết này hữu ích với bạn.\n'
)
PLAIN_SAMPLE = 'Sáng 5/8, nhóm gửi bản nháp cho 12 người đọc thử. Hai người đề nghị bỏ phần mở đầu.\n'


def load_linter():
    spec = importlib.util.spec_from_file_location('vi_tells', SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_cli(*args, stdin=None):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    return subprocess.run([sys.executable, '-B', str(SCRIPT), *args], input=stdin,
                          capture_output=True, text=True, encoding='utf-8', env=env)


class CatalogueTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vt = load_linter()
        cls.cat = cls.vt.load_catalogue(CATALOGUE)

    def test_schema_and_unique_ids(self):
        data = json.loads(CATALOGUE.read_text('utf-8'))
        ids = [e['id'] for e in data['patterns'] + data['manual']]
        self.assertEqual(len(ids), len(set(ids)))
        for entry in data['patterns']:
            for key in self.vt.REQUIRED:
                self.assertIn(key, entry, entry['id'])
            self.assertIn(entry['kind'], ('regex', 'density'))
            self.assertIn(entry['strength'], self.vt.STRENGTHS)
            self.assertIn(entry['scope'], data['scopes'])

    def test_examples(self):
        for entry, regex in self.cat['_compiled']:
            norm = (lambda s: s) if entry.get('raw') else self.vt.nfc
            for hit in entry['examples']['hit']:
                self.assertTrue(regex.search(norm(hit)), f'{entry["id"]} misses its hit: {hit}')
            for miss in entry['examples']['miss']:
                self.assertFalse(regex.search(norm(miss)), f'{entry["id"]} hits its miss: {miss}')

    def test_ids_match_vi_md(self):
        text = (SKILL / 'languages' / 'vi.md').read_text('utf-8')
        defined = set(re.findall(r'\*\*(VI-\d\d)\b', text))
        data = json.loads(CATALOGUE.read_text('utf-8'))
        catalogue = {e['id'][:5] for e in data['patterns'] + data['manual']}
        self.assertEqual(defined, catalogue)

    def test_bad_catalogue_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / 'bad.json'
            bad.write_text(json.dumps({'scopes': {'any': ''}, 'patterns': [
                {'id': 'VI-01', 'name': 'x', 'kind': 'regex', 'scope': 'any', 'strength': 'weak',
                 'regex': '(', 'why': '', 'fix': '', 'examples': {'hit': [], 'miss': []},
                 'source': ''}]}), 'utf-8')
            with self.assertRaises(self.vt.CatalogueError):
                self.vt.load_catalogue(bad)
            self.assertEqual(run_cli('--patterns', str(bad), '-', stdin='x').returncode, 2)


class LinterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vt = load_linter()
        cls.cat = cls.vt.load_catalogue(CATALOGUE)

    def lint(self, text, **kw):
        return self.vt.lint(text, self.cat, **kw)

    def test_agent_sample_clusters(self):
        result = self.lint(AGENT_SAMPLE)
        self.assertEqual(result['summary']['clusters'], 2)
        ids = {f['id'] for f in result['findings']}
        self.assertTrue({'VI-01', 'VI-13', 'VI-21a', 'VI-30a', 'VI-03a', 'VI-03b'} <= ids)

    def test_plain_text_is_clean(self):
        self.assertEqual(self.lint(PLAIN_SAMPLE)['findings'], [])

    def test_nfd_matches_nfc(self):
        nfd = unicodedata.normalize('NFD', AGENT_SAMPLE)
        strip = lambda r: [(f['line'], f['col'], f['id']) for f in r['findings'] if f['id'] != 'VI-56']
        self.assertEqual(strip(self.lint(nfd)), strip(self.lint(AGENT_SAMPLE)))
        self.assertIn('VI-56', {f['id'] for f in self.lint(nfd)['findings']})
        self.assertNotIn('VI-56', {f['id'] for f in self.lint(AGENT_SAMPLE)['findings']})

    def test_masking(self):
        tell = 'hệ thống chạy một cách nhanh chóng'
        text = (f'---\ntitle: {tell}\n---\n\n```\n{tell}\n```\n\nXem `{tell}` tại '
                f'https://example.com/{tell.replace(" ", "-")} và <span title="{tell}">x</span>.\n')
        self.assertEqual(self.lint(text)['findings'], [])
        self.assertTrue(self.lint(f'Hệ thống chạy {tell}.')['findings'])

    def test_quotes_masked_unless_included(self):
        text = f'> Hy vọng bài viết này hữu ích với bạn.\n\nAnh nói: “Hy vọng bài viết này hữu ích.”\n'
        self.assertEqual(self.lint(text)['findings'], [])
        self.assertEqual(len(self.lint(text, include_quotes=True)['findings']), 2)

    def test_masked_quote_is_not_a_space(self):
        self.assertEqual(self.lint('Vụ án “Đưa hối lộ”; “Nhận hối lộ” đã khởi tố.')['findings'], [])

    def test_doctype_scopes(self):
        text = 'Không lưu được. Lưu ảnh thất bại.'
        self.assertNotIn('VI-53', {f['id'] for f in self.lint(text)['findings']})
        self.assertIn('VI-53', {f['id'] for f in self.lint(text, doctype='ui')['findings']})

    def test_density_kind(self):
        data = json.loads(CATALOGUE.read_text('utf-8'))
        data['patterns'] = [{
            'id': 'VI-99', 'name': 'test', 'kind': 'density', 'scope': 'any', 'strength': 'weak',
            'regex': r'\bmột\b', 'ignore_case': True, 'per_1000_words': 100, 'why': 'w', 'fix': 'f',
            'examples': {'hit': [], 'miss': []}, 'source': 'test'}]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'cat.json'
            path.write_text(json.dumps(data, ensure_ascii=False), 'utf-8')
            cat = self.vt.load_catalogue(path)
        dense = self.vt.lint('một hai một ba một', cat)
        sparse = self.vt.lint('một ' + 'chữ ' * 50, cat)
        self.assertEqual(len(dense['findings']), 1)
        self.assertEqual(sparse['findings'], [])

    def test_cli_exit_codes_and_json(self):
        clean = run_cli('-', stdin=PLAIN_SAMPLE)
        self.assertEqual(clean.returncode, 0, clean.stderr)
        dirty = run_cli('--json', '-', stdin=AGENT_SAMPLE)
        self.assertEqual(dirty.returncode, 1, dirty.stderr)
        payload = json.loads(dirty.stdout)
        self.assertEqual(set(payload), {'file', 'findings', 'clusters', 'summary'})
        finding = payload['findings'][0]
        for key in ('path', 'line', 'col', 'id', 'strength', 'match', 'why', 'fix'):
            self.assertIn(key, finding)
        self.assertEqual(run_cli('--no-such-flag', '-').returncode, 2)
        self.assertEqual(run_cli('/no/such/file.md').returncode, 2)

    def test_text_output(self):
        out = run_cli('-', stdin=AGENT_SAMPLE).stdout
        self.assertRegex(out, r'(?m)^-:1:1 VI-01 medium "')
        self.assertIn('2 cluster(s)', out)

    @unittest.skipUnless(os.environ.get(CORPUS_ENV), f'set {CORPUS_ENV} to a folder of n*.txt')
    def test_human_corpus_has_no_clusters(self):
        files = sorted(Path(os.environ[CORPUS_ENV]).glob('n*.txt'))
        self.assertTrue(files, 'corpus folder has no n*.txt files')
        flagged = []
        for path in files:
            result = self.lint(path.read_text('utf-8'), path=path.name)
            flagged += [(path.name, c['line'], c['ids']) for c in result['clusters']]
        self.assertEqual(flagged, [])


if __name__ == '__main__':
    unittest.main()
