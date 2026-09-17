# 案例索引

全部条目未复现；点赞为各自主帖的取数快照。图文总览见 [首页](../README.md)。

## 浏览器与电脑操作

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [Browser Use · Ultrafast](2026-09-18-browser-use/README.md) | 用 Jev 操作浏览器，演示自动查询航班。 | [6,891](https://x.com/gregpr07/status/2100411066966749359) |
| [Stagehand 浏览器控制](2026-09-18-stagehand/README.md) | 把页面无障碍树交给 Jev，由 Stagehand 执行选中的动作。 | [393](https://x.com/kylejeong/status/2100622054945095934) |
| [Cua · jev-use](2026-09-18-cua-jev-use/README.md) | Cua Driver 的 Jev 语义动作选择预览，当前公开实现以浏览器表单为例。 | [1,162](https://x.com/trycua/status/2100649543079502213) |
| [CoreML + OCR 桌面点击](2026-09-18-coreml-ocr/README.md) | 本地识别按钮和文字，只把文字候选交给 Jev 选点击目标。 | [564](https://x.com/milindlabs/status/2100631847155994852) |
| [OpenCode + agent-desktop](2026-09-18-agent-desktop/README.md) | LLM 保留上下文，Jev 负责选择桌面交互目标。 | [870](https://x.com/mdlahfir/status/2100359236924637349) |
| [Kernel 浏览器演示](2026-09-18-kernel-browser/README.md) | Jev 配合 Kernel 的在线浏览器操作示例。 | [235](https://x.com/stevekrouse/status/2100321685081559542) |
| [语音控制浏览器](2026-09-18-voice-browser/README.md) | 把语音指令转换成文字，让 Jev 选择浏览器动作。 | [1,829](https://x.com/moritzkremb/status/2100577979021832365) |
| [OpenCode 应用测试](2026-09-18-opencode-qa/README.md) | 把 Jev 用在 OpenCode 的应用测试演示中。 | [1,133](https://x.com/Neriousy/status/2100287208166969746) |

## 模型、技能与工具路由

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [Eve 条件式模型路由](2026-09-18-eve-router/README.md) | 按预设标准选择处理请求的模型。 | [821](https://x.com/eve/status/2100430918762832180) |
| [请求到模型路由器](2026-09-18-ephraim-router/README.md) | Jev 为输入请求选模型，并把请求转发给它。 | [1,503](https://x.com/ephraimduncan/status/2100454070536351824) |
| [Firstmate 任务分派](2026-09-18-firstmate/README.md) | 根据用户偏好选择 agent harness、模型和推理强度。 | [1,615](https://x.com/kunchenguid/status/2100468943853085061) |
| [本地编码代理分工](2026-09-18-local-delegation/README.md) | 在 Claude Code、Codex、OpenCode 之间按任务类型分派。 | [777](https://x.com/mdlahfir/status/2100314182201802811) |
| [Skillbox 技能选择](2026-09-18-skillbox/README.md) | 给单一 MCP 技能库加入 Jev，筛选与请求相关的技能。 | [724](https://x.com/thekitze/status/2100556122570792999) |
| [Coding Garden 工具助手](2026-09-18-coding-garden-assistant/README.md) | 通过 Jev 选择搜索、天气、待办和 Home Assistant 等工具。 | [334](https://x.com/CodingGarden/status/2100665210419950031) |
| [Eve 工具调用代理](2026-09-18-eve-tool-agent/README.md) | 把代理选择工具时的 LLM 推理环节换成 Jev。 | [1,117](https://x.com/oviniciuslana/status/2100457622407168509) |
| [ai-cli 终端决策入口](2026-09-18-ai-cli/README.md) | 把是非判断、选项选择和评分接入终端代理。 | [874](https://x.com/ctatedev/status/2100584917092409479) |

## 代码质量与安全检查

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [jev-review MCP](2026-09-18-jev-review/README.md) | 让编码代理在工作中获取多项质量评分并迭代。 | [445](https://x.com/niazmorshed_/status/2100465662867218857) |
| [14 项 PR 风险检查](2026-09-18-typed-pr-review/README.md) | 一次评估 diff 的多种风险，并把不确定项升级复核。 | [1,927](https://x.com/redp314/status/2100585126652481915) |
| [jev-rabbit 自然语言规则](2026-09-18-jev-rabbit/README.md) | 用自然语言写代码审查规则的 PR bot 原型。 | [327](https://x.com/thekitze/status/2100616530275029139) |
| [代码库复杂度分类器](2026-09-18-codebase-classifier/README.md) | 用 Jev 分类代码库，探索识别代理造成的过度设计。 | [1,165](https://x.com/ryanvogel/status/2100068006592123055) |
| [fx auto mode 命令安全分类](2026-09-18-fx-safety/README.md) | 在代理自动模式中评估命令安全分类器。 | [591](https://x.com/fazxes/status/2100300097695232164) |
| [越狱提示预筛](2026-09-18-jailbreak-screen/README.md) | 用 Jev 对疑似越狱提示做初步检测。 | [264](https://x.com/mayfer/status/2100343452865265747) |
| [资料上传判断器](2026-09-18-upload-check/README.md) | 上传资料前，用 Jev 判断是否允许上传。 | [284](https://x.com/iwasakoya/status/2100471523358474709) |

## 数据分类与信息整理

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [1kpapers 论文分类](2026-09-18-papers/README.md) | 先摘要，再把 1,018 篇 AI 论文分入 24 个主题。 | [1,684](https://x.com/nutlope/status/2100426999546184123) |
| [DuckDB 语义分类扩展](2026-09-18-duckdb/README.md) | 在 CSV、Parquet 或 DuckDB 表中逐行做 Jev 分类。 | [1,310](https://x.com/hamiltonulmer/status/2100370557405667768) |
| [500 封邮件分类](2026-09-18-email-batch/README.md) | 批量判断邮件类别并展示结果。 | [3,161](https://x.com/rileybrown/status/2100404532119269426) |
| [Jev + Kimi 邮件反欺诈](2026-09-18-email-fraud/README.md) | 先快速分类，再把低置信度邮件交给 Kimi K3。 | [542](https://x.com/nutlope/status/2100614659690713543) |
| [银行流水收款方整理](2026-09-18-bank-payee/README.md) | 从杂乱的银行交易描述中整理商户或收款方名称。 | [633](https://x.com/jlongster/status/2100179852053639236) |
| [日语客服升级意图](2026-09-18-support-intent/README.md) | 判断客户是否要求人工服务、是否曾多次咨询。 | [351](https://x.com/ku_suke/status/2100392430805856469) |

## 内容与广告分析

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [实时帖子潜力分析器](2026-09-18-live-viral/README.md) | 停止输入 0.5 秒后，分析帖子的类别和传播潜力。 | [830](https://x.com/rileybrown/status/2100425868053008758) |
| [帖子传播分类器](2026-09-18-viral-classifier/README.md) | 尝试区分更可能传播的帖子。 | [387](https://x.com/robj3d3/status/2100631889585606959) |
| [X 传播评分模拟器](2026-09-18-x-algorithm-sim/README.md) | 根据权重模拟帖子传播评分，并带公共信息流。 | [877](https://x.com/leojrr/status/2100470174130250127) |
| [收藏率分位预测实验](2026-09-18-bookmark-prediction/README.md) | 预测帖子在前后十天窗口中是否位于收藏量前 25%。 | [287](https://x.com/AM09_21/status/2100430480642642395) |
| [3,282 条历史帖子分析](2026-09-18-post-analytics/README.md) | 给历史内容打标签，比较主题、语气和写作方式与点赞的关系。 | [262](https://x.com/iannuttall/status/2100668908227162567) |
| [StealAds 广告拆解预览](2026-09-18-ad-analysis/README.md) | 批量分析广告的钩子、形式、优惠、行动号召等要素。 | [1,678](https://x.com/TheMattBerman/status/2100654891756589230) |
| [JevMeter 言论指标仪表](2026-09-18-jevmeter/README.md) | 按统一问题分析辩论、访谈等逐句文本。 | [1,017](https://x.com/chetaslua/status/2100473581251748216) |

## 网页与信息流过滤

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [自然语言 X 内容过滤器](2026-09-18-x-filter/README.md) | 用自然语言规则隐藏或折叠 X 帖子。 | [950](https://x.com/marcelpociot/status/2100520134481735729) |
| [Unclutter 页面清理](2026-09-18-unclutter/README.md) | 识别并清理广告、Cookie 横幅、追加销售等页面元素。 | [497](https://x.com/thekitze/status/2100595129874817340) |

## 上下文与记忆筛选

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [工具调用上下文压缩](2026-09-18-context-compaction/README.md) | 给历史工具调用评分，删掉与当前任务无关的内容。 | [1,646](https://x.com/tamarajtran/status/2100694549362553153) |
| [记忆系统检索筛选](2026-09-18-memory-retrieval/README.md) | 把 Jev 加入自建记忆系统，减少送入模型的内容。 | [335](https://x.com/moritzkremb/status/2100566009312940457) |

## 游戏决策与求解

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [官方 Doom 演示](2026-09-18-doom/README.md) | 用 Jev 在游戏循环里持续做动作决策。 | [4,585](https://x.com/CompleteSkeptic/status/2099925687465570372) |
| [Super Mario · @faadilhshaik](2026-09-18-mario-faadhil/README.md) | 把快速结构化决策接入超级马里奥。 | [2,686](https://x.com/faadilhshaik/status/2100086301894881578) |
| [Super Mario · Jev / Qwen 对照](2026-09-18-mario-comparison/README.md) | 给 Jev 与 Qwen3.8 相同的结构化状态和五个动作选项。 | [284](https://x.com/karaage0703/status/2100569924238471355) |
| [Super Mario · 1-1 关卡](2026-09-18-mario-ppo/README.md) | 对照自己训练 PPO 的经历，展示 Jev 完成 1-1。 | [248](https://x.com/shantanugoel/status/2100455295801827769) |
| [Astra + Jev 吃豆人](2026-09-18-pacman/README.md) | Astra 给策略，Jev 快速执行局部动作。 | [860](https://x.com/daniel_mac8/status/2100335929273524541) |
| [贪吃蛇逐步决策](2026-09-18-snake/README.md) | 每移动一步就请求 Jev 选择动作。 | [204](https://x.com/chenchengpro/status/2100516953496670430) |
| [俄罗斯方块](2026-09-18-tetris/README.md) | 让 Jev 选择俄罗斯方块的游戏操作。 | [956](https://x.com/marcus_lowe/status/2100315518930661861) |
| [Jev Plays Pokémon](2026-09-18-pokemon/README.md) | 持续运行的宝可梦代理，记录长期进展与调用成本。 | [220](https://x.com/0xBOYD/status/2100539883836018697) |
| [杀戮尖塔 2 代打](2026-09-18-slay-spire/README.md) | 用 Jev 替换较慢模型做卡牌游戏行动决策。 | [598](https://x.com/coolish/status/2100570517954838897) |
| [5+0 国际象棋对局](2026-09-18-chess/README.md) | 比较 Jev、Fable 与 Astra 在计时棋局中的表现。 | [1,985](https://x.com/aimlapi/status/2100372930282573876) |
| [Subway Surfers 并行演示](2026-09-18-subway-runners/README.md) | 展示 Jev 控制跑酷玩法，并行运行多局。 | [1,474](https://x.com/_MaxBlade/status/2100634359099232678) |
| [魔方分阶段解法](2026-09-18-rubiks-cube/README.md) | 代码实现初学者解法，Jev 判断当前属于哪种情况。 | [494](https://x.com/redp314/status/2100489858951073858) |
| [Mario Kart 64](2026-09-18-mario-kart/README.md) | 用 Jev 进行马里奥赛车驾驶的游戏演示。 | [204](https://x.com/shreypandya/status/2100606445758898287) |

## NPC、驾驶与群体模拟

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [按需求行动的 NPC](2026-09-18-npc-needs/README.md) | 根据 NPC 当前需求，选择环境中合适的物品或工具。 | [201](https://x.com/m_iraji/status/2100394212743159944) |
| [500 个 3D agents](2026-09-18-npc-500/README.md) | 在 3D 环境中测试多代理并行决策。 | [572](https://x.com/crislenta/status/2100457614073327754) |
| [“FSD”驾驶模拟演示](2026-09-18-driving-toy/README.md) | 作者以重建 FSD 命名的车辆驾驶原型。 | [3,993](https://x.com/jpschroeder/status/2100347770867458384) |
| [不暂停的实时驾驶模拟](2026-09-18-realtime-driving/README.md) | 模型思考时车辆仍在运动的驾驶控制实验。 | [270](https://x.com/SigGravitas/status/2100325221932958134) |
| [Jev 无人机仿真](2026-09-18-drone-sim/README.md) | 在 MuJoCo 中用 Jev 选择无人机战术动作，飞行控制与安全反射由代码处理。 | [330](https://x.com/RomanSlack1/status/2100335978229690683) |
| [Unstable Government 小镇](2026-09-18-unstable-government/README.md) | 输入一条法规，让 40 位虚拟居民做出不同反应。 | [395](https://x.com/threepointone/status/2100576921629163848) |
| [150 位虚构用户意向](2026-09-18-synthetic-personas/README.md) | 对虚构 personas 批量询问产品采用意愿。 | [792](https://x.com/ytiskw/status/2100474943154827344) |

## 实时交互与组合实验

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [TypeGPU 实时语义特效](2026-09-18-typegpu-realtime/README.md) | 本地视觉、语音推理后，由 Jev 决定灯光和后期效果。 | [251](https://x.com/reczko_konrad/status/2100646448324833512) |
| [Ask Jev](2026-09-18-ask-jev/README.md) | 让用户输入问题，体验 Jev 的判断式交互。 | [423](https://x.com/waynesutton/status/2100487878992388279) |
| [有限词表聊天](2026-09-18-word-chat/README.md) | 给 Jev 数百个单词及标点选项，逐步拼成文本。 | [2,644](https://x.com/hi_im_isaac_/status/2100408276949385668) |
| [29 选项字符生成](2026-09-18-character-chat/README.md) | 把下一字符拆成 29 个是非判断，再循环拼接文本。 | [866](https://x.com/ryanvogel/status/2100218045549412499) |
| [并行像素绘图](2026-09-18-pixel-drawing/README.md) | 通过像素层面的并行判断构成图像。 | [1,461](https://x.com/anshuc/status/2100246929611411501) |
| [RISC-jeV 逻辑门实验](2026-09-18-riscv/README.md) | 让 Jev 模拟逻辑门，接入 SERV RISC-V 实现。 | [208](https://x.com/i2cjak/status/2100454307405365673) |

## 交易执行演示

| 应用 | 简介 | 主帖点赞 |
| --- | --- | ---: |
| [Monad / Kuru 交易机器人](2026-09-18-trading-bot/README.md) | 从行情中选买卖动作，并接入链上订单簿执行。 | [4,142](https://x.com/jarrodwatts/status/2100356151468585346) |
