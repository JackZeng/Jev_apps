# Jev 应用案例与原理拆解

从 X 收集 **TypeSafe Jev** 的真实应用演示，整理用途、实现思路和同类优劣。**首批 67 个案例 · 11 类 · 每条主帖收录时均 ≥ 200 赞 · 每条附图或视频**。

更新日期：**2026-09-18（北京时间）**。这是本次检索覆盖到的案例集，不承诺穷尽 X；目前全部**未复现**。正文中的性能、成本与效果均标明为作者报告，优劣是根据公开设计作出的分析，不是本仓库跑分。

Jev 接收状态与类型化问题，输出可供代码使用的选择、评分或是非判断。它在下面许多应用中充当决策组件，周围仍需要观测、执行器，有时也需要 LLM。[官方介绍](https://docs.typesafe.ai/introduction) · [基本原理与阅读方法](breakdowns/2026-09-18-how-jev-apps-work.md)

## 收录与阅读规则

- **门槛按单条主帖判断**：点赞 ≥ 200，明确使用 TypeSafe Jev，有具体演示或实现截图；同项目更新与转载合并，点赞不相加。
- **数字是快照**：检索来自 X；精确点赞与媒体元数据通过 FxTwitter 公共接口复核，可能有缓存或延迟。每篇保留原帖时间、取数时间和来源。[检索与证据说明](references/README.md) · [结构化目录与点赞快照](data/catalog.json)
- **预览可点击**：表中的图来自原帖图片或视频封面，点击打开对应来源。详情保留视频直链/原图；X 图片 CDN、视频直链或帖子可能失效，优先回原帖查看。Skillbox 的图来自它被引用的旧版介绍，已单独说明。
- **同类放一起**：每组下面给选择建议，详细对比逐项列出优势与限制。类别内按用途排列，不按点赞排名。视频只是演示证据，不证明长期可靠性。

## 分类导航

| 类别 | 案例数 | 对比与原理 |
| --- | ---: | --- |
| [浏览器与电脑操作](#browser) | 8 | [阅读分析](breakdowns/2026-09-18-browser.md) |
| [模型、技能与工具路由](#routing) | 8 | [阅读分析](breakdowns/2026-09-18-routing.md) |
| [代码质量与安全检查](#review) | 7 | [阅读分析](breakdowns/2026-09-18-review.md) |
| [数据分类与信息整理](#data) | 6 | [阅读分析](breakdowns/2026-09-18-data.md) |
| [内容与广告分析](#content) | 7 | [阅读分析](breakdowns/2026-09-18-content.md) |
| [网页与信息流过滤](#filter) | 2 | [阅读分析](breakdowns/2026-09-18-filter.md) |
| [上下文与记忆筛选](#memory) | 2 | [阅读分析](breakdowns/2026-09-18-memory.md) |
| [游戏决策与求解](#games) | 13 | [阅读分析](breakdowns/2026-09-18-games.md) |
| [NPC、驾驶与群体模拟](#simulation) | 7 | [阅读分析](breakdowns/2026-09-18-simulation.md) |
| [实时交互与组合实验](#interaction) | 6 | [阅读分析](breakdowns/2026-09-18-interaction.md) |
| [交易执行演示](#finance) | 1 | [阅读分析](breakdowns/2026-09-18-finance.md) |

[案例索引](cases/README.md) · [全部拆解](breakdowns/README.md) · [待补证据](inbox/README.md) · [收录流程](CONTRIBUTING.md)

## 全部应用列表

<a id="browser"></a>

### 浏览器与电脑操作（8）

要研究浏览器循环，优先看 Browser Use 与 Stagehand：前者明确 DOM 动态动作空间及文本回退，后者明确无障碍树和执行器分工。桌面应用可看 CoreML/OCR，Cua 当前公开预览可用于研究受约束的语义动作执行；需要长任务上下文则看 agent-desktop。语音入口和 QA 演示解决的是交互或验收问题，不宜只按速度排名。

[逐项优劣与原理对比](breakdowns/2026-09-18-browser.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**Browser Use · Ultrafast**](cases/2026-09-18-browser-use/README.md)<br>用 Jev 操作浏览器，演示自动查询航班。 | [6,891](https://x.com/gregpr07/status/2100411066966749359) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="160" alt="Browser Use · Ultrafast预览">](https://x.com/gregpr07/status/2100411066966749359)<br>[视频](https://x.com/gregpr07/status/2100411066966749359) |
| [**Stagehand 浏览器控制**](cases/2026-09-18-stagehand/README.md)<br>把页面无障碍树交给 Jev，由 Stagehand 执行选中的动作。 | [393](https://x.com/kylejeong/status/2100622054945095934) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100495119065722880/img/7A1mijkU3Z_Zj7PM.jpg" width="160" alt="Stagehand 浏览器控制预览">](https://x.com/kylejeong/status/2100622054945095934)<br>[视频](https://x.com/kylejeong/status/2100622054945095934) |
| [**Cua · jev-use**](cases/2026-09-18-cua-jev-use/README.md)<br>Cua Driver 的 Jev 语义动作选择预览，当前公开实现以浏览器表单为例。 | [1,162](https://x.com/trycua/status/2100649543079502213) | [<img src="https://pbs.twimg.com/media/HSb_nmIWYAAkGKa.jpg?name=orig" width="160" alt="Cua · jev-use预览">](https://x.com/trycua/status/2100649543079502213)<br>[图片](https://x.com/trycua/status/2100649543079502213) |
| [**CoreML + OCR 桌面点击**](cases/2026-09-18-coreml-ocr/README.md)<br>本地识别按钮和文字，只把文字候选交给 Jev 选点击目标。 | [564](https://x.com/milindlabs/status/2100631847155994852) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100629037790183424/img/NR6wQpZiC-xjCEsC.jpg" width="160" alt="CoreML + OCR 桌面点击预览">](https://x.com/milindlabs/status/2100631847155994852)<br>[视频](https://x.com/milindlabs/status/2100631847155994852) |
| [**OpenCode + agent-desktop**](cases/2026-09-18-agent-desktop/README.md)<br>LLM 保留上下文，Jev 负责选择桌面交互目标。 | [870](https://x.com/mdlahfir/status/2100359236924637349) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100358791321755648/img/t6Bd787flQiGeoJ_.jpg" width="160" alt="OpenCode + agent-desktop预览">](https://x.com/mdlahfir/status/2100359236924637349)<br>[视频](https://x.com/mdlahfir/status/2100359236924637349) |
| [**Kernel 浏览器演示**](cases/2026-09-18-kernel-browser/README.md)<br>Jev 配合 Kernel 的在线浏览器操作示例。 | [235](https://x.com/stevekrouse/status/2100321685081559542) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100321453455425537/img/hVYy_d3Nuw9XhSwg.jpg" width="160" alt="Kernel 浏览器演示预览">](https://x.com/stevekrouse/status/2100321685081559542)<br>[视频](https://x.com/stevekrouse/status/2100321685081559542) |
| [**语音控制浏览器**](cases/2026-09-18-voice-browser/README.md)<br>把语音指令转换成文字，让 Jev 选择浏览器动作。 | [1,829](https://x.com/moritzkremb/status/2100577979021832365) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100577954338373633/img/tbH43kHpUotE3hzK.jpg" width="160" alt="语音控制浏览器预览">](https://x.com/moritzkremb/status/2100577979021832365)<br>[视频](https://x.com/moritzkremb/status/2100577979021832365) |
| [**OpenCode 应用测试**](cases/2026-09-18-opencode-qa/README.md)<br>把 Jev 用在 OpenCode 的应用测试演示中。 | [1,133](https://x.com/Neriousy/status/2100287208166969746) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" width="160" alt="OpenCode 应用测试预览">](https://x.com/Neriousy/status/2100287208166969746)<br>[视频](https://x.com/Neriousy/status/2100287208166969746) |

<a id="routing"></a>

### 模型、技能与工具路由（8）

模型选择看 Eve 与 Ephraim 的演示；已有代理编排可以看 Firstmate 和本地分工。技能库检索看 Skillbox；想连接日常工具看 Coding Garden；Eve 工具代理展示局部替换；ai-cli 是统一接入入口。这些方案可以组合，并非互相替代。

[逐项优劣与原理对比](breakdowns/2026-09-18-routing.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**Eve 条件式模型路由**](cases/2026-09-18-eve-router/README.md)<br>按预设标准选择处理请求的模型。 | [821](https://x.com/eve/status/2100430918762832180) | [<img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" width="160" alt="Eve 条件式模型路由预览">](https://x.com/eve/status/2100430918762832180)<br>[图片](https://x.com/eve/status/2100430918762832180) |
| [**请求到模型路由器**](cases/2026-09-18-ephraim-router/README.md)<br>Jev 为输入请求选模型，并把请求转发给它。 | [1,503](https://x.com/ephraimduncan/status/2100454070536351824) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100454021852954624/img/hqULLONlXw40573G.jpg" width="160" alt="请求到模型路由器预览">](https://x.com/ephraimduncan/status/2100454070536351824)<br>[视频](https://x.com/ephraimduncan/status/2100454070536351824) |
| [**Firstmate 任务分派**](cases/2026-09-18-firstmate/README.md)<br>根据用户偏好选择 agent harness、模型和推理强度。 | [1,615](https://x.com/kunchenguid/status/2100468943853085061) | [<img src="https://pbs.twimg.com/media/HSYK_gbagAAqKqr.jpg?name=orig" width="160" alt="Firstmate 任务分派预览">](https://x.com/kunchenguid/status/2100468943853085061)<br>[图片](https://x.com/kunchenguid/status/2100468943853085061) |
| [**本地编码代理分工**](cases/2026-09-18-local-delegation/README.md)<br>在 Claude Code、Codex、OpenCode 之间按任务类型分派。 | [777](https://x.com/mdlahfir/status/2100314182201802811) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100314084990414848/img/iePXR9Edae7YVCT_.jpg" width="160" alt="本地编码代理分工预览">](https://x.com/mdlahfir/status/2100314182201802811)<br>[视频](https://x.com/mdlahfir/status/2100314182201802811) |
| [**Skillbox 技能选择**](cases/2026-09-18-skillbox/README.md)<br>给单一 MCP 技能库加入 Jev，筛选与请求相关的技能。 | [724](https://x.com/thekitze/status/2100556122570792999) | [<img src="https://pbs.twimg.com/media/HRidCpLaMAAqV-7.jpg?name=orig" width="160" alt="Skillbox 技能选择预览">](https://x.com/thekitze/status/2096598298220277856)<br>[图片](https://x.com/thekitze/status/2096598298220277856) |
| [**Coding Garden 工具助手**](cases/2026-09-18-coding-garden-assistant/README.md)<br>通过 Jev 选择搜索、天气、待办和 Home Assistant 等工具。 | [334](https://x.com/CodingGarden/status/2100665210419950031) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" width="160" alt="Coding Garden 工具助手预览">](https://x.com/CodingGarden/status/2100665210419950031)<br>[视频](https://x.com/CodingGarden/status/2100665210419950031) |
| [**Eve 工具调用代理**](cases/2026-09-18-eve-tool-agent/README.md)<br>把代理选择工具时的 LLM 推理环节换成 Jev。 | [1,117](https://x.com/oviniciuslana/status/2100457622407168509) | [<img src="https://pbs.twimg.com/media/HSZSqLGXwAA1jSL.jpg?name=orig" width="160" alt="Eve 工具调用代理预览">](https://x.com/oviniciuslana/status/2100457622407168509)<br>[图片](https://x.com/oviniciuslana/status/2100457622407168509) |
| [**ai-cli 终端决策入口**](cases/2026-09-18-ai-cli/README.md)<br>把是非判断、选项选择和评分接入终端代理。 | [874](https://x.com/ctatedev/status/2100584917092409479) | [<img src="https://pbs.twimg.com/media/HSbG2YLWkAAPqmU.jpg?name=orig" width="160" alt="ai-cli 终端决策入口预览">](https://x.com/ctatedev/status/2100584917092409479)<br>[图片](https://x.com/ctatedev/status/2100584917092409479) |

<a id="review"></a>

### 代码质量与安全检查（7）

PR 评审可对照 14 项检查、jev-review 和 jev-rabbit：分别重在明确风险与升级、迭代评分、自然语言团队规则。代码库分类器关注整体结构。命令安全、越狱预筛和上传判断对应不同防线，应分别评估漏报。

[逐项优劣与原理对比](breakdowns/2026-09-18-review.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**jev-review MCP**](cases/2026-09-18-jev-review/README.md)<br>让编码代理在工作中获取多项质量评分并迭代。 | [445](https://x.com/niazmorshed_/status/2100465662867218857) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100465308519759872/img/2uIG43VFGvWzku0s.jpg" width="160" alt="jev-review MCP预览">](https://x.com/niazmorshed_/status/2100465662867218857)<br>[视频](https://x.com/niazmorshed_/status/2100465662867218857) |
| [**14 项 PR 风险检查**](cases/2026-09-18-typed-pr-review/README.md)<br>一次评估 diff 的多种风险，并把不确定项升级复核。 | [1,927](https://x.com/redp314/status/2100585126652481915) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100585029533372416/img/ZcrsntW2yWgtB_HD.jpg" width="160" alt="14 项 PR 风险检查预览">](https://x.com/redp314/status/2100585126652481915)<br>[视频](https://x.com/redp314/status/2100585126652481915) |
| [**jev-rabbit 自然语言规则**](cases/2026-09-18-jev-rabbit/README.md)<br>用自然语言写代码审查规则的 PR bot 原型。 | [327](https://x.com/thekitze/status/2100616530275029139) | [<img src="https://pbs.twimg.com/media/HSbjmhQbQAA4G5A.jpg?name=orig" width="160" alt="jev-rabbit 自然语言规则预览">](https://x.com/thekitze/status/2100616530275029139)<br>[图片](https://x.com/thekitze/status/2100616530275029139) |
| [**代码库复杂度分类器**](cases/2026-09-18-codebase-classifier/README.md)<br>用 Jev 分类代码库，探索识别代理造成的过度设计。 | [1,165](https://x.com/ryanvogel/status/2100068006592123055) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100067392223076352/img/BqXd-11SCr3_ff8q.jpg" width="160" alt="代码库复杂度分类器预览">](https://x.com/ryanvogel/status/2100068006592123055)<br>[视频](https://x.com/ryanvogel/status/2100068006592123055) |
| [**fx auto mode 命令安全分类**](cases/2026-09-18-fx-safety/README.md)<br>在代理自动模式中评估命令安全分类器。 | [591](https://x.com/fazxes/status/2100300097695232164) | [<img src="https://pbs.twimg.com/media/HSW-E8wWgAAyw9O.jpg?name=orig" width="160" alt="fx auto mode 命令安全分类预览">](https://x.com/fazxes/status/2100300097695232164)<br>[图片](https://x.com/fazxes/status/2100300097695232164) |
| [**越狱提示预筛**](cases/2026-09-18-jailbreak-screen/README.md)<br>用 Jev 对疑似越狱提示做初步检测。 | [264](https://x.com/mayfer/status/2100343452865265747) | [<img src="https://pbs.twimg.com/media/HSXq9mqbsAAtHoT.jpg?name=orig" width="160" alt="越狱提示预筛预览">](https://x.com/mayfer/status/2100343452865265747)<br>[图片](https://x.com/mayfer/status/2100343452865265747) |
| [**资料上传判断器**](cases/2026-09-18-upload-check/README.md)<br>上传资料前，用 Jev 判断是否允许上传。 | [284](https://x.com/iwasakoya/status/2100471523358474709) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100471095627591680/img/jQewHJZ85th2EEv3.jpg" width="160" alt="资料上传判断器预览">](https://x.com/iwasakoya/status/2100471523358474709)<br>[视频](https://x.com/iwasakoya/status/2100471523358474709) |

<a id="data"></a>

### 数据分类与信息整理（6）

整理大批文本看邮件分类和 DuckDB；有生成前处理的流程看论文分类；需要处理不确定结果看 Jev + Kimi。银行描述是提取/归一化场景，客服意图是多问题判断；不要把分类、提取和预测的指标混用。

[逐项优劣与原理对比](breakdowns/2026-09-18-data.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**1kpapers 论文分类**](cases/2026-09-18-papers/README.md)<br>先摘要，再把 1,018 篇 AI 论文分入 24 个主题。 | [1,684](https://x.com/nutlope/status/2100426999546184123) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100425141947604992/img/AITyHwcOWq1jw-3Z.jpg" width="160" alt="1kpapers 论文分类预览">](https://x.com/nutlope/status/2100426999546184123)<br>[视频](https://x.com/nutlope/status/2100426999546184123) |
| [**DuckDB 语义分类扩展**](cases/2026-09-18-duckdb/README.md)<br>在 CSV、Parquet 或 DuckDB 表中逐行做 Jev 分类。 | [1,310](https://x.com/hamiltonulmer/status/2100370557405667768) | [<img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" width="160" alt="DuckDB 语义分类扩展预览">](https://x.com/hamiltonulmer/status/2100370557405667768)<br>[图片](https://x.com/hamiltonulmer/status/2100370557405667768) |
| [**500 封邮件分类**](cases/2026-09-18-email-batch/README.md)<br>批量判断邮件类别并展示结果。 | [3,161](https://x.com/rileybrown/status/2100404532119269426) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100403183533125632/img/54ZFO-CHvDeC-rw-.jpg" width="160" alt="500 封邮件分类预览">](https://x.com/rileybrown/status/2100404532119269426)<br>[视频](https://x.com/rileybrown/status/2100404532119269426) |
| [**Jev + Kimi 邮件反欺诈**](cases/2026-09-18-email-fraud/README.md)<br>先快速分类，再把低置信度邮件交给 Kimi K3。 | [542](https://x.com/nutlope/status/2100614659690713543) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100608348219478016/img/23vFEVMegwLrMa8g.jpg" width="160" alt="Jev + Kimi 邮件反欺诈预览">](https://x.com/nutlope/status/2100614659690713543)<br>[视频](https://x.com/nutlope/status/2100614659690713543) |
| [**银行流水收款方整理**](cases/2026-09-18-bank-payee/README.md)<br>从杂乱的银行交易描述中整理商户或收款方名称。 | [633](https://x.com/jlongster/status/2100179852053639236) | [<img src="https://pbs.twimg.com/media/HSVWcZ9WcAAcwPe.jpg?name=orig" width="160" alt="银行流水收款方整理预览">](https://x.com/jlongster/status/2100179852053639236)<br>[图片](https://x.com/jlongster/status/2100179852053639236) |
| [**日语客服升级意图**](cases/2026-09-18-support-intent/README.md)<br>判断客户是否要求人工服务、是否曾多次咨询。 | [351](https://x.com/ku_suke/status/2100392430805856469) | [<img src="https://pbs.twimg.com/media/HSYXuW5aoAAghbD.jpg?name=orig" width="160" alt="日语客服升级意图预览">](https://x.com/ku_suke/status/2100392430805856469)<br>[图片](https://x.com/ku_suke/status/2100392430805856469) |

<a id="content"></a>

### 内容与广告分析（7）

实时分析器适合写作反馈；收藏分位实验把预测目标定义得更具体；历史帖子分析适合描述性复盘；广告拆解服务素材整理。传播分类器与 X 算法模拟器的泛化证据较少。JevMeter 是按规则分析言论的仪表，不能当成已验证的事实核查器。

[逐项优劣与原理对比](breakdowns/2026-09-18-content.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**实时帖子潜力分析器**](cases/2026-09-18-live-viral/README.md)<br>停止输入 0.5 秒后，分析帖子的类别和传播潜力。 | [830](https://x.com/rileybrown/status/2100425868053008758) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100424897491070976/img/kKnsb68jNUZZzSBi.jpg" width="160" alt="实时帖子潜力分析器预览">](https://x.com/rileybrown/status/2100425868053008758)<br>[视频](https://x.com/rileybrown/status/2100425868053008758) |
| [**帖子传播分类器**](cases/2026-09-18-viral-classifier/README.md)<br>尝试区分更可能传播的帖子。 | [387](https://x.com/robj3d3/status/2100631889585606959) | [<img src="https://pbs.twimg.com/media/HSbxP15bMAA1LaU.jpg?name=orig" width="160" alt="帖子传播分类器预览">](https://x.com/robj3d3/status/2100631889585606959)<br>[图片](https://x.com/robj3d3/status/2100631889585606959) |
| [**X 传播评分模拟器**](cases/2026-09-18-x-algorithm-sim/README.md)<br>根据权重模拟帖子传播评分，并带公共信息流。 | [877](https://x.com/leojrr/status/2100470174130250127) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100467692117295104/img/01ZWSKAA75eSiFlc.jpg" width="160" alt="X 传播评分模拟器预览">](https://x.com/leojrr/status/2100470174130250127)<br>[视频](https://x.com/leojrr/status/2100470174130250127) |
| [**收藏率分位预测实验**](cases/2026-09-18-bookmark-prediction/README.md)<br>预测帖子在前后十天窗口中是否位于收藏量前 25%。 | [287](https://x.com/AM09_21/status/2100430480642642395) | [<img src="https://pbs.twimg.com/media/HSYtFVgaoAIPpi5.jpg?name=orig" width="160" alt="收藏率分位预测实验预览">](https://x.com/AM09_21/status/2100430480642642395)<br>[图片](https://x.com/AM09_21/status/2100430480642642395) |
| [**3,282 条历史帖子分析**](cases/2026-09-18-post-analytics/README.md)<br>给历史内容打标签，比较主题、语气和写作方式与点赞的关系。 | [262](https://x.com/iannuttall/status/2100668908227162567) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100668725737213952/img/m210oIkCyuGX5Dqr.jpg" width="160" alt="3,282 条历史帖子分析预览">](https://x.com/iannuttall/status/2100668908227162567)<br>[视频](https://x.com/iannuttall/status/2100668908227162567) |
| [**StealAds 广告拆解预览**](cases/2026-09-18-ad-analysis/README.md)<br>批量分析广告的钩子、形式、优惠、行动号召等要素。 | [1,678](https://x.com/TheMattBerman/status/2100654891756589230) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100654321792684032/img/cXvU50KmCe6QFu86.jpg" width="160" alt="StealAds 广告拆解预览预览">](https://x.com/TheMattBerman/status/2100654891756589230)<br>[视频](https://x.com/TheMattBerman/status/2100654891756589230) |
| [**JevMeter 言论指标仪表**](cases/2026-09-18-jevmeter/README.md)<br>按统一问题分析辩论、访谈等逐句文本。 | [1,017](https://x.com/chetaslua/status/2100473581251748216) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100473445868003328/img/1ukjahQYLgbIEmyI.jpg" width="160" alt="JevMeter 言论指标仪表预览">](https://x.com/chetaslua/status/2100473581251748216)<br>[视频](https://x.com/chetaslua/status/2100473581251748216) |

<a id="filter"></a>

### 网页与信息流过滤（2）

只想控制 X 信息流，比较自然语言 X 过滤器；想清理整个网页的广告、横幅和追加销售区域，看 Unclutter。前者分类帖子内容，后者判断页面元素；同一条规则很难在两个层次直接复用。

[逐项优劣与原理对比](breakdowns/2026-09-18-filter.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**自然语言 X 内容过滤器**](cases/2026-09-18-x-filter/README.md)<br>用自然语言规则隐藏或折叠 X 帖子。 | [950](https://x.com/marcelpociot/status/2100520134481735729) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100519256425140224/img/-A44e4qCo8mVP8ws.jpg" width="160" alt="自然语言 X 内容过滤器预览">](https://x.com/marcelpociot/status/2100520134481735729)<br>[视频](https://x.com/marcelpociot/status/2100520134481735729) |
| [**Unclutter 页面清理**](cases/2026-09-18-unclutter/README.md)<br>识别并清理广告、Cookie 横幅、追加销售等页面元素。 | [497](https://x.com/thekitze/status/2100595129874817340) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100595059041370112/img/cyfF5qMMKBPQTMAG.jpg" width="160" alt="Unclutter 页面清理预览">](https://x.com/thekitze/status/2100595129874817340)<br>[视频](https://x.com/thekitze/status/2100595129874817340) |

<a id="memory"></a>

### 上下文与记忆筛选（2）

工具调用压缩处理当前会话的历史；记忆检索筛选处理外部记忆的召回候选。两者都以减少输入为目标，适用位置不同。优先观察信息保留与任务质量，再比较 token 降幅。

[逐项优劣与原理对比](breakdowns/2026-09-18-memory.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**工具调用上下文压缩**](cases/2026-09-18-context-compaction/README.md)<br>给历史工具调用评分，删掉与当前任务无关的内容。 | [1,646](https://x.com/tamarajtran/status/2100694549362553153) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100694537672998912/img/OF8vottg6-45ZgNl.jpg" width="160" alt="工具调用上下文压缩预览">](https://x.com/tamarajtran/status/2100694549362553153)<br>[视频](https://x.com/tamarajtran/status/2100694549362553153) |
| [**记忆系统检索筛选**](cases/2026-09-18-memory-retrieval/README.md)<br>把 Jev 加入自建记忆系统，减少送入模型的内容。 | [335](https://x.com/moritzkremb/status/2100566009312940457) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100565973376061440/img/jeTib61RNpwXn853.jpg" width="160" alt="记忆系统检索筛选预览">](https://x.com/moritzkremb/status/2100566009312940457)<br>[视频](https://x.com/moritzkremb/status/2100566009312940457) |

<a id="games"></a>

### 游戏决策与求解（13）

马里奥三个实现并排比较：@faadilhshaik 展示基本接入，Jev/Qwen 版本明确相同结构化状态与五选一，PPO 对照展示实现投入。吃豆人体现规划/执行分层；宝可梦体现长期进度；棋局显示速度与棋力分离；魔方的确定性代码承担解法。其余演示适合研究动作空间，而不是据短片排通用能力榜。

[逐项优劣与原理对比](breakdowns/2026-09-18-games.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**官方 Doom 演示**](cases/2026-09-18-doom/README.md)<br>用 Jev 在游戏循环里持续做动作决策。 | [4,585](https://x.com/CompleteSkeptic/status/2099925687465570372) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2099924592534183936/img/hBGk8j8MRxBgPyg9.jpg" width="160" alt="官方 Doom 演示预览">](https://x.com/CompleteSkeptic/status/2099925687465570372)<br>[视频](https://x.com/CompleteSkeptic/status/2099925687465570372) |
| [**Super Mario · @faadilhshaik**](cases/2026-09-18-mario-faadhil/README.md)<br>把快速结构化决策接入超级马里奥。 | [2,686](https://x.com/faadilhshaik/status/2100086301894881578) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100085174826647552/img/6YMRQKKZYBPsW2oo.jpg" width="160" alt="Super Mario · @faadilhshaik预览">](https://x.com/faadilhshaik/status/2100086301894881578)<br>[视频](https://x.com/faadilhshaik/status/2100086301894881578) |
| [**Super Mario · Jev / Qwen 对照**](cases/2026-09-18-mario-comparison/README.md)<br>给 Jev 与 Qwen3.8 相同的结构化状态和五个动作选项。 | [284](https://x.com/karaage0703/status/2100569924238471355) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100567975317454849/img/UjFbLkeMH5RdOrlS.jpg" width="160" alt="Super Mario · Jev / Qwen 对照预览">](https://x.com/karaage0703/status/2100569924238471355)<br>[视频](https://x.com/karaage0703/status/2100569924238471355) |
| [**Super Mario · 1-1 关卡**](cases/2026-09-18-mario-ppo/README.md)<br>对照自己训练 PPO 的经历，展示 Jev 完成 1-1。 | [248](https://x.com/shantanugoel/status/2100455295801827769) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100454863335501825/img/RbCmluMnOGM4rHPb.jpg" width="160" alt="Super Mario · 1-1 关卡预览">](https://x.com/shantanugoel/status/2100455295801827769)<br>[视频](https://x.com/shantanugoel/status/2100455295801827769) |
| [**Astra + Jev 吃豆人**](cases/2026-09-18-pacman/README.md)<br>Astra 给策略，Jev 快速执行局部动作。 | [860](https://x.com/daniel_mac8/status/2100335929273524541) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100335842451492864/img/gC9HxZoXRIgMLKrW.jpg" width="160" alt="Astra + Jev 吃豆人预览">](https://x.com/daniel_mac8/status/2100335929273524541)<br>[视频](https://x.com/daniel_mac8/status/2100335929273524541) |
| [**贪吃蛇逐步决策**](cases/2026-09-18-snake/README.md)<br>每移动一步就请求 Jev 选择动作。 | [204](https://x.com/chenchengpro/status/2100516953496670430) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100516335155646464/img/pow4ZDKeRwkBVSvy.jpg" width="160" alt="贪吃蛇逐步决策预览">](https://x.com/chenchengpro/status/2100516953496670430)<br>[视频](https://x.com/chenchengpro/status/2100516953496670430) |
| [**俄罗斯方块**](cases/2026-09-18-tetris/README.md)<br>让 Jev 选择俄罗斯方块的游戏操作。 | [956](https://x.com/marcus_lowe/status/2100315518930661861) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100315393860730880/img/u0iH2SHQny2hkd4Q.jpg" width="160" alt="俄罗斯方块预览">](https://x.com/marcus_lowe/status/2100315518930661861)<br>[视频](https://x.com/marcus_lowe/status/2100315518930661861) |
| [**Jev Plays Pokémon**](cases/2026-09-18-pokemon/README.md)<br>持续运行的宝可梦代理，记录长期进展与调用成本。 | [220](https://x.com/0xBOYD/status/2100539883836018697) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100539819172544512/img/0EZ7yznRwL7qi4K8.jpg" width="160" alt="Jev Plays Pokémon预览">](https://x.com/0xBOYD/status/2100539883836018697)<br>[视频](https://x.com/0xBOYD/status/2100539883836018697) |
| [**杀戮尖塔 2 代打**](cases/2026-09-18-slay-spire/README.md)<br>用 Jev 替换较慢模型做卡牌游戏行动决策。 | [598](https://x.com/coolish/status/2100570517954838897) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100569632482746369/img/TPuOBiHYCWUWxNOc.jpg" width="160" alt="杀戮尖塔 2 代打预览">](https://x.com/coolish/status/2100570517954838897)<br>[视频](https://x.com/coolish/status/2100570517954838897) |
| [**5+0 国际象棋对局**](cases/2026-09-18-chess/README.md)<br>比较 Jev、Fable 与 Astra 在计时棋局中的表现。 | [1,985](https://x.com/aimlapi/status/2100372930282573876) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100371773275406336/img/NmHPy0pAprSsC6Gi.jpg" width="160" alt="5+0 国际象棋对局预览">](https://x.com/aimlapi/status/2100372930282573876)<br>[视频](https://x.com/aimlapi/status/2100372930282573876) |
| [**Subway Surfers 并行演示**](cases/2026-09-18-subway-runners/README.md)<br>展示 Jev 控制跑酷玩法，并行运行多局。 | [1,474](https://x.com/_MaxBlade/status/2100634359099232678) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100633400717565952/img/KlytLNSLCQA-yY2E.jpg" width="160" alt="Subway Surfers 并行演示预览">](https://x.com/_MaxBlade/status/2100634359099232678)<br>[视频](https://x.com/_MaxBlade/status/2100634359099232678) |
| [**魔方分阶段解法**](cases/2026-09-18-rubiks-cube/README.md)<br>代码实现初学者解法，Jev 判断当前属于哪种情况。 | [494](https://x.com/redp314/status/2100489858951073858) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100479486382809088/img/r6daGpDnvsCr3LyL.jpg" width="160" alt="魔方分阶段解法预览">](https://x.com/redp314/status/2100489858951073858)<br>[视频](https://x.com/redp314/status/2100489858951073858) |
| [**Mario Kart 64**](cases/2026-09-18-mario-kart/README.md)<br>用 Jev 进行马里奥赛车驾驶的游戏演示。 | [204](https://x.com/shreypandya/status/2100606445758898287) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100605130869784576/img/gdGysXaHMdzFOU8W.jpg" width="160" alt="Mario Kart 64预览">](https://x.com/shreypandya/status/2100606445758898287)<br>[视频](https://x.com/shreypandya/status/2100606445758898287) |

<a id="simulation"></a>

### NPC、驾驶与群体模拟（7）

NPC 需求选择适合研究角色行为，500 agents 演示关注并发吞吐。驾驶原型中，不暂停的模拟器更明确暴露延迟约束；无人机原型有代码线索。小镇与虚构 personas 属于叙事和构思工具，不能据合成人物反应预测真实世界。

[逐项优劣与原理对比](breakdowns/2026-09-18-simulation.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**按需求行动的 NPC**](cases/2026-09-18-npc-needs/README.md)<br>根据 NPC 当前需求，选择环境中合适的物品或工具。 | [201](https://x.com/m_iraji/status/2100394212743159944) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100394190643355648/img/52O-mJZSxj4IGHos.jpg" width="160" alt="按需求行动的 NPC预览">](https://x.com/m_iraji/status/2100394212743159944)<br>[视频](https://x.com/m_iraji/status/2100394212743159944) |
| [**500 个 3D agents**](cases/2026-09-18-npc-500/README.md)<br>在 3D 环境中测试多代理并行决策。 | [572](https://x.com/crislenta/status/2100457614073327754) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100457262372560897/img/zSIVGvaQhEZLMd9-.jpg" width="160" alt="500 个 3D agents预览">](https://x.com/crislenta/status/2100457614073327754)<br>[视频](https://x.com/crislenta/status/2100457614073327754) |
| [**“FSD”驾驶模拟演示**](cases/2026-09-18-driving-toy/README.md)<br>作者以重建 FSD 命名的车辆驾驶原型。 | [3,993](https://x.com/jpschroeder/status/2100347770867458384) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100347372844756992/img/CaExDBw3MTf0ia58.jpg" width="160" alt="“FSD”驾驶模拟演示预览">](https://x.com/jpschroeder/status/2100347770867458384)<br>[视频](https://x.com/jpschroeder/status/2100347770867458384) |
| [**不暂停的实时驾驶模拟**](cases/2026-09-18-realtime-driving/README.md)<br>模型思考时车辆仍在运动的驾驶控制实验。 | [270](https://x.com/SigGravitas/status/2100325221932958134) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100323655389474816/img/LLOAJ3wie1phk45K.jpg" width="160" alt="不暂停的实时驾驶模拟预览">](https://x.com/SigGravitas/status/2100325221932958134)<br>[视频](https://x.com/SigGravitas/status/2100325221932958134) |
| [**Jev 无人机仿真**](cases/2026-09-18-drone-sim/README.md)<br>在 MuJoCo 中用 Jev 选择无人机战术动作，飞行控制与安全反射由代码处理。 | [330](https://x.com/RomanSlack1/status/2100335978229690683) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100335726097494016/img/EljFdjduS88MyP9d.jpg" width="160" alt="Jev 无人机仿真预览">](https://x.com/RomanSlack1/status/2100335978229690683)<br>[视频](https://x.com/RomanSlack1/status/2100335978229690683) |
| [**Unstable Government 小镇**](cases/2026-09-18-unstable-government/README.md)<br>输入一条法规，让 40 位虚拟居民做出不同反应。 | [395](https://x.com/threepointone/status/2100576921629163848) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100576552849117184/img/fdEy6tirVMqee5pe.jpg" width="160" alt="Unstable Government 小镇预览">](https://x.com/threepointone/status/2100576921629163848)<br>[视频](https://x.com/threepointone/status/2100576921629163848) |
| [**150 位虚构用户意向**](cases/2026-09-18-synthetic-personas/README.md)<br>对虚构 personas 批量询问产品采用意愿。 | [792](https://x.com/ytiskw/status/2100474943154827344) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100474178457698304/img/DXGnHg-iUrEhsFgE.jpg" width="160" alt="150 位虚构用户意向预览">](https://x.com/ytiskw/status/2100474943154827344)<br>[视频](https://x.com/ytiskw/status/2100474943154827344) |

<a id="interaction"></a>

### 实时交互与组合实验（6）

TypeGPU 案例把本地感知与远端语义判断结合；Ask Jev 提供简单判断界面；词表和字符聊天展示选择循环；像素绘图与 RISC-jeV 展示将大量小判断组合成输出。这些适合作为机制启发，不应直接当成替代专用模型或程序的产品。

[逐项优劣与原理对比](breakdowns/2026-09-18-interaction.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**TypeGPU 实时语义特效**](cases/2026-09-18-typegpu-realtime/README.md)<br>本地视觉、语音推理后，由 Jev 决定灯光和后期效果。 | [251](https://x.com/reczko_konrad/status/2100646448324833512) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100644432211062784/img/iduKHYZdESQ5FBR7.jpg" width="160" alt="TypeGPU 实时语义特效预览">](https://x.com/reczko_konrad/status/2100646448324833512)<br>[视频](https://x.com/reczko_konrad/status/2100646448324833512) |
| [**Ask Jev**](cases/2026-09-18-ask-jev/README.md)<br>让用户输入问题，体验 Jev 的判断式交互。 | [423](https://x.com/waynesutton/status/2100487878992388279) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100486117325955072/img/_QailXRTsMGQ_atc.jpg" width="160" alt="Ask Jev预览">](https://x.com/waynesutton/status/2100487878992388279)<br>[视频](https://x.com/waynesutton/status/2100487878992388279) |
| [**有限词表聊天**](cases/2026-09-18-word-chat/README.md)<br>给 Jev 数百个单词及标点选项，逐步拼成文本。 | [2,644](https://x.com/hi_im_isaac_/status/2100408276949385668) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100407646226649088/img/qVPomAIwJ_lKpO2J.jpg" width="160" alt="有限词表聊天预览">](https://x.com/hi_im_isaac_/status/2100408276949385668)<br>[视频](https://x.com/hi_im_isaac_/status/2100408276949385668) |
| [**29 选项字符生成**](cases/2026-09-18-character-chat/README.md)<br>把下一字符拆成 29 个是非判断，再循环拼接文本。 | [866](https://x.com/ryanvogel/status/2100218045549412499) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100217973000617984/img/AFareJummI08B_QB.jpg" width="160" alt="29 选项字符生成预览">](https://x.com/ryanvogel/status/2100218045549412499)<br>[视频](https://x.com/ryanvogel/status/2100218045549412499) |
| [**并行像素绘图**](cases/2026-09-18-pixel-drawing/README.md)<br>通过像素层面的并行判断构成图像。 | [1,461](https://x.com/anshuc/status/2100246929611411501) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100245288183066624/img/ARkl8CTLZxp1KXSa.jpg" width="160" alt="并行像素绘图预览">](https://x.com/anshuc/status/2100246929611411501)<br>[视频](https://x.com/anshuc/status/2100246929611411501) |
| [**RISC-jeV 逻辑门实验**](cases/2026-09-18-riscv/README.md)<br>让 Jev 模拟逻辑门，接入 SERV RISC-V 实现。 | [208](https://x.com/i2cjak/status/2100454307405365673) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100454137695469568/img/pGRTotN_ZQaAuc4V.jpg" width="160" alt="RISC-jeV 逻辑门实验预览">](https://x.com/i2cjak/status/2100454307405365673)<br>[视频](https://x.com/i2cjak/status/2100454307405365673) |

<a id="finance"></a>

### 交易执行演示（1）

目前收录一个交易机器人，尚无同类样本可公平对比。它展示行情、决策和链上执行的连接方式；本库不据此评价盈利能力。

[逐项优劣与原理对比](breakdowns/2026-09-18-finance.md)

| 应用与简介 | 主帖点赞 | 图片 / 视频 |
| --- | ---: | --- |
| [**Monad / Kuru 交易机器人**](cases/2026-09-18-trading-bot/README.md)<br>从行情中选买卖动作，并接入链上订单簿执行。 | [4,142](https://x.com/jarrodwatts/status/2100356151468585346) | [<img src="https://pbs.twimg.com/amplify_video_thumb/2100355999064379392/img/BiAbeDjN57avf2VK.jpg" width="160" alt="Monad / Kuru 交易机器人预览">](https://x.com/jarrodwatts/status/2100356151468585346)<br>[视频](https://x.com/jarrodwatts/status/2100356151468585346) |

## 继续维护

新增线索先放 [待整理区](inbox/README.md)。正式案例在 [data/catalog.json](data/catalog.json) 中维护摘要、证据与媒体，再执行：

```sh
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

脚本只在本地生成 Markdown，不联网、不需要第三方依赖，不会自动刷新点赞。人工核对新快照后再更新取数时间。详见 [贡献流程](CONTRIBUTING.md) 与 [分类约定](docs/taxonomy.md)。

所有第三方图片、视频和代码权利归各自作者；收录不表示背书。本库以原创摘要和来源链接为主。
