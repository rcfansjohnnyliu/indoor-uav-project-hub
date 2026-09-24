"""Publish observed GitHub changes without inferring task acceptance."""
import datetime as dt
import os
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

now = dt.datetime.now(ZoneInfo('Asia/Shanghai'))
source = Path('source-control-plane')
base = 'https://github.com/rcfansjohnnyliu/indoor-uav-control-plane'
lines = [f'# {now:%Y-%m-%d} 研发小汇报', '',
         f'核验时间：{now:%Y-%m-%d %H:%M:%S}（北京时间）。', '']
if os.environ.get('SOURCE_OUTCOME') == 'success':
    def git(*args):
        return subprocess.check_output(['git', '-C', str(source), *args], text=True).strip()
    head = git('rev-parse', 'HEAD')
    head_date = git('log', '-1', '--format=%cI')
    since = (now - dt.timedelta(days=1)).isoformat()
    changes = git('log', f'--since={since}', '--format=%H %s')
    lines += [f'已读取控制面分支 `codex/cp-auto-control-plane`，HEAD：[{head[:12]}]({base}/commit/{head})。', '',
              f'该分支最新提交时间：{head_date}。这不代表本地开发状态的实时更新时间。', '',
              '## 最近 24 小时已推送的变更', '']
    if changes:
        for change in changes.splitlines():
            sha, subject = change.split(' ', 1)
            subject = subject.replace('<', '&lt;').replace('>', '&gt;')
            lines.append(f'- [{sha[:8]}]({base}/commit/{sha}) {subject}')
    else:
        lines.append('此分支最近 24 小时无已推送的新提交；本地未推送的开发进度未核验。')
    lines += ['', '## 进度证据入口', '']
    found = False
    for path in ['docs/control-plane/M6_T03_MAC_RESUMPTION.md', 'tasks/todo.md',
                 'docs/architecture/hgaf-replan/03_HGAF_DEVELOPMENT_PLAN.md']:
        if (source / path).is_file():
            found = True
            updated = git('log', '-1', '--format=%cI', '--', path)
            lines.append(f'- [{path}]({base}/blob/{head}/{path})（最后提交时间：{updated}）。')
    if not found:
        lines.append('远端分支没有预期的最新任务证据文档，不能核实实时任务进度。参见[人工核验基线](2026-09-24-baseline.md)，其日期不代表当前状态。')
else:
    lines += ['**本次控制面来源读取失败，当前开发进度无法核验。** 请检查本次 Actions 运行及来源读取权限。']
lines += ['', '## 核验范围与下一步', '',
          '- 上述提交和文档用于定位变化，不能据此推断测试通过、本地验收或 Dashi DONE。',
          '- Dashi 实时状态及 NUC Product 本地仓库尚未接入此 GitHub 定时任务；本报告不宣称它们已完成实时核验。',
          '- 任务状态请核对最新证据和 Dashi；执行仍须遵守有效契约及人工门禁。',
          '- 如需完整实时日报，后续还须接入 Dashi 和 Product 的受控只读进度数据。', '']
reports = Path('reports')
reports.mkdir(exist_ok=True)
content = '\n'.join(lines)
(reports / f'{now:%Y-%m-%d}.md').write_text(content, encoding='utf-8')
(reports / 'latest.md').write_text(content, encoding='utf-8')
