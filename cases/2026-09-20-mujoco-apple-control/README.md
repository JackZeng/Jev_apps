# MuJoCo · 三模型搬苹果对照

**简体中文** | [English](README.en.md)

> 让模拟机械臂把苹果放进盘子，比较三种模型的方向与夹爪决策。

**内容更新：** 2026-09-20 11:01:10（北京时间，UTC+08:00）

**🟢 A · 功能/原理证据较清楚**<br>固定版本披露单次试验、物理控制分工和回放计时；A 表示可检查性较好，本库未运行校验或真实机器人。<br>[判断依据与来源](../../references/2026-09-20-increment8-audit.md#mujoco-apple-control)

## 用人话解释原理

模型像指挥员，选择向哪边挪、何时抓放；代码负责机械臂关节和物理运动。

[返回总表](../../README.md#simulation) · [同类优劣与原理](../../breakdowns/2026-09-18-simulation.md)

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | NPC、驾驶与群体模拟 |
| 来源平台 / 原作者 | X / [@openroboto](https://x.com/openroboto) |
| 原帖 | [查看原帖](https://x.com/openroboto/status/2101310974359941332) |
| 原帖发布时间（UTC） | 2026-09-19T14:02:31+00:00 |
| 主帖点赞快照 | **272**（门槛 ≥ 200） |
| 点赞与媒体取数时间（UTC） | 2026-09-20T02:47:32+00:00 |
| 元数据核验渠道 | [FxTwitter 公共接口](https://api.fxtwitter.com/status/2101310974359941332)；可能有缓存 |
| 最后来源复查 | 2026-09-20，核对公开说明与元数据；未运行应用 |
| Jev 版本 | 原帖未明确固定版本，未知 |
| 验证状态 / 可用性 | 未复现 / 未知（未运行验证） |

## 图片与视频

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101310940260270080/img/mCYBqjSwjUf4UV6d.jpg" width="640" alt="MuJoCo · 三模型搬苹果对照预览">](https://x.com/openroboto/status/2101310974359941332)<br>[视频](https://x.com/openroboto/status/2101310974359941332)

一分钟对照视频与协议回复合并；Mini 来自较早的一次同初始场景配对试验，非三模型同一次并行运行。

- [视频直链 1](https://video.twimg.com/amplify_video/2101310940260270080/vid/avc1/1280x720/7XlK_MEooTisJ5Ry.mp4?tag=29)（元数据时长 59.2 秒）

媒体来源：[原始发布页](https://x.com/openroboto/status/2101310974359941332)。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

让模拟机械臂把苹果放进盘子，比较三种模型的方向与夹爪决策。

**可借鉴点（分析）**：相较双臂积木短片，公开了响应记录、轨迹、源代码快照、成功判据和离线校验入口，便于后续复核。

## 输入、操作与输出

固定版本每周期两次请求：先选动作意图，再选 XYZ 方向及夹爪开/保持/合。输入是模拟器几何和接触反馈；共享执行器负责步长、IK 与物理推进，不是摄像头感知或关节力矩生成。

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| 作者记录 Jev 181.847 秒/0.018825 美元、GPT-6 Astra 707.274 秒/5.933624 美元完成；GPT-4.1 mini 达到 160 周期上限。约 1/315 费用仅属这些记录。 | 作者陈述 | [结果文档](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/README.md) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口](https://api.fxtwitter.com/status/2101310974359941332) | 仅上述时间快照，非实时数值 |



补充更新与去重来源：

- [@openroboto 的补充帖](https://x.com/openroboto/status/2101310978856276075)：发布于 2026-09-19T14:02:32+00:00；2026-09-20T02:53:28+00:00 取数时 16 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2101310978856276075)。
- [@openroboto 的补充帖](https://x.com/openroboto/status/2101310983931040038)：发布于 2026-09-19T14:02:33+00:00；2026-09-20T02:53:28+00:00 取数时 13 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2101310983931040038)。
- [@openroboto 的补充帖](https://x.com/openroboto/status/2101382220690895046)：发布于 2026-09-19T18:45:37+00:00；2026-09-20T02:53:28+00:00 取数时 8 赞，仅作补充、不计入门槛。[取数来源](https://api.fxtwitter.com/status/2101382220690895046)。

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

- [项目入口 1](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/README.md)
- [项目入口 2](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/docs/RESULTS.md)
- [项目入口 3](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/incremental_policy.py)
- [项目入口 4](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/verify_replay.py)

## 原理拆解与同类比较

每控制器仅一个 seed-0 试验；不能估计成功率。回放按模拟时间同步并去掉 API 等待，不能把视频长度当实际完成时间。

同类逐项对比、公共流程和建议实验见 [专题分析](../../breakdowns/2026-09-18-simulation.md)。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| 2026-09-20 | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
