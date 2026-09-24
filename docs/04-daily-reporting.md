# 每日研发小汇报

GitHub Actions 配置为北京时间每日 18:00（UTC 10:00）生成 `reports/YYYY-MM-DD.md` 和 `reports/latest.md`。GitHub 定时调度可能延迟；可在 Actions 页面手动运行。首页的基线表不会被自动推断更新，最新观察由汇报展示。

目前自动读取 Control Plane 的 `codex/cp-auto-control-plane` 分支，使用独立只读 deploy key，凭据存储在 Actions Secret。Dashi 和 NUC Product 尚未接入自动采集，日报会明确标注该覆盖缺口；以下完整核验顺序仍是后续接入目标。来源读取失败时发布明确的失败报告并让工作流失败。停用 Actions 中的 Daily development report 即可停止定时更新。

## 每日核验顺序

1. 只读查询 Dashi 任务板，记录任务 ID、状态、更新时间；查询失败即标记“未复核”。
2. 只读检查 Control Plane 与 Product 的 HEAD、工作区状态和当天提交；不得把提交数等同于验收。
3. 对照不可变契约、本地权威验收和证据索引；把“实现”“测试通过”“本地验收”“Dashi 审计”分开。
4. 人工或自动生成不超过一页的摘要：今日变化、验证、阻断、下一步、来源与核验时间。
5. 无变化也写“无已核实变化”；来源不可用时写“无法核验”，不复制昨天的 PASS 作为今日事实。

## 模板

```markdown
# YYYY-MM-DD 研发小汇报

- 核验时间（北京时间）：
- 今日已核实变化：
- 验证与证据：
- 当前阻断 / 人工门禁：
- 下一步：
- 来源：Dashi 任务链接；Control Plane HEAD；Product HEAD；证据文档
- 未核实事项：
```

日报是展示材料，不得更改 Dashi `DONE`、本地权威验收、重试预算或任务权限。自动更新需要一个有持续运行保障的调度器，以及 Dashi、GitHub 和 Product 资料的只读访问；发布写入权限仅限本资料库。
