# 当前任务与下一步

核验时间：2026-09-24（北京时间）。本页基于 Control Plane 文档与 Product 仓库只读检查；未读取 Dashi 实时任务板。

| 项目 | 已确认情况 | 下一步 / 门禁 |
|---|---|---|
| Product 代码 | HEAD `21c295cc4783aa371ef6d22be9c6518cd7a218b3`，工作区干净 | 后续任务须重新核验 HEAD 和工作区 |
| M6-T02 | 2026-09-23 检查点记载本地 `ACCEPTED`，attempt 1 | 核对 Dashi 投影及审计状态 |
| M6-T03 | 检查点记载 `READY`、验收 `PENDING`、attempt 0；运行时仍绑定旧契约 | 先取得任务专属 Human Authority，刷新 Dashi 绑定，按治理流程发布并核对不可变修订，再检查依赖、HEAD、runner 和重试预算；通过前不派发 |
| 硬件 / HIL / 飞行 | 无本次任务授权记录 | 保持人工门禁 |

M6-T03 的限定范围是离线、非 arming 的命令路径验证，使用 mock/录制输入；其软件证据不能替代真实 FCU、台架、HIL 或飞行验证。

## 已知资料时差

`orchestration/PROJECT_STATE.md` 与 `orchestration/TASK_GRAPH.md` 仍保留 M1-F 时期的任务快照，因此不能作为 M6 实时进度。当前 M6 描述取自 2026-09-23 的恢复检查点；Dashi 实时版本和状态尚未独立核实。
