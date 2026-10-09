"""Regression checks against real Git sources and the report command."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/daily_report.py'


class DailyReportTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / 'source-control-plane'
        self.source.mkdir()
        self.git('init', '-b', 'codex/simplify-development-workflow')
        self.git('config', 'user.name', 'Report Test')
        self.git('config', 'user.email', 'test@example.invalid')
        (self.source / 'tasks').mkdir()
        (self.source / 'tasks/current.md').write_text('Status: PLANNED\n')
        (self.source / 'tasks/plan.md').write_text('Deadline: 2026-11-09\n')
        snapshot = self.source / 'docs/project-progress/snapshots'
        snapshot.mkdir(parents=True)
        (snapshot / 'manifest.json').write_text(json.dumps({
            'captured_at': '2026-10-09T12:00:00+08:00',
            'sources': {'product': {'head': '011c835' + '0' * 33}},
        }))
        self.git('add', '.')
        environment = dict(os.environ, GIT_AUTHOR_DATE='2026-09-28T12:00:00+08:00',
                           GIT_COMMITTER_DATE='2026-09-28T12:00:00+08:00')
        self.git('commit', '-m', 'Recorded plan', env=environment)

    def git(self, *arguments, env=None):
        return subprocess.check_output(['git', '-C', str(self.source), *arguments],
                                       text=True, stderr=subprocess.DEVNULL, env=env).strip()

    def report(self, outcome='success'):
        result = subprocess.run([sys.executable, str(SCRIPT)], cwd=self.root,
                                env=dict(os.environ, SOURCE_OUTCOME=outcome),
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return (self.root / 'reports/latest.md').read_text()

    def test_active_tasks_and_source_version_are_visible(self):
        report = self.report()
        head = self.git('rev-parse', 'HEAD')
        self.assertIn('codex/simplify-development-workflow', report)
        self.assertIn(f'/blob/{head}/tasks/current.md', report)
        self.assertIn(f'/blob/{head}/tasks/plan.md', report)
        self.assertNotIn('任务状态请核对最新证据和 Dashi', report)

    def test_failed_checkout_does_not_reuse_existing_source_as_current(self):
        report = self.report('failure')
        self.assertIn('来源读取失败', report)
        self.assertNotIn('/commit/', report)
        self.assertIn('无法核验', report)

    def test_missing_active_tasks_are_reported_as_unverified(self):
        (self.source / 'tasks/current.md').unlink()
        self.git('add', '-u')
        self.git('commit', '-m', 'Missing active status')
        report = self.report()
        self.assertIn('tasks/current.md 缺失', report)
        self.assertIn('无法核验', report)

    def test_product_snapshot_is_dated_and_not_claimed_live(self):
        manifest_path = self.source / 'docs/project-progress/snapshots/manifest.json'
        manifest = json.loads(manifest_path.read_text())
        manifest['captured_at'] = '2026-10-10T12:00:00+08:00'
        manifest['sources']['product']['captured_at'] = '2026-10-09T12:00:00+08:00'
        manifest_path.write_text(json.dumps(manifest))
        report = self.report()
        self.assertIn('2026-10-09T12:00:00+08:00', report)
        self.assertIn('011c835', report)
        self.assertIn('Product 快照', report)
        self.assertIn('非实时', report)
        self.assertIn('2026-09-28T12:00:00+08:00', report)

    def test_private_commit_subjects_stay_out_of_public_report(self):
        self.git('commit', '--allow-empty', '-m', 'PRIVATE_DIAGNOSTIC_MARKER internal path and observation')
        report = self.report()
        self.assertNotIn('PRIVATE_DIAGNOSTIC_MARKER', report)
        self.assertIn('私有', report)

    def test_product_manifest_links_to_private_source_and_missing_is_explicit(self):
        report = self.report()
        head = self.git('rev-parse', 'HEAD')
        self.assertIn(f'/blob/{head}/docs/project-progress/snapshots/manifest.json', report)
        (self.source / 'docs/project-progress/snapshots/manifest.json').unlink()
        report = self.report()
        self.assertIn('Product 快照清单缺失', report)
        self.assertIn('无法核验', report)

    def test_invalid_git_checkout_produces_an_explicit_failure_report(self):
        import shutil
        shutil.rmtree(self.source / '.git')
        report = self.report()
        self.assertIn('来源读取失败', report)
        self.assertIn('无法核验', report)


if __name__ == '__main__':
    unittest.main()
