# 2026-09-23 · 扩大回查补录

**简体中文** | [English](2026-09-23-expanded-audit.en.md)

内容更新 **2026-09-23 12:45:07 北京时间**。再补 **35 项**、合并更新 **2 项**，共 **183 项、11 类**（A 35 / B 127 / C 21）。加上此前一轮的 11 项，两轮合计新增 46 项。全部仍为**未复现**。

## 扩大检索后发现了什么

此前只选出 11 项，确实没有充分覆盖线索。本轮回查 101 条未正式收录线索，并遍历公开 [JEVLAB](https://jev-lab.com/en/?platform=x&scope=global) 五页中的全部 349 条 X 卡片；[MadeWithJev](https://madewithjev.com/) 和仓库待整理区也用于发现原帖。索引卡片只算线索，不直接当独立应用。与已有目录按来源 ID 去重后，共 302 条候选：取得 301 条快照、1 条未取得；其中 118 条同时达到 200 赞及主帖媒体门槛。沿 Halite 引用另找到 1 条原始演示，因此**筛选台账共 303 条来源帖**。池外回复、文章等补充依据在案例中单列，不算额外应用。

**这 35 项中，8 项原帖晚于 9 月 21 日 11:02:26 北京时间，27 项是此前遗漏的较早案例。** 这是目录补录，不是 35 个刚发布的新产品。公开索引有覆盖和时效限制，本轮不代表 X 全量导出。FxTwitter 指标可能缓存；本轮审核原帖文字、元数据及部分作者文档/源码，没有独立运行项目，也没有逐帧验证所有视频。

## 筛选台账

[303 条来源及中英文处理理由 CSV](2026-09-23-expanded-screening.csv)。每条来源只归一种处理结果，多帖可以对应一个项目；待核不等于项目虚假。

| 处理 | 帖数 |
| --- | ---: |
| 非独立应用 | 12 |
| 缺主帖媒体 | 28 |
| 新案例主帖 | 35 |
| 仍待深入核对 | 60 |
| 未达点赞门槛 | 154 |
| 独立兼容/仿制模型 | 5 |
| 重复传播 | 2 |
| 并入案例的补充帖 | 5 |
| 未取得快照 | 1 |
| 引用帖不能代替原帖 | 1 |

## 去重与判断变化

- 两位 Monid 作者的演示只算一个集成；Halite 同作者的相关游戏对照合成一项。
- Higgsfield 较早的素材筛选演示并入现有语音广告流程，补清 Jev 负责选择、其他模型负责生成，不新增卡片。
- StealAds 人设评分并入广告分析，等级由 B 调至 C：模拟“停下来看广告”不能证明能替代真人焦点小组。
- MaxFusion 的 1,891 条广告重复演示、已有上下文压缩素材的再传播不另收。独立 Smash 控制器以及 PostgreSQL / DuckDB 实现保留独立案例，按用途比较。
- 六个新案例附固定版本源码。A 评价可检查的实现证据，不代表独立复现；B 为原型明确但效果待验证，C 提醒宣传超出现有证据。
- 保留旧主帖快照和首次收录时间，仅 37 个变更案例刷新内容时间，另 146 个旧案例与首页六个精选保持不变。

## 逐项依据

<a id="working-memory-passage"></a>

### Passage · 看教材是否一下塞进太多概念 · A

A 针对公开流程与明确边界；不支持“让个性化教育提前数年”或成本估算的普遍外推。

支持范围是英文教学文字；分数不是实测学生记忆容量或过载概率。代码公开但采用自定义许可，商业或多人组织使用需另看条款。

详情与原理：[Passage · 看教材是否一下塞进太多概念](../cases/2026-09-23-working-memory-passage/README.md)

来源：[X @Austin_Way](https://x.com/Austin_Way/status/2102131624921968704)

实现 / 方法（源码链接固定到审核版本）：[1](https://github.com/AustinAWay/Working-Memory-Jev/blob/cee3edb9922115d759778434878f6c56b483b390/README.md) · [2](https://github.com/AustinAWay/Working-Memory-Jev/blob/cee3edb9922115d759778434878f6c56b483b390/docs/architecture.md)

原帖发布：2026-09-21T20:23:29+00:00；快照：**609 赞**，2026-09-23T04:31:26+00:00；[取数来源](https://api.fxtwitter.com/status/2102131624921968704)。

<a id="jev-workflow-builder"></a>

### Jev Workflow Builder · 把判断连成工作流 · A

A 针对可检查的节点执行与模型分工，不代表工作流效果或生产可用性已验证。

缺密钥时源码明确返回 mock 关键词结果，不能把无密钥演示当 Jev 推理；未验证生产并发和可靠性。

详情与原理：[Jev Workflow Builder · 把判断连成工作流](../cases/2026-09-23-jev-workflow-builder/README.md)

来源：[X @ctnicholasdev](https://x.com/ctnicholasdev/status/2102070640589279318)

实现 / 方法（源码链接固定到审核版本）：[1](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/README.md) · [2](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/app/workflow/server/typesafe.ts) · [3](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/app/workflow/server/executor.ts)

原帖发布：2026-09-21T16:21:09+00:00；快照：**638 赞**，2026-09-23T04:31:24+00:00；[取数来源](https://api.fxtwitter.com/status/2102070640589279318)。

<a id="agentrun"></a>

### AgentRun · 让重复工作逐渐变成固定流程 · B

工作流和评测范围有原始文章支持；性能、正确率及跨任务推广保持 B，非独立复现。

对照来自作者的合规告警任务，未公开完整原始案例和独立审计；少查资料也可能漏证据，不能只看费用。

详情与原理：[AgentRun · 让重复工作逐渐变成固定流程](../cases/2026-09-23-agentrun/README.md)

来源：[X @_aj](https://x.com/_aj/status/2102061534956662818) · [X @MiguelriosEN](https://x.com/MiguelriosEN/status/2101029313906987422) · [X @MiguelriosEN](https://x.com/MiguelriosEN/status/2101033282414768456)

实现 / 方法（源码链接固定到审核版本）：[1](https://x.com/i/article/2100840456200581120)

原帖发布：2026-09-21T15:44:59+00:00；快照：**2142 赞**，2026-09-23T04:31:25+00:00；[取数来源](https://api.fxtwitter.com/status/2102061534956662818)。

<a id="neatlogs-detections"></a>

### Neatlogs · 在代理运行记录里找语义异常 · B

结合产品文档补清检测对象后收录；Jev 集成依据作者公告，质量与完整可用性待验证。

文档中语义检测早已存在，不能把所有历史检测归给 Jev；新增集成的精确提示、阈值和误报率未公开。检测是记录标注，不会自动修复代理。

详情与原理：[Neatlogs · 在代理运行记录里找语义异常](../cases/2026-09-23-neatlogs-detections/README.md)

来源：[X @simranrambles](https://x.com/simranrambles/status/2102313324293820530)

实现 / 方法（源码链接固定到审核版本）：[1](https://docs.neatlogs.com/docs/features/detections)

原帖发布：2026-09-22T08:25:30+00:00；快照：**235 赞**，2026-09-23T04:31:28+00:00；[取数来源](https://api.fxtwitter.com/status/2102313324293820530)。

<a id="monid-jev-tools"></a>

### Monid · 给工具工作流加上批量判断 · B

两位作者的同一 Monid 集成合成一条；任务可辨，速度和质量不作普遍保证。

2,000 是工具目录规模，不是已验证任务数；30 倍缺完整基线，视频的转写/视觉处理成本未知。

详情与原理：[Monid · 给工具工作流加上批量判断](../cases/2026-09-23-monid-jev-tools/README.md)

来源：[X @shengkunye](https://x.com/shengkunye/status/2102112693041938825) · [X @Jasperli0122](https://x.com/Jasperli0122/status/2102140451763749077)

原帖发布：2026-09-21T19:08:16+00:00；快照：**238 赞**，2026-09-23T04:31:25+00:00；[取数来源](https://api.fxtwitter.com/status/2102112693041938825)。

<a id="starcraft2-squads"></a>

### StarCraft II · 大模型定计划，Jev 指挥小队 · B

明确收录 StarCraft II 原型，引用的其他游戏不混算，胜率与泛化待验证。

缺地图、对手、重复胜率和全流程费用；引用的 Warcraft 实验来自另一作者，不是本项目战绩。

详情与原理：[StarCraft II · 大模型定计划，Jev 指挥小队](../cases/2026-09-23-starcraft2-squads/README.md)

来源：[X @GZhan57](https://x.com/GZhan57/status/2102126922688012410)

原帖发布：2026-09-21T20:04:48+00:00；快照：**709 赞**，2026-09-23T04:31:26+00:00；[取数来源](https://api.fxtwitter.com/status/2102126922688012410)。

<a id="smash-pi-controller"></a>

### Smash Bros. · 树莓派按键与 Jev 选招 · B

作者主动说明失败表现，支持有限控制原型，不夸大为高水平对战。

作者承认对 CPU 8 很弱；精确视觉特征、动作候选和长期胜率未披露，不能当高手级游戏 AI。

详情与原理：[Smash Bros. · 树莓派按键与 Jev 选招](../cases/2026-09-23-smash-pi-controller/README.md)

来源：[X @aokiti_tech](https://x.com/aokiti_tech/status/2102123079912808849) · [X @aokiti_tech](https://x.com/aokiti_tech/status/2101506737417363546)

原帖发布：2026-09-21T19:49:32+00:00；快照：**249 赞**，2026-09-23T04:31:26+00:00；[取数来源](https://api.fxtwitter.com/status/2102123079912808849)。

<a id="halite-hybrid"></a>

### Halite · 战略模型与逐船执行对照 · B

两个同作者 Halite 实验合并；单次速度与对局结果都不推导为模型普遍优劣。

不同游戏、设置不能直接合成总排名；未获得完整赛程、随机种子、原始日志和可复现协议。

详情与原理：[Halite · 战略模型与逐船执行对照](../cases/2026-09-23-halite-hybrid/README.md)

来源：[X @Sentdex](https://x.com/Sentdex/status/2101828851458293827) · [X @Sentdex](https://x.com/Sentdex/status/2102192643480678651)

原帖发布：2026-09-21T00:20:22+00:00；快照：**386 赞**，2026-09-23T04:32:45+00:00；[取数来源](https://api.fxtwitter.com/status/2101828851458293827)。

<a id="yc-startup-search"></a>

### YC 公司搜索 · 按描述寻找创业公司 · B

具体目录与查询演示可辨；检索覆盖、视觉预处理和费用口径待验证。

缺已知答案集合、召回率与错误匹配统计；索引成本和单次查询成本应分开。

详情与原理：[YC 公司搜索 · 按描述寻找创业公司](../cases/2026-09-23-yc-startup-search/README.md)

来源：[X @aaayandev](https://x.com/aaayandev/status/2102137061490794730)

原帖发布：2026-09-21T20:45:05+00:00；快照：**1495 赞**，2026-09-23T04:31:26+00:00；[取数来源](https://api.fxtwitter.com/status/2102137061490794730)。

<a id="predictive-keyboard"></a>

### 预测键盘 · 提前点亮可能要按的键 · B

可确认作者描述的硬件原型，不能据此推定提高打字效率或支持任意应用。

不是在键盘上离线运行 Jev；没有预测命中率、干扰率或击键效率对照。

详情与原理：[预测键盘 · 提前点亮可能要按的键](../cases/2026-09-23-predictive-keyboard/README.md)

来源：[X @neogoose_btw](https://x.com/neogoose_btw/status/2101556786528760050)

原帖发布：2026-09-20T06:19:17+00:00；快照：**478 赞**，2026-09-23T04:30:03+00:00；[取数来源](https://api.fxtwitter.com/status/2101556786528760050)。

<a id="abide-rules"></a>

### Abide · 每次改代码都检查项目约定 · A

A 针对源码与透明评测；“全部抓住并修复”不受回放结果支持，概率仍需项目校准。

回放评测不验证代理是否真的修好；复核者是 Claude，并非独立人工实验。单次编辑误报很多，不能保证抓住每次违规。

详情与原理：[Abide · 每次改代码都检查项目约定](../cases/2026-09-23-abide-rules/README.md)

来源：[X @OhansEmmanuel](https://x.com/OhansEmmanuel/status/2101034822760288452)

实现 / 方法（源码链接固定到审核版本）：[1](https://github.com/coldteadotai/abide/blob/f2683828965ced03da07abae811e78af0383040c/README.md) · [2](https://github.com/coldteadotai/abide/blob/f2683828965ced03da07abae811e78af0383040c/packages/cli/src/lib/jev.ts) · [3](https://github.com/coldteadotai/abide/blob/f2683828965ced03da07abae811e78af0383040c/benchmarks/replay/README.md)

原帖发布：2026-09-18T19:45:11+00:00；快照：**921 赞**，2026-09-23T04:32:32+00:00；[取数来源](https://api.fxtwitter.com/status/2101034822760288452)。

<a id="jev-reviewer-papers"></a>

### Jev Reviewer · 从论文中找到可核对的原句 · A

A 针对可检查的选句与复核实现；不将“不改写”解读为绝无语义错误。

逐字引用仍可能选错证据；扫描 PDF 需先 OCR，图表内容不直接检索。浏览器保存文件不等于推理离线，文本会用于 API 请求。

详情与原理：[Jev Reviewer · 从论文中找到可核对的原句](../cases/2026-09-23-jev-reviewer-papers/README.md)

来源：[X @ASofiMahmudi](https://x.com/ASofiMahmudi/status/2100985031703269425)

实现 / 方法（源码链接固定到审核版本）：[1](https://github.com/choxos/jev-reviewer/blob/da15868cdca5e64555e6643243a52ea71f60cf3b/README.md) · [2](https://github.com/choxos/jev-reviewer/blob/da15868cdca5e64555e6643243a52ea71f60cf3b/docs/jev.js)

原帖发布：2026-09-18T16:27:20+00:00；快照：**244 赞**，2026-09-23T04:32:36+00:00；[取数来源](https://api.fxtwitter.com/status/2100985031703269425)。

<a id="pg-jev"></a>

### pg-jev · 用日常语言筛数据库里的行 · A

A 针对公开批处理与缓存实现；不把免向量索引当作无限规模或无误差检索。

需要 plpython3u 和超级用户权限，许多托管数据库不能安装；大表首次查询要付调用成本，缓存毫秒数不是重新推理速度。

详情与原理：[pg-jev · 用日常语言筛数据库里的行](../cases/2026-09-23-pg-jev/README.md)

来源：[X @iam_zachi](https://x.com/iam_zachi/status/2100679300756435135)

实现 / 方法（源码链接固定到审核版本）：[1](https://github.com/realZachi/pg-jev/blob/afd11fa856d7a2b831a1bfd8ee7f869ce8efcd62/README.md) · [2](https://github.com/realZachi/pg-jev/blob/afd11fa856d7a2b831a1bfd8ee7f869ce8efcd62/sql/jev--0.2.0.sql)

原帖发布：2026-09-17T20:12:28+00:00；快照：**2832 赞**，2026-09-23T04:32:47+00:00；[取数来源](https://api.fxtwitter.com/status/2100679300756435135)。

<a id="typesafe-adblock"></a>

### TypeSafe AdBlock · 按含义识别网页广告 · A

A 针对公开实现；“不可检测”和通用拦截效果无依据，准确范围以候选与测试条件为限。

源码并非检查所有元素；候选规则外的广告会漏掉，也可能误删内容。仓库明确不处理跟踪、恶意内容或视频广告。

详情与原理：[TypeSafe AdBlock · 按含义识别网页广告](../cases/2026-09-23-typesafe-adblock/README.md)

来源：[X @iam_zachi](https://x.com/iam_zachi/status/2100529273186472318)

实现 / 方法（源码链接固定到审核版本）：[1](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/README.md) · [2](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/src/typesafe.js)

原帖发布：2026-09-17T10:16:19+00:00；快照：**3889 赞**，2026-09-23T04:32:49+00:00；[取数来源](https://api.fxtwitter.com/status/2100529273186472318)。

<a id="voice-turn-end"></a>

### 语音轮次判断 · 停顿时先别急着插话 · B

明确的轮次结束实验，不能由一次快响应推定自然对话质量。

没有不同语速、语言、噪声下的打断率和等待体验对照。

详情与原理：[语音轮次判断 · 停顿时先别急着插话](../cases/2026-09-23-voice-turn-end/README.md)

来源：[X @uezochan](https://x.com/uezochan/status/2100608556823388486)

原帖发布：2026-09-17T15:31:22+00:00；快照：**443 赞**，2026-09-23T04:32:49+00:00；[取数来源](https://api.fxtwitter.com/status/2100608556823388486)。

<a id="mujoco-two-stage"></a>

### MuJoCo 两段决策 · 先选目标，再动机械臂 · B

保留失败背景与分工，是独立作者实验，不与其他 MuJoCo 视频混同。

没有反复抓取成功率、碰撞统计或真实硬件结果；仿真画面不等于视觉控制。

详情与原理：[MuJoCo 两段决策 · 先选目标，再动机械臂](../cases/2026-09-23-mujoco-two-stage/README.md)

来源：[X @dimentary](https://x.com/dimentary/status/2101018760371171420)

原帖发布：2026-09-18T18:41:22+00:00；快照：**626 赞**，2026-09-23T04:32:34+00:00；[取数来源](https://api.fxtwitter.com/status/2101018760371171420)。

<a id="chess-glm-comparison"></a>

### 国际象棋对照 · 走得快不等于下得好 · B

B：有限对局证据，速度优势与棋力表现不混为一谈。

只有单盘结果，不能据此建立稳定棋力排名；计时和费用范围缺完整日志。

详情与原理：[国际象棋对照 · 走得快不等于下得好](../cases/2026-09-23-chess-glm-comparison/README.md)

来源：[X @nutlope](https://x.com/nutlope/status/2101010773157761481)

原帖发布：2026-09-18T18:09:37+00:00；快照：**324 赞**，2026-09-23T04:32:35+00:00；[取数来源](https://api.fxtwitter.com/status/2101010773157761481)。

<a id="prompt-box-router"></a>

### Prompt Box · 自动选模型、电脑和项目目录 · B

配置分派原型有依据，权限边界和任务效果待验证。

机器目录候选如何提供、权限如何约束尚未披露；选对字段不代表任务一定完成。

详情与原理：[Prompt Box · 自动选模型、电脑和项目目录](../cases/2026-09-23-prompt-box-router/README.md)

来源：[X @sawyerhood](https://x.com/sawyerhood/status/2100994779291259187)

原帖发布：2026-09-18T17:06:04+00:00；快照：**203 赞**，2026-09-23T04:32:35+00:00；[取数来源](https://api.fxtwitter.com/status/2100994779291259187)。

<a id="corent-router"></a>

### Corent · 按任务费用设置不同路由门槛 · B

分工清楚，仍不能把模型数量或概率当最佳模型选择的证明。

千余模型是平台规模，不是逐一验证过的路由效果；阈值校准、回退对象和误选损失未披露。

详情与原理：[Corent · 按任务费用设置不同路由门槛](../cases/2026-09-23-corent-router/README.md)

来源：[X @corentAI](https://x.com/corentAI/status/2100965880242770423)

实现 / 方法（源码链接固定到审核版本）：[1](https://corent.tech)

原帖发布：2026-09-18T15:11:14+00:00；快照：**326 赞**，2026-09-23T04:32:38+00:00；[取数来源](https://api.fxtwitter.com/status/2100965880242770423)。

<a id="lurk-reddit-monitor"></a>

### Lurk · 持续找值得关注的 Reddit 讨论 · B

产品与筛选用途明确；营销引用效果和长期运行质量未验证。

发现讨论不保证品牌被 AI 引用；帖子覆盖、误报、通知延迟和免费额度未独立核实。

详情与原理：[Lurk · 持续找值得关注的 Reddit 讨论](../cases/2026-09-23-lurk-reddit-monitor/README.md)

来源：[X @mxfp4](https://x.com/mxfp4/status/2101070906852298910)

实现 / 方法（源码链接固定到审核版本）：[1](https://lurk.so)

原帖发布：2026-09-18T22:08:34+00:00；快照：**751 赞**，2026-09-23T04:32:30+00:00；[取数来源](https://api.fxtwitter.com/status/2101070906852298910)。

<a id="hn-venice-classification"></a>

### Hacker News 分类 · 批量整理 24,000 条帖子 · B

按具体分类演示收录，不把同帖网关发布单独算作另一个应用。

仅看数量与速度不能判断标签正确率；网关接口、抓取和存储开销应分开。

详情与原理：[Hacker News 分类 · 批量整理 24,000 条帖子](../cases/2026-09-23-hn-venice-classification/README.md)

来源：[X @sabrinaesaquino](https://x.com/sabrinaesaquino/status/2101102660997017747)

原帖发布：2026-09-19T00:14:45+00:00；快照：**221 赞**，2026-09-23T04:32:29+00:00；[取数来源](https://api.fxtwitter.com/status/2101102660997017747)。

<a id="ocr-page-router"></a>

### OCR Router · 只把需要识别的页面送去 OCR · B

具体路由任务明确，输入编码和漏检率待核；与 DocJev 的类别/分页任务不同。

不能推断 Jev 直接看 PDF 图像；漏送扫描页会漏内容，缺标注数据与完整质量/成本对照。

详情与原理：[OCR Router · 只把需要识别的页面送去 OCR](../cases/2026-09-23-ocr-page-router/README.md)

来源：[X @MisbahSy](https://x.com/MisbahSy/status/2100979972194369925)

原帖发布：2026-09-18T16:07:14+00:00；快照：**483 赞**，2026-09-23T04:32:37+00:00；[取数来源](https://api.fxtwitter.com/status/2100979972194369925)。

<a id="mac-voice-fast-actions"></a>

### Mac 语音操作 · 话没说完就开始打开应用 · B

有限动作演示，不能把起步快等同于整个任务快或可靠。

一句话尚未完整时可能改口；缺误操作、撤销、任务成功率及总延迟数据。

详情与原理：[Mac 语音操作 · 话没说完就开始打开应用](../cases/2026-09-23-mac-voice-fast-actions/README.md)

来源：[X @instantricecook](https://x.com/instantricecook/status/2100814590300889426)

原帖发布：2026-09-18T05:10:04+00:00；快照：**6130 赞**，2026-09-23T04:32:46+00:00；[取数来源](https://api.fxtwitter.com/status/2100814590300889426)。

<a id="secondhand-playwright"></a>

### 二手商品助手 · 逐件判断是否符合需求 · B

明确商品筛选原型；记录作者的出价/联系演示，不把它当真实购买效果。

没有卖家回复、成交或误出价记录；自动动作不等于成功购得商品，完整成本不明确。

详情与原理：[二手商品助手 · 逐件判断是否符合需求](../cases/2026-09-23-secondhand-playwright/README.md)

来源：[X @AlanDaitch](https://x.com/AlanDaitch/status/2100757989212754085)

原帖发布：2026-09-18T01:25:09+00:00；快照：**947 赞**，2026-09-23T04:32:46+00:00；[取数来源](https://api.fxtwitter.com/status/2100757989212754085)。

<a id="smash-four-agents"></a>

### Smash 四角色 · 多个决策循环同时对战 · B

独立作者与视频，和 Pi 控制器同类比较；行为可展示，费用及战斗能力待验证。

缺强对手比较、胜率和延迟分布；四名角色都有动作不代表战术水平高。

详情与原理：[Smash 四角色 · 多个决策循环同时对战](../cases/2026-09-23-smash-four-agents/README.md)

来源：[X @maubaron](https://x.com/maubaron/status/2100738237237002706)

原帖发布：2026-09-18T00:06:40+00:00；快照：**3680 赞**，2026-09-23T04:32:46+00:00；[取数来源](https://api.fxtwitter.com/status/2100738237237002706)。

<a id="news-brand-matching"></a>

### Newsjack · 给品牌匹配当天新闻 · B

具体匹配任务有原帖；费用/速度是自测，获得媒体报道的效果不作事实保证。

未验证记者回应或报道转化；同一时间内处理量不等于同等输出质量，完整采集成本未知。

详情与原理：[Newsjack · 给品牌匹配当天新闻](../cases/2026-09-23-news-brand-matching/README.md)

来源：[X @elvissun](https://x.com/elvissun/status/2100951347080421409)

实现 / 方法（源码链接固定到审核版本）：[1](http://newsjack.sh)

原帖发布：2026-09-18T14:13:29+00:00；快照：**3930 赞**，2026-09-23T04:32:40+00:00；[取数来源](https://api.fxtwitter.com/status/2100951347080421409)。

<a id="backdoor-job-matching"></a>

### Backdoor · 对照履历筛选岗位线索 · C

C 针对把语义匹配描述成录用机会预测；保留筛选原型，不认可未经验证的概率含义。

匹配分不是录用概率；缺真实招聘结果和偏差评估，不能据此预测“最可能拿到哪些工作”。

详情与原理：[Backdoor · 对照履历筛选岗位线索](../cases/2026-09-23-backdoor-job-matching/README.md)

来源：[X @sarvagya_kul](https://x.com/sarvagya_kul/status/2100980770206879849)

原帖发布：2026-09-18T16:10:24+00:00；快照：**1770 赞**，2026-09-23T04:30:00+00:00；[取数来源](https://api.fxtwitter.com/status/2100980770206879849)。

<a id="gojiberry-outreach"></a>

### Gojiberry · 检查销售线索与消息是否匹配 · C

C 针对“预测消息表现/最有效活动”的结果外推；语义匹配演示本身保留。

判断合不合适不能等同于预测回复率或成交；缺真实 A/B 试验和完整采集成本，MCP 当时是预告。

详情与原理：[Gojiberry · 检查销售线索与消息是否匹配](../cases/2026-09-23-gojiberry-outreach/README.md)

来源：[X @romanbuildsaas](https://x.com/romanbuildsaas/status/2100891604735099103)

原帖发布：2026-09-18T10:16:05+00:00；快照：**3364 赞**，2026-09-23T04:29:59+00:00；[取数来源](https://api.fxtwitter.com/status/2100891604735099103)。

<a id="flowsery-replay"></a>

### Flowsery · 从网页回放中挑出可疑问题 · C

C 针对从批量判断跳到自动修复的归因；按有媒体的事件排查原型收录，明确未知分工。

Jev 不直接生成 PR 代码；“看完回放并修好”把多环节混为一谈。缺人工真值、误报和补丁验收，功能当时仍预告接入。

详情与原理：[Flowsery · 从网页回放中挑出可疑问题](../cases/2026-09-23-flowsery-replay/README.md)

来源：[X @tarasshyn](https://x.com/tarasshyn/status/2101012033340571952)

原帖发布：2026-09-18T18:14:38+00:00；快照：**835 赞**，2026-09-23T04:30:01+00:00；[取数来源](https://api.fxtwitter.com/status/2101012033340571952)。

<a id="voice-partial-tools"></a>

### 半句语音选工具 · 提前判断下一步 · B

任务和替换位置明确，提前行动的收益与风险需用真实对话测量。

提前选择可能因改口出错；没有与等待完整句子的错误率、延迟和任务完成率对照。

详情与原理：[半句语音选工具 · 提前判断下一步](../cases/2026-09-23-voice-partial-tools/README.md)

来源：[X @BhosalePratim](https://x.com/BhosalePratim/status/2100986774742765991)

原帖发布：2026-09-18T16:34:16+00:00；快照：**477 赞**，2026-09-23T04:32:36+00:00；[取数来源](https://api.fxtwitter.com/status/2100986774742765991)。

<a id="mutuals-character"></a>

### Mutuals · 用多个判断拼出角色反应 · B

独立产品作者的原型；Jev 负责哪些参数与最终表演质量仍待核。

“没有预设表情”不证明没有预设动作或参数范围；缺自然度评测与逐环节延迟。

详情与原理：[Mutuals · 用多个判断拼出角色反应](../cases/2026-09-23-mutuals-character/README.md)

来源：[X @john_bortotti](https://x.com/john_bortotti/status/2101019513676345555)

原帖发布：2026-09-18T18:44:21+00:00；快照：**790 赞**，2026-09-23T04:32:34+00:00；[取数来源](https://api.fxtwitter.com/status/2101019513676345555)。

<a id="whale-city-game"></a>

### 鲸背城市 · 用决策推进生存故事 · B

B 支持分工明确的互动实验，视频由另一模型生成，不归给 Jev。

没有游戏状态、平衡性、有效行动校验和完整费用；视频片段数量不等于独立成功任务数。

详情与原理：[鲸背城市 · 用决策推进生存故事](../cases/2026-09-23-whale-city-game/README.md)

来源：[X @gokayfem](https://x.com/gokayfem/status/2101022590722810271)

原帖发布：2026-09-18T18:56:35+00:00；快照：**268 赞**，2026-09-23T04:32:33+00:00；[取数来源](https://api.fxtwitter.com/status/2101022590722810271)。

<a id="email-1500-ryan"></a>

### 个人邮箱分类 · 用 1,500 封邮件试验整理 · B

与其他作者的 500 封邮件演示分开，同类比较；只按批量分类实验收录。

作者满意不等于准确率；缺漏分、错分和其他邮箱泛化数据，也不能推断完整邮箱助手能力。

详情与原理：[个人邮箱分类 · 用 1,500 封邮件试验整理](../cases/2026-09-23-email-1500-ryan/README.md)

来源：[X @ryanvogel](https://x.com/ryanvogel/status/2100042788851101842)

原帖发布：2026-09-16T02:03:12+00:00；快照：**3550 赞**，2026-09-23T04:32:51+00:00；[取数来源](https://api.fxtwitter.com/status/2100042788851101842)。

<a id="plain-english-interpreter"></a>

### 自然语言逻辑解释器 · 把规则交给程序执行 · B

作为语言执行原型收录，未知实现保持未知，不推断具备形式证明能力。

“Jev 不能推理”是作者观点，不是该演示证明的模型结论；完整性、终止性和错误传播未评测。

详情与原理：[自然语言逻辑解释器 · 把规则交给程序执行](../cases/2026-09-23-plain-english-interpreter/README.md)

来源：[X @narphorium](https://x.com/narphorium/status/2100985027093749764)

原帖发布：2026-09-18T16:27:19+00:00；快照：**501 赞**，2026-09-23T04:32:36+00:00；[取数来源](https://api.fxtwitter.com/status/2100985027093749764)。

<a id="visual-reference-finder"></a>

### 视觉参考查找 · 按描述找创作素材 · B

检索用途明确；图像处理分工与结果质量未验证，获取入口不等于素材使用授权。

100 张结果不等于 100 张都相关；缺来源覆盖、重复率、准确性及使用权逐图说明。

详情与原理：[视觉参考查找 · 按描述找创作素材](../cases/2026-09-23-visual-reference-finder/README.md)

来源：[X @albicodes](https://x.com/albicodes/status/2100720936852857271)

原帖发布：2026-09-17T22:57:55+00:00；快照：**712 赞**，2026-09-23T04:32:47+00:00；[取数来源](https://api.fxtwitter.com/status/2100720936852857271)。

<a id="higgsfield-voice-ads"></a>

### Higgsfield · 用语音串起广告制作 · B

补到同项目较早的官方分工说明：Jev 选择素材，生成由其他组件完成；流程可靠性和完整成本仍未验证。

不能把图像、视频生成全归给 Jev；缺源码、重复任务成功率、制作质量和整套成本对照。

详情与原理：[Higgsfield · 用语音串起广告制作](../cases/2026-09-23-higgsfield-voice-ads/README.md)

来源：[X @higgsfield_ai](https://x.com/higgsfield_ai/status/2102369525048168862) · [X @higgsfield_ai](https://x.com/higgsfield_ai/status/2101117855622463719)

原帖发布：2026-09-22T12:08:49+00:00；快照：**202 赞**，2026-09-23T03:53:20+00:00；[取数来源](https://api.fxtwitter.com/status/2102369525048168862)。

<a id="ad-analysis"></a>

### StealAds 广告拆解预览 · C

同一 StealAds 项目合并，不新增卡片。C 针对“取代焦点小组”的宣传：模拟判断不能证明真实受众行为。

虚构画像的判断不是消费者调查，不能替代真实焦点小组；没有实际行为验证，StealAds/MCP 仍按原帖预告记录。

详情与原理：[StealAds 广告拆解预览](../cases/2026-09-18-ad-analysis/README.md)

来源：[X @TheMattBerman](https://x.com/TheMattBerman/status/2100654891756589230) · [X @TheMattBerman](https://x.com/TheMattBerman/status/2101439340588974096)

原帖发布：2026-09-17T18:35:29+00:00；快照：**1678 赞**，2026-09-17T22:42:26.368800+00:00；[取数来源](https://api.fxtwitter.com/status/2100654891756589230)。
