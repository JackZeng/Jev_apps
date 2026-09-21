# DocJev · 给文档分类、拆分合订本

**简体中文** | [English](README.en.md)

> 识别文档类别，并找出一份合订 PDF 中各文件的起止页。

**内容更新：** 2026-09-21 11:02:26（北京时间，UTC+08:00）

**🟢 A · 功能/原理证据较清楚**<br>实现和测量边界清楚；“同等准确、约六倍快”只部分成立，拆分质量有差异且计时不含完整处理。<br>[判断依据与来源](../../references/2026-09-21-increment9-audit.md#docjev)

## 用人话解释原理

像整理一叠混装文件：OCR 先把纸面读成文字，Jev 再判断每页属于什么、是否另起一份文件。

[返回总表](../../README.md#data) · [同类优劣与原理](../../breakdowns/2026-09-18-data.md)

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | 数据分类与信息整理 |
| 来源平台 / 原作者 | X / [@jerryjliu0](https://x.com/jerryjliu0) |
| 原帖 | [查看原帖](https://x.com/jerryjliu0/status/2101738281046294552) |
| 原帖发布时间（UTC） | 2026-09-20T18:20:29+00:00 |
| 主帖点赞快照 | **695**（门槛 ≥ 200） |
| 点赞与媒体取数时间（UTC） | 2026-09-21T02:44:57+00:00 |
| 元数据核验渠道 | [FxTwitter 公共接口](https://api.fxtwitter.com/status/2101738281046294552)；可能有缓存 |
| 最后来源复查 | 2026-09-21，核对公开说明与元数据；未运行应用 |
| Jev 版本 | 原帖未明确固定版本，未知 |
| 验证状态 / 可用性 | 未复现 / 未知（未运行验证） |

## 图片与视频

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101738161546391552/img/aTJ-mBG_YeF98yMQ.jpg" width="640" alt="DocJev · 给文档分类、拆分合订本预览">](https://x.com/jerryjliu0/status/2101738281046294552)<br>[视频](https://x.com/jerryjliu0/status/2101738281046294552)

主帖 24 秒视频；源码与评测固定到同一版本。

- [视频直链 1](https://video.twimg.com/amplify_video/2101738161546391552/vid/avc1/1920x1080/nBgVsuxAS-XY62FK.mp4?tag=29)（元数据时长 24.1 秒）

媒体来源：[原始发布页](https://x.com/jerryjliu0/status/2101738281046294552)。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

识别文档类别，并找出一份合订 PDF 中各文件的起止页。

**可借鉴点（分析）**：比单纯的税务文件分类多了连续页面拆分，并公开小样本报告，便于检查错误。

## 输入、操作与输出

固定源码用 Choice 选择文档类别、Noul 判断页间边界；LiteParse 可在本地读页，Jev 决策仍调用云端，另可选 LlamaParse。

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| 公开报告：分类两模型均 40/40；拆分 Jev 7/8、Luna 8/8。决策中位数分别为 138.6/794.3ms、209.6/1352.3ms，不含 OCR。 | 作者陈述 | [结果文档](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/benchmarks/results/real-small-v1-run01/report.md) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口](https://api.fxtwitter.com/status/2101738281046294552) | 仅上述时间快照，非实时数值 |



补充更新与去重来源：

无。

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

- [项目入口 1](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/README.md)
- [项目入口 2](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/src/jev_docs/engines/jev.py)
- [项目入口 3](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/benchmarks/results/real-small-v1-run01/report.md)

## 原理拆解与同类比较

测试只有 40 份短英文 PDF 和 8 份拼接包，标签未经人工复核；不能推广到扫描件、长文档或生产准确率。

同类逐项对比、公共流程和建议实验见 [专题分析](../../breakdowns/2026-09-18-data.md)。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| 2026-09-21 | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
