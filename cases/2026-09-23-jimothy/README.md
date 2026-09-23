# Jimothy · 把 Jev 的示范教给本地分类器

**简体中文** | [English](README.en.md)

> 收集 Jev 对特定任务的判断，训练能在浏览器或服务器本地运行的小分类器。

**内容更新：** 2026-09-23 12:09:12（北京时间，UTC+08:00）

**🟢 A · 功能/原理证据较清楚**<br>A 针对可检查的数据与训练分工；小模型速度不能直接当完整流程速度，教师错误也可能被继承。<br>[判断依据与来源](../../references/2026-09-23-increment10-audit.md#jimothy)

## 用人话解释原理

像让老师先批一批练习，再用这些例子教出只擅长这类题的学徒。

[返回总表](../../README.md#data) · [同类优劣与原理](../../breakdowns/2026-09-18-data.md)

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | 数据分类与信息整理 |
| 来源平台 / 原作者 | X / [@AndrewPrifer](https://x.com/AndrewPrifer) |
| 原帖 | [查看原帖](https://x.com/AndrewPrifer/status/2102162296739099126) |
| 原帖发布时间（UTC） | 2026-09-21T22:25:22+00:00 |
| 主帖点赞快照 | **367**（门槛 ≥ 200） |
| 点赞与媒体取数时间（UTC） | 2026-09-23T03:56:58+00:00 |
| 元数据核验渠道 | [FxTwitter 公共接口](https://api.fxtwitter.com/status/2102162296739099126)；可能有缓存 |
| 最后来源复查 | 2026-09-23，核对公开说明与元数据；未运行应用 |
| Jev 版本 | 原帖未明确固定版本，未知 |
| 验证状态 / 可用性 | 未复现 / 未知（未运行验证） |

## 图片与视频

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102161913723691008/img/elm99ez4yx84JJO2.jpg" width="640" alt="Jimothy · 把 Jev 的示范教给本地分类器预览">](https://x.com/AndrewPrifer/status/2102162296739099126)<br>[视频](https://x.com/AndrewPrifer/status/2102162296739099126)

21 秒演示与固定教师接口、训练说明；未训练或执行导出模型。

- [视频直链 1](https://video.twimg.com/amplify_video/2102161913723691008/vid/avc1/908x714/hZWNZe-tLGn2woXE.mp4?tag=29)（元数据时长 21.9 秒）

媒体来源：[原始发布页](https://x.com/AndrewPrifer/status/2102162296739099126)。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

收集 Jev 对特定任务的判断，训练能在浏览器或服务器本地运行的小分类器。

**可借鉴点（分析）**：适合重复、边界稳定的分类任务；比一次性教师数据实验多了训练和导出工具。

## 输入、操作与输出

工具读取已有标签，或经 Gateway 调用 Jev 并缓存响应；用 MiniLM 特征或 TF-IDF 训练分类头，分开做模型选择、校准与接受阈值评估。

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| 主帖称 15–45MB、快 10–20 倍；仓库速度示例是 M3 Max 上预热后的单条推理，不含模型加载、教师取数和训练。 | 作者陈述 | [结果文档](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/README.md) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口](https://api.fxtwitter.com/status/2102162296739099126) | 仅上述时间快照，非实时数值 |



补充更新与去重来源：

无。

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

- [项目入口 1](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/README.md)
- [项目入口 2](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/src/teacher.ts)
- [项目入口 3](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/docs/automatic-training.md)

## 原理拆解与同类比较

本地运行的是学生模型，不是 Jev 权重；回退 Jev 要由应用实现。阈值只衡量与所供标签的一致性，不能保证新分布或真实正确率。

同类逐项对比、公共流程和建议实验见 [专题分析](../../breakdowns/2026-09-18-data.md)。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| 2026-09-23 | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
