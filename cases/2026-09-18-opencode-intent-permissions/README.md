# OpenCode · 意图感知权限插件

**简体中文** | [English](README.en.md)

> 用“只访问 Google”等自然语言规则，检查代理换着工具发起的操作。

**内容更新：** 2026-09-19 16:55:36（北京时间，UTC+08:00）

**🟡 B · 效果待验证**<br>文档明确 Code Mode execute 可绕过插件。应理解为若干拦截演示，不能扩展成无法绕过的网络安全边界。<br>[判断依据与来源](../../references/2026-09-19-claims-audit.md#opencode-intent-permissions)

## 用人话解释原理

像门卫既看通行规则也听你要办什么事：Jev 判断工具输入的意图，插件再决定放行、询问或拒绝。OpenCode 原有权限仍在外层控制。

[返回总表](../../README.md#review) · [同类优劣与原理](../../breakdowns/2026-09-18-review.md)

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | 代码质量与安全检查 |
| 来源平台 / 原作者 | X / [@OpeOginni](https://x.com/OpeOginni) |
| 原帖 | [查看原帖](https://x.com/OpeOginni/status/2100702649834188855) |
| 原帖发布时间（UTC） | 2026-09-17T21:45:15+00:00 |
| 主帖点赞快照 | **235**（门槛 ≥ 200） |
| 点赞与媒体取数时间（UTC） | 2026-09-18T06:07:34+00:00 |
| 元数据核验渠道 | [FxTwitter 公共接口](https://api.fxtwitter.com/status/2100702649834188855)；可能有缓存 |
| 最后来源复查 | 2026-09-19，核对公开说明与元数据；未运行应用 |
| Jev 版本 | 原帖未明确固定版本，未知 |
| 验证状态 / 可用性 | 未复现 / 未知（未运行验证） |

## 图片与视频

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100701224920129536/img/-vzxHYoZxMjXKOKh.jpg" width="640" alt="OpenCode · 意图感知权限插件预览">](https://x.com/OpeOginni/status/2100702649834188855)<br>[视频](https://x.com/OpeOginni/status/2100702649834188855)

主帖含约 91 秒演示视频和配置图；正式收录依据作者原帖，不累计转发点赞。

- [视频直链 1](https://video.twimg.com/amplify_video/2100701224920129536/vid/avc1/1112x720/ghw0VjLAOMM6qB14.mp4?tag=14)（元数据时长 90.6 秒）
- [原图 2](https://pbs.twimg.com/media/HScw-Q-XEAA2AMF.jpg?name=orig)

媒体来源：[原始发布页](https://x.com/OpeOginni/status/2100702649834188855)。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

用“只访问 Google”等自然语言规则，检查代理换着工具发起的操作。

**可借鉴点（分析）**：能对 shell、webfetch 等不同工具表达相同的语义限制，减少逐条穷举命令；与命令危险性评分相比，进一步接入权限决策。

## 输入、操作与输出

oc-auto-perms 0.1.0 文档说明：选定工具的输入、策略和最近请求交给 Jev 判断，按有序规则输出 allow/ask/deny；低置信或 API 错误转为 ask。原生 deny 保持拒绝，原生 ask 保持确认；Jev 只进一步收紧原生 allow。

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| 作者演示以自然语言限制只能访问 Google，称挡住了视频中的不同访问尝试；原帖本轮已达 235 赞。 | 作者陈述 | [主帖正文及附带媒体](https://x.com/OpeOginni/status/2100702649834188855) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口](https://api.fxtwitter.com/status/2100702649834188855) | 仅上述时间快照，非实时数值 |

**从待整理区转入：** 上轮 2026-09-18 02:38:04 UTC 快照为 160 赞；本轮 06:07:34 UTC 为 235 赞，才满足正式门槛。[作者回复](https://x.com/OpeOginni/status/2100705405013754312)给出包地址；核对 [npm 元数据及 README](https://registry.npmjs.org/oc-auto-perms)，当时 latest 为 0.1.0。仅阅读文档，未安装插件。

补充更新与去重来源：

- [@OpeOginni 的补充帖](https://x.com/OpeOginni/status/2100705405013754312)：发布于 2026-09-17T21:56:12+00:00；2026-09-18T06:11:15+00:00 取数时 5 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2100705405013754312)。

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

- [项目入口 1](https://www.npmjs.com/package/oc-auto-perms)
- [项目入口 2](https://github.com/OpeOginni/oc-plugins/tree/main/packages/oc-auto-perms)

## 原理拆解与同类比较

视频中的拦截不证明无法绕过；应保留确定性硬边界。0.1.0 明确不支持 Code Mode execute，策略、近期用户消息及工具输入会送至 TypeSafe；本库未执行攻击或权限测试。

同类逐项对比、公共流程和建议实验见 [专题分析](../../breakdowns/2026-09-18-review.md)。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| 2026-09-18 | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
