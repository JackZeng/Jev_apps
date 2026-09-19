# Jev: small decisions, surprising applications

[简体中文](README.md) | **English**

Most AI tools are known for writing answers. **TypeSafe Jev specializes in making judgments.**
Give it the current situation and a question or set of choices; it returns a choice, score or yes/no judgment for code to act on.
This guide explores what people have built with it—and what their demonstrations actually establish.

**112 examples · 11 categories** · Sources checked through 2026-09-19

[Browse all applications](#all-apps) · [How Jev works](breakdowns/2026-09-18-how-jev-apps-work.en.md) · [Latest additions](CHANGELOG.en.md)

## Six ideas worth understanding

Start with examples that have clear uses and inspectable mechanisms. Click an image to see its original demo.

### An AI clicks. Who reads the page?

[Browser Use · Ultrafast](cases/2026-09-18-browser-use/README.en.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="480" alt="Browser Use · Ultrafast">](https://x.com/gregpr07/status/2100411066966749359)

Code reads the page and lists controls; Jev picks an action. A text model helps when words need to be entered.

**Keep in mind:** The result depends on the whole system, not Jev alone.

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#browser-use) · [X · 6,891 likes at collection](https://x.com/gregpr07/status/2100411066966749359) · [How it works & evidence](cases/2026-09-18-browser-use/README.en.md)

**Content updated:** 2026-09-19

### Can choices become an interface?

[json-render: assemble interfaces from component choices](cases/2026-09-19-json-render-ui/README.en.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101022081810911232/img/3tKdQ3Y2_ZGSg3Q7.jpg" width="480" alt="json-render: assemble interfaces from component choices">](https://x.com/ctatedev/status/2101022101750571357)

Like building with blocks: Jev selects components and relationships; code assembles a renderable interface.

**Keep in mind:** A valid structure does not guarantee correct content or good design.

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#json-render-ui) · [X · 3,341 likes at collection](https://x.com/ctatedev/status/2101022101750571357) · [How it works & evidence](cases/2026-09-19-json-render-ui/README.en.md)

**Content updated:** 2026-09-19

### How do you skip a spoken sponsor segment?

[YouTube sponsor-segment skipping](cases/2026-09-18-youtube-sponsor-skip/README.en.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100792834526007296/img/8AFbjqEeZrJUEHid.jpg" width="480" alt="YouTube sponsor-segment skipping">](https://x.com/tdinh_me/status/2100793777103466615)

Jev identifies sponsor content in captions; code maps those lines to playback times and skips ahead.

**Keep in mind:** Captions and segment boundaries can be wrong; audio mode also needs transcription.

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#youtube-sponsor-skip) · [X · 238 likes at collection](https://x.com/tdinh_me/status/2100793777103466615) · [How it works & evidence](cases/2026-09-18-youtube-sponsor-skip/README.en.md)

**Content updated:** 2026-09-19

### Solving a cube: judgment or formulas?

[Staged Rubik's Cube solver](cases/2026-09-18-rubiks-cube/README.en.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100479486382809088/img/r6daGpDnvsCr3LyL.jpg" width="480" alt="Staged Rubik&#x27;s Cube solver">](https://x.com/redp314/status/2100489858951073858)

The formulas live in code. Jev recognizes the current situation; code selects a formula and checks the moves.

**Keep in mind:** This is model-and-code teamwork, not evidence that the model invented the solution.

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#rubiks-cube) · [X · 494 likes at collection](https://x.com/redp314/status/2100489858951073858) · [How it works & evidence](cases/2026-09-18-rubiks-cube/README.en.md)

**Content updated:** 2026-09-19

### What kind of form is each page?

[Tax Doc Classifier: label tax PDF pages](cases/2026-09-19-tax-doc-classifier/README.en.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100973360989773825/img/yMtL6CxrKMVXQEHV.jpg" width="480" alt="Tax Doc Classifier: label tax PDF pages">](https://x.com/nedwize/status/2100973868324417852)

Code extracts page text; Jev identifies the form type. Uncertain pages are held for review.

**Keep in mind:** The author publishes test results, which do not establish reliability on every format.

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#tax-doc-classifier) · [X · 1,506 likes at collection](https://x.com/nedwize/status/2100973868324417852) · [How it works & evidence](cases/2026-09-19-tax-doc-classifier/README.en.md)

**Content updated:** 2026-09-19

### Does every task need the strongest model?

[Claude Code Mod: model and effort routing](cases/2026-09-19-claude-code-jev-router/README.en.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" width="480" alt="Claude Code Mod: model and effort routing">](https://x.com/dani_avila7/status/2101176629745561686)

Like ticket triage: Jev judges task difficulty, and a plugin chooses subagent models and main-session reasoning effort.

**Keep in mind:** The routing mechanism is inspectable; real savings and quality effects remain unverified.

[Clearer mechanism](references/2026-09-19-increment7-audit.en.md#claude-code-jev-router) · [X · 417 likes at collection](https://x.com/dani_avila7/status/2101176629745561686) · [How it works & evidence](cases/2026-09-19-claude-code-jev-router/README.en.md)

**Content updated:** 2026-09-19

<a id="all-apps"></a>

## All applications

Expand a category to browse every example, including the six above. Dates are content-update dates in Beijing time.

Evidence labels link to the assessment: **Clearer mechanism / Effectiveness unverified / Claims lack support**. They describe public evidence; none of these applications has been independently reproduced here.

<a id="browser"></a>

<details>
<summary><strong>Operate browsers and computers</strong> · 12</summary>

These systems connect observation to action. Browser tools often read page structure; desktop tools may use accessibility trees or OCR. Compare task coverage before speed.

[Compare approaches](breakdowns/2026-09-18-browser.en.md)

### [Browser Use · Ultrafast](cases/2026-09-18-browser-use/README.en.md)

Describe a flight search and let the agent click, type and find results on the website.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="320" alt="Browser Use · Ultrafast">](https://x.com/gregpr07/status/2100411066966749359)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#browser-use) · [X · 6,891 likes at collection](https://x.com/gregpr07/status/2100411066966749359) · [How it works & evidence](cases/2026-09-18-browser-use/README.en.md)

**Content updated:** 2026-09-19

### [Stagehand browser control](cases/2026-09-18-stagehand/README.en.md)

Let Jev choose the next browser action and Stagehand carry it out.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100495119065722880/img/7A1mijkU3Z_Zj7PM.jpg" width="320" alt="Stagehand browser control">](https://x.com/kylejeong/status/2100622054945095934)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#stagehand) · [X · 393 likes at collection](https://x.com/kylejeong/status/2100622054945095934) · [How it works & evidence](cases/2026-09-18-stagehand/README.en.md)

**Content updated:** 2026-09-19

### [Cua · jev-use](cases/2026-09-18-cua-jev-use/README.en.md)

Give Jev a list of allowed browser actions, execute its choice, then check the result.

[<img src="https://pbs.twimg.com/media/HSb_nmIWYAAkGKa.jpg?name=orig" width="320" alt="Cua · jev-use">](https://x.com/trycua/status/2100649543079502213)

[Claims lack support](references/2026-09-19-claims-audit.en.md#cua-jev-use) · [X · 1,162 likes at collection](https://x.com/trycua/status/2100649543079502213) · [How it works & evidence](cases/2026-09-18-cua-jev-use/README.en.md)

**Content updated:** 2026-09-19

### [CoreML + OCR desktop clicks](cases/2026-09-18-coreml-ocr/README.en.md)

Recognize buttons and labels on a Mac, then ask Jev which one to click.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100629037790183424/img/NR6wQpZiC-xjCEsC.jpg" width="320" alt="CoreML + OCR desktop clicks">](https://x.com/milindlabs/status/2100631847155994852)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#coreml-ocr) · [X · 564 likes at collection](https://x.com/milindlabs/status/2100631847155994852) · [How it works & evidence](cases/2026-09-18-coreml-ocr/README.en.md)

**Content updated:** 2026-09-19

### [OpenCode + agent-desktop](cases/2026-09-18-agent-desktop/README.en.md)

One model remembers the task while Jev helps choose desktop targets quickly.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100358791321755648/img/t6Bd787flQiGeoJ_.jpg" width="320" alt="OpenCode + agent-desktop">](https://x.com/mdlahfir/status/2100359236924637349)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#agent-desktop) · [X · 870 likes at collection](https://x.com/mdlahfir/status/2100359236924637349) · [How it works & evidence](cases/2026-09-18-agent-desktop/README.en.md)

**Content updated:** 2026-09-19

### [Kernel browser demo](cases/2026-09-18-kernel-browser/README.en.md)

Try a web demo of Jev controlling a browser.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100321453455425537/img/hVYy_d3Nuw9XhSwg.jpg" width="320" alt="Kernel browser demo">](https://x.com/stevekrouse/status/2100321685081559542)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#kernel-browser) · [X · 235 likes at collection](https://x.com/stevekrouse/status/2100321685081559542) · [How it works & evidence](cases/2026-09-18-kernel-browser/README.en.md)

**Content updated:** 2026-09-19

### [Voice-controlled browser](cases/2026-09-18-voice-browser/README.en.md)

Speak a command, such as “go back,” and let the browser act.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100577954338373633/img/tbH43kHpUotE3hzK.jpg" width="320" alt="Voice-controlled browser">](https://x.com/moritzkremb/status/2100577979021832365)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#voice-browser) · [X · 1,829 likes at collection](https://x.com/moritzkremb/status/2100577979021832365) · [How it works & evidence](cases/2026-09-18-voice-browser/README.en.md)

**Content updated:** 2026-09-19

### [OpenCode app testing](cases/2026-09-18-opencode-qa/README.en.md)

Let a coding assistant interact with an app to help check it after development.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" width="320" alt="OpenCode app testing">](https://x.com/Neriousy/status/2100287208166969746)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#opencode-qa) · [X · 1,133 likes at collection](https://x.com/Neriousy/status/2100287208166969746) · [How it works & evidence](cases/2026-09-18-opencode-qa/README.en.md)

**Content updated:** 2026-09-19

### [Runlayer: parallel adversarial browser testing](cases/2026-09-18-runlayer-adversarial-testing/README.en.md)

Run multiple browser sessions to explore how a new release might fail during use.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100881920343105536/img/c1y4THiGwA2GfXGa.jpg" width="320" alt="Runlayer: parallel adversarial browser testing">](https://x.com/rafalwilinski/status/2100882207879434359)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#runlayer-adversarial-testing) · [X · 820 likes at collection](https://x.com/rafalwilinski/status/2100882207879434359) · [How it works & evidence](cases/2026-09-18-runlayer-adversarial-testing/README.en.md)

**Content updated:** 2026-09-19

### [Sac: Codex + Jev for Mac Calendar](cases/2026-09-18-sac-calendar-computer-use/README.en.md)

Add a Jev decision layer to Codex computer use and compare creating a calendar event side by side.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100853279089647616/img/H6altwjZQ28_1bfY.jpg" width="320" alt="Sac: Codex + Jev for Mac Calendar">](https://x.com/Saccc_c/status/2100864907046768890)

[Claims lack support](references/2026-09-19-increment7-audit.en.md#sac-calendar-computer-use) · [X · 217 likes at collection](https://x.com/Saccc_c/status/2100864907046768890) · [How it works & evidence](cases/2026-09-18-sac-calendar-computer-use/README.en.md)

**Content updated:** 2026-09-19

### [ego lite: filter Amazon products](cases/2026-09-19-ego-product-decisions/README.en.md)

Combine browser tooling and models to filter products on a webpage.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100969567715790848/img/IXAgXZrtsLGyeYRA.jpg" width="320" alt="ego lite: filter Amazon products">](https://x.com/ego_agent/status/2100970015977804008)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#ego-product-decisions) · [X · 366 likes at collection](https://x.com/ego_agent/status/2100970015977804008) · [How it works & evidence](cases/2026-09-19-ego-product-decisions/README.en.md)

**Content updated:** 2026-09-19

### [Tester Army: web and mobile end-to-end testing](cases/2026-09-19-tester-army-e2e/README.en.md)

Explore agent-driven interface tests in a framework targeting web and mobile.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100966360192868352/img/8GCSVzX1AYF4caav.jpg" width="320" alt="Tester Army: web and mobile end-to-end testing">](https://x.com/o_kwasniewski/status/2100966838905585687)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#tester-army-e2e) · [X · 505 likes at collection](https://x.com/o_kwasniewski/status/2100966838905585687) · [How it works & evidence](cases/2026-09-19-tester-army-e2e/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="routing"></a>

<details>
<summary><strong>Choose an assistant for the task</strong> · 11</summary>

Models, skills and tools serve different needs; Jev helps assign work. Model routing affects cost and quality, while skill routing finds capabilities. The two can work together.

[Compare approaches](breakdowns/2026-09-18-routing.en.md)

### [Eve criteria-based model router](cases/2026-09-18-eve-router/README.en.md)

Choose which model should handle a request before sending it there.

[<img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" width="320" alt="Eve criteria-based model router">](https://x.com/eve/status/2100430918762832180)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#eve-router) · [X · 821 likes at collection](https://x.com/eve/status/2100430918762832180) · [How it works & evidence](cases/2026-09-18-eve-router/README.en.md)

**Content updated:** 2026-09-19

### [Request-to-model router](cases/2026-09-18-ephraim-router/README.en.md)

Pick a model for each question and send the request automatically.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100454021852954624/img/hqULLONlXw40573G.jpg" width="320" alt="Request-to-model router">](https://x.com/ephraimduncan/status/2100454070536351824)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#ephraim-router) · [X · 1,503 likes at collection](https://x.com/ephraimduncan/status/2100454070536351824) · [How it works & evidence](cases/2026-09-18-ephraim-router/README.en.md)

**Content updated:** 2026-09-19

### [Firstmate task dispatch](cases/2026-09-18-firstmate/README.en.md)

Choose an AI worker and effort level based on the task and user preferences.

[<img src="https://pbs.twimg.com/media/HSYK_gbagAAqKqr.jpg?name=orig" width="320" alt="Firstmate task dispatch">](https://x.com/kunchenguid/status/2100468943853085061)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#firstmate) · [X · 1,615 likes at collection](https://x.com/kunchenguid/status/2100468943853085061) · [How it works & evidence](cases/2026-09-18-firstmate/README.en.md)

**Content updated:** 2026-09-19

### [Local coding-agent delegation](cases/2026-09-18-local-delegation/README.en.md)

Send routine work, hard questions and long coding tasks to different AI assistants.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100314084990414848/img/iePXR9Edae7YVCT_.jpg" width="320" alt="Local coding-agent delegation">](https://x.com/mdlahfir/status/2100314182201802811)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#local-delegation) · [X · 777 likes at collection](https://x.com/mdlahfir/status/2100314182201802811) · [How it works & evidence](cases/2026-09-18-local-delegation/README.en.md)

**Content updated:** 2026-09-19

### [Skillbox skill selection](cases/2026-09-18-skillbox/README.en.md)

Find useful skills for the current task in a large AI skill library.

[<img src="https://pbs.twimg.com/media/HRidCpLaMAAqV-7.jpg?name=orig" width="320" alt="Skillbox skill selection">](https://x.com/thekitze/status/2096598298220277856)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#skillbox) · [X · 724 likes at collection](https://x.com/thekitze/status/2100556122570792999) · [How it works & evidence](cases/2026-09-18-skillbox/README.en.md)

**Content updated:** 2026-09-19

### [Coding Garden tool assistant](cases/2026-09-18-coding-garden-assistant/README.en.md)

Ask for weather, information or to-do actions and let an assistant call the right tool.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" width="320" alt="Coding Garden tool assistant">](https://x.com/CodingGarden/status/2100665210419950031)

[Claims lack support](references/2026-09-19-claims-audit.en.md#coding-garden-assistant) · [X · 334 likes at collection](https://x.com/CodingGarden/status/2100665210419950031) · [How it works & evidence](cases/2026-09-18-coding-garden-assistant/README.en.md)

**Content updated:** 2026-09-19

### [Eve tool-calling agent](cases/2026-09-18-eve-tool-agent/README.en.md)

Let Jev choose an agent's next tool to reduce selection overhead.

[<img src="https://pbs.twimg.com/media/HSZSqLGXwAA1jSL.jpg?name=orig" width="320" alt="Eve tool-calling agent">](https://x.com/oviniciuslana/status/2100457622407168509)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#eve-tool-agent) · [X · 1,117 likes at collection](https://x.com/oviniciuslana/status/2100457622407168509) · [How it works & evidence](cases/2026-09-18-eve-tool-agent/README.en.md)

**Content updated:** 2026-09-19

### [ai-cli decision interface](cases/2026-09-18-ai-cli/README.en.md)

Give terminal-based assistants access to Jev judgments, choices and scores.

[<img src="https://pbs.twimg.com/media/HSbG2YLWkAAPqmU.jpg?name=orig" width="320" alt="ai-cli decision interface">](https://x.com/ctatedev/status/2100584917092409479)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#ai-cli) · [X · 874 likes at collection](https://x.com/ctatedev/status/2100584917092409479) · [How it works & evidence](cases/2026-09-18-ai-cli/README.en.md)

**Content updated:** 2026-09-19

### [Hono JevRouter: route requests by meaning](cases/2026-09-18-hono-semantic-router/README.en.md)

Choose responses such as HTML or Markdown based on whether a request appears to come from a person or an AI.

[<img src="https://pbs.twimg.com/media/HSfKgItbcAAwVIl.jpg?name=orig" width="320" alt="Hono JevRouter: route requests by meaning">](https://x.com/yusukebe/status/2100871075743859182)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#hono-semantic-router) · [X · 405 likes at collection](https://x.com/yusukebe/status/2100871075743859182) · [How it works & evidence](cases/2026-09-18-hono-semantic-router/README.en.md)

**Content updated:** 2026-09-19

### [Codex Model Router: choose a model each turn](cases/2026-09-19-codex-model-router/README.en.md)

Select a model and reasoning settings for each Codex task.

[<img src="https://pbs.twimg.com/media/HSgeLlIX0AAjedL.png?name=orig" width="320" alt="Codex Model Router: choose a model each turn">](https://x.com/antonioleivag/status/2100962426439000484)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#codex-model-router) · [X · 437 likes at collection](https://x.com/antonioleivag/status/2100962426439000484) · [How it works & evidence](cases/2026-09-19-codex-model-router/README.en.md)

**Content updated:** 2026-09-19

### [Claude Code Mod: model and effort routing](cases/2026-09-19-claude-code-jev-router/README.en.md)

Choose subagent models and adjust reasoning effort in the main conversation.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" width="320" alt="Claude Code Mod: model and effort routing">](https://x.com/dani_avila7/status/2101176629745561686)

[Clearer mechanism](references/2026-09-19-increment7-audit.en.md#claude-code-jev-router) · [X · 417 likes at collection](https://x.com/dani_avila7/status/2101176629745561686) · [How it works & evidence](cases/2026-09-19-claude-code-jev-router/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="review"></a>

<details>
<summary><strong>Check code and risky actions</strong> · 11</summary>

Break a broad review into specific judgments. Code review looks for defects; permission checks govern actions. Both false alarms and missed problems matter, and scores do not replace tests.

[Compare approaches](breakdowns/2026-09-18-review.en.md)

### [jev-review MCP](cases/2026-09-18-jev-review/README.en.md)

Score AI-written code and let the coding agent revise it using feedback.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100465308519759872/img/2uIG43VFGvWzku0s.jpg" width="320" alt="jev-review MCP">](https://x.com/niazmorshed_/status/2100465662867218857)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#jev-review) · [X · 445 likes at collection](https://x.com/niazmorshed_/status/2100465662867218857) · [How it works & evidence](cases/2026-09-18-jev-review/README.en.md)

**Content updated:** 2026-09-19

### [14-check PR risk review](cases/2026-09-18-typed-pr-review/README.en.md)

Screen code changes for risks such as exposed secrets or removed tests, and escalate uncertainty.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100585029533372416/img/ZcrsntW2yWgtB_HD.jpg" width="320" alt="14-check PR risk review">](https://x.com/redp314/status/2100585126652481915)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#typed-pr-review) · [X · 1,927 likes at collection](https://x.com/redp314/status/2100585126652481915) · [How it works & evidence](cases/2026-09-18-typed-pr-review/README.en.md)

**Content updated:** 2026-09-19

### [jev-rabbit natural-language rules](cases/2026-09-18-jev-rabbit/README.en.md)

Write code-review rules in plain language and have a bot check changes against them.

[<img src="https://pbs.twimg.com/media/HSbjmhQbQAA4G5A.jpg?name=orig" width="320" alt="jev-rabbit natural-language rules">](https://x.com/thekitze/status/2100616530275029139)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#jev-rabbit) · [X · 327 likes at collection](https://x.com/thekitze/status/2100616530275029139) · [How it works & evidence](cases/2026-09-18-jev-rabbit/README.en.md)

**Content updated:** 2026-09-19

### [Codebase complexity classifier](cases/2026-09-18-codebase-classifier/README.en.md)

Explore whether a codebase makes simple things unnecessarily complicated.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100067392223076352/img/BqXd-11SCr3_ff8q.jpg" width="320" alt="Codebase complexity classifier">](https://x.com/ryanvogel/status/2100068006592123055)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#codebase-classifier) · [X · 1,165 likes at collection](https://x.com/ryanvogel/status/2100068006592123055) · [How it works & evidence](cases/2026-09-18-codebase-classifier/README.en.md)

**Content updated:** 2026-09-19

### [fx auto mode safety classifier](cases/2026-09-18-fx-safety/README.en.md)

Check a command's potential risk before an agent executes it automatically.

[<img src="https://pbs.twimg.com/media/HSW-E8wWgAAyw9O.jpg?name=orig" width="320" alt="fx auto mode safety classifier">](https://x.com/fazxes/status/2100300097695232164)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#fx-safety) · [X · 591 likes at collection](https://x.com/fazxes/status/2100300097695232164) · [How it works & evidence](cases/2026-09-18-fx-safety/README.en.md)

**Content updated:** 2026-09-19

### [Jailbreak prompt prescreen](cases/2026-09-18-jailbreak-screen/README.en.md)

Prescreen prompts for attempts to bypass an AI system's rules.

[<img src="https://pbs.twimg.com/media/HSXq9mqbsAAtHoT.jpg?name=orig" width="320" alt="Jailbreak prompt prescreen">](https://x.com/mayfer/status/2100343452865265747)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#jailbreak-screen) · [X · 264 likes at collection](https://x.com/mayfer/status/2100343452865265747) · [How it works & evidence](cases/2026-09-18-jailbreak-screen/README.en.md)

**Content updated:** 2026-09-19

### [Document upload checker](cases/2026-09-18-upload-check/README.en.md)

Before uploading a document, check whether its contents should be shared.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100471095627591680/img/jQewHJZ85th2EEv3.jpg" width="320" alt="Document upload checker">](https://x.com/iwasakoya/status/2100471523358474709)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#upload-check) · [X · 284 likes at collection](https://x.com/iwasakoya/status/2100471523358474709) · [How it works & evidence](cases/2026-09-18-upload-check/README.en.md)

**Content updated:** 2026-09-19

### [Code judgments from ESLint rule descriptions](cases/2026-09-18-eslint-rule-judgments/README.en.md)

Give Jev a rule’s text description and ask whether a small code snippet complies.

[<img src="https://pbs.twimg.com/media/HSdqjcJa8AAGjPE.jpg?name=orig" width="320" alt="Code judgments from ESLint rule descriptions">](https://x.com/mizchi/status/2100765201385869434)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#eslint-rule-judgments) · [X · 351 likes at collection](https://x.com/mizchi/status/2100765201385869434) · [How it works & evidence](cases/2026-09-18-eslint-rule-judgments/README.en.md)

**Content updated:** 2026-09-19

### [OpenCode intent-aware permissions](cases/2026-09-18-opencode-intent-permissions/README.en.md)

Check an agent’s actions across tools using policies such as “only access Google.”

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100701224920129536/img/-vzxHYoZxMjXKOKh.jpg" width="320" alt="OpenCode intent-aware permissions">](https://x.com/OpeOginni/status/2100702649834188855)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#opencode-intent-permissions) · [X · 235 likes at collection](https://x.com/OpeOginni/status/2100702649834188855) · [How it works & evidence](cases/2026-09-18-opencode-intent-permissions/README.en.md)

**Content updated:** 2026-09-19

### [Code comments: accuracy and usefulness scores](cases/2026-09-18-code-comment-scoring/README.en.md)

Check whether a comment is correct and whether it adds useful information beyond the code.

[<img src="https://pbs.twimg.com/media/HSX4qrBWcAAA3K4.jpg?name=orig" width="320" alt="Code comments: accuracy and usefulness scores">](https://x.com/markjaquith/status/2100359340087501296)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#code-comment-scoring) · [X · 1,777 likes at collection](https://x.com/markjaquith/status/2100359340087501296) · [How it works & evidence](cases/2026-09-18-code-comment-scoring/README.en.md)

**Content updated:** 2026-09-19

### [Script.it: flag issues before writing review comments](cases/2026-09-19-script-code-review/README.en.md)

Score a git diff first, then ask a language model for explanations only when issues are flagged.

[<img src="https://pbs.twimg.com/media/HSgGI1wWQAAY5zl.jpg?name=orig" width="320" alt="Script.it: flag issues before writing review comments">](https://x.com/liorshkiller/status/2100936106615140757)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#script-code-review) · [X · 202 likes at collection](https://x.com/liorshkiller/status/2100936106615140757) · [How it works & evidence](cases/2026-09-19-script-code-review/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="data"></a>

<details>
<summary><strong>Organize files and information</strong> · 16</summary>

Label emails, identify forms or find relevant files. Classification, retrieval and numerical estimates fail in different ways; one speed ranking cannot compare them fairly.

[Compare approaches](breakdowns/2026-09-18-data.en.md)

### [1kpapers research classification](cases/2026-09-18-papers/README.en.md)

Organize over a thousand AI papers so readers can browse them by topic.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100425141947604992/img/AITyHwcOWq1jw-3Z.jpg" width="320" alt="1kpapers research classification">](https://x.com/nutlope/status/2100426999546184123)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#papers) · [X · 1,684 likes at collection](https://x.com/nutlope/status/2100426999546184123) · [How it works & evidence](cases/2026-09-18-papers/README.en.md)

**Content updated:** 2026-09-19

### [DuckDB semantic classification](cases/2026-09-18-duckdb/README.en.md)

Classify text rows while working with a table.

[<img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" width="320" alt="DuckDB semantic classification">](https://x.com/hamiltonulmer/status/2100370557405667768)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#duckdb) · [X · 1,310 likes at collection](https://x.com/hamiltonulmer/status/2100370557405667768) · [How it works & evidence](cases/2026-09-18-duckdb/README.en.md)

**Content updated:** 2026-09-19

### [Batch classification of 500 emails](cases/2026-09-18-email-batch/README.en.md)

Sort a large batch of emails into categories instead of filing them one by one.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100403183533125632/img/54ZFO-CHvDeC-rw-.jpg" width="320" alt="Batch classification of 500 emails">](https://x.com/rileybrown/status/2100404532119269426)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#email-batch) · [X · 3,161 likes at collection](https://x.com/rileybrown/status/2100404532119269426) · [How it works & evidence](cases/2026-09-18-email-batch/README.en.md)

**Content updated:** 2026-09-19

### [Jev + Kimi email fraud detection](cases/2026-09-18-email-fraud/README.en.md)

Screen emails for fraud quickly, then send uncertain cases to a larger model.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100608348219478016/img/23vFEVMegwLrMa8g.jpg" width="320" alt="Jev + Kimi email fraud detection">](https://x.com/nutlope/status/2100614659690713543)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#email-fraud) · [X · 542 likes at collection](https://x.com/nutlope/status/2100614659690713543) · [How it works & evidence](cases/2026-09-18-email-fraud/README.en.md)

**Content updated:** 2026-09-19

### [Bank transaction payee cleanup](cases/2026-09-18-bank-payee/README.en.md)

Turn messy bank transaction descriptions into recognizable merchant names.

[<img src="https://pbs.twimg.com/media/HSVWcZ9WcAAcwPe.jpg?name=orig" width="320" alt="Bank transaction payee cleanup">](https://x.com/jlongster/status/2100179852053639236)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#bank-payee) · [X · 633 likes at collection](https://x.com/jlongster/status/2100179852053639236) · [How it works & evidence](cases/2026-09-18-bank-payee/README.en.md)

**Content updated:** 2026-09-19

### [Japanese support escalation intent](cases/2026-09-18-support-intent/README.en.md)

Detect whether a Japanese support message asks for a human or mentions repeated contact.

[<img src="https://pbs.twimg.com/media/HSYXuW5aoAAghbD.jpg?name=orig" width="320" alt="Japanese support escalation intent">](https://x.com/ku_suke/status/2100392430805856469)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#support-intent) · [X · 351 likes at collection](https://x.com/ku_suke/status/2100392430805856469) · [How it works & evidence](cases/2026-09-18-support-intent/README.en.md)

**Content updated:** 2026-09-19

### [Intent-driven spreadsheet ratings](cases/2026-09-18-predictive-spreadsheet/README.en.md)

Name a column “Urgency” and have the text in each row receive a corresponding rating.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100779722447667200/img/gvsEg2-3oD6FRZhc.jpg" width="320" alt="Intent-driven spreadsheet ratings">](https://x.com/dabit3/status/2100780008193020049)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#predictive-spreadsheet) · [X · 337 likes at collection](https://x.com/dabit3/status/2100780008193020049) · [How it works & evidence](cases/2026-09-18-predictive-spreadsheet/README.en.md)

**Content updated:** 2026-09-19

### [Email classification: four-model speed comparison](cases/2026-09-18-email-speed-race/README.en.md)

Classify a set of emails with four models and compare progress and elapsed time on one screen.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100829070514864128/img/V3ix1we5Euhs8DsY.jpg" width="320" alt="Email classification: four-model speed comparison">](https://x.com/usutaku_channel/status/2100829343954173965)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#email-speed-race) · [X · 445 likes at collection](https://x.com/usutaku_channel/status/2100829343954173965) · [How it works & evidence](cases/2026-09-18-email-speed-race/README.en.md)

**Content updated:** 2026-09-19

### [Calorie Notebook: text-based food logging](cases/2026-09-18-calorie-notebook/README.en.md)

Write down what you ate and receive quick calorie, nutrient and total values in the interface.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100857416984477696/img/RAMEV-YddA05BR1X.jpg" width="320" alt="Calorie Notebook: text-based food logging">](https://x.com/thekitze/status/2100857642566758849)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#calorie-notebook) · [X · 326 likes at collection](https://x.com/thekitze/status/2100857642566758849) · [How it works & evidence](cases/2026-09-18-calorie-notebook/README.en.md)

**Content updated:** 2026-09-19

### [Box: triage and file incident reports](cases/2026-09-19-box-incident-triage/README.en.md)

Read incident reports, judge impact and severity, and route them to handling folders.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100999115949953024/img/6D1_NvmSfMLGDstw.jpg" width="320" alt="Box: triage and file incident reports">](https://x.com/levie/status/2101007708044574906)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#box-incident-triage) · [X · 317 likes at collection](https://x.com/levie/status/2101007708044574906) · [How it works & evidence](cases/2026-09-19-box-incident-triage/README.en.md)

**Content updated:** 2026-09-19

### [NoSugarForKids: multi-criterion snack scoring](cases/2026-09-19-snack-scoring/README.en.md)

Score children’s snacks in batches to organize a product catalog.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101005796603809792/img/19SyyiWW5wotfFfW.jpg" width="320" alt="NoSugarForKids: multi-criterion snack scoring">](https://x.com/nikunj/status/2101006585481073093)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#snack-scoring) · [X · 312 likes at collection](https://x.com/nikunj/status/2101006585481073093) · [How it works & evidence](cases/2026-09-19-snack-scoring/README.en.md)

**Content updated:** 2026-09-19

### [Tax Doc Classifier: label tax PDF pages](cases/2026-09-19-tax-doc-classifier/README.en.md)

Identify which tax form each PDF page belongs to for downstream organization.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100973360989773825/img/yMtL6CxrKMVXQEHV.jpg" width="320" alt="Tax Doc Classifier: label tax PDF pages">](https://x.com/nedwize/status/2100973868324417852)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#tax-doc-classifier) · [X · 1,506 likes at collection](https://x.com/nedwize/status/2100973868324417852) · [How it works & evidence](cases/2026-09-19-tax-doc-classifier/README.en.md)

**Content updated:** 2026-09-19

### [Gmail: search by intent](cases/2026-09-19-gmail-intent-search/README.en.md)

Filter relevant messages from a natural-language request instead of relying only on keywords.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100959260616151040/img/nb1GFqB_cwNesugB.jpg" width="320" alt="Gmail: search by intent">](https://x.com/dabit3/status/2100960281769738433)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#gmail-intent-search) · [X · 574 likes at collection](https://x.com/dabit3/status/2100960281769738433) · [How it works & evidence](cases/2026-09-19-gmail-intent-search/README.en.md)

**Content updated:** 2026-09-19

### [OCR + Jev: organize images](cases/2026-09-19-ocr-image-organizer/README.en.md)

Read text from images, then categorize them by content.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100953271238320128/img/vzUjAo15Bg8tVa_q.jpg" width="320" alt="OCR + Jev: organize images">](https://x.com/fayazara/status/2100953838891192789)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#ocr-image-organizer) · [X · 246 likes at collection](https://x.com/fayazara/status/2100953838891192789) · [How it works & evidence](cases/2026-09-19-ocr-image-organizer/README.en.md)

**Content updated:** 2026-09-19

### [macOS Downloads: organize files by rules](cases/2026-09-19-downloads-organizer/README.en.md)

Watch Downloads and move matching files to destinations defined by custom rules.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100906588626173952/img/1KnNI3B3aUJEwFvI.jpg" width="320" alt="macOS Downloads: organize files by rules">](https://x.com/marcelpociot/status/2100906882365788167)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#downloads-organizer) · [X · 889 likes at collection](https://x.com/marcelpociot/status/2100906882365788167) · [How it works & evidence](cases/2026-09-19-downloads-organizer/README.en.md)

**Content updated:** 2026-09-19

### [Synthetic interview notes: batch classification and scoring](cases/2026-09-19-synthetic-interview-classifier/README.en.md)

Sort 100 fictional interview records into advance, hold or decline and assign component scores.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101206578284380160/img/WUIj3LeQ4Nrch8yD.jpg" width="320" alt="Synthetic interview notes: batch classification and scoring">](https://x.com/masa_okamura108/status/2101206603240477030)

[Effectiveness unverified](references/2026-09-19-increment7-audit.en.md#synthetic-interview-classifier) · [X · 278 likes at collection](https://x.com/masa_okamura108/status/2101206603240477030) · [How it works & evidence](cases/2026-09-19-synthetic-interview-classifier/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="content"></a>

<details>
<summary><strong>Analyze content and reach</strong> · 10</summary>

Some tools label ads; others connect articles or predict reach. Describing content differs from predicting the future, and a high score does not guarantee traffic or citations.

[Compare approaches](breakdowns/2026-09-18-content.en.md)

### [Live post-potential analyzer](cases/2026-09-18-live-viral/README.en.md)

Get feedback on a post's type and potential reach as you write.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100424897491070976/img/kKnsb68jNUZZzSBi.jpg" width="320" alt="Live post-potential analyzer">](https://x.com/rileybrown/status/2100425868053008758)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#live-viral) · [X · 830 likes at collection](https://x.com/rileybrown/status/2100425868053008758) · [How it works & evidence](cases/2026-09-18-live-viral/README.en.md)

**Content updated:** 2026-09-19

### [Viral-post classifier](cases/2026-09-18-viral-classifier/README.en.md)

Try to identify posts that may attract more attention.

[<img src="https://pbs.twimg.com/media/HSbxP15bMAA1LaU.jpg?name=orig" width="320" alt="Viral-post classifier">](https://x.com/robj3d3/status/2100631889585606959)

[Claims lack support](references/2026-09-19-claims-audit.en.md#viral-classifier) · [X · 387 likes at collection](https://x.com/robj3d3/status/2100631889585606959) · [How it works & evidence](cases/2026-09-18-viral-classifier/README.en.md)

**Content updated:** 2026-09-19

### [X reach-score simulator](cases/2026-09-18-x-algorithm-sim/README.en.md)

Simulate reach scores to compare different ways of writing a post.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100467692117295104/img/01ZWSKAA75eSiFlc.jpg" width="320" alt="X reach-score simulator">](https://x.com/leojrr/status/2100470174130250127)

[Claims lack support](references/2026-09-19-claims-audit.en.md#x-algorithm-sim) · [X · 877 likes at collection](https://x.com/leojrr/status/2100470174130250127) · [How it works & evidence](cases/2026-09-18-x-algorithm-sim/README.en.md)

**Content updated:** 2026-09-19

### [Bookmark-percentile prediction](cases/2026-09-18-bookmark-prediction/README.en.md)

Predict whether a post ranks in the top quarter for bookmarks among nearby dates.

[<img src="https://pbs.twimg.com/media/HSYtFVgaoAIPpi5.jpg?name=orig" width="320" alt="Bookmark-percentile prediction">](https://x.com/AM09_21/status/2100430480642642395)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#bookmark-prediction) · [X · 287 likes at collection](https://x.com/AM09_21/status/2100430480642642395) · [How it works & evidence](cases/2026-09-18-bookmark-prediction/README.en.md)

**Content updated:** 2026-09-19

### [Analysis of 3,282 historical posts](cases/2026-09-18-post-analytics/README.en.md)

Review thousands of past posts to see which topics and styles performed well.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100668725737213952/img/m210oIkCyuGX5Dqr.jpg" width="320" alt="Analysis of 3,282 historical posts">](https://x.com/iannuttall/status/2100668908227162567)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#post-analytics) · [X · 262 likes at collection](https://x.com/iannuttall/status/2100668908227162567) · [How it works & evidence](cases/2026-09-18-post-analytics/README.en.md)

**Content updated:** 2026-09-19

### [StealAds ad-analysis preview](cases/2026-09-18-ad-analysis/README.en.md)

Break many ads into hooks, offers and calls to action for creative research.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100654321792684032/img/cXvU50KmCe6QFu86.jpg" width="320" alt="StealAds ad-analysis preview">](https://x.com/TheMattBerman/status/2100654891756589230)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#ad-analysis) · [X · 1,678 likes at collection](https://x.com/TheMattBerman/status/2100654891756589230) · [How it works & evidence](cases/2026-09-18-ad-analysis/README.en.md)

**Content updated:** 2026-09-19

### [JevMeter speech-analysis dashboard](cases/2026-09-18-jevmeter/README.en.md)

Score sentences in debates or interviews to examine speech patterns and content features.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100473445868003328/img/1ukjahQYLgbIEmyI.jpg" width="320" alt="JevMeter speech-analysis dashboard">](https://x.com/chetaslua/status/2100473581251748216)

[Claims lack support](references/2026-09-19-claims-audit.en.md#jevmeter) · [X · 1,017 likes at collection](https://x.com/chetaslua/status/2100473581251748216) · [How it works & evidence](cases/2026-09-18-jevmeter/README.en.md)

**Content updated:** 2026-09-19

### [SEO internal links: match existing text to relevant pages](cases/2026-09-19-seo-internal-links/README.en.md)

Scan site articles and suggest relevant internal links using text already present.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101018477087592448/img/9YlAHKLLo_h6rgtK.jpg" width="320" alt="SEO internal links: match existing text to relevant pages">](https://x.com/borjafat/status/2101018783976722479)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#seo-internal-links) · [X · 721 likes at collection](https://x.com/borjafat/status/2101018783976722479) · [How it works & evidence](cases/2026-09-19-seo-internal-links/README.en.md)

**Content updated:** 2026-09-19

### [MaxFusion: classify advertising creatives](cases/2026-09-19-maxfusion-ad-classifier/README.en.md)

Label ads by style and customer-journey stage for account-level analysis.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100940464870301696/img/g-uzVt-FDP21an26.jpg" width="320" alt="MaxFusion: classify advertising creatives">](https://x.com/OriSilver/status/2100941251478458871)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#maxfusion-ad-classifier) · [X · 320 likes at collection](https://x.com/OriSilver/status/2100941251478458871) · [How it works & evidence](cases/2026-09-19-maxfusion-ad-classifier/README.en.md)

**Content updated:** 2026-09-19

### [Ryze AI: SEO/GEO audits and fixes](cases/2026-09-19-ryze-seo-geo/README.en.md)

Add Jev to website visibility audits, analyzing pages and AI-search citations to guide fixes.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101089408099516416/img/Smzn-jtE8prvdY90.jpg" width="320" alt="Ryze AI: SEO/GEO audits and fixes">](https://x.com/irabukht/status/2101090579127951694)

[Claims lack support](references/2026-09-19-increment7-audit.en.md#ryze-seo-geo) · [X · 790 likes at collection](https://x.com/irabukht/status/2101090579127951694) · [How it works & evidence](cases/2026-09-19-ryze-seo-geo/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="filter"></a>

<details>
<summary><strong>Filter unwanted content</strong> · 4</summary>

Turn preferences into filtering rules. Feed tools judge posts, page cleaners judge elements, and video tools locate time segments. Each needs a way to correct mistakes.

[Compare approaches](breakdowns/2026-09-18-filter.en.md)

### [Natural-language X content filter](cases/2026-09-18-x-filter/README.en.md)

Tell the browser in your own words which X posts you would rather not see.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100519256425140224/img/-A44e4qCo8mVP8ws.jpg" width="320" alt="Natural-language X content filter">](https://x.com/marcelpociot/status/2100520134481735729)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#x-filter) · [X · 950 likes at collection](https://x.com/marcelpociot/status/2100520134481735729) · [How it works & evidence](cases/2026-09-18-x-filter/README.en.md)

**Content updated:** 2026-09-19

### [Unclutter page cleanup](cases/2026-09-18-unclutter/README.en.md)

Clear ads, promotional dialogs and similar clutter to make webpages easier to read.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100595059041370112/img/cyfF5qMMKBPQTMAG.jpg" width="320" alt="Unclutter page cleanup">](https://x.com/thekitze/status/2100595129874817340)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#unclutter) · [X · 497 likes at collection](https://x.com/thekitze/status/2100595129874817340) · [How it works & evidence](cases/2026-09-18-unclutter/README.en.md)

**Content updated:** 2026-09-19

### [YouTube sponsor-segment skipping](cases/2026-09-18-youtube-sponsor-skip/README.en.md)

Detect spoken sponsor segments while watching YouTube and jump past them.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100792834526007296/img/8AFbjqEeZrJUEHid.jpg" width="320" alt="YouTube sponsor-segment skipping">](https://x.com/tdinh_me/status/2100793777103466615)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#youtube-sponsor-skip) · [X · 238 likes at collection](https://x.com/tdinh_me/status/2100793777103466615) · [How it works & evidence](cases/2026-09-18-youtube-sponsor-skip/README.en.md)

**Content updated:** 2026-09-19

### [X reply cleanup: flag low-value comments](cases/2026-09-19-x-reply-cleanup/README.en.md)

Identify suspected low-value replies to help clean up a post’s discussion.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100888448118759424/img/MafhEAfm3BlPst1X.jpg" width="320" alt="X reply cleanup: flag low-value comments">](https://x.com/iannuttall/status/2100888635943883244)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#x-reply-cleanup) · [X · 223 likes at collection](https://x.com/iannuttall/status/2100888635943883244) · [How it works & evidence](cases/2026-09-19-x-reply-cleanup/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="memory"></a>

<details>
<summary><strong>Help AI keep useful context</strong> · 3</summary>

As conversations grow, what should stay? These tools decide when to compact, what to keep or what to retrieve. Fewer tokens are useful only if later work still succeeds.

[Compare approaches](breakdowns/2026-09-18-memory.en.md)

### [Tool-history context compaction](cases/2026-09-18-context-compaction/README.en.md)

Trim an AI assistant's work history to retain what matters now.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100694537672998912/img/OF8vottg6-45ZgNl.jpg" width="320" alt="Tool-history context compaction">](https://x.com/tamarajtran/status/2100694549362553153)

[Claims lack support](references/2026-09-19-claims-audit.en.md#context-compaction) · [X · 1,646 likes at collection](https://x.com/tamarajtran/status/2100694549362553153) · [How it works & evidence](cases/2026-09-18-context-compaction/README.en.md)

**Content updated:** 2026-09-19

### [Memory retrieval filtering](cases/2026-09-18-memory-retrieval/README.en.md)

Filter an AI memory store so the next model sees relevant material.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100565973376061440/img/jeTib61RNpwXn853.jpg" width="320" alt="Memory retrieval filtering">](https://x.com/moritzkremb/status/2100566009312940457)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#memory-retrieval) · [X · 335 likes at collection](https://x.com/moritzkremb/status/2100566009312940457) · [How it works & evidence](cases/2026-09-18-memory-retrieval/README.en.md)

**Content updated:** 2026-09-19

### [Compact Adviser: choose when to compact](cases/2026-09-19-compact-adviser/README.en.md)

Suggest when a coding conversation has reached a suitable point for context compaction.

[<img src="https://pbs.twimg.com/media/HShbIHcbcAAJvsR.jpg?name=orig" width="320" alt="Compact Adviser: choose when to compact">](https://x.com/kunchenguid/status/2101032677940117875)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#compact-adviser) · [X · 242 likes at collection](https://x.com/kunchenguid/status/2101032677940117875) · [How it works & evidence](cases/2026-09-19-compact-adviser/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="games"></a>

<details>
<summary><strong>Play games and solve puzzles</strong> · 16</summary>

Turn game state into choices and watch small decisions add up. Some systems only select actions; others use planners or predefined solutions. Smooth footage does not establish strong play.

[Compare approaches](breakdowns/2026-09-18-games.en.md)

### [Official Doom demo](cases/2026-09-18-doom/README.en.md)

Use Jev to choose game actions repeatedly in a Doom demo.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2099924592534183936/img/hBGk8j8MRxBgPyg9.jpg" width="320" alt="Official Doom demo">](https://x.com/CompleteSkeptic/status/2099925687465570372)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#doom) · [X · 4,585 likes at collection](https://x.com/CompleteSkeptic/status/2099925687465570372) · [How it works & evidence](cases/2026-09-18-doom/README.en.md)

**Content updated:** 2026-09-19

### [Super Mario · @faadilhshaik](cases/2026-09-18-mario-faadhil/README.en.md)

Let Jev control Super Mario to demonstrate fast action selection.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100085174826647552/img/6YMRQKKZYBPsW2oo.jpg" width="320" alt="Super Mario · @faadilhshaik">](https://x.com/faadilhshaik/status/2100086301894881578)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#mario-faadhil) · [X · 2,686 likes at collection](https://x.com/faadilhshaik/status/2100086301894881578) · [How it works & evidence](cases/2026-09-18-mario-faadhil/README.en.md)

**Content updated:** 2026-09-19

### [Super Mario · Jev / Qwen comparison](cases/2026-09-18-mario-comparison/README.en.md)

Give Jev and Qwen the same Mario information and compare action choices.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100567975317454849/img/UjFbLkeMH5RdOrlS.jpg" width="320" alt="Super Mario · Jev / Qwen comparison">](https://x.com/karaage0703/status/2100569924238471355)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#mario-comparison) · [X · 284 likes at collection](https://x.com/karaage0703/status/2100569924238471355) · [How it works & evidence](cases/2026-09-18-mario-comparison/README.en.md)

**Content updated:** 2026-09-19

### [Super Mario · World 1-1](cases/2026-09-18-mario-ppo/README.en.md)

Demonstrate Jev on Mario's first level alongside the author's earlier game-AI training experience.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100454863335501825/img/RbCmluMnOGM4rHPb.jpg" width="320" alt="Super Mario · World 1-1">](https://x.com/shantanugoel/status/2100455295801827769)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#mario-ppo) · [X · 248 likes at collection](https://x.com/shantanugoel/status/2100455295801827769) · [How it works & evidence](cases/2026-09-18-mario-ppo/README.en.md)

**Content updated:** 2026-09-19

### [Astra + Jev Pac-Man](cases/2026-09-18-pacman/README.en.md)

One model plans while Jev chooses quick local moves to play Pac-Man.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100335842451492864/img/gC9HxZoXRIgMLKrW.jpg" width="320" alt="Astra + Jev Pac-Man">](https://x.com/daniel_mac8/status/2100335929273524541)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#pacman) · [X · 860 likes at collection](https://x.com/daniel_mac8/status/2100335929273524541) · [How it works & evidence](cases/2026-09-18-pacman/README.en.md)

**Content updated:** 2026-09-19

### [Step-by-step Snake](cases/2026-09-18-snake/README.en.md)

Ask Jev for the next move at every step of Snake.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100516335155646464/img/pow4ZDKeRwkBVSvy.jpg" width="320" alt="Step-by-step Snake">](https://x.com/chenchengpro/status/2100516953496670430)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#snake) · [X · 204 likes at collection](https://x.com/chenchengpro/status/2100516953496670430) · [How it works & evidence](cases/2026-09-18-snake/README.en.md)

**Content updated:** 2026-09-19

### [Tetris](cases/2026-09-18-tetris/README.en.md)

Let Jev make Tetris decisions and observe how blocks are placed.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100315393860730880/img/u0iH2SHQny2hkd4Q.jpg" width="320" alt="Tetris">](https://x.com/marcus_lowe/status/2100315518930661861)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#tetris) · [X · 956 likes at collection](https://x.com/marcus_lowe/status/2100315518930661861) · [How it works & evidence](cases/2026-09-18-tetris/README.en.md)

**Content updated:** 2026-09-19

### [Jev Plays Pokémon](cases/2026-09-18-pokemon/README.en.md)

Let Jev play Pokémon over time and track progress and decision costs.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100539819172544512/img/0EZ7yznRwL7qi4K8.jpg" width="320" alt="Jev Plays Pokémon">](https://x.com/0xBOYD/status/2100539883836018697)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#pokemon) · [X · 220 likes at collection](https://x.com/0xBOYD/status/2100539883836018697) · [How it works & evidence](cases/2026-09-18-pokemon/README.en.md)

**Content updated:** 2026-09-19

### [Slay the Spire 2 agent](cases/2026-09-18-slay-spire/README.en.md)

Use Jev to choose card-game actions with less waiting between decisions.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100569632482746369/img/TPuOBiHYCWUWxNOc.jpg" width="320" alt="Slay the Spire 2 agent">](https://x.com/coolish/status/2100570517954838897)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#slay-spire) · [X · 598 likes at collection](https://x.com/coolish/status/2100570517954838897) · [How it works & evidence](cases/2026-09-18-slay-spire/README.en.md)

**Content updated:** 2026-09-19

### [5+0 blitz chess](cases/2026-09-18-chess/README.en.md)

Compare model playing strength and decision speed in timed chess.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100371773275406336/img/NmHPy0pAprSsC6Gi.jpg" width="320" alt="5+0 blitz chess">](https://x.com/aimlapi/status/2100372930282573876)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#chess) · [X · 1,985 likes at collection](https://x.com/aimlapi/status/2100372930282573876) · [How it works & evidence](cases/2026-09-18-chess/README.en.md)

**Content updated:** 2026-09-19

### [Parallel Subway Surfers demo](cases/2026-09-18-subway-runners/README.en.md)

Demonstrate Jev controlling multiple runner-style games at once.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100633400717565952/img/KlytLNSLCQA-yY2E.jpg" width="320" alt="Parallel Subway Surfers demo">](https://x.com/_MaxBlade/status/2100634359099232678)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#subway-runners) · [X · 1,474 likes at collection](https://x.com/_MaxBlade/status/2100634359099232678) · [How it works & evidence](cases/2026-09-18-subway-runners/README.en.md)

**Content updated:** 2026-09-19

### [Staged Rubik's Cube solver](cases/2026-09-18-rubiks-cube/README.en.md)

Code knows the cube-solving methods; Jev identifies which case to apply.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100479486382809088/img/r6daGpDnvsCr3LyL.jpg" width="320" alt="Staged Rubik&#x27;s Cube solver">](https://x.com/redp314/status/2100489858951073858)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#rubiks-cube) · [X · 494 likes at collection](https://x.com/redp314/status/2100489858951073858) · [How it works & evidence](cases/2026-09-18-rubiks-cube/README.en.md)

**Content updated:** 2026-09-19

### [Mario Kart 64](cases/2026-09-18-mario-kart/README.en.md)

Watch Jev control Mario Kart in a continuous-driving demo.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100605130869784576/img/gdGysXaHMdzFOU8W.jpg" width="320" alt="Mario Kart 64">](https://x.com/shreypandya/status/2100606445758898287)

[Claims lack support](references/2026-09-19-claims-audit.en.md#mario-kart) · [X · 204 likes at collection](https://x.com/shreypandya/status/2100606445758898287) · [How it works & evidence](cases/2026-09-18-mario-kart/README.en.md)

**Content updated:** 2026-09-19

### [Minecraft with Jev, Astra and local policies](cases/2026-09-18-minecraft-hybrid/README.en.md)

Split Minecraft play across models: long-term planning, quick reactions, and local movement and aiming.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100727359569530880/img/IGuQpzilRkIsw1Wb.jpg" width="320" alt="Minecraft with Jev, Astra and local policies">](https://x.com/wuyang_zhou/status/2100727660875808913)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#minecraft-hybrid) · [X · 354 likes at collection](https://x.com/wuyang_zhou/status/2100727660875808913) · [How it works & evidence](cases/2026-09-18-minecraft-hybrid/README.en.md)

**Content updated:** 2026-09-19

### [Sprite Fusion: generate runner terrain in real time](cases/2026-09-19-game-level-generation/README.en.md)

Select new platforms and gaps ahead of a moving player.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100952449661992960/img/GEVdw9BvAW7Dv2Gx.jpg" width="320" alt="Sprite Fusion: generate runner terrain in real time">](https://x.com/HugoDuprez/status/2100953089003921543)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#game-level-generation) · [X · 1,289 likes at collection](https://x.com/HugoDuprez/status/2100953089003921543) · [How it works & evidence](cases/2026-09-19-game-level-generation/README.en.md)

**Content updated:** 2026-09-19

### [Flappy Bird: navigate obstacles](cases/2026-09-19-flappy-bird/README.en.md)

Use Jev in controlling a bird through obstacles.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100937854813700096/img/AlsBUETn77dLd0r8.jpg" width="320" alt="Flappy Bird: navigate obstacles">](https://x.com/thymikee/status/2100937960115838984)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#flappy-bird) · [X · 254 likes at collection](https://x.com/thymikee/status/2100937960115838984) · [How it works & evidence](cases/2026-09-19-flappy-bird/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="simulation"></a>

<details>
<summary><strong>Experiment in simulated worlds</strong> · 10</summary>

Explore decisions in traffic, robotics and virtual characters. Code usually handles physics and movement. Success in a simulation still needs validation in the real world.

[Compare approaches](breakdowns/2026-09-18-simulation.en.md)

### [Needs-driven NPCs](cases/2026-09-18-npc-needs/README.en.md)

Let game characters choose objects or activities that meet their needs.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100394190643355648/img/52O-mJZSxj4IGHos.jpg" width="320" alt="Needs-driven NPCs">](https://x.com/m_iraji/status/2100394212743159944)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#npc-needs) · [X · 201 likes at collection](https://x.com/m_iraji/status/2100394212743159944) · [How it works & evidence](cases/2026-09-18-npc-needs/README.en.md)

**Content updated:** 2026-09-19

### [500 agents in a 3D environment](cases/2026-09-18-npc-500/README.en.md)

Run decisions for many virtual characters in one 3D world.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100457262372560897/img/zSIVGvaQhEZLMd9-.jpg" width="320" alt="500 agents in a 3D environment">](https://x.com/crislenta/status/2100457614073327754)

[Claims lack support](references/2026-09-19-claims-audit.en.md#npc-500) · [X · 572 likes at collection](https://x.com/crislenta/status/2100457614073327754) · [How it works & evidence](cases/2026-09-18-npc-500/README.en.md)

**Content updated:** 2026-09-19

### [“FSD” driving simulation](cases/2026-09-18-driving-toy/README.en.md)

A small driving simulation that the author calls “rebuilding FSD.”

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100347372844756992/img/CaExDBw3MTf0ia58.jpg" width="320" alt="“FSD” driving simulation">](https://x.com/jpschroeder/status/2100347770867458384)

[Claims lack support](references/2026-09-19-claims-audit.en.md#driving-toy) · [X · 3,993 likes at collection](https://x.com/jpschroeder/status/2100347770867458384) · [How it works & evidence](cases/2026-09-18-driving-toy/README.en.md)

**Content updated:** 2026-09-19

### [Unpaused real-time driving](cases/2026-09-18-realtime-driving/README.en.md)

Keep the car moving while Jev thinks to test real-time simulated driving.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100323655389474816/img/LLOAJ3wie1phk45K.jpg" width="320" alt="Unpaused real-time driving">](https://x.com/SigGravitas/status/2100325221932958134)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#realtime-driving) · [X · 270 likes at collection](https://x.com/SigGravitas/status/2100325221932958134) · [How it works & evidence](cases/2026-09-18-realtime-driving/README.en.md)

**Content updated:** 2026-09-19

### [Jev drone simulation](cases/2026-09-18-drone-sim/README.en.md)

Fly through simulated obstacles with Jev choosing tactics and code stabilizing the drone.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100335726097494016/img/EljFdjduS88MyP9d.jpg" width="320" alt="Jev drone simulation">](https://x.com/RomanSlack1/status/2100335978229690683)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#drone-sim) · [X · 330 likes at collection](https://x.com/RomanSlack1/status/2100335978229690683) · [How it works & evidence](cases/2026-09-18-drone-sim/README.en.md)

**Content updated:** 2026-09-19

### [Unstable Government town](cases/2026-09-18-unstable-government/README.en.md)

Introduce a law in a fictional town and watch residents react before a newspaper is generated.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100576552849117184/img/fdEy6tirVMqee5pe.jpg" width="320" alt="Unstable Government town">](https://x.com/threepointone/status/2100576921629163848)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#unstable-government) · [X · 395 likes at collection](https://x.com/threepointone/status/2100576921629163848) · [How it works & evidence](cases/2026-09-18-unstable-government/README.en.md)

**Content updated:** 2026-09-19

### [150 fictional user personas](cases/2026-09-18-synthetic-personas/README.en.md)

Ask fictional users about product interest to explore early ideas.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100474178457698304/img/DXGnHg-iUrEhsFgE.jpg" width="320" alt="150 fictional user personas">](https://x.com/ytiskw/status/2100474943154827344)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#synthetic-personas) · [X · 792 likes at collection](https://x.com/ytiskw/status/2100474943154827344) · [How it works & evidence](cases/2026-09-18-synthetic-personas/README.en.md)

**Content updated:** 2026-09-19

### [Jev City: nine-intersection traffic simulation](cases/2026-09-19-traffic-light-city/README.en.md)

Choose signal directions in a virtual road network and observe queues and waiting time.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101161072447180800/img/sRIOALT11TUpdAdU.jpg" width="320" alt="Jev City: nine-intersection traffic simulation">](https://x.com/leojrr/status/2101161666410893328)

[Claims lack support](references/2026-09-19-increment7-audit.en.md#traffic-light-city) · [X · 1,081 likes at collection](https://x.com/leojrr/status/2101161666410893328) · [How it works & evidence](cases/2026-09-19-traffic-light-city/README.en.md)

**Content updated:** 2026-09-19

### [Vital-sign simulation: judging state changes](cases/2026-09-19-vital-signs-simulator/README.en.md)

Compare rule alarms with Jev judgments in normal-state and slow-heart-rate simulations.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101125501234630656/img/pxMddfrpMLTvBhaR.jpg" width="320" alt="Vital-sign simulation: judging state changes">](https://x.com/roiyaruRIZ/status/2101130711067431018)

[Claims lack support](references/2026-09-19-increment7-audit.en.md#vital-signs-simulator) · [X · 216 likes at collection](https://x.com/roiyaruRIZ/status/2101130711067431018) · [How it works & evidence](cases/2026-09-19-vital-signs-simulator/README.en.md)

**Content updated:** 2026-09-19

### [Dual-arm robot simulation: layered action decisions](cases/2026-09-19-dual-arm-robot-sim/README.en.md)

Manipulate blocks in simulation, with Jev handling the middle decision layer.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101070240444772353/img/Ci_PCLcMigmoAdks.jpg" width="320" alt="Dual-arm robot simulation: layered action decisions">](https://x.com/Raptor_zip/status/2101091398447505567)

[Effectiveness unverified](references/2026-09-19-increment7-audit.en.md#dual-arm-robot-sim) · [X · 229 likes at collection](https://x.com/Raptor_zip/status/2101091398447505567) · [How it works & evidence](cases/2026-09-19-dual-arm-robot-sim/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="interaction"></a>

<details>
<summary><strong>Turn judgments into interactions</strong> · 15</summary>

Choose a color or component, or decide whether speech needs a response. Small judgments can create new interfaces. Compare meaning, structure and false activations as well as latency.

[Compare approaches](breakdowns/2026-09-18-interaction.en.md)

### [TypeGPU real-time semantic effects](cases/2026-09-18-typegpu-realtime/README.en.md)

Let camera and microphone input influence lighting and visual effects.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100644432211062784/img/iduKHYZdESQ5FBR7.jpg" width="320" alt="TypeGPU real-time semantic effects">](https://x.com/reczko_konrad/status/2100646448324833512)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#typegpu-realtime) · [X · 251 likes at collection](https://x.com/reczko_konrad/status/2100646448324833512) · [How it works & evidence](cases/2026-09-18-typegpu-realtime/README.en.md)

**Content updated:** 2026-09-19

### [Ask Jev](cases/2026-09-18-ask-jev/README.en.md)

Enter a question and see Jev's judgment instead of a long written answer.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100486117325955072/img/_QailXRTsMGQ_atc.jpg" width="320" alt="Ask Jev">](https://x.com/waynesutton/status/2100487878992388279)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#ask-jev) · [X · 423 likes at collection](https://x.com/waynesutton/status/2100487878992388279) · [How it works & evidence](cases/2026-09-18-ask-jev/README.en.md)

**Content updated:** 2026-09-19

### [Finite-vocabulary chat](cases/2026-09-18-word-chat/README.en.md)

Give Jev a common-word list and let it build a conversation one word at a time.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100407646226649088/img/qVPomAIwJ_lKpO2J.jpg" width="320" alt="Finite-vocabulary chat">](https://x.com/hi_im_isaac_/status/2100408276949385668)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#word-chat) · [X · 2,644 likes at collection](https://x.com/hi_im_isaac_/status/2100408276949385668) · [How it works & evidence](cases/2026-09-18-word-chat/README.en.md)

**Content updated:** 2026-09-19

### [29-option character generation](cases/2026-09-18-character-chat/README.en.md)

Let Jev choose one letter or punctuation mark at a time to build text.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100217973000617984/img/AFareJummI08B_QB.jpg" width="320" alt="29-option character generation">](https://x.com/ryanvogel/status/2100218045549412499)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#character-chat) · [X · 866 likes at collection](https://x.com/ryanvogel/status/2100218045549412499) · [How it works & evidence](cases/2026-09-18-character-chat/README.en.md)

**Content updated:** 2026-09-19

### [Parallel pixel drawing](cases/2026-09-18-pixel-drawing/README.en.md)

Combine many pixel-level judgments to experiment with drawing through Jev.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100245288183066624/img/ARkl8CTLZxp1KXSa.jpg" width="320" alt="Parallel pixel drawing">](https://x.com/anshuc/status/2100246929611411501)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#pixel-drawing) · [X · 1,461 likes at collection](https://x.com/anshuc/status/2100246929611411501) · [How it works & evidence](cases/2026-09-18-pixel-drawing/README.en.md)

**Content updated:** 2026-09-19

### [RISC-jeV logic-gate experiment](cases/2026-09-18-riscv/README.en.md)

Use Jev for simple logic decisions and compose them into small computer instructions.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100454137695469568/img/pGRTotN_ZQaAuc4V.jpg" width="320" alt="RISC-jeV logic-gate experiment">](https://x.com/i2cjak/status/2100454307405365673)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#riscv) · [X · 208 likes at collection](https://x.com/i2cjak/status/2100454307405365673) · [How it works & evidence](cases/2026-09-18-riscv/README.en.md)

**Content updated:** 2026-09-19

### [Intent-aware predictive launcher](cases/2026-09-18-predictive-launcher/README.en.md)

Find files without remembering names: type “the PDF I just downloaded” and rank relevant matches first.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100756324845862913/img/8ew1NdHs6k5cReoF.jpg" width="320" alt="Intent-aware predictive launcher">](https://x.com/dabit3/status/2100756930054504776)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#predictive-launcher) · [X · 252 likes at collection](https://x.com/dabit3/status/2100756930054504776) · [How it works & evidence](cases/2026-09-18-predictive-launcher/README.en.md)

**Content updated:** 2026-09-19

### [Live shopping assistant and avatar expressions](cases/2026-09-18-live-commerce-assistant/README.en.md)

Recommend products during a conversation and change a virtual shop assistant’s expression with the dialogue.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100735518963355648/img/o0S0IxXnxWjnlNOG.jpg" width="320" alt="Live shopping assistant and avatar expressions">](https://x.com/rinte0321/status/2100736454850908344)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#live-commerce-assistant) · [X · 217 likes at collection](https://x.com/rinte0321/status/2100736454850908344) · [How it works & evidence](cases/2026-09-18-live-commerce-assistant/README.en.md)

**Content updated:** 2026-09-19

### [Live emoji suggestions](cases/2026-09-18-emoji-suggestions/README.en.md)

Suggest emoji that fit the meaning of text as it is entered.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100705222016520192/img/BxzTN_rxkA_FLvwe.jpg" width="320" alt="Live emoji suggestions">](https://x.com/riku720720/status/2100705558512963602)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#emoji-suggestions) · [X · 230 likes at collection](https://x.com/riku720720/status/2100705558512963602) · [How it works & evidence](cases/2026-09-18-emoji-suggestions/README.en.md)

**Content updated:** 2026-09-19

### [Voice-and-pointing canvas control](cases/2026-09-18-voice-gesture-canvas/README.en.md)

Use speech and pointing together to say “put that over there” on a canvas.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100729243185324032/img/YNw8njfnSXu-Tbyr.jpg" width="320" alt="Voice-and-pointing canvas control">](https://x.com/jackcheng/status/2100729670991802386)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#voice-gesture-canvas) · [X · 915 likes at collection](https://x.com/jackcheng/status/2100729670991802386) · [How it works & evidence](cases/2026-09-18-voice-gesture-canvas/README.en.md)

**Content updated:** 2026-09-19

### [Probably: semantic judgments as program control](cases/2026-09-18-probably-language/README.en.md)

Write judgments such as “is this email urgent?” into branches, then ask a text model to draft a reply.

[<img src="https://pbs.twimg.com/media/HSdr-ILWUAAN29Y.jpg?name=orig" width="320" alt="Probably: semantic judgments as program control">](https://x.com/southpolesteve/status/2100767781868150938)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#probably-language) · [X · 894 likes at collection](https://x.com/southpolesteve/status/2100767781868150938) · [How it works & evidence](cases/2026-09-18-probably-language/README.en.md)

**Content updated:** 2026-09-19

### [Shell history: semantic command suggestions](cases/2026-09-18-shell-history-suggestions/README.en.md)

Type part of a command or describe an intent to select a suggestion from past commands.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100858390683475969/img/PRKkLSCaQKsfoXRI.jpg" width="320" alt="Shell history: semantic command suggestions">](https://x.com/thorstenball/status/2100858434904109099)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#shell-history-suggestions) · [X · 396 likes at collection](https://x.com/thorstenball/status/2100858434904109099) · [How it works & evidence](cases/2026-09-18-shell-history-suggestions/README.en.md)

**Content updated:** 2026-09-19

### [json-render: assemble interfaces from component choices](cases/2026-09-19-json-render-ui/README.en.md)

Turn interface requests into constrained component layouts, including additions, removals and moves.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101022081810911232/img/3tKdQ3Y2_ZGSg3Q7.jpg" width="320" alt="json-render: assemble interfaces from component choices">](https://x.com/ctatedev/status/2101022101750571357)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#json-render-ui) · [X · 3,341 likes at collection](https://x.com/ctatedev/status/2101022101750571357) · [How it works & evidence](cases/2026-09-19-json-render-ui/README.en.md)

**Content updated:** 2026-09-19

### [CNVS: gate voice commands without a wake word](cases/2026-09-19-cnvs-voice-gate/README.en.md)

Decide whether a spoken utterance is directed at the computer.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100966551826444288/img/i2s52ZeMNTOO-IRD.jpg" width="320" alt="CNVS: gate voice commands without a wake word">](https://x.com/_MaxBlade/status/2100967959879471519)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#cnvs-voice-gate) · [X · 1,053 likes at collection](https://x.com/_MaxBlade/status/2100967959879471519) · [How it works & evidence](cases/2026-09-19-cnvs-voice-gate/README.en.md)

**Content updated:** 2026-09-19

### [Words and colors: visualize 16-color judgments](cases/2026-09-19-color-judgments/README.en.md)

Enter words and visualize the model’s judgments about colors.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100898643117068288/img/p9Jp61lJyiq-UoWK.jpg" width="320" alt="Words and colors: visualize 16-color judgments">](https://x.com/mattdesl/status/2100899669802963060)

[Clearer mechanism](references/2026-09-19-claims-audit.en.md#color-judgments) · [X · 3,441 likes at collection](https://x.com/mattdesl/status/2100899669802963060) · [How it works & evidence](cases/2026-09-19-color-judgments/README.en.md)

**Content updated:** 2026-09-19

</details>

<a id="finance"></a>

<details>
<summary><strong>Explore trading and backtests</strong> · 4</summary>

Some examples test strategies on historical data; others demonstrate execution. Backtests need time-valid data, while execution needs fill and risk checks. Speed and low cost do not establish profit.

[Compare approaches](breakdowns/2026-09-18-finance.en.md)

### [Monad / Kuru trading bot](cases/2026-09-18-trading-bot/README.en.md)

Let Jev choose buy or sell from price information and have code submit the order.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100355999064379392/img/BiAbeDjN57avf2VK.jpg" width="320" alt="Monad / Kuru trading bot">](https://x.com/jarrodwatts/status/2100356151468585346)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#trading-bot) · [X · 4,142 likes at collection](https://x.com/jarrodwatts/status/2100356151468585346) · [How it works & evidence](cases/2026-09-18-trading-bot/README.en.md)

**Content updated:** 2026-09-19

### [AI Hedge Fund: strategy backtesting](cases/2026-09-19-ai-hedge-fund-backtest/README.en.md)

Choose a strategy and stock tickers to run an experiment on historical data.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100959729350561792/img/wc-JtyIBGa_9qgNL.jpg" width="320" alt="AI Hedge Fund: strategy backtesting">](https://x.com/virattt/status/2100959848623899005)

[Claims lack support](references/2026-09-19-claims-audit.en.md#ai-hedge-fund-backtest) · [X · 613 likes at collection](https://x.com/virattt/status/2100959848623899005) · [How it works & evidence](cases/2026-09-19-ai-hedge-fund-backtest/README.en.md)

**Content updated:** 2026-09-19

### [Danish equities: a full-year historical strategy experiment](cases/2026-09-19-danish-stock-backtest/README.en.md)

Experiment with trading decisions on 2025 market data using news and other signals.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100938100272746496/img/8yisuerchTVTcFTn.jpg" width="320" alt="Danish equities: a full-year historical strategy experiment">](https://x.com/tommy_jepsen/status/2100939646653903063)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#danish-stock-backtest) · [X · 269 likes at collection](https://x.com/tommy_jepsen/status/2100939646653903063) · [How it works & evidence](cases/2026-09-19-danish-stock-backtest/README.en.md)

**Content updated:** 2026-09-19

### [Nifty intraday trading: an account demo with a stop-loss report](cases/2026-09-19-nifty-trading/README.en.md)

Demonstrate Jev-connected Nifty trading and report a triggered stop loss.

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100928264831410176/img/VP6eszCSb95ePMo4.jpg" width="320" alt="Nifty intraday trading: an account demo with a stop-loss report">](https://x.com/IndraVahan/status/2100929105382564113)

[Effectiveness unverified](references/2026-09-19-claims-audit.en.md#nifty-trading) · [X · 673 likes at collection](https://x.com/IndraVahan/status/2100929105382564113) · [How it works & evidence](cases/2026-09-19-nifty-trading/README.en.md)

**Content updated:** 2026-09-19

</details>

## About this collection

Original application posts must have at least **200 likes** and relevant media. Updates to one project are merged; independent implementations are grouped for comparison. Counts are snapshots, not credibility scores, and this is not an exhaustive inventory of X.

Exact metric timestamps, technical details and assessment grades are kept in the linked records. Media remains with its original creators; click through if a preview stops working.

[Case index](cases/README.en.md) · [Sources & method](references/README.en.md) · [Pending evidence](inbox/README.en.md) · [Contribute a case](CONTRIBUTING.en.md)
