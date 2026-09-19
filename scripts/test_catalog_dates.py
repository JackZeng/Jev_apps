"""Regression checks for publishing a bilingual increment across Beijing midnight."""
import copy
import json
from pathlib import Path
import unittest

from build_catalog import generate
from catalog_en import generate_en

ROOT = Path(__file__).resolve().parents[1]


class CrossDayPublishing(unittest.TestCase):
    def setUp(self):
        self.d = json.loads((ROOT / 'data/catalog.json').read_text())
        self.en = json.loads((ROOT / 'data/catalog.en.json').read_text())
        self.old = copy.deepcopy(next(c for c in self.d['cases'] if c['slug'] == 'stagehand'))
        self.new = copy.deepcopy(self.old)
        self.new.update(slug='midnight-regression', readme_added_at='2027-01-01T16:01:02+00:00',
                        readme_updated_at='2027-01-01T16:01:02+00:00')
        # Keep the real homepage's featured references while adding the midnight case.
        self.d['cases'] = [self.old, self.new] + [
            c for c in self.d['cases'] if c['slug'] != self.old['slug']
        ]
        self.d['updates'] = [dict(reviewed_at='2027-01-01T16:00:01+00:00',
                                  new_cases=[self.new['slug']], updated_cases=[])]
        self.d['latest_update'] = self.d['updates'][-1]
        self.en['cases'][self.new['slug']] = copy.deepcopy(self.en['cases'][self.old['slug']])

    def test_bilingual_paths_and_timestamps_survive_midnight(self):
        before = copy.deepcopy(self.d)
        for english, files in [(False, generate(self.d)), (True, generate_en(self.d, self.en))]:
            suffix = '.en' if english else ''
            old_path = f'cases/2026-09-18-stagehand/README{suffix}.md'
            new_path = f'cases/2027-01-02-midnight-regression/README{suffix}.md'
            self.assertIn(old_path, files)
            self.assertIn(new_path, files)
            self.assertNotIn(f'cases/2026-09-18-midnight-regression/README{suffix}.md', files)
            self.assertIn(new_path, files[f'README{suffix}.md'])
            self.assertIn('2027-01-02', files[f'README{suffix}.md'])
            self.assertIn('2027-01-02 00:01:02', files[new_path])
            self.assertNotIn('2027-01-02', files[old_path])
            self.assertIn('2026-09-18-browser', files[new_path])
        self.assertEqual(before, self.d, 'Generating pages must not mutate recorded dates')

    def test_source_refresh_keeps_first_collection_path(self):
        self.d['latest_update']['updated_cases'] = [self.old['slug']]
        for suffix, files in [('', generate(self.d)), ('.en', generate_en(self.d, self.en))]:
            path = f'cases/2026-09-18-stagehand/README{suffix}.md'
            self.assertIn(path, files)
            self.assertIn('2027-01-02', files[path])
            self.assertNotIn('cases/2027-01-02-stagehand', '\n'.join(files))
        self.assertEqual(self.old['readme_added_at'], self.d['cases'][0]['readme_added_at'])


if __name__ == '__main__':
    unittest.main()
