# DuckDB / MotherDuck · 在 SQL 里给文字分类

**简体中文** | [English](README.en.md)

> 查询表格时直接调用 Jev 分类，不必先把文本导出。

**内容更新：** 2026-09-23 12:09:12（北京时间，UTC+08:00）

**🟡 B · 效果待验证**<br>新文章补充数据集、查询和统计口径，但仍是厂商自测；B 保留。NULL 排除和训练划分来源需一并看，不能把宣传倍率当通用结论。<br>[判断依据与来源](../../references/2026-09-23-increment10-audit.md#duckdb)

## 用人话解释原理

像给表格加一个分拣按钮：SQL 取行，Jev 判断类别，结果再回到表格里统计。

[返回总表](../../README.md#data) · [同类优劣与原理](../../breakdowns/2026-09-18-data.md)

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | 数据分类与信息整理 |
| 来源平台 / 原作者 | X / [@hamiltonulmer](https://x.com/hamiltonulmer) |
| 原帖 | [查看原帖](https://x.com/hamiltonulmer/status/2100370557405667768) |
| 原帖发布时间（UTC） | 2026-09-16T23:45:38+00:00 |
| 主帖点赞快照 | **1,310**（门槛 ≥ 200） |
| 点赞与媒体取数时间（UTC） | 2026-09-17T22:42:25.668728+00:00 |
| 元数据核验渠道 | [FxTwitter 公共接口](https://api.fxtwitter.com/status/2100370557405667768)；可能有缓存 |
| 最后来源复查 | 2026-09-23，核对公开说明与元数据；未运行应用 |
| Jev 版本 | 原帖未明确固定版本，未知 |
| 验证状态 / 可用性 | 未复现 / 未知（未运行验证） |

## 图片与视频

[<img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" width="640" alt="DuckDB / MotherDuck · 在 SQL 里给文字分类预览">](https://x.com/hamiltonulmer/status/2100370557405667768)<br>[图片](https://x.com/hamiltonulmer/status/2100370557405667768)

保留 DuckDB 原帖快照，合并 MotherDuck 配图与方法文章，未执行 SQL。

- [原图 1](https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig)

媒体来源：[原始发布页](https://x.com/hamiltonulmer/status/2100370557405667768)。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

查询表格时直接调用 Jev 分类，不必先把文本导出。

**可借鉴点（分析）**：保留 SQL 分析流程；托管版本补充公开查询示例和较大样本的分类对照。

## 输入、操作与输出

原作者的 DuckDB 扩展调用 Jev；同作者参与的 MotherDuck 官方文章介绍托管 prompt_jev()，在 SQL 中返回 Choice、Noul 或 Score。两种部署合并比较，不认定为同一程序。

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| 旧帖为 1,000 行约 10 秒，重写快 20–40 倍是和旧扩展比。新官方示例报告 Jev/Terra：89%/88%，40 秒/31分59秒，$0.50/$37.58；各数字限该查询设置。 | 作者陈述 | [结果文档](https://motherduck.com/blog/motherduck-supports-jev/) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口](https://api.fxtwitter.com/status/2100370557405667768) | 仅上述时间快照，非实时数值 |



补充更新与去重来源：

- [@hamiltonulmer 的补充帖](https://x.com/hamiltonulmer/status/2101700765656264896)：发布于 2026-09-20T15:51:24+00:00；2026-09-21T02:45:54+00:00 取数时 503 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2101700765656264896)。
- [@motherduck 的补充帖](https://x.com/motherduck/status/2102077291081896307)：发布于 2026-09-21T16:47:35+00:00；2026-09-23T03:55:29+00:00 取数时 456 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2102077291081896307)。 [补充媒体 1](https://pbs.twimg.com/media/HSwUH3TbAAAdWbK.jpg?name=orig)

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

- [项目入口 1](https://motherduck.com/blog/motherduck-supports-jev/)

## 原理拆解与同类比较

MotherDuck 功能面向付费方案。评测用 AG News 训练划分抽取的 10 万行，准确率公式排除 NULL；不同并发及全流程条件不足以证明普遍等准或省费。

同类逐项对比、公共流程和建议实验见 [专题分析](../../breakdowns/2026-09-18-data.md)。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| 2026-09-18 | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
| 2026-09-21T11:02:26+08:00 | 合并补充来源，完善原理、证据或教程说明；[去重记录](../../CHANGELOG.md) |
| 2026-09-23T12:09:12+08:00 | 合并补充来源，完善原理、证据或教程说明；[去重记录](../../CHANGELOG.md) |
