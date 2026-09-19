# Jev 全部案例：宣传主张与证据审核

**简体中文** | [English](2026-09-19-claims-audit.en.md)

审核完成：**2026-09-19 11:30:00 北京时间（UTC+08:00）**。范围为本库 **106 个案例、11 类**，基于目录提交 `2027762`，逐项复查主帖文字并核对重点项目的公开文档/代码。**没有独立运行这 106 个项目，也没有把缺证据当成造假。** 本报告评价公开主张与证据的距离，不评价作者诚信。

| 结论 | 数量 | 应该怎样理解 |
| --- | ---: | --- |
| [A · 功能/原理证据较清楚](#tier-a) | 18 | 有可检查的实现、明确输入输出或清楚限定的实验；不表示所有宣传数字成立或产品已成熟 |
| [B · 演示合理，效果仍待验证](#tier-b) | 78 | 主要是短视频、单次结果或私有自测；不足以确认泛化、准确率、长期成本，但也不足以认定夸大 |
| [C · 特定宣传明显超出证据](#tier-c) | 10 | 存在绝对保证、跨场景外推、无同条件证据的优劣断言，或与自有文档不一致的宣传；不表示整个项目不存在 |

**我的判断：最常被夸大的不是“能不能做出这个演示”，而是“是不是 Jev 单独完成、能否长期可靠、是否真的同质量快/便宜几十倍”。** “一次得分 99%”不是“准确率 99%”；500 个角色不等于 500 个角色都在每帧推理；删去 94% 内容也不等于保留 100% 有用信息。

## 判断依据

1. **主张要具体。** 实现截图证明有输出；源码支持一种实现方式；独立数据和重复对照才支持可靠性。点赞只用于收录门槛，不用于可信度打分。
2. **看清职责。** 官方 API 将状态和问题转成选项、评分或是非结果；观察、执行和复杂组合通常在周围代码中。[官方介绍](https://docs.typesafe.ai/introduction)
3. **不把分数当真值。** `confidence` 来自候选概率分布，并非测试集准确率；门槛仍需在具体任务上检验。[官方置信度文档](https://docs.typesafe.ai/confidence)
4. **注意版本和适用范围。** Jev 1.13 的官方限制明确列出精确计算、多步间接推理、对抗输入和链式文字生成等弱项。该文档只约束指定版本，不能证明某个组合系统必定失败。[Jev 1.13 限制](https://docs.typesafe.ai/model-jaggedness/jev-1.13)
5. **比较完整任务。** 要求相同输入、质量标准、计时范围，并计算前处理、其他模型、重试和执行器成本。不同基准或缩减任务不能只拿倍率排榜。

## 先看这几个容易误读的例子

- **税表分类器：** 有范围明确的零错分结果；另一批空白表格有 38 次低置信度失败。可以相信“公开了这组测试记录”，不能概括为任何税务文档都 100% 正确。[固定文档](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/README.md)
- **Browser Use / WebMCP：** 49 个任务各尝试 3 次，任务覆盖 49/49，但成功尝试 141/147；两个口径不同。这并不是“每次都成功”。[基准页](https://webmcp.com/benchmark)
- **Script.it：** 作者同时说明召回 75% 已确认 bug；更便宜的流程也漏掉更多问题，不能写成“同质量成本低 100 倍”。[作者原帖](https://x.com/liorshkiller/status/2100936106615140757)
- **Probably 和 shell 历史补全：** 分别公开托管页为缓存回放、演示历史为虚构数据。这些披露不等于造假，但页面播放速度或样例不能当日常实际使用效果。[Probably](https://probably-lang.southpolesteve.workers.dev) · [shell 文档](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/README.md)
- **Cua 状态纠正：** 本轮确认 #3916 已合并；#3943 已有可选视觉扩展实现但仍为草稿。旧目录的未合并状态是历史快照，不能作为今天否认实现存在的理由；同样也不能把合并当作跨平台通用能力认证。[#3916](https://github.com/trycua/cua/pull/3916) · [#3943](https://github.com/trycua/cua/pull/3943)

<a id="tier-c"></a>

## C · 特定宣传明显超出证据（10）

以下针对具体主张判定；同一项目仍可能包含有价值的真实实现。

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="cua-jev-use"></a>[Cua · jev-use](../cases/2026-09-18-cua-jev-use/README.md) | 快速电脑操作已经解决，并提供 macOS、Windows、Linux 开发预览。 | 语义动作示例确有实现；本轮确认 #3916 已于 2026-09-18 18:01:55 UTC 合并。#3943 已进展为可选视觉扩展实现，但仍是未合并草稿。 | 宣传把有限示例扩展成通用电脑操作结论；#3916 明言不发布 Driver 运行时能力、不认证原生桌面，最新候选未运行可选 live 工作流。不能沿用旧目录中“#3916 未合并”的状态。 | [来源 1](https://x.com/trycua/status/2100649543079502213) · [来源 2](https://github.com/trycua/cua/pull/3916) · [来源 3](https://github.com/trycua/cua/pull/3943) |
| <a id="coding-garden-assistant"></a>[Coding Garden 工具助手](../cases/2026-09-18-coding-garden-assistant/README.md) | 不用生成式 LLM 的聊天助手，响应即时且没有幻觉。 | 视频支持调用搜索、百科、天气等工具并展示来源的助手原型。 | 没有自由写作不等于永不出错：工具选错、参数选错或来源错误仍可能导致错误答案；来源未提供覆盖性证据支撑“无幻觉”。 | [来源 1](https://x.com/CodingGarden/status/2100665210419950031) |
| <a id="viral-classifier"></a>[帖子传播分类器](../cases/2026-09-18-viral-classifier/README.md) | 声称解决传播预测、永不奖励骗回复内容，且匹敌 Fable 5.1、快 100 倍。 | 补充帖提供 9,481 篇、207 位作者、每篇 61 个问题及约三次选对两次的自报结果。 | 缺少独立时间/作者划分、基线和对照配置；这些证据不足以支持“解决了”、永不误判或通用 100 倍性能结论。 | [来源 1](https://x.com/robj3d3/status/2100631889585606959) · [来源 2](https://x.com/robj3d3/status/2100722975645598191) |
| <a id="x-algorithm-sim"></a>[X 传播评分模拟器](../cases/2026-09-18-x-algorithm-sim/README.md) | 声称重建了 X 算法、采用真实权重且预测极准。 | 原帖只展示带评分与公共信息流的模拟界面。 | 没有权重出处、真实线上推荐模型等价性或预测误差测试；评分界面不能证明复刻推荐系统。 | [来源 1](https://x.com/leojrr/status/2100470174130250127) |
| <a id="jevmeter"></a>[JevMeter 言论指标仪表](../cases/2026-09-18-jevmeter/README.md) | 后续宣传称可实时 fact check，首帖则明确不是事实核查。 | 公开代码与文档支持转写后逐句打标签和渲染指标；README 与首帖明确说明分数不是事实核查。 | 后续“事实核查”越过了已实现功能：检测说法/修辞特征不等于对照外部证据判真伪。200 条自编测试的 99% 也只是预设问题分类成绩。 | [来源 1](https://x.com/chetaslua/status/2100473581251748216) · [来源 2](https://x.com/chetaslua/status/2100602714204049588) · [来源 3](https://github.com/ChetasLua/jevmeter/blob/cbf8e117b5b8835e3294c3a8ee652c7dfa737a9a/README.md) |
| <a id="context-compaction"></a>[工具调用上下文压缩](../cases/2026-09-18-context-compaction/README.md) | 即时压缩；补充使用帖报告约 1 秒把近百万 token 降到约 8.6 万。 | 有真实 API 集成及筛选实现；确实可以删减消息。代码送给 Jev 的状态有对话上下文，但省略工具输出正文。 | 体积下降不证明信息保真或后续任务质量。仓库还包含明确不调用 API 的录屏动画，不能拿该动画证明实时性能；另有 live demo，不能因此称整个项目造假。 | [来源 1](https://x.com/tamarajtran/status/2100694549362553153) · [来源 2](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/README.md) · [来源 3](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/state.ts) |
| <a id="mario-kart"></a>[Mario Kart 64](../cases/2026-09-18-mario-kart/README.md) | 作者宣称 Jev 玩 Mario Kart 很好，并说 Astra 电脑操作完全比不上。 | 现有证据支持一个 Jev 游戏演示。 | 原帖没有 Astra 同场景对照、相同输入与工具、圈速或碰撞数据；单方演示支撑不了对另一系统的明确优劣结论。 | [来源 1](https://x.com/shreypandya/status/2100606445758898287) |
| <a id="npc-500"></a>[500 个 3D agents](../cases/2026-09-18-npc-500/README.md) | 500 个实时 agent，平均 500ms、35 API calls/s；作者据此称智能延迟已不再是瓶颈。 | 原帖给出场景人数、请求平均延迟和总吞吐，但未定义每个 agent 的决策更新频率。 | 总计 35 calls/s 不是每个角色 35 次；若每角色一次调用，轮询 500 个约需 14.3 秒（条件推算，批处理未知）。这些指标不足以证明 500 个角色都在实时独立决策，更不能排除延迟瓶颈。 | [来源 1](https://x.com/crislenta/status/2100457614073327754) |
| <a id="driving-toy"></a>[“FSD”驾驶模拟演示](../cases/2026-09-18-driving-toy/README.md) | 作者说不到一小时重建 Tesla Full Self Driving。 | 现有材料支持搭建了驾驶演示原型。 | 把仿真原型叫重建 FSD 跨越了证据边界：没有实车感知、开放道路测试、长程成功率或同条件系统对照；不能据此推出汽车自动驾驶能力。 | [来源 1](https://x.com/jpschroeder/status/2100347770867458384) |
| <a id="ai-hedge-fund-backtest"></a>[AI Hedge Fund · 策略回测](../cases/2026-09-19-ai-hedge-fund-backtest/README.md) | 作者称获得前沿水平交易决策，比 LLM 快 100 倍且便宜 100 倍。 | 原帖和短视频支持策略、标的选择及 Jev 回测流程的演示。 | 未公布比较模型、同一任务和精度定义、费用与时间记录；约 7 秒流程视频无法支持质量等同与双重 100 倍改善。回测也不是实盘收益。 | [来源 1](https://x.com/virattt/status/2100959848623899005) |

<a id="tier-a"></a>

## A · 功能/原理证据较清楚（18）

A 只肯定表中明确支持的范围，不认证未测过的准确率、节省幅度或通用能力。

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="browser-use"></a>[Browser Use · Ultrafast](../cases/2026-09-18-browser-use/README.md) | 航班查询约 7 秒、$0.0039；补充 WebMCP 对照称完成全部 49 个任务。 | 固定版文档披露 DOM 动作选项、小模型填文本、结果独立检查和计时起点；公开基准区分任务完成与尝试成功。 | 7 秒从首次观测后计时；WebMCP 为 141/147 次成功，不是每次都成功，也不是 Jev 单独执行。费用中位数不能直接证明帖子另述的总费用降幅。 | [来源 1](https://x.com/gregpr07/status/2100411066966749359) · [来源 2](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/README.md) · [来源 3](https://webmcp.com/benchmark) |
| <a id="ai-cli"></a>[ai-cli 终端决策入口](../cases/2026-09-18-ai-cli/README.md) | 让能运行命令行的 agent 调用 Jev 的是非、选项与评分能力。 | 本轮 npm 文档明确 evaluate 子命令、三种类型、Jev 默认模型、JSON 输出、错误和超时语义；是可核查的接入工具。 | CLI 存在不代表其判断正确，文档也明确类型化输出不能保证正确；本轮没有安装运行。 | [来源 1](https://x.com/ctatedev/status/2100584917092409479) · [来源 2](https://www.npmjs.com/package/ai-cli) |
| <a id="support-intent"></a>[日语客服升级意图](../cases/2026-09-18-support-intent/README.md) | Jev 能对一条日语客服消息判断人工升级意图与此前是否已联系。 | 原帖完整给出同一条日语输入、两个问题及 98% Yes / 97% Yes 输出；文字内容确实明确提出转人工并已联系三次。 | 这里只确认这个清楚的单例；两个百分比是该次模型输出，不能写成日语客服准确率。 | [来源 1](https://x.com/ku_suke/status/2100392430805856469) |
| <a id="mario-comparison"></a>[Super Mario · Jev / Qwen 对照](../cases/2026-09-18-mario-comparison/README.md) | Jev 与 Qwen 在相同输入条件下玩马里奥。 | 作者明确：游戏信息先转为结构化数据，两者都五选一；没有把 Jev 表述为视觉模型。 | 只支持这份有限动作演示的设置透明；缺少重复运行统计，不能判断通用游戏能力排名。 | [来源 1](https://x.com/karaage0703/status/2100569924238471355) |
| <a id="chess"></a>[5+0 国际象棋对局](../cases/2026-09-18-chess/README.md) | 5+0 国际象棋中，Jev 对 Fable 超时胜、对 Astra 第 18 步被将死。 | 作者同时公开获胜原因、落后局面和失败；把速度优势与棋力区别开。 | 仅有限对局和作者报告，不能推断 Elo 或普遍胜率；A 表示结论范围与证据相符，不表示已复现。 | [来源 1](https://x.com/aimlapi/status/2100372930282573876) |
| <a id="rubiks-cube"></a>[魔方分阶段解法](../cases/2026-09-18-rubiks-cube/README.md) | 代码加 Jev 用 94 步复原魔方，模型耗时合计约 4 秒。 | 作者明确初学者解法写在代码中，Jev 判断当前属于哪种情况，代码检查选择；主动披露视频放慢。 | 94 次转动不等于 94 次模型请求；4 秒是模型时间，不是独立思考最优解或真实机械手复原时间。 | [来源 1](https://x.com/redp314/status/2100489858951073858) |
| <a id="drone-sim"></a>[Jev 无人机仿真](../cases/2026-09-18-drone-sim/README.md) | MuJoCo 无人机中用 Jev 选择局部动作，并公开成功和失败实验。 | 固定版 README 明确 Jev 读符号场景、只给战术建议；感知、飞控和可否决动作的安全层由代码负责，还披露单次成功及早期三种子无优势结果。 | 只支持有限仿真组合系统；不是 Jev 直接看图飞真机，也不是总体优于传统控制；隧道任务仍不可靠。 | [来源 1](https://x.com/RomanSlack1/status/2100335978229690683) · [来源 2](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/README.md) |
| <a id="word-chat"></a>[有限词表聊天](../cases/2026-09-18-word-chat/README.md) | 从几百个常见英文词和标点中选择，组成文本。 | 原作者主动说明有限词表，逐词选择循环与视频符合可组合分类器的机制。 | 能拼文字不等于拥有通用文本生成 API；词表表达、长文质量和效率未证实。 | [来源 1](https://x.com/hi_im_isaac_/status/2100408276949385668) |
| <a id="character-chat"></a>[29 选项字符生成](../cases/2026-09-18-character-chat/README.md) | 29 个是非问题选下一个字符，再循环；称用 Jev 做了 LLM。 | 正文完整解释 26 字母加空格、逗号、句号以及最高概率追加机制。 | “从第一原理造 LLM”是宽泛叫法；这里可靠的事实是字符选择循环，不是训练了新语言模型。 | [来源 1](https://x.com/ryanvogel/status/2100218045549412499) |
| <a id="youtube-sponsor-skip"></a>[YouTube 赞助片段跳过](../cases/2026-09-18-youtube-sponsor-skip/README.md) | Chrome 扩展识别 YouTube 赞助段落并跳过，约 0.005 美元/视频。 | 固定版本文档及 src/jev.js、src/live.js 公开字幕分窗、行号选择、程序映射时间和音频模式的转写分工，支持功能机制。 | A 只针对可检查实现。成本依模式/时长变化，音频模式另付 Deepgram；监听跳跃可能越界，README 提供评测方法但未给出已完成准确率结果。 | [来源 1](https://x.com/tdinh_me/status/2100793777103466615) · [来源 2](https://github.com/trungdq88/youtube-sponsor-detection/blob/de01f0568d043035889a296a61ce21e0accc8b16/README.md) · [来源 3](https://github.com/trungdq88/youtube-sponsor-detection/blob/de01f0568d043035889a296a61ce21e0accc8b16/src/jev.js) |
| <a id="probably-language"></a>[Probably · 用语义判断控制程序](../cases/2026-09-18-probably-language/README.md) | 将 Jev 判断嵌入 if/match/while，小语言串起工作流。 | 官网明示 TypeScript 解释器、Jev 判断、独立 LLM 写作，以及玩具语言限制。 | 线上示例只回放缓存；自定义输入需本地真实调用。回放速度不是模型性能，作者已清楚披露。 | [来源 1](https://x.com/southpolesteve/status/2100767781868150938) · [来源 2](https://probably-lang.southpolesteve.workers.dev) |
| <a id="hono-semantic-router"></a>[Hono JevRouter · 按请求含义分流](../cases/2026-09-18-hono-semantic-router/README.md) | 根据 HTTP 请求含义选择处理入口。 | 源码逐项判断路由描述并选首个过阈值匹配；文档披露概率独立、默认阈值和普通路由优先。 | 作者明确实验性质，不应作认证或授权；概率匹配不保证判断正确，并增加延迟与调用费用。 | [来源 1](https://x.com/yusukebe/status/2100871075743859182) · [来源 2](https://github.com/yusukebe/hono-jev-router/blob/04f6e103e1397bca659ab85c042011a1f14b679d/src/index.ts) · [来源 3](https://github.com/yusukebe/hono-jev-router) |
| <a id="shell-history-suggestions"></a>[终端历史命令 · 语义补全](../cases/2026-09-18-shell-history-suggestions/README.md) | 从 shell 历史选下一条命令。 | 固定文档给出最近 100 条不同历史、前缀筛选、Choice 与 Noul 门控和过期结果丢弃。 | 演示使用虚构历史，作者不称日常在用；文档报告 0.7–0.9 秒而非普遍百毫秒，未测长期接受率。 | [来源 1](https://x.com/thorstenball/status/2100858434904109099) · [来源 2](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/README.md) |
| <a id="json-render-ui"></a>[json-render · 用组件选择拼出界面](../cases/2026-09-19-json-render-ui/README.md) | 用 Jev 即时生成 UI，毫秒内渲染。 | 固定文档可核查组件选择、二阶段布局、代码装配 JSON；明确不是完整页面模板，也不让 Jev 写自由文本。 | “即时”不能外推到任意界面；候选、文本、14 元素/批和深度 4 有限制。未给同质量端到端速度对照。 | [来源 1](https://x.com/ctatedev/status/2101022101750571357) · [来源 2](https://github.com/vercel-labs/json-render/blob/3ad381881194e7011ad3ccd6d668033495a06c29/apps/web/lib/jev/README.md) |
| <a id="tax-doc-classifier"></a>[Tax Doc Classifier · 税务 PDF 页面识别](../cases/2026-09-19-tax-doc-classifier/README.md) | 对自有税务文档语料实现 100% 分类，费用约每页 0.001 美元，比原流程便宜 34 倍、快 6 倍。 | 固定文档公开文本提取与分类流程：314 张已填表页零错分/零严格失败；753 张空白表格零错分但 38 次低置信度失败，并披露无跨页缓存的 Sonnet 对照。 | 100% 只能按特定语料和指标解释；拒绝不能隐去。仅英文联邦表格、扫描件另需 OCR，34 倍是该旧流程对照，非所有 LLM 的通用差距。 | [来源 1](https://x.com/nedwize/status/2100973868324417852) · [来源 2](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/README.md) |
| <a id="codex-model-router"></a>[Codex Model Router · 每轮选择模型](../cases/2026-09-19-codex-model-router/README.md) | 把 Jev 接入 Codex 做逐轮路由；用户表示有效但过度选择 Sol，需要调参。 | 固定版公开代理、分层策略和低置信回退，用户原帖也主动披露失败与缓存未知，有限“路由接入可行”有依据。 | 仓库的约 60% 节省来自 237 轮回放，不能当该用户实时费用与相同质量的结果；是否选到足够强且最便宜模型未验证。 | [来源 1](https://x.com/antonioleivag/status/2100962426439000484) · [来源 2](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/README.md) |
| <a id="game-level-generation"></a>[Sprite Fusion · 实时生成跑酷地形](../cases/2026-09-19-game-level-generation/README.md) | Jev 在玩家前方实时生成跑酷地形。 | 作者文章给出有限地块参数、状态输入和一次四个表面的选择；代码摆放地块。五次请求实测 319–375ms，并明确不是低于 100ms。 | 这里的生成是有限参数组合，不是模型画素材或生成无限制完整游戏；五次测量不能证明长程可玩性。 | [来源 1](https://x.com/HugoDuprez/status/2100953089003921543) · [来源 2](https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev) |
| <a id="color-judgments"></a>[词语与颜色 · 16 色概率可视化](../cases/2026-09-19-color-judgments/README.md) | 让 Jev “理解颜色”，输出词语相关配色。 | 作者明确只有 16 个预设颜色，渲染其概率权重；调色板公开。 | 证据支持词语到固定调色板的联想，不支持视觉识色或色彩科学准确性。 | [来源 1](https://x.com/mattdesl/status/2100899669802963060) · [来源 2](https://x.com/mattdesl/status/2100907712984883362) · [来源 3](https://github.com/mattdesl/bitframes/blob/main/docs/palette.md) |

<a id="tier-b"></a>

## B · 演示合理，效果仍待验证（78）

### 浏览器与电脑操作

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="stagehand"></a>[Stagehand 浏览器控制](../cases/2026-09-18-stagehand/README.md) | 远程浏览器近乎即时完成该任务，花费 $0.001。 | 原帖提供视频并说明无障碍树输入、Jev 选动作、Stagehand 执行的循环。 | 没有任务集、重复次数和完整成本拆分；支持一次演示，不足以证明通用浏览器可靠性。 | [来源 1](https://x.com/kylejeong/status/2100622054945095934) |
| <a id="coreml-ocr"></a>[CoreML + OCR 桌面点击](../cases/2026-09-18-coreml-ocr/README.md) | 不发屏幕像素给远端、约 90ms 每次判断，电脑操作非常快。 | 作者明确本机 CoreML 分割和 OCR 读标签，只有文字交给 Jev；这与文本决策机制一致。 | 90ms 是单次判断，不是 OCR、点击、重新观测的总延迟；“没有延迟”是宣传修辞。未证明完整任务成功率，也不是完全离线。 | [来源 1](https://x.com/milindlabs/status/2100631847155994852) |
| <a id="agent-desktop"></a>[OpenCode + agent-desktop](../cases/2026-09-18-agent-desktop/README.md) | Jev 加速 OpenCode 的电脑操作。 | 作者说明 LLM 管记忆、agent-desktop 取状态，Jev 选元素，附操作视频。 | 快照编码方式和可复现对照未知；不能由此推断 Jev 直接看截图或独立完成任务。 | [来源 1](https://x.com/mdlahfir/status/2100359236924637349) |
| <a id="kernel-browser"></a>[Kernel 浏览器演示](../cases/2026-09-18-kernel-browser/README.md) | Jev 与 Kernel 结合，浏览器操作很快。 | 有该组合的短视频和作者提供的体验入口。 | 没有公开观测编码、动作约束、失败处理或测评；快速一例不代表复杂任务效果。 | [来源 1](https://x.com/stevekrouse/status/2100321685081559542) |
| <a id="voice-browser"></a>[语音控制浏览器](../cases/2026-09-18-voice-browser/README.md) | 语音控制浏览器；约 300ms 返回判断，单次 $0.0002。 | 原帖明确先转写，再把文字给 Jev，随后浏览器执行；作者另有教程。 | 数字不包含完整收音、转写和执行链路；句子未说完就动作也可能是提前识别，不能等同完整指令均已理解。 | [来源 1](https://x.com/moritzkremb/status/2100577979021832365) |
| <a id="opencode-qa"></a>[OpenCode 应用测试](../cases/2026-09-18-opencode-qa/README.md) | Jev 加 OpenCode 会使应用测试很快。 | 原帖自称小演示并提供操作视频。 | 未公开断言、失败判据和缺陷检出率；自动点击快与测试有效是两件事。 | [来源 1](https://x.com/Neriousy/status/2100287208166969746) |
| <a id="runlayer-adversarial-testing"></a>[Runlayer · 并行浏览器对抗测试](../cases/2026-09-18-runlayer-adversarial-testing/README.md) | 并行浏览器对抗测试尝试破坏每次发布，成本很低。 | 视频有多窗口，作者补充 Runlayer agents、agent-browser 和 Chromium 组合。 | 窗口数量不是路径覆盖；没有缺陷复现、断言、误报或全成本明细。“几分钱”没有固定分母。 | [来源 1](https://x.com/rafalwilinski/status/2100882207879434359) |
| <a id="sac-calendar-computer-use"></a>[Sac · Codex + Jev 操作 Mac 日历](../cases/2026-09-18-sac-calendar-computer-use/README.md) | 加入 Jev 判断的 Codex 日历操作更快、更流畅，token 接近。 | 原帖限定同一添加 Mac 日历事件任务并提供并排视频；作者回复称是在现有 computer use 上做判断。 | 只是一轮，观测编码、计时起点、模型配置和重复次数未知；不能把被引用的通用十倍说法当本例实测。 | [来源 1](https://x.com/Saccc_c/status/2100864907046768890) |
| <a id="ego-product-decisions"></a>[ego lite · Amazon 商品筛选](../cases/2026-09-19-ego-product-decisions/README.md) | 20 次商品决策 3.71 秒，对照 Sol 54.45 秒，两边 10/10。 | 主帖明确同一任务，公开组合为 ego lite、Jev、DeepSeek Flash，并有视频结果面板。 | 20 个决策与 10/10 是不同口径；评分标准、重复和模型分工未知，不能宣传成 Jev 单独完成购物或普遍快十五倍。 | [来源 1](https://x.com/ego_agent/status/2100970015977804008) |
| <a id="tester-army-e2e"></a>[Tester Army · Web / 手机端测试演示](../cases/2026-09-19-tester-army-e2e/README.md) | 在构建支持 Web、手机等平台的开源代理测试框架，即将提供。 | 原帖提供约 70 秒演示，明确仍在构建而非宣称正式发行。 | 未核到可运行发布、跨平台断言和缺陷检出评测；视频不证明稳定自动测试能力。 | [来源 1](https://x.com/o_kwasniewski/status/2100966838905585687) |

### 模型、技能与工具路由

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="eve-router"></a>[Eve 条件式模型路由](../cases/2026-09-18-eve-router/README.md) | 依据条件超快选择模型。 | 截图支持按标准输出候选模型这一具体试验。 | 没有公开准确率、回退策略或总费用与质量对照。 | [来源 1](https://x.com/eve/status/2100430918762832180) |
| <a id="ephraim-router"></a>[请求到模型路由器](../cases/2026-09-18-ephraim-router/README.md) | Jev 找出最适合请求的模型，再转发。 | 视频展示请求经选择后交给模型的流程。 | “最适合”需要质量与成本标签；现有来源没有统一评测或最优性依据。 | [来源 1](https://x.com/ephraimduncan/status/2100454070536351824) |
| <a id="firstmate"></a>[Firstmate 任务分派](../cases/2026-09-18-firstmate/README.md) | 达到 Fable 水平的分派质量，速度约 10 倍；整体分派费用下降 71%。 | 作者明确限定 25 个任务与 Fable 选择一致，并把 Jev 局部费用与含上层工具调用的整体分派费用分开。 | 一致率不是执行任务的正确率；样本小且私有。可接受为作者的小样本分派对照，不能扩大到整个 agent 的同等质量。 | [来源 1](https://x.com/kunchenguid/status/2100468943853085061) |
| <a id="local-delegation"></a>[本地编码代理分工](../cases/2026-09-18-local-delegation/README.md) | 解决本地 harness/model 分派；不同难度任务交给不同代理。 | 作者描述确定性 hook 与 Jev 分类组合，并给出三类路由例子。 | 没有公布准确率或任务结果；确定性触发器并不能使模型判断确定无误。“解决”不足以作为产品成熟度证据。 | [来源 1](https://x.com/mdlahfir/status/2100314182201802811) |
| <a id="skillbox"></a>[Skillbox 技能选择](../cases/2026-09-18-skillbox/README.md) | 从原先多轮找技能，变成直接返回相关技能。 | 作者陈述已集成按查询选技能，具体用途符合有限候选匹配。 | “30 轮”没有统计定义；所用预览来自更早介绍，不是本次 Jev 集成实测画面，也无技能召回率。 | [来源 1](https://x.com/thekitze/status/2100556122570792999) |
| <a id="eve-tool-agent"></a>[Eve 工具调用代理](../cases/2026-09-18-eve-tool-agent/README.md) | 替换工具选择环节后，费用约降至 1/8，时间与质量接近。 | 作者说明仅替换工具调用选择，在既有代理里保留其他模型，并明确是早期结果。 | 样本和质量评分缺失；不能解读成 Jev 在所有 agent 任务中同质省八倍。 | [来源 1](https://x.com/oviniciuslana/status/2100457622407168509) |

### 代码质量与安全检查

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="jev-review"></a>[jev-review MCP](../cases/2026-09-18-jev-review/README.md) | 实验性 MCP 插件让代理评分、改进、再评分。 | 作者明确标为实验，并展示这一反馈循环。 | 缺少独立质量标签和改进前后盲评；分数升高可能只是迎合评分，不保证代码更正确。 | [来源 1](https://x.com/niazmorshed_/status/2100465662867218857) |
| <a id="typed-pr-review"></a>[14 项 PR 风险检查](../cases/2026-09-18-typed-pr-review/README.md) | 14 项 PR 风险检查约半秒，6 个 PR 每个 $0.00007，称约比 Claude 便宜 200 倍。 | 来源明确只展示 6 个 PR，规则检查与程序 verdict 分工清楚，不确定关键项升级人工或大模型。 | 这是特定风险分类，未证明与完整 Claude 评审相同的漏洞召回；200 倍只可保留为作者该演示费用对照。 | [来源 1](https://x.com/redp314/status/2100585126652481915) |
| <a id="jev-rabbit"></a>[jev-rabbit 自然语言规则](../cases/2026-09-18-jev-rabbit/README.md) | 用英文规则做 PR 评审，计划当晚公开。 | 原帖展示开发中原型并明确未来发布。 | 未核到实际发行或测试；不能把预告当已发布产品，也不能证明自然语言规则总是可准确执行。 | [来源 1](https://x.com/thekitze/status/2100616530275029139) |
| <a id="codebase-classifier"></a>[代码库复杂度分类器](../cases/2026-09-18-codebase-classifier/README.md) | 代码库分类器可能解决 agent 过度设计的问题。 | 有分类演示，作者用“可能”表达推测。 | 分类标准、输入范围和对照缺失；识别复杂度不等于能提出安全重构或减少过度设计。 | [来源 1](https://x.com/ryanvogel/status/2100068006592123055) |
| <a id="fx-safety"></a>[fx auto mode 命令安全分类](../cases/2026-09-18-fx-safety/README.md) | 安全命令分类比 Luna 快 5–18 倍且更准。 | 有作者基准结果截图，任务明确为 fx auto mode 安全分类。 | 没有公开完整数据、危险命令漏放率及分布；平均准确率不足以证明可以安全自动放行。 | [来源 1](https://x.com/fazxes/status/2100300097695232164) |
| <a id="jailbreak-screen"></a>[越狱提示预筛](../cases/2026-09-18-jailbreak-screen/README.md) | 初步越狱检测优于 Luna，认为以后可接近 100%。 | 作者明确说是早期尝试，并把接近满分写成未来期望。 | 现有截图不能支持已达 100%；已知越狱模式与未知攻击的泛化需要分开。 | [来源 1](https://x.com/mayfer/status/2100343452865265747) |
| <a id="upload-check"></a>[资料上传判断器](../cases/2026-09-18-upload-check/README.md) | 制作了判断资料是否可以上传的小工具。 | 交互视频支持有上传许可分类这一具体原型。 | 组织政策、敏感字段覆盖及漏检率未知；没有声称或证据证明能替代正式权限控制。 | [来源 1](https://x.com/iwasakoya/status/2100471523358474709) |
| <a id="eslint-rule-judgments"></a>[按 ESLint 规则说明判断代码](../cases/2026-09-18-eslint-rule-judgments/README.md) | 只给 ESLint 规则说明，约九成判断正确。 | 作者补充明确使用生成的小代码片段，而非整仓库分析。 | 尚缺公开样本、各规则表现和独立测试；九成不能当真实 PR 正确率，更不等同确定性 lint。 | [来源 1](https://x.com/mizchi/status/2100765201385869434) |
| <a id="opencode-intent-permissions"></a>[OpenCode · 意图感知权限插件](../cases/2026-09-18-opencode-intent-permissions/README.md) | 视频里用自然语言禁止访问 Google 以外域名，拦住代理尝试的各条路径。 | 原帖是视频尝试的结果；现行 0.1.1 文档公开规则顺序、置信门槛和 ask 回退，保留原生 deny/ask。 | 文档明确 Code Mode execute 可绕过插件。应理解为若干拦截演示，不能扩展成无法绕过的网络安全边界。 | [来源 1](https://x.com/OpeOginni/status/2100702649834188855) · [来源 2](https://www.npmjs.com/package/oc-auto-perms) |
| <a id="code-comment-scoring"></a>[代码注释 · 准确性与实用性评分](../cases/2026-09-18-code-comment-scoring/README.md) | 判断代码注释是否准确、有用。 | 两个截图样例把“正确但复述代码”和“描述错误”区分开，作者回复也承认只是初筛。 | 仅两个简单例子，0–100 分是输出分数而非测试准确率；复杂代码能力与评分校准未证明。 | [来源 1](https://x.com/markjaquith/status/2100359340087501296) |
| <a id="script-code-review"></a>[Script.it · 先筛问题再写评审](../cases/2026-09-19-script-code-review/README.md) | 内部评审约快 50 倍、便宜 100 倍，零误报且召回 75% bug。 | 作者明确先评分 diff、命中才生成说明；零误报限定曾被开发者反驳的问题集合，同时披露原 ensemble 找到更多 bug。 | 私有数据规模与标注不公开；不能把零误报扩大为永不误报，也不是等召回率的成本比较。作者已说明损失，故不判夸张。 | [来源 1](https://x.com/liorshkiller/status/2100936106615140757) |

### 数据分类与信息整理

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="papers"></a>[1kpapers 论文分类](../cases/2026-09-18-papers/README.md) | 分类 1,018 篇论文只花 0.08 美元、每篇中位延迟 256ms。 | 原帖明确先由 DeepSeek 生成摘要，再让 Jev 从 24 类里选择，并分别披露摘要与分类费用。 | 端到端推理约 4.07 美元；作者还在评估 Jev 标签，不能把已上线网站当作 Jev 分类质量验证。 | [来源 1](https://x.com/nutlope/status/2100426999546184123) |
| <a id="duckdb"></a>[DuckDB 语义分类扩展](../cases/2026-09-18-duckdb/README.md) | DuckDB 扩展约 10 秒分类 1,000 行，比 LLM 更好。 | 原帖提供扩展结果截图，文本行分类与 SQL 集成是明确、合理的任务。 | 没有标注准确率、模型对照或并发配置；吞吐量和便利性不能证明普遍优于所有 LLM。 | [来源 1](https://x.com/hamiltonulmer/status/2100370557405667768) |
| <a id="email-batch"></a>[500 封邮件分类](../cases/2026-09-18-email-batch/README.md) | 数秒分类 500 封邮件，成本 0.035 美元。 | 有批量分类视频，任务输入与输出范围明确。 | 邮件构成、标签、正确率和计时边界未公开；目前仅支持一次批量演示与作者成本报告。 | [来源 1](https://x.com/rileybrown/status/2100404532119269426) |
| <a id="email-fraud"></a>[Jev + Kimi 邮件反欺诈](../cases/2026-09-18-email-fraud/README.md) | Jev 与 Kimi 组合在 100 封邮件中答对 96 封，约 0.07 美元。 | 原帖披露 50 封正常、50 封欺诈，31 封低分升级给 Kimi，以及 16 秒总时长和分项费用。 | 96% 属于组合流程；95% 阈值不是已经校准的欺诈概率，也没有真实低欺诈基率下的误报率。 | [来源 1](https://x.com/nutlope/status/2100614659690713543) |
| <a id="bank-payee"></a>[银行流水收款方整理](../cases/2026-09-18-bank-payee/README.md) | 首次尝试银行商户名整理已达到约 95% 的期望效果。 | 原帖有多组交易说明与输出名称，支持名称清洗实验的存在。 | 作者措辞是粗略完成度，不是标注测试集 95% 准确率；候选生成和名称构造尚不明确。 | [来源 1](https://x.com/jlongster/status/2100179852053639236) |
| <a id="predictive-spreadsheet"></a>[按列名意图评分的电子表格](../cases/2026-09-18-predictive-spreadsheet/README.md) | 列名写 Urgency，就能在约 100ms 按行理解意图并分级。 | 演示呈现列名、文本行和评级互动，支持按语义判别替代手写标签的原型。 | 问题如何构建、评分是否稳定、计时覆盖多少行未公开；不能推广成任意列名都能获得可靠公式。 | [来源 1](https://x.com/dabit3/status/2100780008193020049) |
| <a id="email-speed-race"></a>[邮件分类 · 四模型速度对照](../cases/2026-09-18-email-speed-race/README.md) | 邮件分类对照中 Jev 明显快于 Luna、Sonnet、Flash。 | 视频界面并列展示相同邮件行与计时，支持存在任务级速度演示。 | 模型完整版本、并发、批处理和正确率未核清；仅凭进度条不能形成通用速度排名。 | [来源 1](https://x.com/usutaku_channel/status/2100829343954173965) |
| <a id="calorie-notebook"></a>[Calorie Notebook · 文字饮食记录](../cases/2026-09-18-calorie-notebook/README.md) | Jev 驱动的饮食记录可以即时返回热量和营养数值。 | 视频显示文本食物条目与数值汇总；作者补充承认 LLM 热量估算通常很差，主要比较速度/价格。 | 未公开数据库、份量解释或误差评测；可以确认交互原型，不能确认营养数值可靠。 | [来源 1](https://x.com/thekitze/status/2100857642566758849) · [来源 2](https://x.com/thekitze/status/2100865980788318254) |
| <a id="box-incident-triage"></a>[Box · 事故报告分级归档](../cases/2026-09-19-box-incident-triage/README.md) | 判断事故报告是否影响客户及严重度，再自动归档并写元数据。 | 原帖逐步描述 Box 取文件、Jev 判断、工作流移动文件及设置元数据，视频与任务边界相符。 | 严重性标准、误判率和权限控制未公开；保险、贷款等只是作者举的未来设想。 | [来源 1](https://x.com/levie/status/2101007708044574906) |
| <a id="snack-scoring"></a>[NoSugarForKids · 零食多维评分](../cases/2026-09-19-snack-scoring/README.md) | 28 秒对 3,000 个儿童零食做多标准评分，成本 0.11 美元。 | 原帖提供评分视频及对应商品网站，支持商品批量判断的实验。 | 评分问题、营养数据来源和校准不明；低成本打分不能证明商品营养判断正确。 | [来源 1](https://x.com/nikunj/status/2101006585481073093) |
| <a id="gmail-intent-search"></a>[Gmail · 按意图找邮件](../cases/2026-09-19-gmail-intent-search/README.md) | Jev 能按意图搜索 Gmail，体验优于仅靠语义初筛。 | 原帖展示一句需求到邮件结果的互动；大收件箱先 embeddings 的做法明确只是建议。 | 没有候选召回范围与人工相关性评测；不能确认大规模收件箱表现或把建议写成已实现流程。 | [来源 1](https://x.com/dabit3/status/2100960281769738433) |
| <a id="ocr-image-organizer"></a>[OCR + Jev · 图片归类](../cases/2026-09-19-ocr-image-organizer/README.md) | OCR 与 Jev 约 40 秒分类 900 张图片。 | 作者明确区分 OCR 与 Jev，提供图片整理视频；文字提取后分类的机制合理。 | 类别、OCR 耗时是否计入和正确率不明；这不是 Jev 直接看图的证据。 | [来源 1](https://x.com/fayazara/status/2100953838891192789) |
| <a id="downloads-organizer"></a>[macOS Downloads · 按规则归档文件](../cases/2026-09-19-downloads-organizer/README.md) | 只用 Jev 识别下载文件是否符合规则，再移动并命名。 | 原帖演示自定义规则与下载目录监控，文件判断和代码执行分工可行。 | 文本提取、最终文件名来源和撤销机制未披露；“无其他 LLM”不等于 Jev 能直接生成任意名称。 | [来源 1](https://x.com/marcelpociot/status/2100906882365788167) |

### 内容与广告分析

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="live-viral"></a>[实时帖子潜力分析器](../cases/2026-09-18-live-viral/README.md) | 停笔 0.5 秒后实时分析帖子的传播潜力并分类。 | 视频与作者说明支持输入变化后更新分类和评分；作者明确承认仍需收集 X 数据、正在实验。 | 界面即时反馈不证明未来传播预测有效；因作者主动限定实验性质，不将整个项目直接判为夸大。 | [来源 1](https://x.com/rileybrown/status/2100425868053008758) |
| <a id="bookmark-prediction"></a>[收藏率分位预测实验](../cases/2026-09-18-bookmark-prediction/README.md) | 在作者自己的约 5,000 条帖子上，预测高收藏分位优于对照且费用低 200 倍。 | 目标定义具体：是否进入前后各十天窗口的收藏量前 25%；原帖给出个人样本时间范围和成本/正确率图。 | 没有充分披露训练测试划分、提示和运行配置；历史窗口含未来是标签定义，不足以直接判定泄漏，也不足以证明面向未来泛化。 | [来源 1](https://x.com/AM09_21/status/2100430480642642395) |
| <a id="post-analytics"></a>[3,282 条历史帖子分析](../cases/2026-09-18-post-analytics/README.md) | 分析 3,282 条历史帖子，得出教学内容更受欢迎及内容组合建议。 | 原帖说明每篇八个问题，并报告教学帖点赞中位数 150、总体 44，属于可理解的历史分组分析。 | 原始标签与帖子表未公开；历史相关性不能证明照着建议发帖就能增长。 | [来源 1](https://x.com/iannuttall/status/2100668908227162567) |
| <a id="ad-analysis"></a>[StealAds 广告拆解预览](../cases/2026-09-18-ad-analysis/README.md) | 40 秒拆解 37 品牌的 724 条广告，推理只花 0.09 美元。 | 原帖有广告分析视频，列出钩子、形式、CTA 等具体标签维度。 | 没有人工标注一致率；素材采集/转写成本不明确，且作者说未来才集成 StealAds/MCP。 | [来源 1](https://x.com/TheMattBerman/status/2100654891756589230) |
| <a id="seo-internal-links"></a>[SEO 内链推荐 · 从已有文字找链接](../cases/2026-09-19-seo-internal-links/README.md) | 586 页内链处理用 45.1 秒、0.21 美元；按页比 Opus 便宜约 190 倍。 | 原帖说明 8,790 次是非判断、584 个链接及 139 页不链接，并公开对照只完成 21 页就停止。 | 190 倍按已处理页面单价计算，整站 43 美元是外推；任务质量、候选范围和并发未对齐，不能作为同质量整站实测比价或 SEO 收益证明。 | [来源 1](https://x.com/borjafat/status/2101018783976722479) |
| <a id="maxfusion-ad-classifier"></a>[MaxFusion · 广告素材分类](../cases/2026-09-19-maxfusion-ad-classifier/README.md) | 19 秒、0.12 美元分类 1,891 条广告并做账号分析。 | 原帖指明用户旅程阶段和广告风格等维度，有独立视频。 | 缺人工标签评测和素材前处理成本；批次更大不能直接证明比 StealAds 更好，MCP 仍是预告。 | [来源 1](https://x.com/OriSilver/status/2100941251478458871) |

### 网页与信息流过滤

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="x-filter"></a>[自然语言 X 内容过滤器](../cases/2026-09-18-x-filter/README.md) | 用自然语言规则实时隐藏或折叠 X 帖子。 | 原帖给出扩展演示，隐藏/折叠是具体可理解的输出动作。 | 没有误杀率、漏检率或长期成本；“未来的广告拦截器”属于愿景，不能当作成熟过滤保证。 | [来源 1](https://x.com/marcelpociot/status/2100520134481735729) |
| <a id="unclutter"></a>[Unclutter 页面清理](../cases/2026-09-18-unclutter/README.md) | 用 Jev 清理广告、cookie 提示、促销和弹窗，免费且自备密钥。 | 原帖展示页面清理并明确 BYOK，支持原型的有限功能描述。 | 没有跨网站误删与兼容性验证；免费扩展不等于模型调用免费，当前记录未核清可复现的源码版本。 | [来源 1](https://x.com/thekitze/status/2100595129874817340) |
| <a id="x-reply-cleanup"></a>[X 回复清理 · 标记低价值评论](../cases/2026-09-19-x-reply-cleanup/README.md) | 清理低价值回复，并让纠正后的误判影响下次判断。 | 主帖视频与补充帖展示标记和纠正功能，支持有限的人机反馈流程。 | 实际处理是隐藏还是屏蔽未核清；更正进入下一次上下文不等于训练模型，也没有准确率证明。 | [来源 1](https://x.com/iannuttall/status/2100888635943883244) · [来源 2](https://x.com/iannuttall/status/2100896325290074606) |

### 上下文与记忆筛选

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="memory-retrieval"></a>[记忆系统检索筛选](../cases/2026-09-18-memory-retrieval/README.md) | token 减少 94%，记忆检索快 2–3 倍。 | 原作者明确称只是一次快速测试，并有对应视频和教程。 | 未给召回率、遗漏信息或后续任务正确率；只能当作者这次测试结果，不能当默认提升比例。 | [来源 1](https://x.com/moritzkremb/status/2100566009312940457) |
| <a id="compact-adviser"></a>[Compact Adviser · 判断何时压缩上下文](../cases/2026-09-19-compact-adviser/README.md) | 在安全任务边界建议压缩；用 40 个会话调优。 | 公开了双问题、阈值曲线、提示模式和 96 个检查点的评估流程，比单纯压缩比例更可检查。 | 原作者说对私有评估集反复调提示；未见独立留出集，不能据此证明未见会话上的安全性或保真率。 | [来源 1](https://x.com/kunchenguid/status/2101032677940117875) · [来源 2](https://github.com/kunchenguid/compact-adviser/blob/17e441a81e9dbacfef15756b7d0cca66461a9b98/README.md) |

### 游戏决策与求解

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="doom"></a>[官方 Doom 演示](../cases/2026-09-18-doom/README.md) | 官方展示 Jev 玩 Doom，称约 10 次调用/秒、7 美元/小时。 | 原帖将其称为代码加 AI 的演示，并报告一组运行频率和费用。 | 未披露状态编码、长期胜率或完整计费日志；不能由游戏画面推断 Jev 原生看图、拥有通用实时游戏能力。 | [来源 1](https://x.com/CompleteSkeptic/status/2099925687465570372) |
| <a id="mario-faadhil"></a>[Super Mario · @faadilhshaik](../cases/2026-09-18-mario-faadhil/README.md) | Jev 玩 Super Mario，作者认为快推理适合实时任务。 | 约 31 秒演示支持存在游戏适配原型；作者提到结构化输出。 | 状态输入、暂停机制、失败次数和多关卡结果未知；成功片段不等于稳定通关。 | [来源 1](https://x.com/faadilhshaik/status/2100086301894881578) |
| <a id="mario-ppo"></a>[Super Mario · 1-1 关卡](../cases/2026-09-18-mario-ppo/README.md) | 作者称 PPO 训练调试一周，Jev 接入不到半小时达到 World 1-1 目标，并预测其成为强大游戏 RL 模型。 | 原帖明确比较个人搭建经历与同一个关卡目标；这可作为开发便利性的作者经验。 | 一周训练与调用现成模型不是同条件性能实验；开发耗时也不能证明强化学习能力或泛化。原帖的未来预测应视为意见。 | [来源 1](https://x.com/shantanugoel/status/2100455295801827769) |
| <a id="pacman"></a>[Astra + Jev 吃豆人](../cases/2026-09-18-pacman/README.md) | Astra 定策略，Jev 毫秒级执行，合作玩吃豆人。 | 作者明确区分两个模型的职责，没有声称 Jev 独自规划整局。 | 毫秒级是局部动作陈述；完整模型成本、胜率、规划调用次数及延迟分布未给。 | [来源 1](https://x.com/daniel_mac8/status/2100335929273524541) |
| <a id="snake"></a>[贪吃蛇逐步决策](../cases/2026-09-18-snake/README.md) | 每一步调用 Jev；200 次请求花 0.02 美元，据此估算 1 美元走一万步。 | 固定每步一次请求时，所述费用的线性换算一致；有游戏循环视频。 | 这是作者本次请求均价的外推，未给账单或长度/成功率；上下文和价格改变后不能沿用。 | [来源 1](https://x.com/chenchengpro/status/2100516953496670430) |
| <a id="tetris"></a>[俄罗斯方块](../cases/2026-09-18-tetris/README.md) | Jev 玩俄罗斯方块，作者用改变一切表达兴奋。 | 短视频和原帖支持一个落块控制演示。 | 没有说明选落点还是连续按键，也没有得分、延迟或基线；改变一切是感想而非可检验性能结论。 | [来源 1](https://x.com/marcus_lowe/status/2100315518930661861) |
| <a id="pokemon"></a>[Jev Plays Pokémon](../cases/2026-09-18-pokemon/README.md) | 8,000 多次决策、1.21 美元，拿到首枚徽章并到月见山。 | 作者报告明确的局部进度，给出持续展示入口；并未宣称整款游戏通关。 | 费用和进度未独立复现，记忆、导航辅助及失败记录未知；首枚徽章不能升级为自主通关能力。 | [来源 1](https://x.com/0xBOYD/status/2100539883836018697) · [来源 2](https://jev-plays-pokemon.standardagents.ai) |
| <a id="slay-spire"></a>[杀戮尖塔 2 代打](../cases/2026-09-18-slay-spire/README.md) | Jev 代打杀戮尖塔 2，每次思考约 0.7 秒，作者称超人类游戏速度。 | 原帖支持快速行动的短演示与一次延迟报告。 | 超人类指宣传中的操作节奏，没有人类对照或胜率；行动快不代表策略强，也未展示完整对局。 | [来源 1](https://x.com/coolish/status/2100570517954838897) |
| <a id="subway-runners"></a>[Subway Surfers 并行演示](../cases/2026-09-18-subway-runners/README.md) | Jev 同时玩 50 局跑酷，称超人类速度、此次不足 1 美分。 | 视频与文字支持多实例游戏演示及作者费用报告。 | 原版客户端、改写环境、批处理和运行时长未说明；50 个实例不等于 50 台手机视觉控制，超人类没有匹配的人类测试。 | [来源 1](https://x.com/_MaxBlade/status/2100634359099232678) |
| <a id="minecraft-hybrid"></a>[Minecraft · Jev、Astra 与本地策略](../cases/2026-09-18-minecraft-hybrid/README.md) | Jev 与 Astra 合作玩 Minecraft，应对多只僵尸。 | 作者回复披露 Astra 长远规划、Jev 即时判断、本地策略负责移动瞄准；另贴原速版本。 | 主视频约加速两倍，不能拿播放速度当模型实时反应；不能把整套系统的战斗能力归于 Jev，也没有通关证据。 | [来源 1](https://x.com/wuyang_zhou/status/2100727660875808913) · [来源 2](https://x.com/wuyang_zhou/status/2100727859400622158) · [来源 3](https://x.com/wuyang_zhou/status/2100741909790490764) |
| <a id="flappy-bird"></a>[Flappy Bird · 飞行避障](../cases/2026-09-19-flappy-bird/README.md) | Jev 轻松玩 Flappy Bird。 | 约 49 秒视频支持该游戏的控制原型演示。 | 没有状态格式、是否暂停、失败局、多局分数和成本；轻松是观感，不能推断稳定水平。 | [来源 1](https://x.com/thymikee/status/2100937960115838984) |

### NPC、驾驶与群体模拟

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="npc-needs"></a>[按需求行动的 NPC](../cases/2026-09-18-npc-needs/README.md) | Jev 依据 NPC 需求挑选环境中满足需求的工具。 | 作者描述了需求到工具选择的流程，也承认 utility AI 和 smart objects 已能完成这类任务。 | 未给相对规则方案的收益、冲突解决或长期行为一致性；不能把模型参与等同于更聪明的 NPC。 | [来源 1](https://x.com/m_iraji/status/2100394212743159944) |
| <a id="realtime-driving"></a>[不暂停的实时驾驶模拟](../cases/2026-09-18-realtime-driving/README.md) | Jev 接入驾驶模拟器，模拟器在模型思考期间不暂停。 | 作者明确区分真正按墙钟运行与事后拼接成实时视频，并明确说是模拟器。 | 仍缺少原始日志、多场景碰撞率和长时测试；这支持实时仿真控制主张，不能外推实车安全。 | [来源 1](https://x.com/SigGravitas/status/2100325221932958134) |
| <a id="unstable-government"></a>[Unstable Government 小镇](../cases/2026-09-18-unstable-government/README.md) | Claude 编候选反应，Jev 为 40 个虚构居民选回应，小镇演出结果。 | 作者明确把它当作互动娱乐，说明两个模型的分工。 | 没有真实居民数据或政策效果验证；不能把合成剧情用于预测现实政策。原帖自身没有作这种外推。 | [来源 1](https://x.com/threepointone/status/2100576921629163848) |
| <a id="synthetic-personas"></a>[150 位虚构用户意向](../cases/2026-09-18-synthetic-personas/README.md) | 150 位虚构用户各答 12 道产品意向题，约 5 秒、1.8 日元。 | 作者明确使用虚构人物，并说明跨地区网络延迟；任务量和成本是本次作者报告。 | 没有真实用户调查、购买行为或校准；只能产出基于人物设定的合成意见，不能作为市场需求证据。 | [来源 1](https://x.com/ytiskw/status/2100474943154827344) |

### 实时交互与组合实验

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="typegpu-realtime"></a>[TypeGPU 实时语义特效](../cases/2026-09-18-typegpu-realtime/README.md) | 3 路神经网络推理与渲染实时运行，Jev 添加语义判断。 | 原帖清楚列出 Moonshine、YOLO26、DepthART、ruNNtime、TypeGPU 与 Jev 的分工，非 Jev 单模型视觉能力。 | 组合系统的演示可信度高于“Jev 直接看听”说法，但缺代码核对、完整延迟与各模块对照。 | [来源 1](https://x.com/reczko_konrad/status/2100646448324833512) |
| <a id="ask-jev"></a>[Ask Jev](../cases/2026-09-18-ask-jev/README.md) | 输入任意问题，让 Jev 给判断。 | 有网站入口与判断界面视频，原文也明确它给判断而非长回答。 | 没有知识准确率或事实核查评测；任意提问入口不等于任意问题都能可靠判断。 | [来源 1](https://x.com/waynesutton/status/2100487878992388279) · [来源 2](https://askjev.ai) |
| <a id="pixel-drawing"></a>[并行像素绘图](../cases/2026-09-18-pixel-drawing/README.md) | 并行预测像素来画图。 | 有小图生成演示，组合许多像素判断在机制上可成立。 | 分辨率、调色板、提示和总体成本未知；不能从短片推断通用高质量图像生成。 | [来源 1](https://x.com/anshuc/status/2100246929611411501) |
| <a id="riscv"></a>[RISC-jeV 逻辑门实验](../cases/2026-09-18-riscv/README.md) | 让 Jev 执行 RISC-V 指令、加法和位运算。 | 作者明说用 Jev 判断逻辑门，再借 SERV 实现组成指令，而非 Jev 原生 CPU。 | 未核查 Jev 到 SERV 的实现与稳定性；这是组合计算实验，没有效率优于确定性逻辑的证据。 | [来源 1](https://x.com/i2cjak/status/2100454307405365673) · [来源 2](https://jev-riscv-production.up.railway.app) |
| <a id="predictive-launcher"></a>[意图预测启动器](../cases/2026-09-18-predictive-launcher/README.md) | 逐键读意图，约 100ms 把刚下载的 PDF 排在首位。 | 视频及原帖支持特定文件查询交互。 | 没有文件规模、计时边界或错误查询集；模型置信度很高不等于检索百分之百正确。 | [来源 1](https://x.com/dabit3/status/2100756930054504776) |
| <a id="live-commerce-assistant"></a>[实时电商导购与头像表情](../cases/2026-09-18-live-commerce-assistant/README.md) | Jev 与 gpt-live-1 在对话中推荐商品并改变头像表情。 | 作者明确是简易接客演示，列出第二个模型。 | 不能把全套效果归给 Jev，也未证明表情联动是 Jev 独有；推荐质量与库存一致性未知。 | [来源 1](https://x.com/rinte0321/status/2100736454850908344) |
| <a id="emoji-suggestions"></a>[实时表情候选](../cases/2026-09-18-emoji-suggestions/README.md) | 约 100–200ms；3 与 200 个候选响应相近。 | 有明确候选规模和短视频，原文是这一演示的观察。 | 缺重复计时、网络条件和语义准确率；两种规模相近不证明任意规模都恒定。 | [来源 1](https://x.com/riku720720/status/2100705558512963602) |
| <a id="voice-gesture-canvas"></a>[语音与手指指向控制画布](../cases/2026-09-18-voice-gesture-canvas/README.md) | 边说边指即可操作画布。 | 作者回复说明记录关键词出现时的指向，再拆成少量问题，并主动承认并不完美。 | 感知库、操作成功率与错误恢复未披露；一个成功演示不证明一般人机交互已经解决。 | [来源 1](https://x.com/jackcheng/status/2100729670991802386) · [来源 2](https://x.com/jackcheng/status/2100769017115902136) |
| <a id="cnvs-voice-gate"></a>[CNVS · 无唤醒词语音指令门控](../cases/2026-09-19-cnvs-voice-gate/README.md) | 持续监听，无唤醒词也能分辨电脑指令和闲聊。 | 具体视频展示语音意图门控，概率判断接到外部语音和动作流程在机制上合理。 | 长期误触发/漏触发和转写组件未知；“环境式 Jarvis”仍是愿景，不是完整自主助手能力证据。 | [来源 1](https://x.com/_MaxBlade/status/2100967959879471519) |

### 交易与历史回测

| 项目 | 被审核的主张 | 证据实际支持什么 | 不能推出什么 / 缺口 | 依据 |
| --- | --- | --- | --- | --- |
| <a id="trading-bot"></a>[Monad / Kuru 交易机器人](../cases/2026-09-18-trading-bot/README.md) | Jev 根据价格流选买卖，由 Monad/Kuru 执行，作者称每约 300ms 区块交易。 | 原帖说明决策与订单执行的分工，给出展示入口；未声称策略赚钱。 | 未独立核验链上订单、持续端到端延迟或净收益；区块间隔不等于每次模型决策加成交的总时延。 | [来源 1](https://x.com/jarrodwatts/status/2100356151468585346) · [来源 2](https://jev-trader.vercel.app/) |
| <a id="danish-stock-backtest"></a>[丹麦股票 · 全年历史策略实验](../cases/2026-09-19-danish-stock-backtest/README.md) | Jev 在丹麦股票 2025 全年 239 个交易日实验，810 万 token、0.32 美元。 | 原帖交代历史区间与新闻、市场等输入；应按历史实验理解，未报告经过核验的收益。 | 没有逐时信息截断、前视偏差控制、手续费或滑点；token 费用不是完整策略成本，不能理解为真实全年实盘获利。 | [来源 1](https://x.com/tommy_jepsen/status/2100939646653903063) |
| <a id="nifty-trading"></a>[Nifty 日内交易 · 含止损的账户演示](../cases/2026-09-19-nifty-trading/README.md) | 作者称真实 Kotak 账户以 10 万卢比、5 倍杠杆做 Nifty 日内交易，当天触及 1,000 卢比止损。 | 原帖主动披露早盘盈利后触及止损，没有把早盘盈利包装成全天盈利。 | 真实账户、成交、净收益和风控执行未独立核验；一次亏损披露也不能证明长期风控可靠或可获利。 | [来源 1](https://x.com/IndraVahan/status/2100929105382564113) |

## 审核范围、时效与使用建议

106 个原始主帖文本均通过 FxTwitter 公共接口重新读取，该接口可能缓存 X 内容；另核对重点补充帖、公开仓库、npm 文档和官方页面。表内依据指向原始帖子或具体文档。目录原有点赞快照与收录时间保留，不把这次审核当成所有性能数字都已复测。**本轮没有逐帧看完全部视频、运行应用或独立复现作者计时。** 英文版用较简洁的行文保留同一分档与核心依据。

如果用来挑研究方向，可以先读 A 档的 18 项学习可检查的机制；B 档的 78 项当成值得补实验的线索；C 档的 10 项保留已展示功能，但应删去或改写超出证据的宣传。没有哪个等级等于可以免测上线。本轮证据也没有证明某个交易策略可盈利、复刻了生产级 FSD，或代理能够普遍零错误运行。

[来源索引](README.md) · [应用总览](../README.md)
