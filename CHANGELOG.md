# 收录更新记录

**简体中文** | [English](CHANGELOG.en.md)

## 2026-09-18 · 第五轮增量

核对截止：**2026-09-18 19:42:10 北京时间（11:42:10 UTC）**。由 79 个增加到 **84 个案例，11 类**，新增 5 个独立实现。旧案例未重复建立，79 条原有内容、时间与主帖点赞快照保持不变。

| 新收录 | 主帖点赞快照 | 去重与证据要点 |
| --- | ---: | --- |
| [Runlayer 并行浏览器测试](cases/2026-09-18-runlayer-adversarial-testing/README.md) | [820](https://x.com/rafalwilinski/status/2100882207879434359) | 作者回复确认 Runlayer agents、agent-browser、Chromium；独立多窗口视频，不把每个会话当应用 |
| [Hono JevRouter](cases/2026-09-18-hono-semantic-router/README.md) | [405](https://x.com/yusukebe/status/2100871075743859182) | HTTP 请求语义分流，区别于模型路由；核对固定版本代码，按注册顺序取首个达标路由，不是最高分 |
| [Sac 的 Mac 日历操作对照](cases/2026-09-18-sac-calendar-computer-use/README.md) | [217](https://x.com/Saccc_c/status/2100864907046768890) | 虽也叫 Jev Use，但作者和视频不同于 Cua；主帖称 token 消耗接近，不沿用引用旧帖的泛化节省主张 |
| [终端历史命令语义补全](cases/2026-09-18-shell-history-suggestions/README.md) | [396](https://x.com/thorstenball/status/2100858434904109099) | 主演示与 Amp 制作过程合并；固定版本文档说明候选筛选、双问题门控，以及演示使用虚构历史 |
| [Calorie Notebook 饮食记录](cases/2026-09-18-calorie-notebook/README.md) | [326](https://x.com/thekitze/status/2100857642566758849) | 独立文字饮食记录界面；同作者的其他项目不重复加入，未披露的估算机制保持未知 |

主帖取数时间为 11:39:02–11:39:31 UTC，精确值见各条记录。全部新增条目同步中英文简介、通俗原理、同类优缺点、媒体与 README 时间，仍未复现。未安装插件、发送本机历史、运行外部项目或调用付费 API。

**合并判断与排除：** [Rob Hallam 的引用](https://x.com/robj3d3/status/2100876506549645608)指向已收录的 [Jack Cheng 画布](cases/2026-09-18-voice-gesture-canvas/README.md)，仅表达观点，不新增条目。[Sac 的入门汇总](https://x.com/Saccc_c/status/2100833094291087773)列举的浏览器、压缩、路由和审核案例均已存在，不把汇总再算一遍。学习会、文章合集、泛用法建议和其他模型的仿制项目不计为新应用。

**待整理复查：** Jev QA tester 原帖本轮 756 赞，仍只有简短文字和视频，具体断言及与现有 OpenCode 演示的实现关系没有补齐；保留待整理。本轮 Runlayer 有明确作者工具说明，不与它仅按“QA”这个用途词合并。

**范围与核对：** X 最新搜索 `Jev min_faves:200 since:2026-09-18`，回看到上轮检索过的 Kun Chen 帖及 Sac 汇总附近；读取五个新案例讨论串、Hono 的固定版本 README/路由实现和 shell 插件的固定版本 README。以原帖 ID、引用链、作者、用途、仓库和媒体去重；不是 X 全量覆盖。Hono playground 未提交测试，源码阅读不等于运行验证。

## 2026-09-18 · 第四轮增量

核对截止：**2026-09-18 16:15:58 北京时间（08:15:58 UTC）**。由 77 个增加到 **79 个案例，11 类**：新增 2 个独立实验，其中 1 个来自待整理区补证；没有重复建立已有项目。旧条目的内容时间与点赞快照保持不变。

| 新收录 | 主帖点赞快照 | 去重与证据要点 |
| --- | ---: | --- |
| [邮件分类 · 四模型速度对照](cases/2026-09-18-email-speed-race/README.md) | [445](https://x.com/usutaku_channel/status/2100829343954173965) | 独立作者、界面和视频；与 500 封邮件分类放在同类比较。作者报告 Jev 更快，但缺完整精度、版本与配置证据，不给出通用速度排名 |
| [代码注释 · 准确性与实用性评分](cases/2026-09-18-code-comment-scoring/README.md) | [1,777](https://x.com/markjaquith/status/2100359340087501296) | 旧线索本轮补证：读图并合并两条作者回复，确认两个评分维度和初筛定位；区别于 ESLint 规则判断与完整 PR 审查 |

两条主帖均于 **08:11:40 UTC** 取数；注释案例补充帖于 **08:15:58 UTC** 取数。新条目同步中英文简介、通俗原理、优缺点、原帖媒体与 README 收录/内容更新时间，仍全部未复现。没有将 99/100 的单例评分当成 99% 测试准确率，也没有将视频长度当成运行耗时。

**去重与暂缓：**

- [Tony 的赞助跳过视频](https://x.com/tdinh_me/status/2100793777103466615)已收录；再次出现在搜索结果中不增加计数。
- [OpenCode 本地分类器讨论](https://x.com/thdxr/status/2100814192919929259)只是提出 Jev 可以替代的设想，没有已接入证据；[接入教程](https://x.com/harrisonitsme/status/2100799749192569167)、学习资料、观点和玩笑不另算应用。
- Foreman 主帖本轮快照为 685 赞；读取 [固定版本 README](https://github.com/thruwire/foreman/blob/2c439828b9fe45ee5d40f6f57be81f7ff1f8a140/README.md)与仓库文件树后，补充了监督循环的说明，但本次仍未找到对应运行图片/视频，保留待整理。

**检索范围：** X 最新搜索 `Jev min_faves:200 since:2026-09-18`，查看到已收录的赞助跳过原帖附近；另复查 Foreman 和代码注释待整理线索。新发现与旧线索补证分开说明，不宣称覆盖所有 X 帖子。按主帖 ID、作者、项目用途、视频和已有目录交叉去重，分类比较同步双语。

## 2026-09-18 · README 时间标注

为全部 77 个项目的中英文简介、案例索引及详情加入首次收录和最近内容更新时间，统一北京时间。历史值按 Git 内容提交回填，后续生成不会自动刷新。此次没有新增案例或重新取数。[时间依据](references/README.md#readme-times)

## 2026-09-18 · 第三轮增量

核对截止：**2026-09-18 14:12:09 北京时间（06:12:09 UTC）**。由 72 个增加到 **77 个案例，11 类**；新增 5 个独立案例，补充 1 个已有条目。下方第二轮记录保留为历史，不覆盖先前的取数事实。

| 新增应用 | 主帖点赞快照 | 去重与证据要点 |
| --- | ---: | --- |
| [YouTube 赞助片段跳过](cases/2026-09-18-youtube-sponsor-skip/README.md) | [238](https://x.com/tdinh_me/status/2100793777103466615) | 扩展和同仓库 Web 页面合为一个项目；区别于隐藏网页广告。核对固定代码版本，语音转写另有成本 |
| [按列名意图评分的表格](cases/2026-09-18-predictive-spreadsheet/README.md) | [337](https://x.com/dabit3/status/2100780008193020049) | 虽引用同作者启动器，但使用独立新视频，任务是给行评级，不能只按作者或引用关系去重 |
| [Probably 实验语言](cases/2026-09-18-probably-language/README.md) | [894](https://x.com/southpolesteve/status/2100767781868150938) | 判断、分支与生成的语言实验；官网托管版是预录回放，自定义程序需本地连接模型 |
| [ESLint 规则说明判断](cases/2026-09-18-eslint-rule-judgments/README.md) | [351](https://x.com/mizchi/status/2100765201385869434) | 新的规则级小片段实验，区别于 PR 审查；作者回复限定了测试规模 |
| [OpenCode 意图权限插件](cases/2026-09-18-opencode-intent-permissions/README.md) | [235](https://x.com/OpeOginni/status/2100702649834188855) | 上轮 160 赞暂缓；本轮作者主帖达标，从待整理区转入。不将高赞转发重复收录 |

新主帖取数时间：权限插件为 06:07:34 UTC；赞助跳过、Probably、ESLint 为 06:08:49 UTC；表格为 06:08:50 UTC。精确来源与补充帖时间见各条目及共享目录。主帖和媒体均无重复，所有新案例仍未复现。

**合并到已有案例：** [Teknium 对 Cua 的引用](https://x.com/Teknium/status/2100783833419505941)仅宣布计划测试，补入 [Cua · jev-use](cases/2026-09-18-cua-jev-use/README.md)，不另建“新集成”。GitHub API 复查 #3916 仍 open、未合并，#3943 仍 open draft、未合并。

**不增加计数的线索：**

- [中文](https://x.com/SUOHA_AI/status/2100780634734002230)与[日文](https://x.com/k_matsumaru/status/2100767258415157493)压缩插件转述都指向已收录的 `fast-jev-compaction`，没有新增独立实现。
- [Sydney 的 LangChain 教程](https://x.com/sydneyrunkle/status/2100754364545761643)及 [Harrison 的引用](https://x.com/hwchase17/status/2100773130041950570)为同一教程来源，归入参考资料，不把文章、分类示例、路由示例逐个包装成应用。
- 泛观点、直播预告和不使用 TypeSafe Jev 的其他模型介绍不计入正式目录。

**检索范围：** 使用 X 最新搜索 `Jev min_faves:200 since:2026-09-18`，回看到上轮已收录的启动器附近；复查上轮未达门槛的权限插件，读取 ESLint 与权限插件讨论串、Sponsor Skip 固定版本源码、Probably 官网和 npm 包说明。包含此前已发布但本轮才发现或达标的帖子，不承诺全量覆盖。

本轮保留了旧案例的全部主帖快照，并增加 `updates` 历史字段，避免后续生成时抹掉前一轮案例更新记录。

## 2026-09-18 · 第二轮增量

核对截止：**2026-09-18 10:43:33 北京时间（02:43:33 UTC）**。从 67 个增加到 **72 个案例，仍为 11 类**：新增 5 个独立案例，补充 4 个已有条目。点赞是各原帖的取数快照，不是此刻的实时值；旧条目的主帖点赞没有批量刷新。

### 新收录

| 应用 | 为什么单独收录 | 主帖点赞快照 |
| --- | --- | ---: |
| [意图预测启动器](cases/2026-09-18-predictive-launcher/README.md) | 按意图排序文件候选，与网页点击、OCR 操作不同 | [252](https://x.com/dabit3/status/2100756930054504776) |
| [实时电商导购与头像表情](cases/2026-09-18-live-commerce-assistant/README.md) | 对话中的商品推荐及表达反馈，与离线客服意图分类不同 | [217](https://x.com/rinte0321/status/2100736454850908344) |
| [Minecraft 三层协作](cases/2026-09-18-minecraft-hybrid/README.md) | Jev 反应、Astra 规划、本地策略执行的独立游戏系统 | [354](https://x.com/wuyang_zhou/status/2100727660875808913) |
| [实时表情候选](cases/2026-09-18-emoji-suggestions/README.md) | 从 emoji 集合选择，与逐字聊天或像素绘图任务不同 | [230](https://x.com/riku720720/status/2100705558512963602) |
| [语音与指向控制画布](cases/2026-09-18-voice-gesture-canvas/README.md) | 用指向解决语言指代并操作对象，与 TypeGPU 视听特效不同 | [915](https://x.com/jackcheng/status/2100729670991802386) |

每条均已同步中英文简介、通俗原理、局限和原帖媒体；新条目仍全部未复现。Minecraft 主视频约 2× 加速，已合并作者提供的原速版本与分层说明。

### 合并更新，不增加案例数

| 原有条目 | 合并内容与依据 |
| --- | --- |
| [工具调用上下文压缩](cases/2026-09-18-context-compaction/README.md) | [作者仓库链接](https://x.com/tamarajtran/status/2100694552369897539)、[Alex 使用报告](https://x.com/altryne/status/2100739055923425589)、[Theo 质疑](https://x.com/theo/status/2100762304862384257)都指向同一原帖或 `tamaratran/fast-jev-compaction`。补读固定代码版本，区分对话裁剪、工具输出省略与不调用 API 的录屏动画 |
| [帖子传播分类器](cases/2026-09-18-viral-classifier/README.md) | [作者新视频](https://x.com/robj3d3/status/2100722975645598191)引用原帖；补充 61 个问题、样本规模及成本报告，未将 Jev + SuperX 另算一个项目 |
| [语音控制浏览器](cases/2026-09-18-voice-browser/README.md) | [作者教程](https://x.com/moritzkremb/status/2100715237267660873)的 5:59 章节是同用途演示，合并来源 |
| [记忆系统检索筛选](cases/2026-09-18-memory-retrieval/README.md) | 同一教程的 11:33 章节属于这个已收录用途；允许一个多案例教程作为两条记录的补充来源，不新建“教程应用” |

[Rikuo 的压缩转述](https://x.com/riku720720/status/2100716449568596261)也引用同一压缩原帖，没有新增实现证据，不另建记录。

### 待补证据与非应用动态

- [OpenCode 意图权限插件](https://x.com/OpeOginni/status/2100702649834188855)：作者原帖取数时 **160 赞**。即使[转发](https://x.com/thdxr/status/2100723765718008238)超过千赞，也不替代主帖门槛，放入待整理区。
- 教程 17:27 的 [YouTube predictor](https://x.com/moritzkremb/status/2100715237267660873)：目录提供线索，但尚未核清输入、输出及独立实现，暂不另计。
- [RAG 筛选建议](https://x.com/kushbhuwalka/status/2100731050075050485)：本次取数 405 赞，但没有具体实现媒体；不能据一句建议认定“解决了 RAG 精度”。
- [OpenRouter beta 公告](https://x.com/OpenRouter/status/2100744709589316009)与 [TypeSafe 转发](https://x.com/typesafeai/status/2100747035746193598)是同一接入动态，不算两个应用；[Laravel AI SDK 公告](https://x.com/taylorotwell/status/2100700952923713641)对应的 [PR #1010](https://github.com/laravel/ai/pull/1010)已合并，属于开发支持资料，不新增终端应用计数。未验证这些服务的实际调用。

### 检索与去重范围

使用 X 最新搜索 `Jev min_faves:200 since:2026-09-17`，复查自上次收录后出现的结果，并回看到已收录的上下文压缩原帖附近；按帖 ID、引用链、作者、项目链接与用途判断是否新增。补查 Minecraft、画布和表情演示讨论串；元数据使用 FxTwitter 公共接口，可能有缓存。未把整个搜索时段称为全量覆盖，也未声称每段视频都已逐帧审查。

新增与合并列表保存在 [共享目录](data/catalog.json) 的 `latest_update`；精确取数时间保存在各主帖及补充帖。下一轮先对照这些 ID 和项目，避免重复加入。

[返回全部应用](README.md) · [待整理区](inbox/README.md) · [来源方法](references/README.md)
