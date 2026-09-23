# 2026-09-23 · 第十轮增量与证据审核

**简体中文** | [English](2026-09-23-increment10-audit.en.md)

核对截止 **2026-09-23 12:09:12 北京时间**。新增 **11** 项、合并更新 **2** 项，共 **148 项、11 类**（A 29 / B 102 / C 17）。全部仍为**未复现**。

本轮使用 X 最新搜索 `Jev min_faves:200 since:2026-09-21`，与上轮截止点（9 月 21 日 11:02:26 北京时间）重叠。核对部分原作者线程、回复、四个固定版本开源仓库及 OpenClaw/MotherDuck 官方文章。本轮是按证据筛选的增量整理，不是 X 全量遍历或导出，不承诺无遗漏。

主帖点赞与媒体采用 FxTwitter 逐帖快照，可能有缓存；不累加回复或引用点赞，精确取数时间和渠道保存在共享数据。本轮未执行第三方项目或调用付费模型。A 表示实现证据可检查，B 表示原型明确但效果待验证，C 表示宣传超出当前证据；等级不代表独立复现。

## 去重决定

| 线索 | 处理 |
| --- | --- |
| DuckDB / MotherDuck | 原扩展作者参与托管功能文章，按相关 SQL 集成合并；说明部署不同，保留原帖快照与首次收录时间。 |
| Mario 教师数据 | 同作者、同 harness；合并更换 DeepSeek 教师的后续，新通关宣传不归给 Jev。 |
| Astra-Ares | 演示与开源回复只计一个控制器；调推理强度与切换模型不是同一机制。 |
| Kaku / Shiori | 独立作者与产品，分别面向笔记和网页书签，同类比较标签与复核流程。 |
| Needle / 联动编辑 | 同作者但分别做检索与编辑，任务、媒体不同，尚无依据视为 Needle 的版本更新；计划中的扩展不另算。 |
| Perch / ESLint 实验 | 独立仓库和实现，归代码审查类比较，不因用途相似就当重复。 |
| Higgsfield | 新语音入口属于此前未收的广告流程，整个流程只计一次。 |
| OpenClaw | Jev 接口集成计一次，各拟议插件与其他决策模型不分别新增。 |
| 转载与仿制模型 | 同片重复、泛宣传和独立 Jev 兼容模型不作为新 TypeSafe Jev 应用。 |

## 逐项依据

<a id="astra-ares"></a>

### Astra-Ares · 按任务进展调节思考力度 · A

A 针对可检查的控制实现；50% 省费与更快运行仍是作者自测，缓存结构保持不等于命中率已验证。

早期预览，需要补丁 CLI；不是在一次生成中途改内部思考。验证文档明确未测工作负载省费与缓存命中率，不能保证普遍省一半。

详情与原理：[Astra-Ares · 按任务进展调节思考力度](../cases/2026-09-23-astra-ares/README.md)

来源：[X @miu21590](https://x.com/miu21590/status/2101857866378362926) · [X @miu21590](https://x.com/miu21590/status/2102404547587318081)

实现 / 方法：[README.md](https://github.com/miuuyy/Astra-Ares/blob/a1dbc976103e300419cb0b4ab54150ad6a3e0b4b/README.md) · [bridge.mjs](https://github.com/miuuyy/Astra-Ares/blob/a1dbc976103e300419cb0b4ab54150ad6a3e0b4b/src/bridge.mjs) · [validation.md](https://github.com/miuuyy/Astra-Ares/blob/a1dbc976103e300419cb0b4ab54150ad6a3e0b4b/docs/validation.md)

主帖快照：**3466 赞**，2026-09-23T03:53:20+00:00；[取数来源](https://api.fxtwitter.com/status/2101857866378362926)。

<a id="webctl"></a>

### webctl · 先筛网页，再交给研究助手 · A

A 表示筛选流程与评测边界可检查；小样本、单次运行与分项计费不足以证明普遍更准更便宜。

30 个问题、每组只跑一次，模型裁判并非人工真值；Jev 和摘要调用未计入 token 统计且另行计费，不能用上下文减少量推导全流程省费。

详情与原理：[webctl · 先筛网页，再交给研究助手](../cases/2026-09-23-webctl/README.md)

来源：[X @dorkitude](https://x.com/dorkitude/status/2102194028704092585)

实现 / 方法：[README.md](https://github.com/dorkitude/webctl/blob/ab99fe743a8f30ad26437eaf8c15d1965ae46d4d/README.md) · [chunks.go](https://github.com/dorkitude/webctl/blob/ab99fe743a8f30ad26437eaf8c15d1965ae46d4d/internal/jev/chunks.go) · [RESULTS.md](https://github.com/dorkitude/webctl/blob/ab99fe743a8f30ad26437eaf8c15d1965ae46d4d/benchmarks/RESULTS.md)

主帖快照：**357 赞**，2026-09-23T03:56:00+00:00；[取数来源](https://api.fxtwitter.com/status/2102194028704092585)。

<a id="jimothy"></a>

### Jimothy · 把 Jev 的示范教给本地分类器 · A

A 针对可检查的数据与训练分工；小模型速度不能直接当完整流程速度，教师错误也可能被继承。

本地运行的是学生模型，不是 Jev 权重；回退 Jev 要由应用实现。阈值只衡量与所供标签的一致性，不能保证新分布或真实正确率。

详情与原理：[Jimothy · 把 Jev 的示范教给本地分类器](../cases/2026-09-23-jimothy/README.md)

来源：[X @AndrewPrifer](https://x.com/AndrewPrifer/status/2102162296739099126)

实现 / 方法：[README.md](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/README.md) · [teacher.ts](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/src/teacher.ts) · [automatic-training.md](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/docs/automatic-training.md)

主帖快照：**367 赞**，2026-09-23T03:56:58+00:00；[取数来源](https://api.fxtwitter.com/status/2102162296739099126)。

<a id="perch"></a>

### Perch · 用自然语言规则检查代码 · A

A 针对扫描与规则实现；不能把置信度当已验证缺陷，仍需定位、复现与回归检查。

概率排名不是缺陷证明；没有独立检出率基准。邻接上下文有上限，超长方法最多八遍，部分读取与失败需查看记录。

详情与原理：[Perch · 用自然语言规则检查代码](../cases/2026-09-23-perch/README.md)

来源：[X @joshuafbrown](https://x.com/joshuafbrown/status/2102085153015451695)

实现 / 方法：[README.md](https://github.com/lakeday-org/perch/blob/69b519d903e5528ca32557fce61d0e2e7d90ced6/README.md) · [scan.js](https://github.com/lakeday-org/perch/blob/69b519d903e5528ca32557fce61d0e2e7d90ced6/src/scan.js) · [scan.md](https://github.com/lakeday-org/perch/blob/69b519d903e5528ca32557fce61d0e2e7d90ced6/docs/scan.md)

主帖快照：**229 赞**，2026-09-23T03:58:14+00:00；[取数来源](https://api.fxtwitter.com/status/2102085153015451695)。

<a id="presentation-coach"></a>

### 演讲教练 · 提醒哪些要点还没讲 · B

用途和原型明确，公开可用性及真实演讲中的准确性尚未验证。

作者明确只在自己的 Slides 本地副本中实现，尚未上线；不据此认定 Jev 直接处理音频或能可靠判断表达质量。

详情与原理：[演讲教练 · 提醒哪些要点还没讲](../cases/2026-09-23-presentation-coach/README.md)

来源：[X @hakimel](https://x.com/hakimel/status/2102355980621324494) · [X @hakimel](https://x.com/hakimel/status/2102473499159703960)

主帖快照：**202 赞**，2026-09-23T03:53:49+00:00；[取数来源](https://api.fxtwitter.com/status/2102355980621324494)。

<a id="kaku-note-tags"></a>

### Kaku · 按已有习惯给笔记打标签 · B

任务与复核流程有作者依据；大规模分类质量、成本和具体模型配置仍待验证。

置信度不等于标注正确率；没有人工标注对照、漏标统计或跨笔记库验证。不能仅凭面向 Obsidian 用户的介绍认定它是 Obsidian 插件。

详情与原理：[Kaku · 按已有习惯给笔记打标签](../cases/2026-09-23-kaku-note-tags/README.md)

来源：[X @gemama0](https://x.com/gemama0/status/2102198046201086356) · [X @gemama0](https://x.com/gemama0/status/2102198213067612337) · [X @gemama0](https://x.com/gemama0/status/2102334807376367678) · [X @gemama0](https://x.com/gemama0/status/2102360440353480999)

实现 / 方法：[kaku.md](https://kaku.md)

主帖快照：**2026 赞**，2026-09-23T03:55:29+00:00；[取数来源](https://api.fxtwitter.com/status/2102198046201086356)。

<a id="semantic-edit-consistency"></a>

### 联动编辑 · 改一处，找出其他需要改的地方 · B

支持联动编辑原型；全量覆盖、实时性和可用性仍待补证据。

开源 Chrome 扩展仍是作者计划，未核实发布；没有长文档漏检、错误建议或完整往返延迟对照。

详情与原理：[联动编辑 · 改一处，找出其他需要改的地方](../cases/2026-09-23-semantic-edit-consistency/README.md)

来源：[X @Saboo_Shubham_](https://x.com/Saboo_Shubham_/status/2102297903247307067)

主帖快照：**225 赞**，2026-09-23T03:54:25+00:00；[取数来源](https://api.fxtwitter.com/status/2102297903247307067)。

<a id="higgsfield-voice-ads"></a>

### Higgsfield · 用语音串起广告制作 · B

可支持语音广告制作的集成演示；精确分工及可靠性未知，保留 B。

不能把图像、视频生成全归给 Jev；缺源码、重复任务成功率、制作质量和整套成本对照。

详情与原理：[Higgsfield · 用语音串起广告制作](../cases/2026-09-23-higgsfield-voice-ads/README.md)

来源：[X @higgsfield_ai](https://x.com/higgsfield_ai/status/2102369525048168862)

主帖快照：**202 赞**，2026-09-23T03:53:20+00:00；[取数来源](https://api.fxtwitter.com/status/2102369525048168862)。

<a id="openclaw-decisions"></a>

### OpenClaw · 给插件接上统一决策接口 · B

接口进展有官方来源，但生产发布与各拟议用途的实际效果未验证；它是可选能力，不会自动开启所有功能。

官方限定于开发检出版本，配套 provider 包仍等待支持版本发布；语音开关、工具过滤、压缩和模型路由多属探索或提案，不能当已全部落地。

详情与原理：[OpenClaw · 给插件接上统一决策接口](../cases/2026-09-23-openclaw-decisions/README.md)

来源：[X @openclaw](https://x.com/openclaw/status/2102488199486656862)

实现 / 方法：[decision-models-in-openclaw](https://openclaw.ai/blog/decision-models-in-openclaw)

主帖快照：**438 赞**，2026-09-23T03:51:47+00:00；[取数来源](https://api.fxtwitter.com/status/2102488199486656862)。

<a id="sf-unreal-city"></a>

### 旧金山城市演示 · 让虚拟街区动起来 · C

C 针对“驱动一切”的宽泛归因；保留城市演示事实，实体行为分工和规模效果仍未知。

“所有东西都由 Jev 驱动”缺实现依据；不能把渲染、物理和整座城市生成归给 Jev，也没有地理准确性或大规模稳定性验证。

详情与原理：[旧金山城市演示 · 让虚拟街区动起来](../cases/2026-09-23-sf-unreal-city/README.md)

来源：[X @MatthewBerman](https://x.com/MatthewBerman/status/2102483668468195539) · [X @MatthewBerman](https://x.com/MatthewBerman/status/2102488078019600433)

主帖快照：**1501 赞**，2026-09-23T03:51:47+00:00；[取数来源](https://api.fxtwitter.com/status/2102483668468195539)。

<a id="btc-polymarket-paper"></a>

### BTC 模拟交易 · 用订单簿估计五分钟涨跌 · B

B 仅支持明确的模拟交易实验，预测准确性和可盈利性均未验证。

没有概率校准、样本外结果或计入手续费、延迟和滑点的对照；模型分数不等于可靠公允价值，也不能由短演示推出盈利。

详情与原理：[BTC 模拟交易 · 用订单簿估计五分钟涨跌](../cases/2026-09-23-btc-polymarket-paper/README.md)

来源：[X @FrankDa18249347](https://x.com/FrankDa18249347/status/2102197241331290121)

实现 / 方法：[Demo](http://jev-poly-crypto-demo-black.vercel.app/)

主帖快照：**356 赞**，2026-09-23T03:55:29+00:00；[取数来源](https://api.fxtwitter.com/status/2102197241331290121)。

<a id="duckdb"></a>

### DuckDB / MotherDuck · 在 SQL 里给文字分类 · B

新文章补充数据集、查询和统计口径，但仍是厂商自测；B 保留。NULL 排除和训练划分来源需一并看，不能把宣传倍率当通用结论。

MotherDuck 功能面向付费方案。评测用 AG News 训练划分抽取的 10 万行，准确率公式排除 NULL；不同并发及全流程条件不足以证明普遍等准或省费。

详情与原理：[DuckDB / MotherDuck · 在 SQL 里给文字分类](../cases/2026-09-18-duckdb/README.md)

来源：[X @hamiltonulmer](https://x.com/hamiltonulmer/status/2100370557405667768) · [X @hamiltonulmer](https://x.com/hamiltonulmer/status/2101700765656264896) · [X @motherduck](https://x.com/motherduck/status/2102077291081896307)

实现 / 方法：[Demo](https://motherduck.com/blog/motherduck-supports-jev/)

主帖快照：**1310 赞**，2026-09-17T22:42:25.668728+00:00；[取数来源](https://api.fxtwitter.com/status/2100370557405667768)。

<a id="mario-lightgbm-teacher"></a>

### Mario 教师数据 · Jev 示范，小模型接手 · B

合并同作者、同 harness 的后续反向证据；保留原始主帖，明确教师已换成 DeepSeek，不能把新通关宣传归给 Jev。

两个教师版本缺相同数据量、未见关卡和多次运行记录；倍率不是 Jev 本体加速，准备与训练成本未知。

详情与原理：[Mario 教师数据 · Jev 示范，小模型接手](../cases/2026-09-21-mario-lightgbm-teacher/README.md)

来源：[X @nwnwnyo](https://x.com/nwnwnyo/status/2101605150242849140) · [X @nwnwnyo](https://x.com/nwnwnyo/status/2102297736011997680)

主帖快照：**945 赞**，2026-09-21T02:49:26+00:00；[取数来源](https://api.fxtwitter.com/status/2101605150242849140)。

## 访问状态与范围

[较新的官方公告](https://x.com/typesafeai/status/2102281508950307159)称为保证容量暂时暂停新用户注册，已有用户继续使用。当前访问状态应以此更新上轮“取消等待名单”的历史记录；公告不计作应用。

细节待核线索进入[待整理区](../inbox/README.md)，不计正式总数。原帖快照与首次收录时间保留，仅这 13 个变更条目刷新内容更新时间，另 135 个旧条目保持不变。中英文保留六个精选与 11 个折叠双列分类。
