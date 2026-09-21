# Third Hand / arc-cua · 选动作操作 Mac

**简体中文** | [English](README.en.md)

> 读取控件和屏幕文字，选择操作，并输入请求或规划器给定的文字。

**内容更新：** 2026-09-21 11:02:26（北京时间，UTC+08:00）

**🟢 A · 功能/原理证据较清楚**<br>A 仅针对公开实现分工；arc-cua 明确复用 Third Hand 的文字输入思路，作为同作者相关方案合并。“解决电脑操作”和普遍提速没有基准支持。<br>[判断依据与来源](../../references/2026-09-21-increment9-audit.md#third-hand)

## 用人话解释原理

像把一项办事任务交给助手：规划器写好目标和便签，Jev 按按钮清单选择下一步，执行器负责点击、填字和等待。

[返回总表](../../README.md#browser) · [同类优劣与原理](../../breakdowns/2026-09-18-browser.md)

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | 浏览器与电脑操作 |
| 来源平台 / 原作者 | X / [@sxhivs](https://x.com/sxhivs) |
| 原帖 | [查看原帖](https://x.com/sxhivs/status/2101367048223982065) |
| 原帖发布时间（UTC） | 2026-09-19T17:45:20+00:00 |
| 主帖点赞快照 | **549**（门槛 ≥ 200） |
| 点赞与媒体取数时间（UTC） | 2026-09-20T02:46:29+00:00 |
| 元数据核验渠道 | [FxTwitter 公共接口](https://api.fxtwitter.com/status/2101367048223982065)；可能有缓存 |
| 最后来源复查 | 2026-09-21，核对公开说明与元数据；未运行应用 |
| Jev 版本 | 原帖未明确固定版本，未知 |
| 验证状态 / 可用性 | 未复现 / 未知（未运行验证） |

## 图片与视频

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101364408870109184/img/w93wxuq73naZx36A.jpg" width="640" alt="Third Hand / arc-cua · 选动作操作 Mac预览">](https://x.com/sxhivs/status/2101367048223982065)<br>[视频](https://x.com/sxhivs/status/2101367048223982065)

保留 Third Hand 原帖与快照，新增 arc-cua 的 11 秒视频、发布回复和独立仓库。

- [视频直链 1](https://video.twimg.com/amplify_video/2101364408870109184/vid/avc1/3024x1964/ywaIWwbhUYD5NIOm.mp4?tag=29)（元数据时长 31.1 秒）

媒体来源：[原始发布页](https://x.com/sxhivs/status/2101367048223982065)。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

读取控件和屏幕文字，选择操作，并输入请求或规划器给定的文字。

**可借鉴点（分析）**：Third Hand 从请求提取文字，无需额外生成模型；arc-cua 接收上游规划器给定的字面值，便于接入其他代理。两者均把选动作与本地执行分开。

## 输入、操作与输出

Third Hand 是 Swift 应用；同作者的 arc-cua 是独立 Python 执行器，沿用其文字输入思路。后者由上游规划器给目标、字面值和验收条件，AX/本地 OCR 读界面，Jev 选动作与输入键，执行器等待界面稳定。

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| 作者附 31 秒演示并声称亚秒延迟；文档将其标为早期实验，完成状态仍需人工判断。 | 作者陈述 | [主帖正文及附带媒体](https://x.com/sxhivs/status/2101367048223982065) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口](https://api.fxtwitter.com/status/2101367048223982065) | 仅上述时间快照，非实时数值 |



补充更新与去重来源：

- [@sxhivs 的补充帖](https://x.com/sxhivs/status/2101367050207981608)：发布于 2026-09-19T17:45:20+00:00；2026-09-20T02:53:28+00:00 取数时 50 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2101367050207981608)。
- [@sxhivs 的补充帖](https://x.com/sxhivs/status/2101729362194432184)：发布于 2026-09-20T17:45:02+00:00；2026-09-21T02:45:24+00:00 取数时 505 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2101729362194432184)。 [补充媒体 1](https://video.twimg.com/amplify_video/2101728406949994496/vid/avc1/3024x1964/wsoMkHs40zGSxksi.mp4?tag=29)
- [@sxhivs 的补充帖](https://x.com/sxhivs/status/2101729364203475072)：发布于 2026-09-20T17:45:03+00:00；2026-09-21T02:55:37+00:00 取数时 28 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2101729364203475072)。

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

- [项目入口 1](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/README.md)
- [项目入口 2](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/TextEntryPlan.swift)
- [项目入口 3](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/JevClient.swift)
- [项目入口 4](https://github.com/shhivv/arc-cua/blob/85fc321715e23f51c222d59d31461b75804ba4ac/README.md)
- [项目入口 5](https://github.com/shhivv/arc-cua/blob/85fc321715e23f51c222d59d31461b75804ba4ac/src/arc_cua/policies/typesafe.py)

## 原理拆解与同类比较

两个仓库不是同一程序；为避免同作者相关桌面方案拆卡，归一条介绍。arc-cua 仍逐步观测并调用 Jev；不能认定“解决了电脑操作”，无标签图形和完整任务成功率仍是缺口。

同类逐项对比、公共流程和建议实验见 [专题分析](../../breakdowns/2026-09-18-browser.md)。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| 2026-09-20 | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
| 2026-09-21T11:02:26+08:00 | 合并补充来源，完善原理、证据或教程说明；[去重记录](../../CHANGELOG.md) |
