# Indoor UAV 研发进度中心

> 私有研发资料库。需求与开发计划已于 2026-09-28 补充；下方是本次只读检查点。每日自动报告仅覆盖 GitHub 来源，详见[采集范围](docs/04-daily-reporting.md)。

**当前规划入口：[七寸 RK3588 开发计划](tasks/plan.md) · [REQ-01～14 实现与证据差距](docs/06-requirements-gap-2026-09-28.md) · [2026-09-28 补充审查](reports/2026-09-28-review.md)**

**交付节奏已调整：每周检查可运行增量，每两周交付演示版本。** [查看首个双周和四轮演示安排](docs/08-demo-delivery-cadence.md)。首个目标为真实视频的指定人员与骨架跟踪，10 月 12 日为首个完整版本目标检查点；这些是计划目标，不代表已派发或已实现。

**1～2 个月产品目标：** 10 月 26～28 日争取核心集成原型，11 月 23～28 日争取限定室内场景的七寸功能原型与重复验收。现场支持和感知硬件尚待确认，目标是否可达按双周实际结果判断，详见[计划](tasks/plan.md)。

## 开发流程已简化

已取消 Dashi 登记、状态同步和旧调度合同的开发前置条件。采用“任务文档 → 实现 → 验证 → 提交 → 汇报”，详见[当前流程](docs/02-development-governance.md)。旧框架归档，历史记录保留。

## 当前进度

[查看最新自动汇报](reports/latest.md) · [查看自动任务运行](https://github.com/rcfansjohnnyliu/indoor-uav-project-hub/actions/workflows/daily-report.yml)

| 领域 | 状态 | 最近可核验证据 |
|---|---|---|
| 自动化基础 M0-A | 已关闭并冻结 | Control Plane `orchestration/PROJECT_STATE.md` |
| 七寸基础飞行 | 用户确认已能稳定定点悬停与飞行 | 2026-09-28 硬件图片及说明：MicoAir743 V2 / PX4 1.15.4；本轮未独立实测 |
| HGAF 软件开发 | 软件原型与离线验证；整机目标尚未验收 | Product HEAD `21c295cc4783aa371ef6d22be9c6518cd7a218b3`，2026-09-28 只读检查，工作区干净 |
| M6-T02 | 本地已验收；录制遥测验证 | 2026-09-28 本地权威记录 `DONE/ACCEPTED`、attempt 1；不等同实时飞控验证 |
| M6-T03 | 已绑定当前 Product HEAD；尚未执行 | 2026-09-28 本地权威记录 `READY/PENDING`、attempt 0；Dashi 在线未核验 |
| 自动开发 | 当前停用 | 三项开发/调度服务 inactive/disabled；日报运行不代表开发运行 |
| 新增交付范围 | 已纳入计划，尚未完成能力验证 | 主动观察、自主降落区域判断、有尺度三维骨架及普通障碍绕行 |
| HIL、硬件、真实飞行 | 人工门禁 | `AGENTS.md` 与 HGAF 研发计划 |

**状态口径：**“本地已验收”是本地证据验证的结果，不等于 Dashi `DONE`。2026-09-28 起以开发协调仓库 `tasks/current.md` 为活动任务清单；Dashi 状态仅为历史记录。此页只展示摘要，不授予硬件权限。

## 导航

- [当前开发计划、工作包与验收门禁](tasks/plan.md)
- [已验证飞行平台与机载接口缺口](docs/09-seven-inch-hardware-baseline.md)
- [补充需求和开源参考原文](docs/references/2026-09-28/README.md)
- [产品目标与研发阶段](docs/01-product-and-roadmap.md)
- [HGAF 具体研发方案](docs/05-execution-plan.md)
- [研发管理流程](docs/02-development-governance.md)
- [当前任务与下一步](docs/03-current-status.md)
- [每日汇报规则](docs/04-daily-reporting.md)
- [2026-09-24 基线汇报](reports/2026-09-24-baseline.md)

## 资料来源与更新原则

权威资料仍保留在原位置：Dashi 任务板、Control Plane 仓库、NUC Product 仓库及经批准的 PRD。此库仅作可读展示与历史日报；每条状态必须附检查时间、来源和证据。无法读取实时 Dashi 时明确标记“未复核”，不得把旧快照当作实时状态。
