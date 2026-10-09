"""Publish observed GitHub sources, keeping Product snapshots and plans distinct."""
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

BASE = 'https://github.com/rcfansjohnnyliu/indoor-uav-control-plane'
SOURCE_BRANCH = 'codex/simplify-development-workflow'


def git(source, *arguments):
    return subprocess.check_output(['git', '-C', str(source), *arguments],
                                   text=True, stderr=subprocess.PIPE).strip()


def source_report(source, now, outcome):
    if outcome != 'success':
        return ['**本次控制面来源读取失败，当前开发进度无法核验。** 请检查 Actions 来源读取权限。']
    try:
        head = git(source, 'rev-parse', 'HEAD')
        head_date = git(source, 'log', '-1', '--format=%cI')
        since = (now - dt.timedelta(days=1)).isoformat()
        changes = git(source, 'log', f'--since={since}', '--format=%H')
        lines = [f'已读取私有控制面分支 `{SOURCE_BRANCH}`，HEAD：[{head[:12]}]({BASE}/commit/{head})。', '',
                 f'最新提交时间：{head_date}。提交时间不代表本地开发状态的实时更新时间。', '',
                 '## 最近 24 小时已推送的变更', '']
        if changes:
            lines.append(f'私有来源最近 24 小时有 {len(changes.splitlines())} 项已推送提交；详细内容请登录私有仓库查阅。')
        else:
            lines.append('此分支最近 24 小时无已推送的新提交；本地未推送进度未核验。')
        lines += ['', '## 活动计划与任务证据', '']
        for path in ['tasks/current.md', 'tasks/plan.md', 'docs/DEVELOPMENT_WORKFLOW.md']:
            if (source / path).is_file():
                updated = git(source, 'log', '-1', '--format=%cI', '--', path)
                lines.append(f'- [{path}]({BASE}/blob/{head}/{path})（最后提交：{updated}）。')
            else:
                lines.append(f'- {path} 缺失，对应计划或进度无法核验。')
        return lines
    except (subprocess.CalledProcessError, OSError):
        return ['**本次控制面来源读取失败，当前开发进度无法核验。** 来源不是可读取的 Git 工作区；未沿用旧报告。']


def snapshot_report(source, outcome):
    if outcome != 'success':
        return ['Product 来源读取失败，当前进度无法核验。']
    try:
        manifest = json.loads((source / 'docs/project-progress/snapshots/manifest.json').read_text(encoding='utf-8'))
        source_head = git(source, 'rev-parse', 'HEAD')
        product = manifest['sources']['product']
        captured = product.get('captured_at') or manifest['captured_at']
        head = product['head']
        return [f'Product 快照采集时间：{captured}；本地源码 HEAD：`{head}`。', '',
                '此快照非实时：Actions 未连接 NUC，也未读取实机或最新本地测试。', '',
                f'- [私有采集清单与文件哈希]({BASE}/blob/{source_head}/docs/project-progress/snapshots/manifest.json)',
                '- [公开进度摘要](../docs/03-current-status.md)',
                f'- [完整私有计划]({BASE}/blob/{source_head}/tasks/plan.md)']
    except (OSError, ValueError, KeyError, TypeError, subprocess.CalledProcessError):
        return ['Product 快照清单缺失或不可读，Product 当前进度无法核验。']


def main():
    now = dt.datetime.now(ZoneInfo('Asia/Shanghai'))
    root = Path.cwd()
    lines = [f'# {now:%Y-%m-%d} 研发小汇报', '',
             f'报告生成时间：{now:%Y-%m-%d %H:%M:%S}（北京时间）。', '']
    source = root / 'source-control-plane'
    outcome = os.environ.get('SOURCE_OUTCOME')
    lines += source_report(source, now, outcome)
    lines += ['', '## Product 快照与读取范围', ''] + snapshot_report(source, outcome)
    lines += ['', '## 状态口径', '',
              '- 活动任务以控制面 tasks/current.md 为准；日报分别展示实施、验证、计划与阻塞的证据入口。',
              '- 提交、计划文档和日报成功均不能证明测试通过或整机跟随完成；请核对原始验收证据。',
              '- 已退役的 Dashi、CP-AUTO 和旧合同不是新软件开发的前置条件。',
              '- 实机、飞控连接、HIL、解锁及输出仍须具体任务授权；此报告不授予权限。', '']
    reports = root / 'reports'
    reports.mkdir(exist_ok=True)
    content = '\n'.join(lines)
    (reports / f'{now:%Y-%m-%d}.md').write_text(content, encoding='utf-8')
    (reports / 'latest.md').write_text(content, encoding='utf-8')


if __name__ == '__main__':
    main()
