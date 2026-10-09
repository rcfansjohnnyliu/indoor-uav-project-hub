# Indoor UAV 研发进度中心

本库为**公开进度总览**。2026-10-09 已通过 GitHub 核实：此前“私有资料库”的说明不准确；完整内部记录保存在私有协调仓库。

当前目标：**2026-11-09 前完成限定室内场景的实机指定人员跟随演示**。目标风险高，整机跟随尚未验收。

[当前开发计划](tasks/plan.md) · [实际进度与阻塞](docs/03-current-status.md) · [最新日报](reports/latest.md)

| 领域 | 已记录进度 | 仍待验证或完成 |
| --- | --- | --- |
| 飞机基础 | 用户确认已装好，人工稳定悬停、室内定位与遥控接管已验证 | 同一计算板/相机/安装/供电载荷的等价性未核实，本轮未独立复飞 |
| 双目采集 | RK3588 双 AR0234 预览恢复并持续更新 | 当前原板静止重复性采集待现场就位；曝光同步未建立 |
| 人体模型 | YOLO26s-Pose FP16 / RKNN 已接入 A 路预览 | 当前无身份输出；双视图同人对应、RK3588 身份集成与米制目标未完成 |
| 身份复用 | 旧平台已有 OSNet 与身份选取/跟踪实现 | 须在当前平台验证数值、性能和指定身份连续性 |
| 标定测距 | 已有静态观察与诊断证据 | 1.15m 冻结检查无有效距离；完整 1–3m 未验收，不能由三次较远静态结果推断全范围精度 |
| 软件测试 | 最近已记录 414 项测试和安全检查通过 | 分支限定的 bootstrap 检查失败仍保留；同步任务未重跑 Product 测试 |
| 跟随系统 | 已有离线接口、控制与生命周期原型 | 动态米制感知、变换、控制、实际闭环 PX4 SITL、去桨和实机跟随尚未验收 |
| 一月交付 | 九项冲刺和完整路线图已记录 | 全部新开发任务仍 PLANNED；Nov9 目标风险高 |


## 查阅入口

- [一月计划、范围与后续路线图](tasks/plan.md)
- [当前任务摘要](tasks/current.md)
- [完整计划与内部证据（私有）](https://github.com/rcfansjohnnyliu/indoor-uav-control-plane/blob/codex/simplify-development-workflow/docs/project-progress/README.md)
- [权威活动任务（私有）](https://github.com/rcfansjohnnyliu/indoor-uav-control-plane/blob/codex/simplify-development-workflow/tasks/current.md)
- [检查点和交付安排](docs/08-demo-delivery-cadence.md)
- [下一项现场准备](docs/10-first-demo-kickoff.md)
- [研发流程](docs/02-development-governance.md)
- [日报读取范围](docs/04-daily-reporting.md)
- [9 月 28 日公开历史归档](docs/archive/2026-09-28/INDEX.md)

每条状态按实现、验证、计划和阻塞区分。私有链接需要仓库访问权限；本公开摘要不包含内部原始记录、原始图像、模型、身份嵌入或凭证。Dashi、CP-AUTO 和旧合同不再是新软件开发前置条件；真实设备、飞控、输出及飞行仍需逐项授权。
