# 日报范围与来源

既有北京时间每日 18:00（UTC 10:00）安排保持不变，支持手动触发。

读取私有协调仓库 `codex/simplify-development-workflow` 的实际远端版本、提交时间、更新数量与计划/任务入口。公开报告不复制内部任务内容或提交说明，完整记录见[私有资料库](https://github.com/rcfansjohnnyliu/indoor-uav-control-plane/blob/codex/simplify-development-workflow/docs/project-progress/README.md)。

Product 资料为有日期/版本的快照，日报未连接 NUC，也不检查真实设备、飞控、飞行或新测试。新报告生成时间不能刷新旧快照时间；来源失败、缺文档或缺清单明确报告无法核验。

实现、验证、计划和阻塞按证据区分；报告运行成功不能证明整机完成。Dashi/CP-AUTO 已退出新软件工作前提。

本地检查：`python3 -m unittest discover -s tests -v`，七项回归包括错误来源、时效、失败、缺任务/清单与私有提交说明不外泄。远端工作流须在发布后核验实际结果。
