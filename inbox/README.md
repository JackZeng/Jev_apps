# 待整理与待补证据

**简体中文** | [English](README.en.md)

本页不计入 README 正式案例总数，也不把转载点赞替代原作者的应用主帖门槛。以下首批线索发现于 2026-09-18；后续发现按小节日期标注。

| 线索 | 原帖 | 当前缺口 / 下一步 |
| --- | --- | --- |
| Foreman 编码代理监督 | [@JoshARosen](https://x.com/JoshARosen/status/2100573432089866717) | 第四轮已核对[固定版本文档](https://github.com/thruwire/foreman/blob/2c439828b9fe45ee5d40f6f57be81f7ff1f8a140/README.md)与文件树：Jev 评估进展、测试和偏移，Python 策略决定后续动作；仍缺对应运行图/视频，文档流程图不当作运行证明 |
| jev-mcp | [@jkudish](https://x.com/jkudish/status/2100413576284712999) | 原帖已超过 200 赞；需补实际运行图、工具接口与对应具体用途，避免只收包名 |
| 汽车零配件 SKU 匹配 | [@marcoporracin](https://x.com/marcoporracin/status/2100571522540695705) | 有明确业务陈述，但未取得对应图片/视频；还需匹配规则和错误样例 |
| 安全流水线对照 | [@grichadev](https://x.com/grichadev/status/2100437998571860087) | 有结果图，但任务细节和测试集不足，不能有效比较具体应用 |
| Jev QA tester | [@krzysztof_moch](https://x.com/krzysztof_moch/status/2100513641556549700) | 有视频但文字极简；需核清与已收 OpenCode 测试演示的实现差异及断言机制 |
| 跨平台电脑操作 | [@awlevin](https://x.com/awlevin/status/2100262612428894676) | 已取得 200+ 赞原帖；需继续拆视频/讨论串中的观测接口与 20x/155x 对照条件 |
| Neel 驾驶演示 | [主帖](https://x.com/Neel490/status/2100400923826606523) · [更新](https://x.com/Neel490/status/2100440723837313349) | 两个帖子已有媒体，需核清独立实现还是其他驾驶项目的演示，避免重复计数 |
| Almost Certain | [@nathanwchan](https://x.com/nathanwchan/status/2100096510436475293) | 有在线入口和图，需先确认具体交互任务及与 Ask Jev 的差异 |
| 实时评分 playground | [@stevekrouse](https://x.com/stevekrouse/status/2100287368221659289) | 有演示与入口，需核对评分维度和输入输出后再建立独立应用记录 |

下一次收录先检查这些缺口。满足主帖点赞 ≥ 200、具体用途、原始来源和对应媒体后，更新结构化目录并移出本页；没有证据的设想保持待整理。

## 2026-09-18 第二轮新增线索

| 线索 | 原帖 | 当前缺口 / 下一步 |
| --- | --- | --- |
| YouTube predictor | [@moritzkremb 完整教程](https://x.com/moritzkremb/status/2100715237267660873) | 293 赞，目录标注 17:27；需核清输入、输出、预测目标及与已有内容分析器的差异。教程中的浏览器、记忆两部分已并入旧条目 |
| RAG 候选块筛选 | [@kushbhuwalka](https://x.com/kushbhuwalka/status/2100731050075050485) | 405 赞，但仅提出筛选思路，无实现媒体；先补代码、数据和精度/召回评估 |

以上数字为第二轮公开接口快照；取数时间：教程为 2026-09-18 02:38:04 UTC，RAG 建议为 02:36:40 UTC。来源与去重决定见 [更新记录](../CHANGELOG.md)；以上暂不计入正式案例。

第三轮已转入正式目录：[OpenCode 意图权限插件](../cases/2026-09-18-opencode-intent-permissions/README.md)。作者原帖由 160 赞升至 235 赞，已从待整理表移除。

第四轮已转入正式目录：[代码注释评分](../cases/2026-09-18-code-comment-scoring/README.md)。读图和作者回复明确了准确性、实用性两个维度；只按两个样例的实验收录，没有源码或成熟产品的保证。Foreman 同轮复查后仍待补媒体。核对截止 2026-09-18 16:15:58 北京时间。

第五轮仅复查 Jev QA tester 原帖正文与元数据：2026-09-18 11:39:31 UTC 快照为 756 赞，仍需核清断言和独立实现，未转入正式目录。本轮新收 [Runlayer 并行测试](../cases/2026-09-18-runlayer-adversarial-testing/README.md)有独立作者、视频和工具组合说明，不因同属 QA 就认定是同一项目。

## 2026-09-19 · 第六轮待补证据

| 线索 | 来源 / 点赞快照 | 待补证据 |
| --- | --- | --- |
| Flowsery 回放分析 | [@tarasshyn · 398](https://x.com/tarasshyn/status/2101012033340571952) | 需说明 Jev 分类、事件解析与 PR 生成的分工；213 个草稿 PR 不能直接写成 Jev 生成代码。 |
| Backdoor 求职匹配 | [@sarvagya_kul · 875](https://x.com/sarvagya_kul/status/2100980770206879849) | 需明确匹配输入、评分含义及结果展示；模型分数不能当真实录用概率。 |
| Gojiberry 线索评分 | [@romanbuildsaas · 2,391](https://x.com/romanbuildsaas/status/2100891604735099103) | 需明确评分标准和输入字段，区分兴趣评分、转化概率与未来 MCP 计划。 |
| 幽默判断 | [@rafalwilinski · 651](https://x.com/rafalwilinski/status/2100959576682012988) | 文字极简，需核清输入、候选和评分任务，才能写可靠的原理介绍。 |
| 表单自动填充 | [@ctnicholasdev · 458](https://x.com/ctnicholasdev/status/2100928133608472817) | 需补字段类型、候选内容来源与 Jev / 其他组件分工。 |
| DeepAPI 滥用判断 | [@DavidOndrej1 · 287](https://x.com/DavidOndrej1/status/2100902217515454507) | 需核清被测行为、标签和基准范围，不能只按“完美”结果图比较。 |
| Skittles 分拣 | [@ForwardFuture · 103](https://x.com/ForwardFuture/status/2100853837288407365) | 原应用帖 103 赞，未达门槛；转帖点赞不替代。还需原作者与实现说明。 |

点赞来自本轮 FxTwitter 取数，可能有缓存。以上不计入 106 个正式案例；Skittles 按原应用帖判断门槛，不用引用帖代替。

## 2026-09-19 · 第七轮待核来源

[Alan Daitch 语音控制视频](https://x.com/AlanDaitch/status/2101090570110169547)：本轮公开快照 238 赞、有约 48 秒视频，但实现作者及与已有语音控制案例的关系尚未核清。先确认来源与重复关系，再决定转正。

## 2026-09-20 · 第八轮待补证据

| 线索 | 原帖 / 点赞快照 | 待补证据 |
| --- | --- | --- |
| LangChain 代理评测 | [@LangChain · 450](https://x.com/LangChain/status/2101454284927959080) | 主帖为文章入口，未直接附运行媒体；需核对文章图表、任务与完整方法。 |
| 实体消歧 | [@hrishioa · 253](https://x.com/hrishioa/status/2101362082369470675) | 主帖无媒体；文章中的 99% 降费、近似准确性与吞吐对照还需完整核查。 |
| jev-lint 命名一致性 | [@mizchi · 348](https://x.com/mizchi/status/2101337282607550589) | 主帖无媒体；需核清新工具与同作者 ESLint 规则实验的关系，再决定合并或独立收录。 |
| GrokBot 路由实验室 | [@0xCodila · 522](https://x.com/0xCodila/status/2101433560796467348) | 主帖含演示但需核对仓库、具体任务及原始实现；“超过 95%”未给比较基准。 |
| 会计模拟 | [@xat_t0b · 1138](https://x.com/xat_t0b/status/2101260322917306612) | 作者称接入 API，需进一步读图核对会计任务、输出与规则；不凭短句推断记账能力。 |
| 设计师演示 | [@heystefan_ · 2882](https://x.com/heystefan_/status/2101369117496521042) | 文字没有说明具体输入输出或 Jev 分工，媒体内容待核。 |
| Web Dev Cody 演示 | [@webdevcody · 1196](https://x.com/webdevcody/status/2101393755513217192) | 文字极简，需核清是实际应用、反例还是戏仿，再决定是否收录。 |
| Jevassembler | [@neogoose_btw · 457](https://x.com/neogoose_btw/status/2101428888874410069) | “不用代码执行 CPU 指令”的表述有戏仿色彩；需核对可执行实现与已有 RISC-jeV 的区别。 |

以上数字为 9 月 20 日 FxTwitter 公开镜像快照，不计入 127 项正式目录。模仿 API 的本地模型、纯观点帖，以及 Ultrafast/Ryze/交通模拟的重复转载也未新增。[核对范围](../references/2026-09-20-increment8-audit.md)。

## 2026-09-21 · 第九轮待补证据

| 线索 | 原帖 / 点赞快照 | 待补证据 |
| --- | --- | --- |
| 智能复制粘贴 | [@marcus_lowe · 7422](https://x.com/marcus_lowe/status/2101476399488160013) | 原帖文字未说明字段映射与 Jev 分工；需核清视频、输入格式及与已有剪贴板案例的关系。 |
| 收藏积压整理 | [@alexchristou_ · 1028](https://x.com/alexchristou_/status/2101674202361221376) | 需核清视频中的分类功能和项目身份，排除已收 Shiori 的重复演示。 |
| 图片搜索 | [@shridharathi · 676](https://x.com/shridharathi/status/2101715395925184678) | 需核查图像描述由谁生成、Jev 实际输入及检索方法，不能推断直接看图。 |
| 按场合找衣服 | [@dbillson · 360](https://x.com/dbillson/status/2101657637871837578) | 需核对商品字段、演示和实现；不能只凭用途相似归为 Drape 或认定独立产品。 |
| 账号 slop 检测 | [@robj3d3 · 206](https://x.com/robj3d3/status/2101786193709142049) | 需补评分定义与可检查入口；百分比不能直接当 AI 生成概率。 |
| 模型路由界面 | [@okkshitij · 343](https://x.com/okkshitij/status/2101704186769404160) | 需核对实际候选模型、决策字段、仓库及与已收路由器的关系。 |
| 自然语言工作流 | [@GilFeig · 492](https://x.com/GilFeig/status/2101674767266845026) | 需核对执行器和固定动作范围；两秒、免费、每次相同缺完整条件与对照。 |
| 按话题剪视频 | [@BurhanUsman · 285](https://x.com/BurhanUsman/status/2101641842441732297) | 需区分字幕预处理、片段选择和视频导出；两秒和费用数字是否包含完整处理未知。 |
| 稀疏注意力实验 | [@sep_is_heim · 1619](https://x.com/sep_is_heim/status/2101603192664740330) | 需核实模型身份、Jev 控制字段、可执行代码与质量对照，不能只用加速数字下结论。 |
| 预测按键键盘 | [@neogoose_btw · 397](https://x.com/neogoose_btw/status/2101556786528760050) | 需核对上下文来源、硬件反馈与预测方法；原帖媒体不替代准确率统计。 |
| jev-browser skill | [@hqmank · 380](https://x.com/hqmank/status/2101529876469522673) | 需先核清仓库与 Ultrafast 等已有工具的依赖关系，再决定合并或独立收录。 |
| 高收益交易宣传 | [@bl888m_eth · 344](https://x.com/bl888m_eth/status/2101684333413368021) | 需完整可核查交易记录、起止余额与费用；界面截图不足以证明宣传收益。 |
| 扫雷 | [@comocc · 224](https://x.com/comocc/status/2101653695821984134) | 原帖有演示，尚待核清棋盘输入、动作执行与同名项目关系。 |
| 智能拖放 | [@MalayVasa · 405](https://x.com/MalayVasa/status/2101649868305653889) | 文字过少，需核清拖放规则、Jev 决策内容与原始实现。 |
| 聊天负面内容过滤 | [@developedbyed · 3933](https://x.com/developedbyed/status/2101628206478512341) | 需核对实际过滤标准和误杀行为；负面情绪不等同于辱骂或有害内容。 |

以上为 9 月 21 日 FxTwitter 快照线索，不计入 137 项正式目录。重复转载、纯发布/宣传帖、模仿 Jev API 的独立本地模型也未新增。[核对范围](../references/2026-09-21-increment9-audit.md)。
