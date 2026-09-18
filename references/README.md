# 来源、检索与快照说明

**简体中文** | [English](README.en.md)

本轮收录日期：**2026-09-18，北京时间**。范围为 X 上明确使用 **TypeSafe Jev** 的应用、可运行原型、实现演示与有具体任务的实验。

## 官方资料

| 资料 | 用途 |
| --- | --- |
| [TypeSafe](https://typesafe.ai) | 确认产品和官方入口 |
| [Introduction](https://docs.typesafe.ai/introduction) | 判断模型定位 |
| [Primitives](https://docs.typesafe.ai/primitives) | Choice、Score、Noul 及批量问题 |
| [Confidence](https://docs.typesafe.ai/confidence) | 概率、置信度和业务阈值的区别 |
| [Patterns](https://docs.typesafe.ai/patterns) | 应用组合与路由模式 |

这里只把 TypeSafe Jev 作为目标，不把同名账号、其他 Jev 产品或模仿 Jev 接口的本地模型混入案例总数。

## 本轮检索方法与范围

1. 用公开网页搜索发现原始帖线索，再在已登录的 X 搜索界面检索 `Jev min_faves:200 since:2026-09-14`，查看最新结果。
2. 对重点作者补查原帖和引用链，排除纯观点、新闻转载、仅设想、同名无关结果。
3. 为具体应用获取原帖正文、作者、发布时间、附带媒体及点赞数；同项目的更新和转载合并。
4. 用 `https://api.fxtwitter.com/status/<post-id>` 返回的公开元数据保存精确数字与媒体地址。该接口是第三方公开镜像，不是 X 官方 API，可能有缓存、延迟或缺失。
5. 首轮筛选出 67 个主帖快照均 ≥ 200 赞、有对应媒体的案例。尚缺关键信息的线索进入 [待整理区](../inbox/README.md)。

这是发布初期到本次检索时点的一批结果，不是 X 全量数据导出。平台排序、搜索索引、可见性、措辞和语言会影响覆盖；没有承诺已找全，也没有设置自动巡检。

## 可以检查什么

[data/catalog.json](../data/catalog.json) 是可审阅的结构化目录，同时保存每条的最小证据快照：

- `post.id` / `post.url` / `post.author`：主帖与原作者。
- `post.published_at`：原帖发布时间，UTC。
- `post.likes` / `post.retrieved_at`：该次接口报告的点赞与取数时间，UTC。
- `post.metrics_source`：实际取数入口。
- `post.media_source` / `post.media`：媒体所属原帖、原图或视频地址、视频封面与时长（如有）。
- `supplementary_posts`：同项目补充帖；不叠加其点赞，也不要求补充帖自身过门槛。
- `reported_result`：对作者报告的原创转述；`advantage` / `limitation`：依据公开信息的分析。

[data/catalog.en.json](../data/catalog.en.json) 只翻译编辑文字。两种语言共享证据、点赞与媒体；翻译不代表重新核对了原帖或刷新了数据。

原帖逐条链接在 [总表](../README.md) 和 [案例详情](../cases/README.md) 中。为了避免重新发布整篇社交媒体内容，仓库不提交完整帖文或个人账号资料，只保留核对所需的公共元数据与原创摘要。

## 媒体与验证边界

表内预览均取自原帖的照片或视频封面；照片不一定是应用运行截图，也可能是作者的代码或实验结果图。Skillbox 的图片来自被引用的早期产品介绍，Jev 集成的主帖没有自己的新图，因此在条目中明确区分了图片与主张的时间。

媒体采用外链，点击可打开其所属 X 页面；详情还保留原图或视频地址。CDN 和视频直链可能变化，GitHub 图片代理也可能缓存，故保留原帖作为回溯入口。本库不重新上传第三方原始素材，权利仍归作者。

已核对原帖公开说明和媒体元数据；没有逐一运行产品，也没有把“看过帖子”标成“已复现”。README 中的数字不是独立基准，外部应用可用性仍需运行确认。

## 最新增量

2026-09-18 第二轮新增 5 个案例、补充 4 个已有条目，该轮结束时共 72 个。检索范围、主帖门槛、合并依据与未收录原因见 [更新记录](../CHANGELOG.md)。旧主帖取数时间保持不变；没有把增量核对写成所有来源都重新检查。

## 第三轮增量与教程参考

2026-09-18 14:12 北京时间：新增 5 个、补充 1 个，当前共 77 个案例。权限插件本轮原帖达标后从待整理区转入。详见 [第三轮更新记录](../CHANGELOG.md)。

[Sydney Runkle：Building a Harness with Jev](https://x.com/sydneyrunkle/status/2100754364545761643)介绍 LangChain 中的分类调用、模型路由和工具风险门控；原帖本轮快照为 855 赞（2026-09-18T06:09:05+00:00 (UTC)，FxTwitter）。文章与转发按同一教程处理，作为原理参考，不拆成多个应用或当作独立性能评测。
