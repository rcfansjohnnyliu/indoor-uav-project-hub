# 当前任务与下一步

核验时间：2026-09-28（北京时间）。本页基于 Control Plane 文档、Product 仓库和本地运行记录只读检查；未读取 Dashi 实时任务板。完整新增需求差距见[需求对照表](06-requirements-gap-2026-09-28.md)。

| 项目 | 已确认情况 | 下一步 / 门禁 |
|---|---|---|
| Product 代码 | HEAD `21c295cc4783aa371ef6d22be9c6518cd7a218b3`，工作区干净 | 后续任务须重新核验 HEAD 和工作区 |
| M6-T02 | 2026-09-28 本地运行记录为 `DONE/ACCEPTED`，attempt 1；范围为录制遥测 | 核对 Dashi 投影及审计状态 |
| M6-T03 | 本地 `READY/PENDING`、attempt 0；已绑定当前 Product HEAD 和修订摘要 `e0c555fecdaf` | 核对已有任务专属授权、Dashi 在线版本、依赖、HEAD、runner 和重试预算；新需求覆盖需走正式契约流程 |
| M6-T04 | 本地 `READY/PENDING`、attempt 0，仍绑定旧 HEAD | 前置 M6-T03 未接受，READY 不代表可派发 |
| 自动开发 | runner、orchestrator timer、controlled-soak 均 inactive/disabled，心跳停在 9 月 20 日 | 核对停用原因和治理条件，不将日报正常等同于持续开发 |
| 硬件 / HIL / 飞行 | 无本次任务授权记录 | 保持人工门禁 |

M6-T03 的限定范围是离线、非 arming 的命令路径验证，使用 mock/录制输入；其软件证据不能替代真实 FCU、台架、HIL 或飞行验证。

## 已知资料时差

`orchestration/PROJECT_STATE.md` 与 `orchestration/TASK_GRAPH.md` 仍保留 M1-F 时期的任务快照，因此不能作为 M6 实时进度。2026-09-23 恢复检查点中的 M6-T03 旧绑定已被本次运行态读取更新。Dashi 实时版本和状态尚未独立核实，GitHub 定时报告也尚未接入本地实时数据。
