# Jev：小判断，能做什么？

**简体中文** | [English](README.en.md)

大多数 AI 以写答案见长，**TypeSafe Jev 擅长做判断。**
给它当前情况和问题或选项，它返回选择、评分或是非判断，再由程序执行。
这里介绍人们用它做出的应用，也解释演示究竟能证明什么。

**112 个案例 · 11 类用途** · 来源核对至 2026-09-19

[浏览全部应用](#all-apps) · [Jev 如何工作](breakdowns/2026-09-18-how-jev-apps-work.md) · [最近收录](CHANGELOG.md)

## 先看这六个点子

从用途直观、原理较清楚的案例开始。点击图片可看原始演示。

### 让 AI 按按钮，谁来读网页？

[Browser Use · Ultrafast](cases/2026-09-18-browser-use/README.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="480" alt="Browser Use · Ultrafast">](https://x.com/gregpr07/status/2100411066966749359)

程序读网页并列出按钮，Jev 选下一步；需要填写文字时，再交给文字模型。

**证据边界：** 结果来自整套工具配合，不能把全部能力都归给 Jev。

[原理较清楚](references/2026-09-19-claims-audit.md#browser-use) · [X · 6,891 赞快照](https://x.com/gregpr07/status/2100411066966749359) · [原理与依据](cases/2026-09-18-browser-use/README.md)

**内容更新：** 2026-09-19

### 不写页面，能不能拼出界面？

[json-render · 用组件选择拼出界面](cases/2026-09-19-json-render-ui/README.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101022081810911232/img/3tKdQ3Y2_ZGSg3Q7.jpg" width="480" alt="json-render · 用组件选择拼出界面">](https://x.com/ctatedev/status/2101022101750571357)

像搭积木：Jev 选择组件、安排关系，程序将结果装配成可以渲染的界面。

**证据边界：** 结构合法，不代表内容正确或设计好看。

[原理较清楚](references/2026-09-19-claims-audit.md#json-render-ui) · [X · 3,341 赞快照](https://x.com/ctatedev/status/2101022101750571357) · [原理与依据](cases/2026-09-19-json-render-ui/README.md)

**内容更新：** 2026-09-19

### 视频里的口播广告，怎么跳过？

[YouTube 赞助片段跳过](cases/2026-09-18-youtube-sponsor-skip/README.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100792834526007296/img/8AFbjqEeZrJUEHid.jpg" width="480" alt="YouTube 赞助片段跳过">](https://x.com/tdinh_me/status/2100793777103466615)

Jev 在字幕中找赞助内容，程序把对应句子换算成播放时间，再执行跳转。

**证据边界：** 字幕与边界判断都可能出错，音频模式还需要语音转写。

[原理较清楚](references/2026-09-19-claims-audit.md#youtube-sponsor-skip) · [X · 238 赞快照](https://x.com/tdinh_me/status/2100793777103466615) · [原理与依据](cases/2026-09-18-youtube-sponsor-skip/README.md)

**内容更新：** 2026-09-19

### 解开魔方，靠判断还是公式？

[魔方分阶段解法](cases/2026-09-18-rubiks-cube/README.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100479486382809088/img/r6daGpDnvsCr3LyL.jpg" width="480" alt="魔方分阶段解法">](https://x.com/redp314/status/2100489858951073858)

公式预先写在代码里，Jev 识别当前属于哪种情况，程序查公式并检查操作。

**证据边界：** 这是模型与解法代码合作，不能当成模型独立发明了解法。

[原理较清楚](references/2026-09-19-claims-audit.md#rubiks-cube) · [X · 494 赞快照](https://x.com/redp314/status/2100489858951073858) · [原理与依据](cases/2026-09-18-rubiks-cube/README.md)

**内容更新：** 2026-09-19

### 一叠表格，怎样分清每一页？

[Tax Doc Classifier · 税务 PDF 页面识别](cases/2026-09-19-tax-doc-classifier/README.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100973360989773825/img/yMtL6CxrKMVXQEHV.jpg" width="480" alt="Tax Doc Classifier · 税务 PDF 页面识别">](https://x.com/nedwize/status/2100973868324417852)

程序提取页面文字，Jev 判断表格类型；拿不准的页面留下来复核。

**证据边界：** 作者公开了测试结果，但这不等于所有格式都能可靠识别。

[原理较清楚](references/2026-09-19-claims-audit.md#tax-doc-classifier) · [X · 1,506 赞快照](https://x.com/nedwize/status/2100973868324417852) · [原理与依据](cases/2026-09-19-tax-doc-classifier/README.md)

**内容更新：** 2026-09-19

### 简单任务，需要最强的模型吗？

[Claude Code Mod · 模型与推理力度路由](cases/2026-09-19-claude-code-jev-router/README.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" width="480" alt="Claude Code Mod · 模型与推理力度路由">](https://x.com/dani_avila7/status/2101176629745561686)

像工单分诊：Jev 判断任务难度，插件据此选择子代理模型和主会话推理力度。

**证据边界：** 路由机制可查，实际省多少钱、是否影响质量仍待验证。

[原理较清楚](references/2026-09-19-increment7-audit.md#claude-code-jev-router) · [X · 417 赞快照](https://x.com/dani_avila7/status/2101176629745561686) · [原理与依据](cases/2026-09-19-claude-code-jev-router/README.md)

**内容更新：** 2026-09-19

<a id="all-apps"></a>

## 按用途找应用

展开分类查看所有案例，包含上面的六项精选。日期均为北京时间的内容更新日期。

证据标签可点开查看依据：**原理较清楚 / 效果待验证 / 主张缺依据**。它们描述公开证据的充分程度；本库尚未独立复现这些应用。

<a id="browser"></a>

<details>
<summary><strong>操作网页与电脑</strong> · 12</summary>

从查网页到操作桌面，关键是把“看见什么”和“下一步做什么”接起来。浏览器方案多读页面结构，桌面方案可能用无障碍树或 OCR；先比较能完成哪些任务，再看速度。

[同类优劣对比](breakdowns/2026-09-18-browser.md)

### [Browser Use · Ultrafast](cases/2026-09-18-browser-use/README.md)

告诉它航班需求，它会自己在网页上点选、填写并查找结果。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="320" alt="Browser Use · Ultrafast">](https://x.com/gregpr07/status/2100411066966749359)

[原理较清楚](references/2026-09-19-claims-audit.md#browser-use) · [X · 6,891 赞快照](https://x.com/gregpr07/status/2100411066966749359) · [原理与依据](cases/2026-09-18-browser-use/README.md)

**内容更新：** 2026-09-19

### [Stagehand 浏览器控制](cases/2026-09-18-stagehand/README.md)

让 Jev 决定网页上下一步怎么操作，再由 Stagehand 动手。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100495119065722880/img/7A1mijkU3Z_Zj7PM.jpg" width="320" alt="Stagehand 浏览器控制">](https://x.com/kylejeong/status/2100622054945095934)

[效果待验证](references/2026-09-19-claims-audit.md#stagehand) · [X · 393 赞快照](https://x.com/kylejeong/status/2100622054945095934) · [原理与依据](cases/2026-09-18-stagehand/README.md)

**内容更新：** 2026-09-19

### [Cua · jev-use](cases/2026-09-18-cua-jev-use/README.md)

给 Jev 一份允许执行的网页操作清单，让它选一个，再检查是否做对。

[<img src="https://pbs.twimg.com/media/HSb_nmIWYAAkGKa.jpg?name=orig" width="320" alt="Cua · jev-use">](https://x.com/trycua/status/2100649543079502213)

[主张缺依据](references/2026-09-19-claims-audit.md#cua-jev-use) · [X · 1,162 赞快照](https://x.com/trycua/status/2100649543079502213) · [原理与依据](cases/2026-09-18-cua-jev-use/README.md)

**内容更新：** 2026-09-19

### [CoreML + OCR 桌面点击](cases/2026-09-18-coreml-ocr/README.md)

先在 Mac 上认出按钮和文字，再让 Jev 选要点击的位置。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100629037790183424/img/NR6wQpZiC-xjCEsC.jpg" width="320" alt="CoreML + OCR 桌面点击">](https://x.com/milindlabs/status/2100631847155994852)

[效果待验证](references/2026-09-19-claims-audit.md#coreml-ocr) · [X · 564 赞快照](https://x.com/milindlabs/status/2100631847155994852) · [原理与依据](cases/2026-09-18-coreml-ocr/README.md)

**内容更新：** 2026-09-19

### [OpenCode + agent-desktop](cases/2026-09-18-agent-desktop/README.md)

一个模型记住任务，Jev 帮它更快地选择桌面操作目标。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100358791321755648/img/t6Bd787flQiGeoJ_.jpg" width="320" alt="OpenCode + agent-desktop">](https://x.com/mdlahfir/status/2100359236924637349)

[效果待验证](references/2026-09-19-claims-audit.md#agent-desktop) · [X · 870 赞快照](https://x.com/mdlahfir/status/2100359236924637349) · [原理与依据](cases/2026-09-18-agent-desktop/README.md)

**内容更新：** 2026-09-19

### [Kernel 浏览器演示](cases/2026-09-18-kernel-browser/README.md)

在网页里体验 Jev 帮忙操作浏览器。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100321453455425537/img/hVYy_d3Nuw9XhSwg.jpg" width="320" alt="Kernel 浏览器演示">](https://x.com/stevekrouse/status/2100321685081559542)

[效果待验证](references/2026-09-19-claims-audit.md#kernel-browser) · [X · 235 赞快照](https://x.com/stevekrouse/status/2100321685081559542) · [原理与依据](cases/2026-09-18-kernel-browser/README.md)

**内容更新：** 2026-09-19

### [语音控制浏览器](cases/2026-09-18-voice-browser/README.md)

说出指令，让浏览器替你点击，例如“返回上一页”。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100577954338373633/img/tbH43kHpUotE3hzK.jpg" width="320" alt="语音控制浏览器">](https://x.com/moritzkremb/status/2100577979021832365)

[效果待验证](references/2026-09-19-claims-audit.md#voice-browser) · [X · 1,829 赞快照](https://x.com/moritzkremb/status/2100577979021832365) · [原理与依据](cases/2026-09-18-voice-browser/README.md)

**内容更新：** 2026-09-19

### [OpenCode 应用测试](cases/2026-09-18-opencode-qa/README.md)

让编码助手自己操作应用，帮忙做开发后的检查。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" width="320" alt="OpenCode 应用测试">](https://x.com/Neriousy/status/2100287208166969746)

[效果待验证](references/2026-09-19-claims-audit.md#opencode-qa) · [X · 1,133 赞快照](https://x.com/Neriousy/status/2100287208166969746) · [原理与依据](cases/2026-09-18-opencode-qa/README.md)

**内容更新：** 2026-09-19

### [Runlayer · 并行浏览器对抗测试](cases/2026-09-18-runlayer-adversarial-testing/README.md)

同时打开多路浏览器，尝试找出新版本在操作中会出什么问题。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100881920343105536/img/c1y4THiGwA2GfXGa.jpg" width="320" alt="Runlayer · 并行浏览器对抗测试">](https://x.com/rafalwilinski/status/2100882207879434359)

[效果待验证](references/2026-09-19-claims-audit.md#runlayer-adversarial-testing) · [X · 820 赞快照](https://x.com/rafalwilinski/status/2100882207879434359) · [原理与依据](cases/2026-09-18-runlayer-adversarial-testing/README.md)

**内容更新：** 2026-09-19

### [Sac · Codex + Jev 操作 Mac 日历](cases/2026-09-18-sac-calendar-computer-use/README.md)

给 Codex 的电脑操作加上 Jev 判断层，用创建日历事件做并排对照。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100853279089647616/img/H6altwjZQ28_1bfY.jpg" width="320" alt="Sac · Codex + Jev 操作 Mac 日历">](https://x.com/Saccc_c/status/2100864907046768890)

[主张缺依据](references/2026-09-19-increment7-audit.md#sac-calendar-computer-use) · [X · 217 赞快照](https://x.com/Saccc_c/status/2100864907046768890) · [原理与依据](cases/2026-09-18-sac-calendar-computer-use/README.md)

**内容更新：** 2026-09-19

### [ego lite · Amazon 商品筛选](cases/2026-09-19-ego-product-decisions/README.md)

组合浏览器工具和模型，筛选网页上的商品。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100969567715790848/img/IXAgXZrtsLGyeYRA.jpg" width="320" alt="ego lite · Amazon 商品筛选">](https://x.com/ego_agent/status/2100970015977804008)

[效果待验证](references/2026-09-19-claims-audit.md#ego-product-decisions) · [X · 366 赞快照](https://x.com/ego_agent/status/2100970015977804008) · [原理与依据](cases/2026-09-19-ego-product-decisions/README.md)

**内容更新：** 2026-09-19

### [Tester Army · Web / 手机端测试演示](cases/2026-09-19-tester-army-e2e/README.md)

用代理执行界面测试，探索 Web 和移动端的端到端测试框架。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100966360192868352/img/8GCSVzX1AYF4caav.jpg" width="320" alt="Tester Army · Web / 手机端测试演示">](https://x.com/o_kwasniewski/status/2100966838905585687)

[效果待验证](references/2026-09-19-claims-audit.md#tester-army-e2e) · [X · 505 赞快照](https://x.com/o_kwasniewski/status/2100966838905585687) · [原理与依据](cases/2026-09-19-tester-army-e2e/README.md)

**内容更新：** 2026-09-19

</details>

<a id="routing"></a>

<details>
<summary><strong>给任务挑选助手</strong> · 11</summary>

模型、技能和工具各有擅长的工作，Jev 负责分派。选模型影响费用与质量，选技能影响能否找到合适能力；两者可以组合。

[同类优劣对比](breakdowns/2026-09-18-routing.md)

### [Eve 条件式模型路由](cases/2026-09-18-eve-router/README.md)

先判断问题需要哪种模型，再把它交给合适的模型处理。

[<img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" width="320" alt="Eve 条件式模型路由">](https://x.com/eve/status/2100430918762832180)

[效果待验证](references/2026-09-19-claims-audit.md#eve-router) · [X · 821 赞快照](https://x.com/eve/status/2100430918762832180) · [原理与依据](cases/2026-09-18-eve-router/README.md)

**内容更新：** 2026-09-19

### [请求到模型路由器](cases/2026-09-18-ephraim-router/README.md)

自动为不同问题挑选回答模型，并直接发送请求。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100454021852954624/img/hqULLONlXw40573G.jpg" width="320" alt="请求到模型路由器">](https://x.com/ephraimduncan/status/2100454070536351824)

[效果待验证](references/2026-09-19-claims-audit.md#ephraim-router) · [X · 1,503 赞快照](https://x.com/ephraimduncan/status/2100454070536351824) · [原理与依据](cases/2026-09-18-ephraim-router/README.md)

**内容更新：** 2026-09-19

### [Firstmate 任务分派](cases/2026-09-18-firstmate/README.md)

按任务难度和用户偏好，挑选合适的 AI 助手及工作档位。

[<img src="https://pbs.twimg.com/media/HSYK_gbagAAqKqr.jpg?name=orig" width="320" alt="Firstmate 任务分派">](https://x.com/kunchenguid/status/2100468943853085061)

[效果待验证](references/2026-09-19-claims-audit.md#firstmate) · [X · 1,615 赞快照](https://x.com/kunchenguid/status/2100468943853085061) · [原理与依据](cases/2026-09-18-firstmate/README.md)

**内容更新：** 2026-09-19

### [本地编码代理分工](cases/2026-09-18-local-delegation/README.md)

把简单活、复杂问题和长时间编程任务分给不同的 AI 助手。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100314084990414848/img/iePXR9Edae7YVCT_.jpg" width="320" alt="本地编码代理分工">](https://x.com/mdlahfir/status/2100314182201802811)

[效果待验证](references/2026-09-19-claims-audit.md#local-delegation) · [X · 777 赞快照](https://x.com/mdlahfir/status/2100314182201802811) · [原理与依据](cases/2026-09-18-local-delegation/README.md)

**内容更新：** 2026-09-19

### [Skillbox 技能选择](cases/2026-09-18-skillbox/README.md)

从一大堆 AI 技能中，快速找出当前任务可能用得上的几个。

[<img src="https://pbs.twimg.com/media/HRidCpLaMAAqV-7.jpg?name=orig" width="320" alt="Skillbox 技能选择">](https://x.com/thekitze/status/2096598298220277856)

[效果待验证](references/2026-09-19-claims-audit.md#skillbox) · [X · 724 赞快照](https://x.com/thekitze/status/2100556122570792999) · [原理与依据](cases/2026-09-18-skillbox/README.md)

**内容更新：** 2026-09-19

### [Coding Garden 工具助手](cases/2026-09-18-coding-garden-assistant/README.md)

用一句话查天气、找资料或处理待办，让助手调用对应工具。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" width="320" alt="Coding Garden 工具助手">](https://x.com/CodingGarden/status/2100665210419950031)

[主张缺依据](references/2026-09-19-claims-audit.md#coding-garden-assistant) · [X · 334 赞快照](https://x.com/CodingGarden/status/2100665210419950031) · [原理与依据](cases/2026-09-18-coding-garden-assistant/README.md)

**内容更新：** 2026-09-19

### [Eve 工具调用代理](cases/2026-09-18-eve-tool-agent/README.md)

让 Jev 接手“下一步用哪个工具”的判断，减少代理在选择上花的时间和费用。

[<img src="https://pbs.twimg.com/media/HSZSqLGXwAA1jSL.jpg?name=orig" width="320" alt="Eve 工具调用代理">](https://x.com/oviniciuslana/status/2100457622407168509)

[效果待验证](references/2026-09-19-claims-audit.md#eve-tool-agent) · [X · 1,117 赞快照](https://x.com/oviniciuslana/status/2100457622407168509) · [原理与依据](cases/2026-09-18-eve-tool-agent/README.md)

**内容更新：** 2026-09-19

### [ai-cli 终端决策入口](cases/2026-09-18-ai-cli/README.md)

让终端里的 AI 助手也能调用 Jev 做判断、选择和评分。

[<img src="https://pbs.twimg.com/media/HSbG2YLWkAAPqmU.jpg?name=orig" width="320" alt="ai-cli 终端决策入口">](https://x.com/ctatedev/status/2100584917092409479)

[原理较清楚](references/2026-09-19-claims-audit.md#ai-cli) · [X · 874 赞快照](https://x.com/ctatedev/status/2100584917092409479) · [原理与依据](cases/2026-09-18-ai-cli/README.md)

**内容更新：** 2026-09-19

### [Hono JevRouter · 按请求含义分流](cases/2026-09-18-hono-semantic-router/README.md)

根据请求像是来自人还是 AI，选择返回网页或 Markdown 等不同内容。

[<img src="https://pbs.twimg.com/media/HSfKgItbcAAwVIl.jpg?name=orig" width="320" alt="Hono JevRouter · 按请求含义分流">](https://x.com/yusukebe/status/2100871075743859182)

[原理较清楚](references/2026-09-19-claims-audit.md#hono-semantic-router) · [X · 405 赞快照](https://x.com/yusukebe/status/2100871075743859182) · [原理与依据](cases/2026-09-18-hono-semantic-router/README.md)

**内容更新：** 2026-09-19

### [Codex Model Router · 每轮选择模型](cases/2026-09-19-codex-model-router/README.md)

按当前任务复杂程度，为 Codex 选择模型和推理配置。

[<img src="https://pbs.twimg.com/media/HSgeLlIX0AAjedL.png?name=orig" width="320" alt="Codex Model Router · 每轮选择模型">](https://x.com/antonioleivag/status/2100962426439000484)

[原理较清楚](references/2026-09-19-claims-audit.md#codex-model-router) · [X · 437 赞快照](https://x.com/antonioleivag/status/2100962426439000484) · [原理与依据](cases/2026-09-19-codex-model-router/README.md)

**内容更新：** 2026-09-19

### [Claude Code Mod · 模型与推理力度路由](cases/2026-09-19-claude-code-jev-router/README.md)

按任务选择子代理模型，并调整主会话的推理力度。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" width="320" alt="Claude Code Mod · 模型与推理力度路由">](https://x.com/dani_avila7/status/2101176629745561686)

[原理较清楚](references/2026-09-19-increment7-audit.md#claude-code-jev-router) · [X · 417 赞快照](https://x.com/dani_avila7/status/2101176629745561686) · [原理与依据](cases/2026-09-19-claude-code-jev-router/README.md)

**内容更新：** 2026-09-19

</details>

<a id="review"></a>

<details>
<summary><strong>检查代码与操作风险</strong> · 11</summary>

把宽泛的“有没有问题”拆成几个具体判断。代码评审找缺陷，权限判断管操作；少误报和不漏报都要看，评分不能替代测试。

[同类优劣对比](breakdowns/2026-09-18-review.md)

### [jev-review MCP](cases/2026-09-18-jev-review/README.md)

给 AI 写出的代码打分，让它根据反馈继续修改。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100465308519759872/img/2uIG43VFGvWzku0s.jpg" width="320" alt="jev-review MCP">](https://x.com/niazmorshed_/status/2100465662867218857)

[效果待验证](references/2026-09-19-claims-audit.md#jev-review) · [X · 445 赞快照](https://x.com/niazmorshed_/status/2100465662867218857) · [原理与依据](cases/2026-09-18-jev-review/README.md)

**内容更新：** 2026-09-19

### [14 项 PR 风险检查](cases/2026-09-18-typed-pr-review/README.md)

快速检查一批代码修改有没有泄密、删测试等风险，不确定时交给人复核。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100585029533372416/img/ZcrsntW2yWgtB_HD.jpg" width="320" alt="14 项 PR 风险检查">](https://x.com/redp314/status/2100585126652481915)

[效果待验证](references/2026-09-19-claims-audit.md#typed-pr-review) · [X · 1,927 赞快照](https://x.com/redp314/status/2100585126652481915) · [原理与依据](cases/2026-09-18-typed-pr-review/README.md)

**内容更新：** 2026-09-19

### [jev-rabbit 自然语言规则](cases/2026-09-18-jev-rabbit/README.md)

把团队的代码审查要求写成人话，让机器人按这些要求检查修改。

[<img src="https://pbs.twimg.com/media/HSbjmhQbQAA4G5A.jpg?name=orig" width="320" alt="jev-rabbit 自然语言规则">](https://x.com/thekitze/status/2100616530275029139)

[效果待验证](references/2026-09-19-claims-audit.md#jev-rabbit) · [X · 327 赞快照](https://x.com/thekitze/status/2100616530275029139) · [原理与依据](cases/2026-09-18-jev-rabbit/README.md)

**内容更新：** 2026-09-19

### [代码库复杂度分类器](cases/2026-09-18-codebase-classifier/README.md)

帮助发现代码是不是把简单事情做得过于复杂。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100067392223076352/img/BqXd-11SCr3_ff8q.jpg" width="320" alt="代码库复杂度分类器">](https://x.com/ryanvogel/status/2100068006592123055)

[效果待验证](references/2026-09-19-claims-audit.md#codebase-classifier) · [X · 1,165 赞快照](https://x.com/ryanvogel/status/2100068006592123055) · [原理与依据](cases/2026-09-18-codebase-classifier/README.md)

**内容更新：** 2026-09-19

### [fx auto mode 命令安全分类](cases/2026-09-18-fx-safety/README.md)

在 AI 自动执行命令前，先判断这条命令可能有多危险。

[<img src="https://pbs.twimg.com/media/HSW-E8wWgAAyw9O.jpg?name=orig" width="320" alt="fx auto mode 命令安全分类">](https://x.com/fazxes/status/2100300097695232164)

[效果待验证](references/2026-09-19-claims-audit.md#fx-safety) · [X · 591 赞快照](https://x.com/fazxes/status/2100300097695232164) · [原理与依据](cases/2026-09-18-fx-safety/README.md)

**内容更新：** 2026-09-19

### [越狱提示预筛](cases/2026-09-18-jailbreak-screen/README.md)

先筛查输入里是否有试图绕过 AI 规则的内容。

[<img src="https://pbs.twimg.com/media/HSXq9mqbsAAtHoT.jpg?name=orig" width="320" alt="越狱提示预筛">](https://x.com/mayfer/status/2100343452865265747)

[效果待验证](references/2026-09-19-claims-audit.md#jailbreak-screen) · [X · 264 赞快照](https://x.com/mayfer/status/2100343452865265747) · [原理与依据](cases/2026-09-18-jailbreak-screen/README.md)

**内容更新：** 2026-09-19

### [资料上传判断器](cases/2026-09-18-upload-check/README.md)

上传资料前先问一句：这份内容适合传出去吗？

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100471095627591680/img/jQewHJZ85th2EEv3.jpg" width="320" alt="资料上传判断器">](https://x.com/iwasakoya/status/2100471523358474709)

[效果待验证](references/2026-09-19-claims-audit.md#upload-check) · [X · 284 赞快照](https://x.com/iwasakoya/status/2100471523358474709) · [原理与依据](cases/2026-09-18-upload-check/README.md)

**内容更新：** 2026-09-19

### [按 ESLint 规则说明判断代码](cases/2026-09-18-eslint-rule-judgments/README.md)

只给规则的文字说明，让 Jev 判断小段代码是否符合规则。

[<img src="https://pbs.twimg.com/media/HSdqjcJa8AAGjPE.jpg?name=orig" width="320" alt="按 ESLint 规则说明判断代码">](https://x.com/mizchi/status/2100765201385869434)

[效果待验证](references/2026-09-19-claims-audit.md#eslint-rule-judgments) · [X · 351 赞快照](https://x.com/mizchi/status/2100765201385869434) · [原理与依据](cases/2026-09-18-eslint-rule-judgments/README.md)

**内容更新：** 2026-09-19

### [OpenCode · 意图感知权限插件](cases/2026-09-18-opencode-intent-permissions/README.md)

用“只访问 Google”等自然语言规则，检查代理换着工具发起的操作。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100701224920129536/img/-vzxHYoZxMjXKOKh.jpg" width="320" alt="OpenCode · 意图感知权限插件">](https://x.com/OpeOginni/status/2100702649834188855)

[效果待验证](references/2026-09-19-claims-audit.md#opencode-intent-permissions) · [X · 235 赞快照](https://x.com/OpeOginni/status/2100702649834188855) · [原理与依据](cases/2026-09-18-opencode-intent-permissions/README.md)

**内容更新：** 2026-09-19

### [代码注释 · 准确性与实用性评分](cases/2026-09-18-code-comment-scoring/README.md)

分别检查注释有没有说错，以及它是否提供了代码之外的有用信息。

[<img src="https://pbs.twimg.com/media/HSX4qrBWcAAA3K4.jpg?name=orig" width="320" alt="代码注释 · 准确性与实用性评分">](https://x.com/markjaquith/status/2100359340087501296)

[效果待验证](references/2026-09-19-claims-audit.md#code-comment-scoring) · [X · 1,777 赞快照](https://x.com/markjaquith/status/2100359340087501296) · [原理与依据](cases/2026-09-18-code-comment-scoring/README.md)

**内容更新：** 2026-09-19

### [Script.it · 先筛问题再写评审](cases/2026-09-19-script-code-review/README.md)

先判断 git diff 有没有问题，命中后才让文字模型写解释。

[<img src="https://pbs.twimg.com/media/HSgGI1wWQAAY5zl.jpg?name=orig" width="320" alt="Script.it · 先筛问题再写评审">](https://x.com/liorshkiller/status/2100936106615140757)

[效果待验证](references/2026-09-19-claims-audit.md#script-code-review) · [X · 202 赞快照](https://x.com/liorshkiller/status/2100936106615140757) · [原理与依据](cases/2026-09-19-script-code-review/README.md)

**内容更新：** 2026-09-19

</details>

<a id="data"></a>

<details>
<summary><strong>整理文件与信息</strong> · 16</summary>

给邮件贴标签、识别表格、挑出相关文件，都是把杂乱信息整理成可用结果。分类、检索和数值估算的错误不同，不能用一张速度榜衡量。

[同类优劣对比](breakdowns/2026-09-18-data.md)

### [1kpapers 论文分类](cases/2026-09-18-papers/README.md)

把一千多篇 AI 论文分门别类，方便按主题浏览。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100425141947604992/img/AITyHwcOWq1jw-3Z.jpg" width="320" alt="1kpapers 论文分类">](https://x.com/nutlope/status/2100426999546184123)

[效果待验证](references/2026-09-19-claims-audit.md#papers) · [X · 1,684 赞快照](https://x.com/nutlope/status/2100426999546184123) · [原理与依据](cases/2026-09-18-papers/README.md)

**内容更新：** 2026-09-19

### [DuckDB 语义分类扩展](cases/2026-09-18-duckdb/README.md)

在分析表格时，顺手让 Jev 给每行文字分个类。

[<img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" width="320" alt="DuckDB 语义分类扩展">](https://x.com/hamiltonulmer/status/2100370557405667768)

[效果待验证](references/2026-09-19-claims-audit.md#duckdb) · [X · 1,310 赞快照](https://x.com/hamiltonulmer/status/2100370557405667768) · [原理与依据](cases/2026-09-18-duckdb/README.md)

**内容更新：** 2026-09-19

### [500 封邮件分类](cases/2026-09-18-email-batch/README.md)

把一大批邮件快速分到不同类别，减少逐封整理。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100403183533125632/img/54ZFO-CHvDeC-rw-.jpg" width="320" alt="500 封邮件分类">](https://x.com/rileybrown/status/2100404532119269426)

[效果待验证](references/2026-09-19-claims-audit.md#email-batch) · [X · 3,161 赞快照](https://x.com/rileybrown/status/2100404532119269426) · [原理与依据](cases/2026-09-18-email-batch/README.md)

**内容更新：** 2026-09-19

### [Jev + Kimi 邮件反欺诈](cases/2026-09-18-email-fraud/README.md)

先快速筛查诈骗邮件，再把拿不准的交给更大的模型复核。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100608348219478016/img/23vFEVMegwLrMa8g.jpg" width="320" alt="Jev + Kimi 邮件反欺诈">](https://x.com/nutlope/status/2100614659690713543)

[效果待验证](references/2026-09-19-claims-audit.md#email-fraud) · [X · 542 赞快照](https://x.com/nutlope/status/2100614659690713543) · [原理与依据](cases/2026-09-18-email-fraud/README.md)

**内容更新：** 2026-09-19

### [银行流水收款方整理](cases/2026-09-18-bank-payee/README.md)

把银行流水里杂乱的交易说明，整理成更容易认出的商户名。

[<img src="https://pbs.twimg.com/media/HSVWcZ9WcAAcwPe.jpg?name=orig" width="320" alt="银行流水收款方整理">](https://x.com/jlongster/status/2100179852053639236)

[效果待验证](references/2026-09-19-claims-audit.md#bank-payee) · [X · 633 赞快照](https://x.com/jlongster/status/2100179852053639236) · [原理与依据](cases/2026-09-18-bank-payee/README.md)

**内容更新：** 2026-09-19

### [日语客服升级意图](cases/2026-09-18-support-intent/README.md)

从日语客服消息里判断：用户是不是想找人工、是不是已经问过多次。

[<img src="https://pbs.twimg.com/media/HSYXuW5aoAAghbD.jpg?name=orig" width="320" alt="日语客服升级意图">](https://x.com/ku_suke/status/2100392430805856469)

[原理较清楚](references/2026-09-19-claims-audit.md#support-intent) · [X · 351 赞快照](https://x.com/ku_suke/status/2100392430805856469) · [原理与依据](cases/2026-09-18-support-intent/README.md)

**内容更新：** 2026-09-19

### [按列名意图评分的电子表格](cases/2026-09-18-predictive-spreadsheet/README.md)

给一列起名“紧急程度”，让每行文字自动获得相应评级。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100779722447667200/img/gvsEg2-3oD6FRZhc.jpg" width="320" alt="按列名意图评分的电子表格">](https://x.com/dabit3/status/2100780008193020049)

[效果待验证](references/2026-09-19-claims-audit.md#predictive-spreadsheet) · [X · 337 赞快照](https://x.com/dabit3/status/2100780008193020049) · [原理与依据](cases/2026-09-18-predictive-spreadsheet/README.md)

**内容更新：** 2026-09-19

### [邮件分类 · 四模型速度对照](cases/2026-09-18-email-speed-race/README.md)

让四个模型给一组邮件分类，在同一页面对照完成进度和耗时。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100829070514864128/img/V3ix1we5Euhs8DsY.jpg" width="320" alt="邮件分类 · 四模型速度对照">](https://x.com/usutaku_channel/status/2100829343954173965)

[效果待验证](references/2026-09-19-claims-audit.md#email-speed-race) · [X · 445 赞快照](https://x.com/usutaku_channel/status/2100829343954173965) · [原理与依据](cases/2026-09-18-email-speed-race/README.md)

**内容更新：** 2026-09-19

### [Calorie Notebook · 文字饮食记录](cases/2026-09-18-calorie-notebook/README.md)

用文字记下吃了什么，界面快速显示热量、营养数值和汇总。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100857416984477696/img/RAMEV-YddA05BR1X.jpg" width="320" alt="Calorie Notebook · 文字饮食记录">](https://x.com/thekitze/status/2100857642566758849)

[效果待验证](references/2026-09-19-claims-audit.md#calorie-notebook) · [X · 326 赞快照](https://x.com/thekitze/status/2100857642566758849) · [原理与依据](cases/2026-09-18-calorie-notebook/README.md)

**内容更新：** 2026-09-19

### [Box · 事故报告分级归档](cases/2026-09-19-box-incident-triage/README.md)

读事故报告，判断影响与严重程度，再放进对应处理文件夹。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100999115949953024/img/6D1_NvmSfMLGDstw.jpg" width="320" alt="Box · 事故报告分级归档">](https://x.com/levie/status/2101007708044574906)

[效果待验证](references/2026-09-19-claims-audit.md#box-incident-triage) · [X · 317 赞快照](https://x.com/levie/status/2101007708044574906) · [原理与依据](cases/2026-09-19-box-incident-triage/README.md)

**内容更新：** 2026-09-19

### [NoSugarForKids · 零食多维评分](cases/2026-09-19-snack-scoring/README.md)

批量给儿童零食打分，帮助整理商品目录。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101005796603809792/img/19SyyiWW5wotfFfW.jpg" width="320" alt="NoSugarForKids · 零食多维评分">](https://x.com/nikunj/status/2101006585481073093)

[效果待验证](references/2026-09-19-claims-audit.md#snack-scoring) · [X · 312 赞快照](https://x.com/nikunj/status/2101006585481073093) · [原理与依据](cases/2026-09-19-snack-scoring/README.md)

**内容更新：** 2026-09-19

### [Tax Doc Classifier · 税务 PDF 页面识别](cases/2026-09-19-tax-doc-classifier/README.md)

识别税务 PDF 每页属于哪种表格，给后续整理提供标签。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100973360989773825/img/yMtL6CxrKMVXQEHV.jpg" width="320" alt="Tax Doc Classifier · 税务 PDF 页面识别">](https://x.com/nedwize/status/2100973868324417852)

[原理较清楚](references/2026-09-19-claims-audit.md#tax-doc-classifier) · [X · 1,506 赞快照](https://x.com/nedwize/status/2100973868324417852) · [原理与依据](cases/2026-09-19-tax-doc-classifier/README.md)

**内容更新：** 2026-09-19

### [Gmail · 按意图找邮件](cases/2026-09-19-gmail-intent-search/README.md)

用一句需求筛出相关邮件，减少只靠关键词搜索的限制。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100959260616151040/img/nb1GFqB_cwNesugB.jpg" width="320" alt="Gmail · 按意图找邮件">](https://x.com/dabit3/status/2100960281769738433)

[效果待验证](references/2026-09-19-claims-audit.md#gmail-intent-search) · [X · 574 赞快照](https://x.com/dabit3/status/2100960281769738433) · [原理与依据](cases/2026-09-19-gmail-intent-search/README.md)

**内容更新：** 2026-09-19

### [OCR + Jev · 图片归类](cases/2026-09-19-ocr-image-organizer/README.md)

先读出图片里的文字，再按内容整理图片。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100953271238320128/img/vzUjAo15Bg8tVa_q.jpg" width="320" alt="OCR + Jev · 图片归类">](https://x.com/fayazara/status/2100953838891192789)

[效果待验证](references/2026-09-19-claims-audit.md#ocr-image-organizer) · [X · 246 赞快照](https://x.com/fayazara/status/2100953838891192789) · [原理与依据](cases/2026-09-19-ocr-image-organizer/README.md)

**内容更新：** 2026-09-19

### [macOS Downloads · 按规则归档文件](cases/2026-09-19-downloads-organizer/README.md)

监控下载目录，把符合自定义规则的文件移动到对应位置。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100906588626173952/img/1KnNI3B3aUJEwFvI.jpg" width="320" alt="macOS Downloads · 按规则归档文件">](https://x.com/marcelpociot/status/2100906882365788167)

[效果待验证](references/2026-09-19-claims-audit.md#downloads-organizer) · [X · 889 赞快照](https://x.com/marcelpociot/status/2100906882365788167) · [原理与依据](cases/2026-09-19-downloads-organizer/README.md)

**内容更新：** 2026-09-19

### [虚构面试记录 · 批量分类与评分](cases/2026-09-19-synthetic-interview-classifier/README.md)

将 100 份虚构面试记录分为通过、保留、暂不考虑，并给出分项评分。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101206578284380160/img/WUIj3LeQ4Nrch8yD.jpg" width="320" alt="虚构面试记录 · 批量分类与评分">](https://x.com/masa_okamura108/status/2101206603240477030)

[效果待验证](references/2026-09-19-increment7-audit.md#synthetic-interview-classifier) · [X · 278 赞快照](https://x.com/masa_okamura108/status/2101206603240477030) · [原理与依据](cases/2026-09-19-synthetic-interview-classifier/README.md)

**内容更新：** 2026-09-19

</details>

<a id="content"></a>

<details>
<summary><strong>读懂内容与传播</strong> · 10</summary>

有的工具给广告贴标签，有的分析文章关联或预测传播。描述内容与预测未来是两回事；高评分也不保证流量或引用。

[同类优劣对比](breakdowns/2026-09-18-content.md)

### [实时帖子潜力分析器](cases/2026-09-18-live-viral/README.md)

写帖子时边写边看反馈，了解内容类型和可能的传播潜力。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100424897491070976/img/kKnsb68jNUZZzSBi.jpg" width="320" alt="实时帖子潜力分析器">](https://x.com/rileybrown/status/2100425868053008758)

[效果待验证](references/2026-09-19-claims-audit.md#live-viral) · [X · 830 赞快照](https://x.com/rileybrown/status/2100425868053008758) · [原理与依据](cases/2026-09-18-live-viral/README.md)

**内容更新：** 2026-09-19

### [帖子传播分类器](cases/2026-09-18-viral-classifier/README.md)

尝试从帖子里挑出更可能引起关注的内容。

[<img src="https://pbs.twimg.com/media/HSbxP15bMAA1LaU.jpg?name=orig" width="320" alt="帖子传播分类器">](https://x.com/robj3d3/status/2100631889585606959)

[主张缺依据](references/2026-09-19-claims-audit.md#viral-classifier) · [X · 387 赞快照](https://x.com/robj3d3/status/2100631889585606959) · [原理与依据](cases/2026-09-18-viral-classifier/README.md)

**内容更新：** 2026-09-19

### [X 传播评分模拟器](cases/2026-09-18-x-algorithm-sim/README.md)

给帖子做传播效果模拟，看看不同写法可能得到什么评分。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100467692117295104/img/01ZWSKAA75eSiFlc.jpg" width="320" alt="X 传播评分模拟器">](https://x.com/leojrr/status/2100470174130250127)

[主张缺依据](references/2026-09-19-claims-audit.md#x-algorithm-sim) · [X · 877 赞快照](https://x.com/leojrr/status/2100470174130250127) · [原理与依据](cases/2026-09-18-x-algorithm-sim/README.md)

**内容更新：** 2026-09-19

### [收藏率分位预测实验](cases/2026-09-18-bookmark-prediction/README.md)

预测一条帖子的收藏量，能不能排进附近日期帖子的前四分之一。

[<img src="https://pbs.twimg.com/media/HSYtFVgaoAIPpi5.jpg?name=orig" width="320" alt="收藏率分位预测实验">](https://x.com/AM09_21/status/2100430480642642395)

[效果待验证](references/2026-09-19-claims-audit.md#bookmark-prediction) · [X · 287 赞快照](https://x.com/AM09_21/status/2100430480642642395) · [原理与依据](cases/2026-09-18-bookmark-prediction/README.md)

**内容更新：** 2026-09-19

### [3,282 条历史帖子分析](cases/2026-09-18-post-analytics/README.md)

回看自己的几千条帖子，找出哪些主题和写法过去更受欢迎。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100668725737213952/img/m210oIkCyuGX5Dqr.jpg" width="320" alt="3,282 条历史帖子分析">](https://x.com/iannuttall/status/2100668908227162567)

[效果待验证](references/2026-09-19-claims-audit.md#post-analytics) · [X · 262 赞快照](https://x.com/iannuttall/status/2100668908227162567) · [原理与依据](cases/2026-09-18-post-analytics/README.md)

**内容更新：** 2026-09-19

### [StealAds 广告拆解预览](cases/2026-09-18-ad-analysis/README.md)

把大量广告拆成开场卖点、优惠和引导动作，方便找创作思路。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100654321792684032/img/cXvU50KmCe6QFu86.jpg" width="320" alt="StealAds 广告拆解预览">](https://x.com/TheMattBerman/status/2100654891756589230)

[效果待验证](references/2026-09-19-claims-audit.md#ad-analysis) · [X · 1,678 赞快照](https://x.com/TheMattBerman/status/2100654891756589230) · [原理与依据](cases/2026-09-18-ad-analysis/README.md)

**内容更新：** 2026-09-19

### [JevMeter 言论指标仪表](cases/2026-09-18-jevmeter/README.md)

给辩论或访谈逐句打指标，观察说话方式和内容特征。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100473445868003328/img/1ukjahQYLgbIEmyI.jpg" width="320" alt="JevMeter 言论指标仪表">](https://x.com/chetaslua/status/2100473581251748216)

[主张缺依据](references/2026-09-19-claims-audit.md#jevmeter) · [X · 1,017 赞快照](https://x.com/chetaslua/status/2100473581251748216) · [原理与依据](cases/2026-09-18-jevmeter/README.md)

**内容更新：** 2026-09-19

### [SEO 内链推荐 · 从已有文字找链接](cases/2026-09-19-seo-internal-links/README.md)

扫描网站文章，挑选相关页面和已有文字作为内部链接。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101018477087592448/img/9YlAHKLLo_h6rgtK.jpg" width="320" alt="SEO 内链推荐 · 从已有文字找链接">](https://x.com/borjafat/status/2101018783976722479)

[效果待验证](references/2026-09-19-claims-audit.md#seo-internal-links) · [X · 721 赞快照](https://x.com/borjafat/status/2101018783976722479) · [原理与依据](cases/2026-09-19-seo-internal-links/README.md)

**内容更新：** 2026-09-19

### [MaxFusion · 广告素材分类](cases/2026-09-19-maxfusion-ad-classifier/README.md)

给广告标注风格和用户旅程阶段，方便按维度分析账号素材。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100940464870301696/img/g-uzVt-FDP21an26.jpg" width="320" alt="MaxFusion · 广告素材分类">](https://x.com/OriSilver/status/2100941251478458871)

[效果待验证](references/2026-09-19-claims-audit.md#maxfusion-ad-classifier) · [X · 320 赞快照](https://x.com/OriSilver/status/2100941251478458871) · [原理与依据](cases/2026-09-19-maxfusion-ad-classifier/README.md)

**内容更新：** 2026-09-19

### [Ryze AI · SEO/GEO 审核与修复](cases/2026-09-19-ryze-seo-geo/README.md)

把 Jev 加入网站搜索可见性审核，分析页面及 AI 搜索引用并提出修复。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101089408099516416/img/Smzn-jtE8prvdY90.jpg" width="320" alt="Ryze AI · SEO/GEO 审核与修复">](https://x.com/irabukht/status/2101090579127951694)

[主张缺依据](references/2026-09-19-increment7-audit.md#ryze-seo-geo) · [X · 790 赞快照](https://x.com/irabukht/status/2101090579127951694) · [原理与依据](cases/2026-09-19-ryze-seo-geo/README.md)

**内容更新：** 2026-09-19

</details>

<a id="filter"></a>

<details>
<summary><strong>过滤不想看的内容</strong> · 4</summary>

把“我不想看到什么”变成可执行的筛选规则。信息流过滤判断帖子，网页清理判断元素，视频跳过判断时间段；各自都要能纠正误判。

[同类优劣对比](breakdowns/2026-09-18-filter.md)

### [自然语言 X 内容过滤器](cases/2026-09-18-x-filter/README.md)

用自己的话告诉浏览器：哪些 X 帖子我不想看。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100519256425140224/img/-A44e4qCo8mVP8ws.jpg" width="320" alt="自然语言 X 内容过滤器">](https://x.com/marcelpociot/status/2100520134481735729)

[效果待验证](references/2026-09-19-claims-audit.md#x-filter) · [X · 950 赞快照](https://x.com/marcelpociot/status/2100520134481735729) · [原理与依据](cases/2026-09-18-x-filter/README.md)

**内容更新：** 2026-09-19

### [Unclutter 页面清理](cases/2026-09-18-unclutter/README.md)

帮网页清掉广告、促销弹窗等干扰，让正文更容易看。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100595059041370112/img/cyfF5qMMKBPQTMAG.jpg" width="320" alt="Unclutter 页面清理">](https://x.com/thekitze/status/2100595129874817340)

[效果待验证](references/2026-09-19-claims-audit.md#unclutter) · [X · 497 赞快照](https://x.com/thekitze/status/2100595129874817340) · [原理与依据](cases/2026-09-18-unclutter/README.md)

**内容更新：** 2026-09-19

### [YouTube 赞助片段跳过](cases/2026-09-18-youtube-sponsor-skip/README.md)

观看 YouTube 时识别口播赞助片段，自动跳到后面的内容。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100792834526007296/img/8AFbjqEeZrJUEHid.jpg" width="320" alt="YouTube 赞助片段跳过">](https://x.com/tdinh_me/status/2100793777103466615)

[原理较清楚](references/2026-09-19-claims-audit.md#youtube-sponsor-skip) · [X · 238 赞快照](https://x.com/tdinh_me/status/2100793777103466615) · [原理与依据](cases/2026-09-18-youtube-sponsor-skip/README.md)

**内容更新：** 2026-09-19

### [X 回复清理 · 标记低价值评论](cases/2026-09-19-x-reply-cleanup/README.md)

识别帖子下面疑似低价值回复，帮助用户清理评论区。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100888448118759424/img/MafhEAfm3BlPst1X.jpg" width="320" alt="X 回复清理 · 标记低价值评论">](https://x.com/iannuttall/status/2100888635943883244)

[效果待验证](references/2026-09-19-claims-audit.md#x-reply-cleanup) · [X · 223 赞快照](https://x.com/iannuttall/status/2100888635943883244) · [原理与依据](cases/2026-09-19-x-reply-cleanup/README.md)

**内容更新：** 2026-09-19

</details>

<a id="memory"></a>

<details>
<summary><strong>帮 AI 留住有用记忆</strong> · 3</summary>

对话变长后，哪些信息值得留下？这些工具分别选择何时压缩、压缩什么、召回什么；节省字数之后，仍要检查任务能否继续做好。

[同类优劣对比](breakdowns/2026-09-18-memory.md)

### [工具调用上下文压缩](cases/2026-09-18-context-compaction/README.md)

给 AI 助手的工作记录瘦身，只把眼下有用的内容继续带着。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100694537672998912/img/OF8vottg6-45ZgNl.jpg" width="320" alt="工具调用上下文压缩">](https://x.com/tamarajtran/status/2100694549362553153)

[主张缺依据](references/2026-09-19-claims-audit.md#context-compaction) · [X · 1,646 赞快照](https://x.com/tamarajtran/status/2100694549362553153) · [原理与依据](cases/2026-09-18-context-compaction/README.md)

**内容更新：** 2026-09-19

### [记忆系统检索筛选](cases/2026-09-18-memory-retrieval/README.md)

从 AI 记忆库里筛出真正相关的内容，减少翻找和阅读负担。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100565973376061440/img/jeTib61RNpwXn853.jpg" width="320" alt="记忆系统检索筛选">](https://x.com/moritzkremb/status/2100566009312940457)

[效果待验证](references/2026-09-19-claims-audit.md#memory-retrieval) · [X · 335 赞快照](https://x.com/moritzkremb/status/2100566009312940457) · [原理与依据](cases/2026-09-18-memory-retrieval/README.md)

**内容更新：** 2026-09-19

### [Compact Adviser · 判断何时压缩上下文](cases/2026-09-19-compact-adviser/README.md)

在编码会话接近合适停顿点时，提示是否该整理上下文。

[<img src="https://pbs.twimg.com/media/HShbIHcbcAAJvsR.jpg?name=orig" width="320" alt="Compact Adviser · 判断何时压缩上下文">](https://x.com/kunchenguid/status/2101032677940117875)

[效果待验证](references/2026-09-19-claims-audit.md#compact-adviser) · [X · 242 赞快照](https://x.com/kunchenguid/status/2101032677940117875) · [原理与依据](cases/2026-09-19-compact-adviser/README.md)

**内容更新：** 2026-09-19

</details>

<a id="games"></a>

<details>
<summary><strong>玩游戏与解谜</strong> · 16</summary>

把游戏状态变成可选动作，就能观察一连串小判断怎样影响结果。有的只选动作，有的配合规划器或现成解法；流畅演示不等于高水平通关。

[同类优劣对比](breakdowns/2026-09-18-games.md)

### [官方 Doom 演示](cases/2026-09-18-doom/README.md)

让 Jev 持续选择游戏动作，演示快速决策如何接入 Doom。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2099924592534183936/img/hBGk8j8MRxBgPyg9.jpg" width="320" alt="官方 Doom 演示">](https://x.com/CompleteSkeptic/status/2099925687465570372)

[效果待验证](references/2026-09-19-claims-audit.md#doom) · [X · 4,585 赞快照](https://x.com/CompleteSkeptic/status/2099925687465570372) · [原理与依据](cases/2026-09-18-doom/README.md)

**内容更新：** 2026-09-19

### [Super Mario · @faadilhshaik](cases/2026-09-18-mario-faadhil/README.md)

让 Jev 操作超级马里奥，展示快速选择动作的效果。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100085174826647552/img/6YMRQKKZYBPsW2oo.jpg" width="320" alt="Super Mario · @faadilhshaik">](https://x.com/faadilhshaik/status/2100086301894881578)

[效果待验证](references/2026-09-19-claims-audit.md#mario-faadhil) · [X · 2,686 赞快照](https://x.com/faadilhshaik/status/2100086301894881578) · [原理与依据](cases/2026-09-18-mario-faadhil/README.md)

**内容更新：** 2026-09-19

### [Super Mario · Jev / Qwen 对照](cases/2026-09-18-mario-comparison/README.md)

给 Jev 和 Qwen 相同的马里奥信息，比较它们怎样选动作。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100567975317454849/img/UjFbLkeMH5RdOrlS.jpg" width="320" alt="Super Mario · Jev / Qwen 对照">](https://x.com/karaage0703/status/2100569924238471355)

[原理较清楚](references/2026-09-19-claims-audit.md#mario-comparison) · [X · 284 赞快照](https://x.com/karaage0703/status/2100569924238471355) · [原理与依据](cases/2026-09-18-mario-comparison/README.md)

**内容更新：** 2026-09-19

### [Super Mario · 1-1 关卡](cases/2026-09-18-mario-ppo/README.md)

展示用 Jev 接入马里奥第一关，与作者之前训练游戏 AI 的经历对照。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100454863335501825/img/RbCmluMnOGM4rHPb.jpg" width="320" alt="Super Mario · 1-1 关卡">](https://x.com/shantanugoel/status/2100455295801827769)

[效果待验证](references/2026-09-19-claims-audit.md#mario-ppo) · [X · 248 赞快照](https://x.com/shantanugoel/status/2100455295801827769) · [原理与依据](cases/2026-09-18-mario-ppo/README.md)

**内容更新：** 2026-09-19

### [Astra + Jev 吃豆人](cases/2026-09-18-pacman/README.md)

一个模型想策略，Jev 负责快速走下一步，合力玩吃豆人。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100335842451492864/img/gC9HxZoXRIgMLKrW.jpg" width="320" alt="Astra + Jev 吃豆人">](https://x.com/daniel_mac8/status/2100335929273524541)

[效果待验证](references/2026-09-19-claims-audit.md#pacman) · [X · 860 赞快照](https://x.com/daniel_mac8/status/2100335929273524541) · [原理与依据](cases/2026-09-18-pacman/README.md)

**内容更新：** 2026-09-19

### [贪吃蛇逐步决策](cases/2026-09-18-snake/README.md)

贪吃蛇每走一步，都先问 Jev 下一步怎么走。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100516335155646464/img/pow4ZDKeRwkBVSvy.jpg" width="320" alt="贪吃蛇逐步决策">](https://x.com/chenchengpro/status/2100516953496670430)

[效果待验证](references/2026-09-19-claims-audit.md#snake) · [X · 204 赞快照](https://x.com/chenchengpro/status/2100516953496670430) · [原理与依据](cases/2026-09-18-snake/README.md)

**内容更新：** 2026-09-19

### [俄罗斯方块](cases/2026-09-18-tetris/README.md)

让 Jev 决定俄罗斯方块的操作，观察它怎样安排落块。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100315393860730880/img/u0iH2SHQny2hkd4Q.jpg" width="320" alt="俄罗斯方块">](https://x.com/marcus_lowe/status/2100315518930661861)

[效果待验证](references/2026-09-19-claims-audit.md#tetris) · [X · 956 赞快照](https://x.com/marcus_lowe/status/2100315518930661861) · [原理与依据](cases/2026-09-18-tetris/README.md)

**内容更新：** 2026-09-19

### [Jev Plays Pokémon](cases/2026-09-18-pokemon/README.md)

让 Jev 长时间玩宝可梦，并记录打到哪里、用了多少次决策。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100539819172544512/img/0EZ7yznRwL7qi4K8.jpg" width="320" alt="Jev Plays Pokémon">](https://x.com/0xBOYD/status/2100539883836018697)

[效果待验证](references/2026-09-19-claims-audit.md#pokemon) · [X · 220 赞快照](https://x.com/0xBOYD/status/2100539883836018697) · [原理与依据](cases/2026-09-18-pokemon/README.md)

**内容更新：** 2026-09-19

### [杀戮尖塔 2 代打](cases/2026-09-18-slay-spire/README.md)

让 Jev 代选卡牌游戏中的行动，减少等模型思考的时间。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100569632482746369/img/TPuOBiHYCWUWxNOc.jpg" width="320" alt="杀戮尖塔 2 代打">](https://x.com/coolish/status/2100570517954838897)

[效果待验证](references/2026-09-19-claims-audit.md#slay-spire) · [X · 598 赞快照](https://x.com/coolish/status/2100570517954838897) · [原理与依据](cases/2026-09-18-slay-spire/README.md)

**内容更新：** 2026-09-19

### [5+0 国际象棋对局](cases/2026-09-18-chess/README.md)

让几个模型下限时国际象棋，同时比较下棋水平与思考速度。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100371773275406336/img/NmHPy0pAprSsC6Gi.jpg" width="320" alt="5+0 国际象棋对局">](https://x.com/aimlapi/status/2100372930282573876)

[原理较清楚](references/2026-09-19-claims-audit.md#chess) · [X · 1,985 赞快照](https://x.com/aimlapi/status/2100372930282573876) · [原理与依据](cases/2026-09-18-chess/README.md)

**内容更新：** 2026-09-19

### [Subway Surfers 并行演示](cases/2026-09-18-subway-runners/README.md)

展示 Jev 同时控制多局跑酷游戏的效果。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100633400717565952/img/KlytLNSLCQA-yY2E.jpg" width="320" alt="Subway Surfers 并行演示">](https://x.com/_MaxBlade/status/2100634359099232678)

[效果待验证](references/2026-09-19-claims-audit.md#subway-runners) · [X · 1,474 赞快照](https://x.com/_MaxBlade/status/2100634359099232678) · [原理与依据](cases/2026-09-18-subway-runners/README.md)

**内容更新：** 2026-09-19

### [魔方分阶段解法](cases/2026-09-18-rubiks-cube/README.md)

程序会魔方公式，Jev 帮它判断当前该用哪一种。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100479486382809088/img/r6daGpDnvsCr3LyL.jpg" width="320" alt="魔方分阶段解法">](https://x.com/redp314/status/2100489858951073858)

[原理较清楚](references/2026-09-19-claims-audit.md#rubiks-cube) · [X · 494 赞快照](https://x.com/redp314/status/2100489858951073858) · [原理与依据](cases/2026-09-18-rubiks-cube/README.md)

**内容更新：** 2026-09-19

### [Mario Kart 64](cases/2026-09-18-mario-kart/README.md)

展示 Jev 玩马里奥赛车，观察连续驾驶时的反应。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100605130869784576/img/gdGysXaHMdzFOU8W.jpg" width="320" alt="Mario Kart 64">](https://x.com/shreypandya/status/2100606445758898287)

[主张缺依据](references/2026-09-19-claims-audit.md#mario-kart) · [X · 204 赞快照](https://x.com/shreypandya/status/2100606445758898287) · [原理与依据](cases/2026-09-18-mario-kart/README.md)

**内容更新：** 2026-09-19

### [Minecraft · Jev、Astra 与本地策略](cases/2026-09-18-minecraft-hybrid/README.md)

让不同模型分工玩 Minecraft：一个管长远计划，一个应急，本地模型负责走路和瞄准。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100727359569530880/img/IGuQpzilRkIsw1Wb.jpg" width="320" alt="Minecraft · Jev、Astra 与本地策略">](https://x.com/wuyang_zhou/status/2100727660875808913)

[效果待验证](references/2026-09-19-claims-audit.md#minecraft-hybrid) · [X · 354 赞快照](https://x.com/wuyang_zhou/status/2100727660875808913) · [原理与依据](cases/2026-09-18-minecraft-hybrid/README.md)

**内容更新：** 2026-09-19

### [Sprite Fusion · 实时生成跑酷地形](cases/2026-09-19-game-level-generation/README.md)

玩家向前跑时，为前方地图选择新的平台和间隙。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100952449661992960/img/GEVdw9BvAW7Dv2Gx.jpg" width="320" alt="Sprite Fusion · 实时生成跑酷地形">](https://x.com/HugoDuprez/status/2100953089003921543)

[原理较清楚](references/2026-09-19-claims-audit.md#game-level-generation) · [X · 1,289 赞快照](https://x.com/HugoDuprez/status/2100953089003921543) · [原理与依据](cases/2026-09-19-game-level-generation/README.md)

**内容更新：** 2026-09-19

### [Flappy Bird · 飞行避障](cases/2026-09-19-flappy-bird/README.md)

让 Jev 参与控制小鸟穿过障碍。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100937854813700096/img/AlsBUETn77dLd0r8.jpg" width="320" alt="Flappy Bird · 飞行避障">](https://x.com/thymikee/status/2100937960115838984)

[效果待验证](references/2026-09-19-claims-audit.md#flappy-bird) · [X · 254 赞快照](https://x.com/thymikee/status/2100937960115838984) · [原理与依据](cases/2026-09-19-flappy-bird/README.md)

**内容更新：** 2026-09-19

</details>

<a id="simulation"></a>

<details>
<summary><strong>在模拟世界里做实验</strong> · 10</summary>

从交通灯、机器人到虚构角色，在沙盘里观察决策的影响。物理与运动通常由程序处理；模拟成功之后，还需要验证现实中的表现。

[同类优劣对比](breakdowns/2026-09-18-simulation.md)

### [按需求行动的 NPC](cases/2026-09-18-npc-needs/README.md)

让游戏角色根据自己的需求，挑选环境中合适的物品或活动。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100394190643355648/img/52O-mJZSxj4IGHos.jpg" width="320" alt="按需求行动的 NPC">](https://x.com/m_iraji/status/2100394212743159944)

[效果待验证](references/2026-09-19-claims-audit.md#npc-needs) · [X · 201 赞快照](https://x.com/m_iraji/status/2100394212743159944) · [原理与依据](cases/2026-09-18-npc-needs/README.md)

**内容更新：** 2026-09-19

### [500 个 3D agents](cases/2026-09-18-npc-500/README.md)

在同一个 3D 世界里，让很多虚拟角色并行做决定。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100457262372560897/img/zSIVGvaQhEZLMd9-.jpg" width="320" alt="500 个 3D agents">](https://x.com/crislenta/status/2100457614073327754)

[主张缺依据](references/2026-09-19-claims-audit.md#npc-500) · [X · 572 赞快照](https://x.com/crislenta/status/2100457614073327754) · [原理与依据](cases/2026-09-18-npc-500/README.md)

**内容更新：** 2026-09-19

### [“FSD”驾驶模拟演示](cases/2026-09-18-driving-toy/README.md)

一个让 Jev 参与开车的模拟小实验，作者把它称作“重建 FSD”。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100347372844756992/img/CaExDBw3MTf0ia58.jpg" width="320" alt="“FSD”驾驶模拟演示">](https://x.com/jpschroeder/status/2100347770867458384)

[主张缺依据](references/2026-09-19-claims-audit.md#driving-toy) · [X · 3,993 赞快照](https://x.com/jpschroeder/status/2100347770867458384) · [原理与依据](cases/2026-09-18-driving-toy/README.md)

**内容更新：** 2026-09-19

### [不暂停的实时驾驶模拟](cases/2026-09-18-realtime-driving/README.md)

模型思考时车也不停，测试 Jev 能否跟上模拟驾驶的节奏。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100323655389474816/img/LLOAJ3wie1phk45K.jpg" width="320" alt="不暂停的实时驾驶模拟">](https://x.com/SigGravitas/status/2100325221932958134)

[效果待验证](references/2026-09-19-claims-audit.md#realtime-driving) · [X · 270 赞快照](https://x.com/SigGravitas/status/2100325221932958134) · [原理与依据](cases/2026-09-18-realtime-driving/README.md)

**内容更新：** 2026-09-19

### [Jev 无人机仿真](cases/2026-09-18-drone-sim/README.md)

在模拟器里让无人机过障碍，Jev 选路线策略，代码负责稳住飞机。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100335726097494016/img/EljFdjduS88MyP9d.jpg" width="320" alt="Jev 无人机仿真">](https://x.com/RomanSlack1/status/2100335978229690683)

[原理较清楚](references/2026-09-19-claims-audit.md#drone-sim) · [X · 330 赞快照](https://x.com/RomanSlack1/status/2100335978229690683) · [原理与依据](cases/2026-09-18-drone-sim/README.md)

**内容更新：** 2026-09-19

### [Unstable Government 小镇](cases/2026-09-18-unstable-government/README.md)

给虚构小镇颁布一条法规，看看居民怎样反应并生成一份报纸。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100576552849117184/img/fdEy6tirVMqee5pe.jpg" width="320" alt="Unstable Government 小镇">](https://x.com/threepointone/status/2100576921629163848)

[效果待验证](references/2026-09-19-claims-audit.md#unstable-government) · [X · 395 赞快照](https://x.com/threepointone/status/2100576921629163848) · [原理与依据](cases/2026-09-18-unstable-government/README.md)

**内容更新：** 2026-09-19

### [150 位虚构用户意向](cases/2026-09-18-synthetic-personas/README.md)

让一群虚构用户回答产品意向问题，帮助整理早期想法。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100474178457698304/img/DXGnHg-iUrEhsFgE.jpg" width="320" alt="150 位虚构用户意向">](https://x.com/ytiskw/status/2100474943154827344)

[效果待验证](references/2026-09-19-claims-audit.md#synthetic-personas) · [X · 792 赞快照](https://x.com/ytiskw/status/2100474943154827344) · [原理与依据](cases/2026-09-18-synthetic-personas/README.md)

**内容更新：** 2026-09-19

### [Jev City · 九路口交通灯模拟](cases/2026-09-19-traffic-light-city/README.md)

在虚拟路网中选择交通灯方向，观察车辆排队与等待时间。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101161072447180800/img/sRIOALT11TUpdAdU.jpg" width="320" alt="Jev City · 九路口交通灯模拟">](https://x.com/leojrr/status/2101161666410893328)

[主张缺依据](references/2026-09-19-increment7-audit.md#traffic-light-city) · [X · 1,081 赞快照](https://x.com/leojrr/status/2101161666410893328) · [原理与依据](cases/2026-09-19-traffic-light-city/README.md)

**内容更新：** 2026-09-19

### [生命体征模拟 · 状态变化判断](cases/2026-09-19-vital-signs-simulator/README.md)

用正常状态和心率偏慢的模拟场景，对照规则报警与 Jev 判断。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101125501234630656/img/pxMddfrpMLTvBhaR.jpg" width="320" alt="生命体征模拟 · 状态变化判断">](https://x.com/roiyaruRIZ/status/2101130711067431018)

[主张缺依据](references/2026-09-19-increment7-audit.md#vital-signs-simulator) · [X · 216 赞快照](https://x.com/roiyaruRIZ/status/2101130711067431018) · [原理与依据](cases/2026-09-19-vital-signs-simulator/README.md)

**内容更新：** 2026-09-19

### [双臂机器人仿真 · 分层动作决策](cases/2026-09-19-dual-arm-robot-sim/README.md)

在模拟环境中按指令操作积木，由 Jev 承担中间层决策。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101070240444772353/img/Ci_PCLcMigmoAdks.jpg" width="320" alt="双臂机器人仿真 · 分层动作决策">](https://x.com/Raptor_zip/status/2101091398447505567)

[效果待验证](references/2026-09-19-increment7-audit.md#dual-arm-robot-sim) · [X · 229 赞快照](https://x.com/Raptor_zip/status/2101091398447505567) · [原理与依据](cases/2026-09-19-dual-arm-robot-sim/README.md)

**内容更新：** 2026-09-19

</details>

<a id="interaction"></a>

<details>
<summary><strong>把判断变成交互</strong> · 15</summary>

选择一个颜色、一个组件，或判断一句话是否需要回应，小判断也能组成新界面。不同作品分别看语义、结构和误触发，不能只比响应快慢。

[同类优劣对比](breakdowns/2026-09-18-interaction.md)

### [TypeGPU 实时语义特效](cases/2026-09-18-typegpu-realtime/README.md)

让摄像头和麦克风感知到的内容，影响画面的灯光与特效。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100644432211062784/img/iduKHYZdESQ5FBR7.jpg" width="320" alt="TypeGPU 实时语义特效">](https://x.com/reczko_konrad/status/2100646448324833512)

[效果待验证](references/2026-09-19-claims-audit.md#typegpu-realtime) · [X · 251 赞快照](https://x.com/reczko_konrad/status/2100646448324833512) · [原理与依据](cases/2026-09-18-typegpu-realtime/README.md)

**内容更新：** 2026-09-19

### [Ask Jev](cases/2026-09-18-ask-jev/README.md)

输入一个问题，看看 Jev 会怎样判断，而不是等它写一大段回答。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100486117325955072/img/_QailXRTsMGQ_atc.jpg" width="320" alt="Ask Jev">](https://x.com/waynesutton/status/2100487878992388279)

[效果待验证](references/2026-09-19-claims-audit.md#ask-jev) · [X · 423 赞快照](https://x.com/waynesutton/status/2100487878992388279) · [原理与依据](cases/2026-09-18-ask-jev/README.md)

**内容更新：** 2026-09-19

### [有限词表聊天](cases/2026-09-18-word-chat/README.md)

只给 Jev 一份常用词清单，让它一个词一个词拼出对话。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100407646226649088/img/qVPomAIwJ_lKpO2J.jpg" width="320" alt="有限词表聊天">](https://x.com/hi_im_isaac_/status/2100408276949385668)

[原理较清楚](references/2026-09-19-claims-audit.md#word-chat) · [X · 2,644 赞快照](https://x.com/hi_im_isaac_/status/2100408276949385668) · [原理与依据](cases/2026-09-18-word-chat/README.md)

**内容更新：** 2026-09-19

### [29 选项字符生成](cases/2026-09-18-character-chat/README.md)

让 Jev 每次挑一个字母或标点，慢慢拼成一段话。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100217973000617984/img/AFareJummI08B_QB.jpg" width="320" alt="29 选项字符生成">](https://x.com/ryanvogel/status/2100218045549412499)

[原理较清楚](references/2026-09-19-claims-audit.md#character-chat) · [X · 866 赞快照](https://x.com/ryanvogel/status/2100218045549412499) · [原理与依据](cases/2026-09-18-character-chat/README.md)

**内容更新：** 2026-09-19

### [并行像素绘图](cases/2026-09-18-pixel-drawing/README.md)

把许多小像素的判断拼在一起，尝试让 Jev 画图。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100245288183066624/img/ARkl8CTLZxp1KXSa.jpg" width="320" alt="并行像素绘图">](https://x.com/anshuc/status/2100246929611411501)

[效果待验证](references/2026-09-19-claims-audit.md#pixel-drawing) · [X · 1,461 赞快照](https://x.com/anshuc/status/2100246929611411501) · [原理与依据](cases/2026-09-18-pixel-drawing/README.md)

**内容更新：** 2026-09-19

### [RISC-jeV 逻辑门实验](cases/2026-09-18-riscv/README.md)

让 Jev 判断最简单的逻辑，再把这些判断拼成小型计算机指令。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100454137695469568/img/pGRTotN_ZQaAuc4V.jpg" width="320" alt="RISC-jeV 逻辑门实验">](https://x.com/i2cjak/status/2100454307405365673)

[效果待验证](references/2026-09-19-claims-audit.md#riscv) · [X · 208 赞快照](https://x.com/i2cjak/status/2100454307405365673) · [原理与依据](cases/2026-09-18-riscv/README.md)

**内容更新：** 2026-09-19

### [意图预测启动器](cases/2026-09-18-predictive-launcher/README.md)

不记文件名也能找文件：输入“刚下载的 PDF”，让相关文件排到前面。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100756324845862913/img/8ew1NdHs6k5cReoF.jpg" width="320" alt="意图预测启动器">](https://x.com/dabit3/status/2100756930054504776)

[效果待验证](references/2026-09-19-claims-audit.md#predictive-launcher) · [X · 252 赞快照](https://x.com/dabit3/status/2100756930054504776) · [原理与依据](cases/2026-09-18-predictive-launcher/README.md)

**内容更新：** 2026-09-19

### [实时电商导购与头像表情](cases/2026-09-18-live-commerce-assistant/README.md)

一边聊天一边推荐商品，让虚拟店员的表情跟着对话变化。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100735518963355648/img/o0S0IxXnxWjnlNOG.jpg" width="320" alt="实时电商导购与头像表情">](https://x.com/rinte0321/status/2100736454850908344)

[效果待验证](references/2026-09-19-claims-audit.md#live-commerce-assistant) · [X · 217 赞快照](https://x.com/rinte0321/status/2100736454850908344) · [原理与依据](cases/2026-09-18-live-commerce-assistant/README.md)

**内容更新：** 2026-09-19

### [实时表情候选](cases/2026-09-18-emoji-suggestions/README.md)

输入文字时，自动推荐与意思相符的 emoji。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100705222016520192/img/BxzTN_rxkA_FLvwe.jpg" width="320" alt="实时表情候选">](https://x.com/riku720720/status/2100705558512963602)

[效果待验证](references/2026-09-19-claims-audit.md#emoji-suggestions) · [X · 230 赞快照](https://x.com/riku720720/status/2100705558512963602) · [原理与依据](cases/2026-09-18-emoji-suggestions/README.md)

**内容更新：** 2026-09-19

### [语音与手指指向控制画布](cases/2026-09-18-voice-gesture-canvas/README.md)

边说边指，在画布里表达“把那个放到这里”。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100729243185324032/img/YNw8njfnSXu-Tbyr.jpg" width="320" alt="语音与手指指向控制画布">](https://x.com/jackcheng/status/2100729670991802386)

[效果待验证](references/2026-09-19-claims-audit.md#voice-gesture-canvas) · [X · 915 赞快照](https://x.com/jackcheng/status/2100729670991802386) · [原理与依据](cases/2026-09-18-voice-gesture-canvas/README.md)

**内容更新：** 2026-09-19

### [Probably · 用语义判断控制程序](cases/2026-09-18-probably-language/README.md)

把“这封邮件是否紧急”这样的判断写进条件分支，再让文字模型按结果起草回复。

[<img src="https://pbs.twimg.com/media/HSdr-ILWUAAN29Y.jpg?name=orig" width="320" alt="Probably · 用语义判断控制程序">](https://x.com/southpolesteve/status/2100767781868150938)

[原理较清楚](references/2026-09-19-claims-audit.md#probably-language) · [X · 894 赞快照](https://x.com/southpolesteve/status/2100767781868150938) · [原理与依据](cases/2026-09-18-probably-language/README.md)

**内容更新：** 2026-09-19

### [终端历史命令 · 语义补全](cases/2026-09-18-shell-history-suggestions/README.md)

输入半条命令或一句意图，从用过的命令里推荐下一条。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100858390683475969/img/PRKkLSCaQKsfoXRI.jpg" width="320" alt="终端历史命令 · 语义补全">](https://x.com/thorstenball/status/2100858434904109099)

[原理较清楚](references/2026-09-19-claims-audit.md#shell-history-suggestions) · [X · 396 赞快照](https://x.com/thorstenball/status/2100858434904109099) · [原理与依据](cases/2026-09-18-shell-history-suggestions/README.md)

**内容更新：** 2026-09-19

### [json-render · 用组件选择拼出界面](cases/2026-09-19-json-render-ui/README.md)

把界面需求变成受约束的组件布局，支持增删和移动组件。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101022081810911232/img/3tKdQ3Y2_ZGSg3Q7.jpg" width="320" alt="json-render · 用组件选择拼出界面">](https://x.com/ctatedev/status/2101022101750571357)

[原理较清楚](references/2026-09-19-claims-audit.md#json-render-ui) · [X · 3,341 赞快照](https://x.com/ctatedev/status/2101022101750571357) · [原理与依据](cases/2026-09-19-json-render-ui/README.md)

**内容更新：** 2026-09-19

### [CNVS · 无唤醒词语音指令门控](cases/2026-09-19-cnvs-voice-gate/README.md)

一直听候选语音，判断这句话是不是在给电脑下指令。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100966551826444288/img/i2s52ZeMNTOO-IRD.jpg" width="320" alt="CNVS · 无唤醒词语音指令门控">](https://x.com/_MaxBlade/status/2100967959879471519)

[效果待验证](references/2026-09-19-claims-audit.md#cnvs-voice-gate) · [X · 1,053 赞快照](https://x.com/_MaxBlade/status/2100967959879471519) · [原理与依据](cases/2026-09-19-cnvs-voice-gate/README.md)

**内容更新：** 2026-09-19

### [词语与颜色 · 16 色概率可视化](cases/2026-09-19-color-judgments/README.md)

输入词语，把模型对颜色的判断画成配色结果。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100898643117068288/img/p9Jp61lJyiq-UoWK.jpg" width="320" alt="词语与颜色 · 16 色概率可视化">](https://x.com/mattdesl/status/2100899669802963060)

[原理较清楚](references/2026-09-19-claims-audit.md#color-judgments) · [X · 3,441 赞快照](https://x.com/mattdesl/status/2100899669802963060) · [原理与依据](cases/2026-09-19-color-judgments/README.md)

**内容更新：** 2026-09-19

</details>

<a id="finance"></a>

<details>
<summary><strong>研究交易与历史回测</strong> · 4</summary>

一类在过去行情上试策略，一类展示交易执行。回测要检查数据时序，执行要核对成交与风控；跑得快、费用低都不证明能盈利。

[同类优劣对比](breakdowns/2026-09-18-finance.md)

### [Monad / Kuru 交易机器人](cases/2026-09-18-trading-bot/README.md)

让 Jev 看价格变化后选买或卖，再由程序把订单送出去。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100355999064379392/img/BiAbeDjN57avf2VK.jpg" width="320" alt="Monad / Kuru 交易机器人">](https://x.com/jarrodwatts/status/2100356151468585346)

[效果待验证](references/2026-09-19-claims-audit.md#trading-bot) · [X · 4,142 赞快照](https://x.com/jarrodwatts/status/2100356151468585346) · [原理与依据](cases/2026-09-18-trading-bot/README.md)

**内容更新：** 2026-09-19

### [AI Hedge Fund · 策略回测](cases/2026-09-19-ai-hedge-fund-backtest/README.md)

选择策略和股票代码，在历史数据上运行策略实验。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100959729350561792/img/wc-JtyIBGa_9qgNL.jpg" width="320" alt="AI Hedge Fund · 策略回测">](https://x.com/virattt/status/2100959848623899005)

[主张缺依据](references/2026-09-19-claims-audit.md#ai-hedge-fund-backtest) · [X · 613 赞快照](https://x.com/virattt/status/2100959848623899005) · [原理与依据](cases/2026-09-19-ai-hedge-fund-backtest/README.md)

**内容更新：** 2026-09-19

### [丹麦股票 · 全年历史策略实验](cases/2026-09-19-danish-stock-backtest/README.md)

用市场、新闻等信息，在 2025 年行情上做交易策略实验。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100938100272746496/img/8yisuerchTVTcFTn.jpg" width="320" alt="丹麦股票 · 全年历史策略实验">](https://x.com/tommy_jepsen/status/2100939646653903063)

[效果待验证](references/2026-09-19-claims-audit.md#danish-stock-backtest) · [X · 269 赞快照](https://x.com/tommy_jepsen/status/2100939646653903063) · [原理与依据](cases/2026-09-19-danish-stock-backtest/README.md)

**内容更新：** 2026-09-19

### [Nifty 日内交易 · 含止损的账户演示](cases/2026-09-19-nifty-trading/README.md)

展示将 Jev 接入 Nifty 日内交易，并报告触发止损。

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100928264831410176/img/VP6eszCSb95ePMo4.jpg" width="320" alt="Nifty 日内交易 · 含止损的账户演示">](https://x.com/IndraVahan/status/2100929105382564113)

[效果待验证](references/2026-09-19-claims-audit.md#nifty-trading) · [X · 673 赞快照](https://x.com/IndraVahan/status/2100929105382564113) · [原理与依据](cases/2026-09-19-nifty-trading/README.md)

**内容更新：** 2026-09-19

</details>

## 关于这份收集

收录原始应用主帖达到 **200 赞**、有对应图片或视频的案例。同项目更新合并，独立实现按用途对比。点赞是历史快照，不是可信度评分；本库不承诺穷尽 X。

精确取数时间、技术细节和审核等级保留在详情与报告中。媒体权利归原作者；预览失效时可点击回原帖查看。

[案例索引](cases/README.md) · [来源与收录方法](references/README.md) · [待补证据](inbox/README.md) · [贡献案例](CONTRIBUTING.md)
