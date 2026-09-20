# 2026-09-20 · 第八轮增量与证据审核

**简体中文** | [English](2026-09-20-increment8-audit.en.md)

核对截止 **2026-09-20 11:01:10 北京时间**。新增 **15** 项、合并更新 **4** 项，共 **127 项、11 类**；全库 A 23 / B 90 / C 14。全部仍为**未复现**。

本轮从上次核对截止（2026-09-19 17:48:49 北京时间）向后检索，并保留交界处重叠。使用 X 最新搜索 `Jev min_faves:200 since:2026-09-19`，再阅读作者线程、固定版本文档与相关源码。X 索引不等于全量数据；这不是“已找全”的承诺。

主帖点赞与媒体来自 FxTwitter 公开接口的逐帖快照，可能有缓存；时间保留在共享数据及下面各项。只计算本项目原帖，不累加回复或引用点赞。作者声明、可检查源码、公开评测与本库复现分开；未调用模型、未执行第三方项目。

A＝实现与边界较清楚；B＝原型/任务明确，效果仍待验证；C＝核心宣传超出证据。A 不等于独立验证。新条目 A 3 / B 12；TipTour 因新增固定源码由 B 调为 A，其他更新保持原等级。

## 去重决定

| 线索 | 决定与理由 |
| --- | --- |
| TipTour 开源 | 同作者、引用原 CoreML/OCR 演示，合并原项目。 |
| Hermes 压缩评测 | 针对已收插件的移植评测，加入上下文压缩的支持/反向证据，不新增应用。 |
| Ryze 七种新工作流 | 同一产品的细化描述，不拆成七个项目；复制效果数字的转载不计数。 |
| 12306 查询 | 作者明确使用 Ultrafast，合并 Browser Use；不因换网站新增。 |
| 会议流程图与面试评分 | 虽同作者，但任务、输出、主帖与媒体不同，分别收录并说明分工。 |
| Third Hand 与其他电脑操作 | 独立 Swift 仓库；提取请求中文字的路径有别于 Ultrafast 生成填字、TipTour 只点击，归同类比较。 |
| 加拿大地图与颜色实验 | 引用启发来源，但有独立地图任务和视频，归交互类比较。 |
| 书籍预测与房源标签 | 同作者但数据、任务和媒体不同；分别归数据类。 |

## 新增与更新的逐项依据

<a id="meeting-flowchart"></a>

## 会议转流程图 · 边聊边整理业务 · B

流程分工与原帖演示支持原型；尚不能据此判断复杂会议的准确率或完整性。

**依据:** 作者描述：逐句判断是否涉及业务及新增/修改/删除/无操作；置信度至少 50% 才交给 LLM 整理步骤，再用 Jev 检查依据、重复和负责人，代码写入 draw.io。

**边界:** 50% 是作者设定的门槛，不是正确率保证；缺完整转录、漏记统计和与人工流程图的对照。

**作者报告:** 作者用虚构的房地产业务访谈展示约两分钟流程，并称视频为一倍速；低置信度内容跳过或留待确认。

案例：[会议转流程图 · 边聊边整理业务](../cases/2026-09-20-meeting-flowchart/README.md)

来源：[X @masa_okamura108](https://x.com/masa_okamura108/status/2101446065526632473)

主帖快照：**439 赞**，2026-09-20T02:45:24+00:00；[取数来源](https://api.fxtwitter.com/status/2101446065526632473)。

<a id="agent-goal-verifier"></a>

## 代理目标核验 · 每轮检查是否做完 · B

可确认作者的核验原型与试验范围；“适合所有验证”和长期代理能力提升仍缺基准。

**依据:** 作者在代理框架的 /goal 功能中加入自定义 verifier，每轮核验目标完成状态；完整输入、判定标准和失败处理尚未公开。

**边界:** 作者明确尚在试验、准备设计基准；不能把判定完成当作测试通过，也没有误停或漏检率。

**作者报告:** 作者称原先由更贵的推理模型核验，换用 Jev 后能更频繁检查；未提供完整质量与费用对照。

案例：[代理目标核验 · 每轮检查是否做完](../cases/2026-09-20-agent-goal-verifier/README.md)

来源：[X @omarsar0](https://x.com/omarsar0/status/2101443311454036477)

主帖快照：**317 赞**，2026-09-20T02:45:24+00:00；[取数来源](https://api.fxtwitter.com/status/2101443311454036477)。

<a id="drape-outfit-selection"></a>

## Drape 试衣实验 · 听要求选衣服 · B

作者澄清了 Jev 只选服装、独立视频环节负责换装；决策计时不证明整个试衣流程的实时性。

**依据:** 作者回复说明，输入包括语音转录与已有服装元数据；Jev 选择服装，实时视频到视频环节使用服装参考图。此实验尚未实际集成到 Drape 应用。

**边界:** 没有披露完整视频模型、转录链路或端到端账单；不能把单次选衣服的速度与费用当成完整试衣成本。

**作者报告:** 作者报告每次 Jev 决策约 620ms、0.0011 美元；并确认费用不含已有元数据的生成。

案例：[Drape 试衣实验 · 听要求选衣服](../cases/2026-09-20-drape-outfit-selection/README.md)

来源：[X @nailthy62](https://x.com/nailthy62/status/2101388186916454439) · [X @nailthy62](https://x.com/nailthy62/status/2101459808587284818) · [X @nailthy62](https://x.com/nailthy62/status/2101420612485103693) · [X @nailthy62](https://x.com/nailthy62/status/2101401929842831381)

主帖快照：**1379 赞**，2026-09-20T02:45:54+00:00；[取数来源](https://api.fxtwitter.com/status/2101388186916454439)。

<a id="goodreads-taste-prediction"></a>

## Goodreads · 预测个人五星书籍 · B

披露个人数据量和留出规模，但缺完整测试协议；性能倍率不能外推其他读者或推荐任务。

**依据:** 作者用约 1,000 条个人 Goodreads 评分作为起点，留出 100 条测试，比较 Jev 与 GPT-5.6 的五星预测。具体提示、切分和类别比例尚未公开核清。

**边界:** 100 条单人样本不足以证明通用推荐效果；还需确认多数类基线、信息泄漏、命中率与召回率。

**作者报告:** 作者报告 Jev 略准确、便宜 53 倍、快 25 倍；属于该设置下的自测，未独立复核。

案例：[Goodreads · 预测个人五星书籍](../cases/2026-09-20-goodreads-taste-prediction/README.md)

来源：[X @venturetwins](https://x.com/venturetwins/status/2101393861667115437)

主帖快照：**238 赞**，2026-09-20T02:45:53+00:00；[取数来源](https://api.fxtwitter.com/status/2101393861667115437)。

<a id="zillow-semantic-filters"></a>

## Zillow 房源 · 用自然语言加筛选条件 · B

可支持自定义房源标签原型；准确率、输入来源及完整计费边界待补证。

**依据:** 作者描述对房源做语义分类，示例包括建筑风格、装修和高速公路邻近程度；原始字段、地理数据及图像转文字过程未披露。

**边界:** 没有公开标注集或误分统计；不能推断 Jev 直接看房屋照片，也不能把邻近程度当作已核实的地图测量。

**作者报告:** 作者称处理数千房源不到 20 秒、费用 0.18 美元；数据获取与其他预处理是否计入未知。

案例：[Zillow 房源 · 用自然语言加筛选条件](../cases/2026-09-20-zillow-semantic-filters/README.md)

来源：[X @venturetwins](https://x.com/venturetwins/status/2101341075684434245)

主帖快照：**527 赞**，2026-09-20T02:47:09+00:00；[取数来源](https://api.fxtwitter.com/status/2101341075684434245)。

<a id="shiori-link-tagging"></a>

## Shiori · 给收藏链接自动打标签 · B

具体用途和对照媒体清楚；尚不足以证明优于 Haiku 或达到生产级分类质量。

**依据:** 作者展示 Shiori 自动标签功能中 Jev 与 Haiku 的对照；网页读取方式、标签集合和多标签规则未公开核清。

**边界:** 视频没有完整标注数据或同条件统计，不能从界面刷新速度认定标签质量相等。

**作者报告:** 主帖展示约 25 秒对照视频，未给可复核的准确率、费用或加速倍率。

案例：[Shiori · 给收藏链接自动打标签](../cases/2026-09-20-shiori-link-tagging/README.md)

来源：[X @brian_lovin](https://x.com/brian_lovin/status/2101321554130809156)

主帖快照：**327 赞**，2026-09-20T02:47:32+00:00；[取数来源](https://api.fxtwitter.com/status/2101321554130809156)。

<a id="jev-align"></a>

## jev-align · 用人工反馈调整判断标准 · A

源码可核对标签、GEPA 优化对象与人工接受流程；A 表示实现证据清楚，不代表已验证泛化收益。

**依据:** 固定版本 CLI 挑选不确定样例与随机审计样本；GEPA 用人工标签优化任务说明，由独立的反思模型提出修改。这是提示与规则优化，不是微调 Jev 权重。

**边界:** 训练分数上升不保证泛化；留出评估是可选配置，还需计算人工标注、反思模型及多轮评估成本。

**作者报告:** 公开代码和约两分钟演示支持工作流；没有在本库复现，也没有统一收益倍率。

案例：[jev-align · 用人工反馈调整判断标准](../cases/2026-09-20-jev-align/README.md)

来源：[X @sethkimmel3](https://x.com/sethkimmel3/status/2101357768640987302)

实现 / 方法：[README.md](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/README.md) · [optimizer.py](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/src/jev_align/optimizer.py)

主帖快照：**511 赞**，2026-09-20T02:47:09+00:00；[取数来源](https://api.fxtwitter.com/status/2101357768640987302)。

<a id="third-hand"></a>

## Third Hand · 从指令里选文本操作 Mac · A

固定源码解释了“无额外 LLM 也能输入”：选择/提取现有文本，不是通用生成；速度与费用未独立验证。

**依据:** 固定版代码读取无障碍控件，必要时用 Apple Vision 本地 OCR；Jev 选择动作及从用户请求提取的候选文本，执行后检查状态。屏幕像素不上传，但任务、标签和值会发给 TypeSafe。

**边界:** 不支持自由写作或任意命令生成；图标、复杂编辑器和手势可能失败。低于一秒与近乎免费缺完整任务基准。

**作者报告:** 作者附 31 秒演示并声称亚秒延迟；文档将其标为早期实验，完成状态仍需人工判断。

案例：[Third Hand · 从指令里选文本操作 Mac](../cases/2026-09-20-third-hand/README.md)

来源：[X @sxhivs](https://x.com/sxhivs/status/2101367048223982065) · [X @sxhivs](https://x.com/sxhivs/status/2101367050207981608)

实现 / 方法：[README.md](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/README.md) · [TextEntryPlan.swift](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/TextEntryPlan.swift) · [JevClient.swift](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/JevClient.swift)

主帖快照：**549 赞**，2026-09-20T02:46:29+00:00；[取数来源](https://api.fxtwitter.com/status/2101367048223982065)。

<a id="mujoco-apple-control"></a>

## MuJoCo · 三模型搬苹果对照 · A

固定版本披露单次试验、物理控制分工和回放计时；A 表示可检查性较好，本库未运行校验或真实机器人。

**依据:** 固定版本每周期两次请求：先选动作意图，再选 XYZ 方向及夹爪开/保持/合。输入是模拟器几何和接触反馈；共享执行器负责步长、IK 与物理推进，不是摄像头感知或关节力矩生成。

**边界:** 每控制器仅一个 seed-0 试验；不能估计成功率。回放按模拟时间同步并去掉 API 等待，不能把视频长度当实际完成时间。

**作者报告:** 作者记录 Jev 181.847 秒/0.018825 美元、GPT-6 Astra 707.274 秒/5.933624 美元完成；GPT-4.1 mini 达到 160 周期上限。约 1/315 费用仅属这些记录。

案例：[MuJoCo · 三模型搬苹果对照](../cases/2026-09-20-mujoco-apple-control/README.md)

来源：[X @openroboto](https://x.com/openroboto/status/2101310974359941332) · [X @openroboto](https://x.com/openroboto/status/2101310978856276075) · [X @openroboto](https://x.com/openroboto/status/2101310983931040038) · [X @openroboto](https://x.com/openroboto/status/2101382220690895046)

实现 / 方法：[README.md](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/README.md) · [RESULTS.md](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/docs/RESULTS.md) · [incremental_policy.py](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/incremental_policy.py) · [verify_replay.py](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/verify_replay.py)

主帖快照：**272 赞**，2026-09-20T02:47:32+00:00；[取数来源](https://api.fxtwitter.com/status/2101310974359941332)。

<a id="voice-spell-game"></a>

## 语音咒语游戏 · 一句话决定魔法 · B

原帖明确判断维度和游戏参数分工；可玩性、识别准确率及稳定性待验证。

**依据:** 作者称 Jev 判断咒语是否成立、属性、形态和威力，结果驱动魔法参数；语音转文字和画面渲染属于外围环节，具体实现未公开核清。

**边界:** 尚缺评分规则、误触发及一致性测试；没有证据说明 Jev 直接处理音频或生成特效。

**作者报告:** 作者展示约 75 秒概念验证视频；未给出可复核端到端延迟或费用。

案例：[语音咒语游戏 · 一句话决定魔法](../cases/2026-09-20-voice-spell-game/README.md)

来源：[X @izumisatoshi05](https://x.com/izumisatoshi05/status/2101287104030609624)

主帖快照：**576 赞**，2026-09-20T02:48:04+00:00；[取数来源](https://api.fxtwitter.com/status/2101287104030609624)。

<a id="emotion-topic-chat-game"></a>

## 聊天小游戏 · 识别情绪与话题 · B

可支持情绪/话题驱动的聊天原型；免费运营和长期对话质量仍无完整证据。

**依据:** 作者明确 Jev 对输入判别情绪与话题，并给出 Cloudflare 部署入口；回复文本来源、分支规则和候选规模尚未核清。

**边界:** 免费开放页面不等于底层服务永远免费；无完整成本、误分类或长对话一致性统计，不能推断回复都由 Jev 生成。

**作者报告:** 作者称费用很低，并提供 21 秒演示与公开试玩入口；本库未运行试玩或调用模型。

案例：[聊天小游戏 · 识别情绪与话题](../cases/2026-09-20-emotion-topic-chat-game/README.md)

来源：[X @gigabit_million](https://x.com/gigabit_million/status/2101285853859545263)

实现 / 方法：[](https://jev-chat.gigabitmillion-games.workers.dev/)

主帖快照：**391 赞**，2026-09-20T02:48:04+00:00；[取数来源](https://api.fxtwitter.com/status/2101285853859545263)。

<a id="canada-word-map"></a>

## 加拿大词语地图 · 把联想画在地图上 · B

原型展示的是模型联想；“理解加拿大”不能当成经过验证的地理或社会知识能力。

**依据:** 作者描述用 Jev 预测词语关联的加拿大区域，并以地图展示；地理候选、提示与分数归一化方式尚未披露。

**边界:** 主观联想不能当人口、文化或地域事实；没有标准答案集或校准验证。

**作者报告:** 作者称响应即时、费用不到一美分；未公开调用次数及计时边界。

案例：[加拿大词语地图 · 把联想画在地图上](../cases/2026-09-20-canada-word-map/README.md)

来源：[X @measure_plan](https://x.com/measure_plan/status/2101315424247820309)

主帖快照：**219 赞**，2026-09-20T02:47:32+00:00；[取数来源](https://api.fxtwitter.com/status/2101315424247820309)。

<a id="contextual-clipboard"></a>

## 情境剪贴板 · 猜此刻要粘贴哪条 · B

用途、输入来源与媒体明确；实际命中率、隐私处理和跨应用稳定性待核。

**依据:** 作者称读取剪贴板历史，并结合输入框和应用上下文交给 Jev 选择；具体采集接口、候选长度和执行确认机制未知。

**边界:** 仅有原型与主观准确评价；需测试相似候选、选错场景及敏感内容的过滤规则。不能视为本地离线工具。

**作者报告:** 作者称是旅途中制作的玩具、感觉较准确，未提供命中率或费用测量。

案例：[情境剪贴板 · 猜此刻要粘贴哪条](../cases/2026-09-20-contextual-clipboard/README.md)

来源：[X @CoooolXyh](https://x.com/CoooolXyh/status/2101284346640654362)

主帖快照：**207 赞**，2026-09-20T02:48:04+00:00；[取数来源](https://api.fxtwitter.com/status/2101284346640654362)。

<a id="x-draft-hype-check"></a>

## X 草稿检查 · 发帖前看看是否太浮夸 · B

可支持草稿风格提醒原型；不能把标签当成事实核查或对人的可靠评价。

**依据:** 作者制作浏览器扩展，用 Jev 判断正在撰写的 X 帖子是否呈现夸张营销风格；具体标签、提示和触发频率未披露。

**边界:** 风格判断具有主观性，不能据此判定作者职业、动机或帖子真伪；缺人工一致性和误报数据。

**作者报告:** 作者附约 44 秒扩展演示，未报告可复核准确率或费用。

案例：[X 草稿检查 · 发帖前看看是否太浮夸](../cases/2026-09-20-x-draft-hype-check/README.md)

来源：[X @unsu0707](https://x.com/unsu0707/status/2101249913099375058)

主帖快照：**446 赞**，2026-09-20T02:51:41+00:00；[取数来源](https://api.fxtwitter.com/status/2101249913099375058)。

<a id="ori-task-classification"></a>

## Ori Eval · 30 类请求分类对照 · B

任务与主要限制披露较清楚，但合成小样本与缺少完整复现材料限制了结论的适用范围。

**依据:** OpenRouter 说明五模型在相同 200 条合成案例上依次、无状态测试；LLM 关闭推理，GLM 5.3 Flash 除外，使用低推理力度。

**边界:** 没有公开完整样本、逐条标签与重跑结果；默认供应商路由会影响部分模型的尾延迟，不能推断所有生产请求的表现。

**作者报告:** 作者称 Jev 比第二快模型快超过 5 倍，五者准确性只差少数案例；费用第二低，Qwen3.8 Flash 更低。

案例：[Ori Eval · 30 类请求分类对照](../cases/2026-09-20-ori-task-classification/README.md)

来源：[X @OpenRouter](https://x.com/OpenRouter/status/2101412965765529853) · [X @OpenRouter](https://x.com/OpenRouter/status/2101412983297778130) · [X @OpenRouter](https://x.com/OpenRouter/status/2101413000725074212) · [X @OpenRouter](https://x.com/OpenRouter/status/2101413013941330371) · [X @OpenRouter](https://x.com/OpenRouter/status/2101413025572172201)

主帖快照：**329 赞**，2026-09-20T02:45:53+00:00；[取数来源](https://api.fxtwitter.com/status/2101412965765529853)。

<a id="coreml-ocr"></a>

## TipTour · CoreML + OCR 桌面点击 · A

固定源码可核对本地感知、点击限制和 12 步预算；90ms 仍只是作者单步报告。A 表示实现更可检查，不代表已验证性能。

**依据:** 已开源为 TipTour。固定版在本地检测界面元素与标签，Jev 选单击/双击/右击目标，执行后重新观测；默认最多 12 次动作。Jev 模式不上传截图，但会发送任务、标签、位置和近期动作记录。

**边界:** 检测错误会影响点击；Jev 模式按排名选目标，没有目标置信度截断，不支持自由写作。Gemini 模式可发送音频和截图，因此“图片留本机”不能扩展到所有模式。

**作者报告:** 原帖报告约 90ms 每次决策；新帖公开代码，但没有新的完整任务集、成功率或端到端速度评测。

案例：[TipTour · CoreML + OCR 桌面点击](../cases/2026-09-18-coreml-ocr/README.md)

来源：[X @milindlabs](https://x.com/milindlabs/status/2100631847155994852) · [X @milindlabs](https://x.com/milindlabs/status/2101260711645372886)

实现 / 方法：[README.md](https://github.com/milind-soni/tiptour-macos/blob/52582467c883d66484542f3be8e259340eb524f1/README.md) · [JevPointerLoop.swift](https://github.com/milind-soni/tiptour-macos/blob/52582467c883d66484542f3be8e259340eb524f1/TipTour/Jev/JevPointerLoop.swift)

主帖快照：**564 赞**，2026-09-17T22:42:22.793465+00:00；[取数来源](https://api.fxtwitter.com/status/2100631847155994852)。

<a id="context-compaction"></a>

## 工具调用上下文压缩 · C

公开反向评测说明单次压缩快不等于长期更省；三份记录、移植版与检索恢复基线是必要限定。原录屏动画也不能充当实时 API 测量。

**依据:** 按源码版本 e3f262a：配对工具调用与结果，保护首条及最近消息，将对话压进状态预算；工具输出正文替换为结果状态和长度。Jev 分别判断是否保留调用及结果，程序据阈值保留、截断或删除。Claude Code hook 在报错或压缩不足时退回内置摘要。

**边界:** 新增 Hermes 评测暴露了筛选与长期空间问题：其移植版在默认阈值下删除全部 851 个未保护候选，反复压缩仍保留不断增长的普通文本。结果限于该适配、样本和预算；不能推广到所有 Jev 记忆方案。

**作者报告:** 原作者称即时压缩。Hermes 三份长记录评测报告：Jev 压缩约 1.4 秒，保留约 115K token、回忆评分 75.5%；其生产摘要加检索恢复路径约 55K、78.9%。本库未运行该评测。

案例：[工具调用上下文压缩](../cases/2026-09-18-context-compaction/README.md)

来源：[X @tamarajtran](https://x.com/tamarajtran/status/2100694549362553153) · [X @tamarajtran](https://x.com/tamarajtran/status/2100694552369897539) · [X @altryne](https://x.com/altryne/status/2100739055923425589) · [X @theo](https://x.com/theo/status/2100762304862384257) · [X @Teknium](https://x.com/Teknium/status/2101398453578555898)

实现 / 方法：[fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) · [116246](https://github.com/NousResearch/hermes-agent/pull/116246) · [SCORECARD-2026-09-19-jev.md](https://github.com/NousResearch/hermes-agent/blob/dba815e7ad800dad19f921ca9ad028eba027e8a4/evals/compaction/results/SCORECARD-2026-09-19-jev.md) · [jev_arm.py](https://github.com/NousResearch/hermes-agent/blob/dba815e7ad800dad19f921ca9ad028eba027e8a4/evals/compaction/jev_arm.py)

主帖快照：**1646 赞**，2026-09-17T22:42:26.956952+00:00；[取数来源](https://api.fxtwitter.com/status/2100694549362553153)。

<a id="ryze-seo-geo"></a>

## Ryze AI · SEO/GEO 审核与修复 · C

新增七类判断说明仍属 Ryze 同一产品；90% 降费、20–30 倍提速和引用效果缺可复核对照，不按工作流数扩充案例。

**依据:** 新帖细化同一产品的七类判断：竞争页面评分、标题等元素保留/修改、问题与页面匹配、引用机会评分、买家搜索词分类、15 个候选内链筛选，以及草稿通过 20 项检查后交人工。采集、文本生成和修改执行仍需外围组件。

**边界:** 这些细节提高了流程可理解性，但没有完整基线、质量和账单对照；“引用机会”分数未校准为真实引用概率，也不保证搜索排名或转化提升。

**作者报告:** 作者称费用较约 250 美元基线下降 90%，多环节提速 30 倍、页面创建提速 20 倍；六秒界面视频未提供可复核对照。

案例：[Ryze AI · SEO/GEO 审核与修复](../cases/2026-09-19-ryze-seo-geo/README.md)

来源：[X @irabukht](https://x.com/irabukht/status/2101090579127951694) · [X @irabukht](https://x.com/irabukht/status/2101123317327372487) · [X @irabukht](https://x.com/irabukht/status/2101375295152652372)

主帖快照：**790 赞**，2026-09-19T09:42:43+00:00；[取数来源](https://api.fxtwitter.com/status/2101090579127951694)。

<a id="browser-use"></a>

## Browser Use · Ultrafast · A

固定版文档与公开基准可核查实现和计时条件；12306 新视频只是同项目的另一使用报告，不新增应用，也不证明任意网站可靠。

**依据:** 作者说明：每一步从 DOM 生成新的动作选项，Jev 选动作，小型 LLM 负责必要的文本输入。

**边界:** 仍有 LLM 文本生成；当前 MVP 不覆盖 shadow DOM、iframe、canvas、上传等；少量同任务重复不代表通用跨网站可靠性。

**作者报告:** 原作者报告航班查询约 7 秒、0.0039 美元。新增使用者以 Pi + DeepSeek 配合 Ultrafast 查询 12306 车次，并发布约 93 秒过程视频；未提供受控速度或费用对照。

案例：[Browser Use · Ultrafast](../cases/2026-09-18-browser-use/README.md)

来源：[X @gregpr07](https://x.com/gregpr07/status/2100411066966749359) · [X @0xidanlevin](https://x.com/0xidanlevin/status/2100937437325205568) · [X @yanhua1010](https://x.com/yanhua1010/status/2101257759497089171)

实现 / 方法：[jev-ultrafast](https://github.com/browser-use/jev-ultrafast) · [README.md](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/README.md) · [benchmark](https://webmcp.com/benchmark) · [WindTunnel](https://github.com/nekuda-ai/WindTunnel)

主帖快照：**6891 赞**，2026-09-17T22:32:51.243200+00:00；[取数来源](https://api.fxtwitter.com/status/2100411066966749359)。

## 范围与待补线索

实现不清、媒体待核及二手转载不进入正式计数，见[待整理区](../inbox/README.md)。既有主帖快照和首次收录时间保留，仅这 19 项刷新内容更新时间。
