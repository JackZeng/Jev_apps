# Claude Code Mod · 模型与推理力度路由

**简体中文** | [English](README.en.md)

> 按任务选择子代理模型，并调整主会话的推理力度。

**内容更新：** 2026-09-19 17:48:49（北京时间，UTC+08:00）

**🟢 A · 功能/原理证据较清楚**<br>固定源码可核对 hooks、默认开关和回退；主帖与当前版本的主模型路由描述有差异，费用收益仍未验证。<br>[判断依据与来源](../../references/2026-09-19-increment7-audit.md#claude-code-jev-router)

## 用人话解释原理

像工单分诊：Jev 判断工作难度，插件把任务交给对应助手；真正写代码的仍是被选中的模型。

[返回总表](../../README.md#routing) · [同类优劣与原理](../../breakdowns/2026-09-18-routing.md)

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | 模型、技能与工具路由 |
| 来源平台 / 原作者 | X / [@dani_avila7](https://x.com/dani_avila7) |
| 原帖 | [查看原帖](https://x.com/dani_avila7/status/2101176629745561686) |
| 原帖发布时间（UTC） | 2026-09-19T05:08:41+00:00 |
| 主帖点赞快照 | **417**（门槛 ≥ 200） |
| 点赞与媒体取数时间（UTC） | 2026-09-19T09:41:40+00:00 |
| 元数据核验渠道 | [FxTwitter 公共接口](https://api.fxtwitter.com/status/2101176629745561686)；可能有缓存 |
| 最后来源复查 | 2026-09-19，核对公开说明与元数据；未运行应用 |
| Jev 版本 | 原帖未明确固定版本，未知 |
| 验证状态 / 可用性 | 未复现 / 未知（未运行验证） |

## 图片与视频

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" width="640" alt="Claude Code Mod · 模型与推理力度路由预览">](https://x.com/dani_avila7/status/2101176629745561686)<br>[视频](https://x.com/dani_avila7/status/2101176629745561686)

与已有 Codex 路由用途相近，但仓库、宿主、作者及视频不同，按独立实现归入同类对比。

- [视频直链 1](https://video.twimg.com/amplify_video/2101176234411425792/vid/avc1/2278x1632/cdyZyiAMhglYXq-s.mp4?tag=29)（元数据时长 25.1 秒）

媒体来源：[原始发布页](https://x.com/dani_avila7/status/2101176629745561686)。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

按任务选择子代理模型，并调整主会话的推理力度。

**可借鉴点（分析）**：相对 Codex Model Router，本例直接接入 Claude Code 的 hooks，并区分主会话与子代理，方便检查缓存和回退策略。

## 输入、操作与输出

固定版本源码在提交提示时分类、在请求和子代理创建时应用结果。默认开启子代理模型和主会话推理力度路由，主模型切换默认关闭；与原帖“只在会话开始选主模型”的描述不同，以该版本代码为准。

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| 原帖附约 25 秒视频；公开代码支持 TypeSafe 或 Vercel Gateway，展示的是路由机制，不证明更便宜且同等质量。 | 作者陈述 | [主帖正文及附带媒体](https://x.com/dani_avila7/status/2101176629745561686) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口](https://api.fxtwitter.com/status/2101176629745561686) | 仅上述时间快照，非实时数值 |



补充更新与去重来源：

无。

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

- [项目入口 1](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/README.md)
- [项目入口 2](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/hooks/jev-model-router.ts)

## 原理拆解与同类比较

尚无完整任务质量、缓存费用和节省对照；无 Jev 密钥时会回退到宿主分类器，此路径不能算 Jev 效果。

同类逐项对比、公共流程和建议实验见 [专题分析](../../breakdowns/2026-09-18-routing.md)。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| 2026-09-19 | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
