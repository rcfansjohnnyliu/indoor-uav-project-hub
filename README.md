# Indoor UAV 研发进度中心

> 私有研发资料库。下方表格为 2026-09-24 的基线；每日自动核验记录见[最新汇报](reports/latest.md)。

## 当前进度

[查看最新自动汇报](reports/latest.md) · [查看自动任务运行](https://github.com/rcfansjohnnyliu/indoor-uav-project-hub/actions/workflows/daily-report.yml)

| 领域 | 状态 | 最近可核验证据 |
|---|---|---|
| 自动化基础 M0-A | 已关闭并冻结 | Control Plane `orchestration/PROJECT_STATE.md` |
| HGAF 软件开发 | 已推进至 M6 阶段 | Product HEAD `21c295cc4783aa371ef6d22be9c6518cd7a218b3`，2026-09-24 只读检查，工作区干净 |
| M6-T02 | 本地已验收 | `docs/control-plane/M6_T03_MAC_RESUMPTION.md`，2026-09-23 检查点 |
| M6-T03 | 等待授权与契约绑定更新；尚未派发 | 同上；Dashi 实时状态未独立复核 |
| HIL、硬件、真实飞行 | 人工门禁 | `AGENTS.md` 与 HGAF 研发计划 |

**状态口径：**“本地已验收”是本地证据验证的结果，不等于 Dashi `DONE`。Dashi 是任务和状态控制面；此页只展示经核实的摘要，不写回任务状态，也不授予执行权限。

## 导航

- [产品目标与研发阶段](docs/01-product-and-roadmap.md)
- [HGAF 具体研发方案](docs/05-execution-plan.md)
- [研发管理流程](docs/02-development-governance.md)
- [当前任务与下一步](docs/03-current-status.md)
- [每日汇报规则](docs/04-daily-reporting.md)
- [2026-09-24 基线汇报](reports/2026-09-24-baseline.md)

## 资料来源与更新原则

权威资料仍保留在原位置：Dashi 任务板、Control Plane 仓库、NUC Product 仓库及经批准的 PRD。此库仅作可读展示与历史日报；每条状态必须附检查时间、来源和证据。无法读取实时 Dashi 时明确标记“未复核”，不得把旧快照当作实时状态。
