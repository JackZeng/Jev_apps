# 2026-09-21 · 第九轮增量与证据审核

**简体中文** | [English](2026-09-21-increment9-audit.en.md)

核对截止 **2026-09-21 11:02:26 北京时间**。新增 **10** 项、合并更新 **2** 项，共 **137 项、11 类**；A 25 / B 96 / C 16。全部仍为**未复现**。

本轮使用 X 最新搜索 `Jev min_faves:200 since:2026-09-20`，与上轮截止点（9 月 20 日 11:01:10 北京时间）重叠，并核对原作者线程、固定版本仓库和公开资源页。AnimeAct 是通过新引用发现的较早原帖。X 索引并非全量数据，不承诺无遗漏。

主帖点赞和媒体采用 FxTwitter 逐帖快照，可能存在缓存；不累加回复或引用点赞，精确取数时间和渠道保存在共享数据中。本轮未执行第三方项目、未调用付费模型。A 表示实现证据较清楚，B 表示原型明确但效果待验证，C 表示核心宣传超出证据；等级不等于复现状态。

## 去重决定

| 线索 | 处理 |
| --- | --- |
| DuckDB 重写 | 同一扩展，新提速的基线是作者旧实现，合并更新。 |
| Third Hand / arc-cua | 同作者的独立 Swift/Python 仓库；后者明确沿用文字输入思路，按相关方案合在一张卡片，说明不是同一程序。 |
| Minecraft | 与已有混合控制器作者、仓库不同；比较固定路线先验和控制分工。 |
| Mario 教师数据 | 独立作者与架构：Jev 准备数据、LightGBM 现场控制；同片转载不重复计数。 |
| Toothless / CNVS | 同类唤醒判断、独立作者与媒体，归同类比较。 |
| Token / 词 / 字符循环 | 独立实验按候选粒度比较，转载不另收。 |
| Jev Field Notes | 只收录整理流程本身，不把集合中的演示重复计数。 |
| AnimeAct | 使用原作者主帖，新引用不新增案例。 |

## 逐项依据

<a id="docjev"></a>

### DocJev · 给文档分类、拆分合订本 · A

实现和测量边界清楚；“同等准确、约六倍快”只部分成立，拆分质量有差异且计时不含完整处理。

完整原理、结果边界与对比：[DocJev · 给文档分类、拆分合订本](../cases/2026-09-21-docjev/README.md)。

来源：[X @jerryjliu0](https://x.com/jerryjliu0/status/2101738281046294552)

实现 / 方法：[README.md](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/README.md) · [jev.py](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/src/jev_docs/engines/jev.py) · [report.md](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/benchmarks/results/real-small-v1-run01/report.md)

主帖快照：**695 赞**，2026-09-21T02:44:57+00:00；[取数来源](https://api.fxtwitter.com/status/2101738281046294552)。

<a id="dasheng-reading"></a>

### 大声读 · 检查朗读有没有漏词、变意 · C

实现可检查，但“平替整套口语产品”及仓库的完全离线表述超出当前评分能力与网络调用事实。

完整原理、结果边界与对比：[大声读 · 检查朗读有没有漏词、变意](../cases/2026-09-21-dasheng-reading/README.md)。

来源：[X @wquguru](https://x.com/wquguru/status/2101711235628810669)

实现 / 方法：[README.md](https://github.com/wquguru/dasheng/blob/1bacff4a075527e6c02da242a72d117e7cb3286b/README.md) · [jev.js](https://github.com/wquguru/dasheng/blob/1bacff4a075527e6c02da242a72d117e7cb3286b/lib/jev.js) · [score.js](https://github.com/wquguru/dasheng/blob/1bacff4a075527e6c02da242a72d117e7cb3286b/lib/score.js)

主帖快照：**351 赞**，2026-09-21T02:45:24+00:00；[取数来源](https://api.fxtwitter.com/status/2101711235628810669)。

<a id="needle-semantic-find"></a>

### Needle · 按意思查找网页原文 · A

固定代码可核对提取、相关性判断和原句选择；A 表示分工清楚，不代表搜索完整性已验证。

完整原理、结果边界与对比：[Needle · 按意思查找网页原文](../cases/2026-09-21-needle-semantic-find/README.md)。

来源：[X @Saboo_Shubham_](https://x.com/Saboo_Shubham_/status/2101576462042366114) · [X @Saboo_Shubham_](https://x.com/Saboo_Shubham_/status/2101577105809240488)

实现 / 方法：[README.md](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/9e860951aaf5c82801779e43e748dcf92042879a/advanced_llm_apps/needle/README.md) · [search.mjs](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/9e860951aaf5c82801779e43e748dcf92042879a/advanced_llm_apps/needle/server/search.mjs)

主帖快照：**1658 赞**，2026-09-21T02:50:32+00:00；[取数来源](https://api.fxtwitter.com/status/2101576462042366114)。

<a id="reddit-radar-mcp"></a>

### Reddit Radar MCP · 按自定义条件筛帖子 · B

任务与演示明确，规模和商业判断效果仍属作者陈述。

完整原理、结果边界与对比：[Reddit Radar MCP · 按自定义条件筛帖子](../cases/2026-09-21-reddit-radar-mcp/README.md)。

来源：[X @oguzhankayancom](https://x.com/oguzhankayancom/status/2101667801274478707)

主帖快照：**295 赞**，2026-09-21T02:47:23+00:00；[取数来源](https://api.fxtwitter.com/status/2101667801274478707)。

<a id="toothless-voice-gate"></a>

### Toothless · 判断一句话是不是在叫助手 · B

可支持语音入口的判断原型；自然接话与长期常驻可靠性仍待验证。

完整原理、结果边界与对比：[Toothless · 判断一句话是不是在叫助手](../cases/2026-09-21-toothless-voice-gate/README.md)。

来源：[X @ashutoshpuro97](https://x.com/ashutoshpuro97/status/2101660362882085299)

主帖快照：**266 赞**，2026-09-21T02:48:14+00:00；[取数来源](https://api.fxtwitter.com/status/2101660362882085299)。

<a id="mario-lightgbm-teacher"></a>

### Mario 教师数据 · Jev 示范，小模型接手 · B

明确区分教师与运行模型；短片和作者说明尚不能证明泛化或稳定通关。

完整原理、结果边界与对比：[Mario 教师数据 · Jev 示范，小模型接手](../cases/2026-09-21-mario-lightgbm-teacher/README.md)。

来源：[X @nwnwnyo](https://x.com/nwnwnyo/status/2101605150242849140)

主帖快照：**945 赞**，2026-09-21T02:49:26+00:00；[取数来源](https://api.fxtwitter.com/status/2101605150242849140)。

<a id="minecraft-fixed-route"></a>

### Minecraft 固定路线 · 规划与动作选择协作 · C

“Jev 操作 WASD/鼠标”的说法与仓库明确的结构化状态及高层动作不一致；收录受限路线实验，不据此认定通用自主通关。

完整原理、结果边界与对比：[Minecraft 固定路线 · 规划与动作选择协作](../cases/2026-09-21-minecraft-fixed-route/README.md)。

来源：[X @rronak_](https://x.com/rronak_/status/2101544156757950697) · [X @rronak_](https://x.com/rronak_/status/2101544158502728002)

实现 / 方法：[README.md](https://github.com/rmalde/minecraft-agent/blob/78b40ed59514e5e2abde33a05ce398ecb2c39e05/README.md) · [config.json](https://github.com/rmalde/minecraft-agent/blob/78b40ed59514e5e2abde33a05ce398ecb2c39e05/optimization/nether/config.json)

主帖快照：**6861 赞**，2026-09-21T02:51:31+00:00；[取数来源](https://api.fxtwitter.com/status/2101544156757950697)。

<a id="token-choice-loop"></a>

### Token 选择循环 · 用选择题逐步拼文字 · B

循环结构和原型有来源；只能证明一种拼接思路，文本质量与效率待验证。

完整原理、结果边界与对比：[Token 选择循环 · 用选择题逐步拼文字](../cases/2026-09-21-token-choice-loop/README.md)。

来源：[X @erikdunteman](https://x.com/erikdunteman/status/2101533797527454109)

主帖快照：**211 赞**，2026-09-21T02:50:32+00:00；[取数来源](https://api.fxtwitter.com/status/2101533797527454109)。

<a id="jev-field-notes-curation"></a>

### Jev Field Notes · 用 Jev 整理 Jev 案例 · B

来源支持作者的整理原型；尚不能证明自动更新完整性、去重率或事实核查能力。

完整原理、结果边界与对比：[Jev Field Notes · 用 Jev 整理 Jev 案例](../cases/2026-09-21-jev-field-notes-curation/README.md)。

来源：[X @omarsar0](https://x.com/omarsar0/status/2101696753749655863)

实现 / 方法：[jev-field-notes](https://academy.dair.ai/resources/jev-field-notes)

主帖快照：**298 赞**，2026-09-21T02:45:54+00:00；[取数来源](https://api.fxtwitter.com/status/2101696753749655863)。

<a id="animeact-jev-demo"></a>

### AnimeAct · 让角色跟着台词做表情和动作 · B

可确认联动演示，精确接口和正式可用性待补；商品页还含未来日期，不能据此当成已发布。

完整原理、结果边界与对比：[AnimeAct · 让角色跟着台词做表情和动作](../cases/2026-09-21-animeact-jev-demo/README.md)。

来源：[X @frombit_jp](https://x.com/frombit_jp/status/2101298040741253195)

实现 / 方法：[8507737](https://frombit.booth.pm/items/8507737)

主帖快照：**2014 赞**，2026-09-21T02:50:32+00:00；[取数来源](https://api.fxtwitter.com/status/2101298040741253195)。

<a id="duckdb"></a>

### DuckDB 语义分类扩展 · B

新数字属于同一 DuckDB 集成的软件优化；作者承认旧版低效，缺同条件公开基准，保留 B 并合并更新。

完整原理、结果边界与对比：[DuckDB 语义分类扩展](../cases/2026-09-18-duckdb/README.md)。

来源：[X @hamiltonulmer](https://x.com/hamiltonulmer/status/2100370557405667768) · [X @hamiltonulmer](https://x.com/hamiltonulmer/status/2101700765656264896)

主帖快照：**1310 赞**，2026-09-17T22:42:25.668728+00:00；[取数来源](https://api.fxtwitter.com/status/2100370557405667768)。

<a id="third-hand"></a>

### Third Hand / arc-cua · 选动作操作 Mac · A

A 仅针对公开实现分工；arc-cua 明确复用 Third Hand 的文字输入思路，作为同作者相关方案合并。“解决电脑操作”和普遍提速没有基准支持。

完整原理、结果边界与对比：[Third Hand / arc-cua · 选动作操作 Mac](../cases/2026-09-20-third-hand/README.md)。

来源：[X @sxhivs](https://x.com/sxhivs/status/2101367048223982065) · [X @sxhivs](https://x.com/sxhivs/status/2101367050207981608) · [X @sxhivs](https://x.com/sxhivs/status/2101729362194432184) · [X @sxhivs](https://x.com/sxhivs/status/2101729364203475072)

实现 / 方法：[README.md](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/README.md) · [TextEntryPlan.swift](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/TextEntryPlan.swift) · [JevClient.swift](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/JevClient.swift) · [README.md](https://github.com/shhivv/arc-cua/blob/85fc321715e23f51c222d59d31461b75804ba4ac/README.md) · [typesafe.py](https://github.com/shhivv/arc-cua/blob/85fc321715e23f51c222d59d31461b75804ba4ac/src/arc_cua/policies/typesafe.py)

主帖快照：**549 赞**，2026-09-20T02:46:29+00:00；[取数来源](https://api.fxtwitter.com/status/2101367048223982065)。

## 状态与范围

[9 月 21 日官方公告](https://x.com/typesafeai/status/2101786156572823624)称 Jev 已取消等待名单。这是服务访问状态，不作为新应用，也不能说明各工具均已可用。

细节不清的线索放入[待整理区](../inbox/README.md)，不计入正式总数。既有主帖快照和首次收录时间保留，仅这 12 项刷新内容更新时间。中英文均保留六个精选与 11 个折叠双列分类。
