# Jev Workflow Builder · 把判断连成工作流

**简体中文** | [English](README.en.md)

> 用画布连接分类、评分、是非判断与文本生成节点。

**内容更新：** 2026-09-23 12:45:07（北京时间，UTC+08:00）

**🟢 A · 功能/原理证据较清楚**<br>A 针对可检查的节点执行与模型分工，不代表工作流效果或生产可用性已验证。<br>[判断依据与来源](../../references/2026-09-23-expanded-audit.md#jev-workflow-builder)

## 用人话解释原理

像画流程图：前一个节点给出判断，后面的节点接着处理。

[返回总表](../../README.md#routing) · [同类优劣与原理](../../breakdowns/2026-09-18-routing.md)

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | 模型、技能与工具路由 |
| 来源平台 / 原作者 | X / [@ctnicholasdev](https://x.com/ctnicholasdev) |
| 原帖 | [查看原帖](https://x.com/ctnicholasdev/status/2102070640589279318) |
| 原帖发布时间（UTC） | 2026-09-21T16:21:09+00:00 |
| 主帖点赞快照 | **638**（门槛 ≥ 200） |
| 点赞与媒体取数时间（UTC） | 2026-09-23T04:31:24+00:00 |
| 元数据核验渠道 | [FxTwitter 公共接口](https://api.fxtwitter.com/status/2102070640589279318)；可能有缓存 |
| 最后来源复查 | 2026-09-23，核对公开说明与元数据；未运行应用 |
| Jev 版本 | 原帖未明确固定版本，未知 |
| 验证状态 / 可用性 | 未复现 / 未知（未运行验证） |

## 图片与视频

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102070615926771715/img/PueMU1HUq0WB86ZG.jpg" width="640" alt="Jev Workflow Builder · 把判断连成工作流预览">](https://x.com/ctnicholasdev/status/2102070640589279318)<br>[视频](https://x.com/ctnicholasdev/status/2102070640589279318)

原作者主帖附媒体；取数快照和补充证据见下，不把转载或同项目更新另计。

- [视频直链 1](https://video.twimg.com/amplify_video/2102070615926771715/vid/avc1/1060x720/s3eKlPvK1XUESV-r.mp4?tag=14)（元数据时长 41.8 秒）

媒体来源：[原始发布页](https://x.com/ctnicholasdev/status/2102070640589279318)。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

用画布连接分类、评分、是非判断与文本生成节点。

**可借鉴点（分析）**：能预览运行和通过 REST 调用，适合试验多步客服分流。

## 输入、操作与输出

Liveblocks 支持协作编辑；服务端把节点配置转为 Jev 三种问题，并传递上游答案，LLM 节点另行生成文字。

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| 原帖演示客服流程；固定源码可检查真实 API 与模拟模式的区别。 | 作者陈述 | [主帖正文及附带媒体](https://x.com/ctnicholasdev/status/2102070640589279318) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口](https://api.fxtwitter.com/status/2102070640589279318) | 仅上述时间快照，非实时数值 |



补充更新与去重来源：

无。

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

- [项目入口 1](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/README.md)
- [项目入口 2](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/app/workflow/server/typesafe.ts)
- [项目入口 3](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/app/workflow/server/executor.ts)

## 原理拆解与同类比较

缺密钥时源码明确返回 mock 关键词结果，不能把无密钥演示当 Jev 推理；未验证生产并发和可靠性。

同类逐项对比、公共流程和建议实验见 [专题分析](../../breakdowns/2026-09-18-routing.md)。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| 2026-09-23 | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
