# 七寸阶段：需求、实现与证据对照

日期：2026-09-28。状态：规划输入与只读审查结果；不是新产品验收或任务派发许可。

需求来源为[用户附件原文](references/2026-09-28/README.md)。本轮检查通过 `vision-nuc-codex` 读取 Product 源码、测试清单、历史工程证据和本地任务权威记录；没有重新运行产品测试，没有操作飞控。以下路径均相对 Product 仓库 `/srv/indoor-uav-product`，任务契约路径相对 Control Plane 仓库。证据范围限本次检查的 `src/`、`tests/`、`tasks/product/` 及相关契约，未见实现不等于排除其他人工试验记录。

## 当前检查点

- Product HEAD：`21c295cc4783aa371ef6d22be9c6518cd7a218b3`，工作区干净。
- Control Plane HEAD：`d4b3e9c0907fe34adca549098be2383a19b9d248`。
- 本次只读运行态核验：M6-T02 `DONE/ACCEPTED`、attempt 1；M6-T03 `READY/PENDING`、attempt 0，绑定当前 Product HEAD，契约摘要 `e0c555fecdaf6f2cd3407ac21809c8647260c17dd4780fba491645a22d556629`。
- M6-T04 虽显示 READY，但契约仍绑定旧 Product HEAD，且依赖 M6-T03；不能据 READY 派发。
- HGAF-T10 本地权威记录仍为 `READY/PENDING`、attempt 0；历史人工接受记录与台账的差异待专门审计。
- production-runner、orchestrator timer、controlled-soak 三项均 `inactive/disabled`；心跳停留在 9 月 20 日。不能确认持续自动开发在运行。
- Dashi 实时服务未核验，本地版本缓存不能代替在线版本。
- `tasks/product/M6-T02-engineering-evidence.json` 记录 7 项专项测试、289 项整体测试与 safety-check 历史 PASS，验证对象为录制遥测。本轮没有复跑，不能解释为真实 FCU 连接验证。

## 需求冲突与处理

| 主题 | 原记录与新材料的差异 | 本轮处理 |
|---|---|---|
| 平台 | 旧 HGAF 方案以 RK3576 为目标；最新要求七寸 RK3588 先验证 | 当前规划采用 RK3588；RK3576/3.5 寸放入后续迁移，保留旧文件及历史证据 |
| 避障阶段 | 旧 Phase A 不含完整环境避障；新七寸阶段包含桌椅/隔断绕行 | 纳入七寸最终交付；空旷跟随只作为中间里程碑，提出契约修订，不改写冻结 PRD 快照 |
| 主动观察、降落区域、三维骨架 | 新材料明确纳入；旧软件契约未完整覆盖 | REQ-06/07/12/13 设置独立工作包和验收门禁 |
| 3 米±0.5 米、最多约 10 人、3～5 分钟 | 上午主任务问答已确认这些数字；附件说明其本次问答未确认，且异常状态不要求严格三米 | 保留上午确认来源，不静默删除或冒充附件确认。正常跟随距离容差保留，距离参考点/水平或空间距离、例外状态、人员场景及重复次数需统一成正式验收定义 |
| 相机与三维 | MIPI 是接口；同步双目为优先候选，型号未定 | 不宣称现有相机是双目或已有深度；设同步、标定、覆盖和采购前可行性门禁 |
| 测高与降落 | 下视雷达只测高；新要求自主判断可降落区域 | 不将测高当区域安全证明；下方感知覆盖是关键路径 |
| 实时与滤波 | 希望感知快于控制、滤波令运动平滑 | 不建立高于 PX4 内环的频率要求；分别核验感知新鲜度、状态估计和轨迹平滑，KF/EKF 保持候选 |

上午数值来源：项目主任务 `01a07eef-6e90-7a53-98ad-e52fb90fd3c4` 的 2026-09-28 六轮需求问答及其后用户“确认”。本轮未把其他任务的执行授权扩展到新增需求。

## REQ-01～REQ-14 对照

表内“历史离线”表示有对应实现、测试及工程证据记录，不代表本轮重新验证，也不等于整条需求完成。工作包 Pxx 是[开发计划](../tasks/plan.md)中的提案编号，不是新建的 Dashi 任务。

| 需求 | 当前实现位置 | 已有验证层级与证据 | 尚缺能力或证据 | 既有任务及依赖 | 下一项工作与完成判据 |
|---|---|---|---|---|---|
| REQ-01 指定身份 | `src/indoor_uav_tracking/identity_manager.py`；`src/indoor_uav_targeting/__init__.py` | 历史离线：`tests/unit/test_hgaf_identity_manager.py`；`tasks/product/HGAF-T03-replay-evidence.json` | 真实骨架/外观融合、同衣多人交叉、误重捕获的保留测试集 | HGAF-T03，依赖 M5-T03；新增对照实验须映射修订/后继任务 | P03/P04：同输入比较关联器，身份不确定时不能输出继续跟随许可 |
| REQ-02 稳定跟随 | `src/indoor_uav_following/follow_policy.py`、`dynamic_follow_target.py` | 历史离线：`tests/unit/test_hgaf_follow_policy.py`；HGAF-T05 replay evidence | 显式 `metric_distance_available=False`；未覆盖三米米制闭环 | HGAF-T05/T06，依赖 HGAF-T04；M7-T05 是试验计划 | P05/P07：定义躯干距离后，在米制回放及真实动力学仿真测量误差、超调、暂停与恢复 |
| REQ-03 躯干参考 | 当前 FollowReference 使用框中心归一化误差 | `tests/unit/test_hgaf_follow_policy.py` 只支持旧抽象 | 尚未发现浮点骨架、躯干参考和关键点缺测切换的完整实现 | HGAF-T04/T05 扩展；依赖 P02/P03 | P05：手脚运动不直接驱动跟随；躯干不可观测明确退化，参考切换无突跳 |
| REQ-04 相机运动补偿 | `src/indoor_uav_targeting/target_state_estimator.py`；`src/indoor_uav_telemetry/fcu_validation.py` | 历史离线：`tests/unit/test_hgaf_target_state_estimator.py`、`test_m6_fcu_telemetry_validation.py` | 当前估计是二维归一化坐标，无完整相机/机体/导航变换；姿态不足以补偿平移 | HGAF-T04、M6-T02；先 P02/P05 | P06：固定人物、相机旋转和平移分离测试；时间错位或自身状态失效拒绝融合 |
| REQ-05 平滑 | `src/indoor_uav_following/trajectory_constraints.py`；`src/indoor_uav_control/__init__.py` | 历史离线：`tests/unit/test_hgaf_trajectory_constraint_layer.py`、`test_setpoint_limits.py` | 无量纲约束不等于米制 jerk/偏航边界；未有实际尾延迟与画面模糊证据 | HGAF-T07，依赖 HGAF-T06/M4-T04 | P07：度量加速度、jerk、偏航及跟随误差；重捕获跳变、过强滤波反例有结果 |
| REQ-06 主动观察 | `src/indoor_uav_following/ego_planner.py` 是无量纲候选规划 | `tests/unit/test_hgaf_ego_planner.py` 不证明主动观察 | 未发现以骨架可见性、观测覆盖和可达性约束选视角的完整链路 | HGAF-T08 为参考基础；新覆盖待登记；依赖 P08 | P09：已观测可达的更好视角能触发调整，不进入未知区域，不持续左右切换 |
| REQ-07 受限退化 | identity manager 与 SafetyFSM 有不确定/HOLD 抽象 | `tests/unit/test_partial_occlusion_persistence.py`、`test_hgaf_safety_fsm.py` | 未表达头肩躯干语义、无可达好视角及暂停后的目标远离处理 | HGAF-T03/T09 扩展；依赖 P03/P08 | P09：无改善路径且自身定位可用时保持允许状态，部分骨架有缺测标记；不按 9/17 计数替代语义 |
| REQ-08 自主避障 | `src/indoor_uav_following/ego_planner.py` | HGAF-T08 replay evidence；模块明确无物理模型 | 未发现深度/占据地图、整机净空、制动距离或动态障碍完整验证 | HGAF-T08 不能视为已实现避障；依赖 P02/P08 | P08/P13：覆盖障碍、可通行、未知与盲区；普通障碍和复杂扩展场景分别验收 |
| REQ-09 遮挡恢复 | `src/indoor_uav_tracking/identity_manager.py`；`src/indoor_uav_control/loss_reappearance_scenarios.py` | 历史离线：`tests/unit/test_reacquisition_gate.py`、`tests/scenarios/test_m5_target_loss_reappearance.py` | 真实外观重识别及变帧率、长遮挡重捕获未验证 | HGAF-T03、M5-T04；依赖 P04 | P04/P07：以真实经过时间定义预测/丢失；错人恢复为失败，正确恢复轨迹连续 |
| REQ-10 新鲜度 | `src/indoor_uav_camera/__init__.py`、`src/indoor_uav_control/stale_input.py` | 历史离线：`tests/unit/test_hgaf_frame_health.py`、`test_stale_input_transitions.py` | 当前 FrameHealth 判断提供的时间戳，不能单独检出伪更新时间、冻结采集或推理卡住 | HGAF-T01/T09 与现有 stale guard；P02 先定义时钟责任 | P02/P11：图像停止、推理停止、传输继续发送旧结果分别注入；消费端依真实观测时间拒绝过期数据 |
| REQ-11 持续丢失 | `src/indoor_uav_control/safety_fsm.py`、`src/indoor_uav_offboard/__init__.py` | 历史离线：`tests/unit/test_hgaf_safety_fsm.py`、`test_offboard_lifecycle.py` | HOLD/ABORT 证据不是实际悬停/下降；等待、接管、低电、定位失效优先级未闭合 | HGAF-T09、M6-T03/T04；依赖 P10 与失效定义 | P10/P12：包括无安全降落区在内的决策表有有限时间退出；仿真先验证再受控实机 |
| REQ-12 降落区域 | 已检目录未发现独立区域感知/许可模块；bench procedure 仅是检查流程 | 无本需求直接通过证据；M6-T01 不覆盖区域判断 | 下方覆盖、几何/占用/有效期、下降持续安全检查 | 无完整匹配契约；提议新任务，不能借 M6-T01 宣称覆盖 | P10：适合/不适合/未知独立输出；桌沿、进入人员及过期区域均不能获降落许可 |
| REQ-13 米制骨架 | detector 目前为注入式 YOLO11n 框接口；`src/indoor_uav_replay/__init__.py` 为字节回放 | `tests/unit/test_yolo11n_detector.py`、`test_prerecorded_replay.py` 不证明姿态或米制三维 | 未发现完整双目同步/标定/左右身份匹配/三角化及骨架存储链路 | M2-T01～T04 为相邻历史基础；M8 是后续 RK3576 路线，不能直接代替 RK3588 任务 | P03/P05/P11：米制、坐标系、真实尺度来源可追溯；无效关节不填零充真值；可重放原始观测 |
| REQ-14 接管与证据 | `src/indoor_uav_safety/bench_procedure.py`、`src/indoor_uav_replay/evidence_orchestrator.py` | 历史离线：`tests/unit/test_m6_bench_procedure.py`、`test_hgaf_sw_t11_orchestrator.py` | 实际接管优先级与全过程同步日志未实机验证 | M6-T01/T03/T04、HGAF-T11；M7-T01～T05 为计划类前置 | P11/P12/P14：同步录像遥测与状态；接管单测；因避碰必须接管的演示不能算自主通过 |

## 完成声明规则

逐项记录未实现、已实现未验证、离线验证、真实动力学仿真验证、硬件验证、受控实飞验收。现有纯逻辑 HOLD 的零输出不能直接转换为实机“悬停”命令；实际行为还取决于定位健康、模式、环境及电量。历史测试参数（例如 100/300 ms）不是本阶段已批准的飞行阈值。未覆盖项不计入完成分子；本轮不提供整机完成百分比。
