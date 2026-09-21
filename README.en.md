# Jev: small decisions, surprising applications

[简体中文](README.md) | **English**

Most AI tools are known for writing answers. **TypeSafe Jev specializes in making judgments.**
Give it the current situation and a question or set of choices; it returns a choice, score or yes/no judgment for code to act on.
This guide explores what people have built with it—and what their demonstrations actually establish.

**137 examples · 11 categories** · Sources checked through 2026-09-21

[Browse all applications](#all-apps) · [How Jev works](breakdowns/2026-09-18-how-jev-apps-work.en.md) · [Latest additions](CHANGELOG.en.md)

## Six ideas worth understanding

Start with examples that have clear uses and inspectable mechanisms. Click an image to see its original demo.

### An AI clicks. Who reads the page?

[Browser Use · Ultrafast](cases/2026-09-18-browser-use/README.en.md)

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="480" alt="Browser Use · Ultrafast">](https://x.com/gregpr07/status/2100411066966749359)

Code reads the page and lists controls; Jev picks an action. A text model helps when words need to be entered.

**Keep in mind:** The result depends on the whole system, not Jev alone.

[Clearer mechanism](references/2026-09-20-increment8-audit.en.md#browser-use) · [X · 6,891 likes at collection](https://x.com/gregpr07/status/2100411066966749359) · [How it works & evidence](cases/2026-09-18-browser-use/README.en.md)

**Content updated:** 2026-09-20

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
<summary><strong>Operate browsers and computers</strong> · 13</summary>

These systems connect observation to action. Browser tools often read page structure; desktop tools may use accessibility trees or OCR. Compare task coverage before speed.

[Compare approaches](breakdowns/2026-09-18-browser.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/gregpr07/status/2100411066966749359"><img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="320" alt="Browser Use · Ultrafast"></a></p>
<p><strong><a href="cases/2026-09-18-browser-use/README.en.md">Browser Use · Ultrafast</a></strong><br>Describe a flight search and let the agent click, type and find results on the website.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#browser-use">Clearer mechanism</a> · <a href="cases/2026-09-18-browser-use/README.en.md">Details</a><br><a href="https://x.com/gregpr07/status/2100411066966749359">X · 6,891 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/kylejeong/status/2100622054945095934"><img src="https://pbs.twimg.com/amplify_video_thumb/2100495119065722880/img/7A1mijkU3Z_Zj7PM.jpg" width="320" alt="Stagehand browser control"></a></p>
<p><strong><a href="cases/2026-09-18-stagehand/README.en.md">Stagehand browser control</a></strong><br>Let Jev choose the next browser action and Stagehand carry it out.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#stagehand">Effectiveness unverified</a> · <a href="cases/2026-09-18-stagehand/README.en.md">Details</a><br><a href="https://x.com/kylejeong/status/2100622054945095934">X · 393 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/trycua/status/2100649543079502213"><img src="https://pbs.twimg.com/media/HSb_nmIWYAAkGKa.jpg?name=orig" width="320" alt="Cua · jev-use"></a></p>
<p><strong><a href="cases/2026-09-18-cua-jev-use/README.en.md">Cua · jev-use</a></strong><br>Give Jev a list of allowed browser actions, execute its choice, then check the result.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#cua-jev-use">Claims lack support</a> · <a href="cases/2026-09-18-cua-jev-use/README.en.md">Details</a><br><a href="https://x.com/trycua/status/2100649543079502213">X · 1,162 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/milindlabs/status/2100631847155994852"><img src="https://pbs.twimg.com/amplify_video_thumb/2100629037790183424/img/NR6wQpZiC-xjCEsC.jpg" width="320" alt="TipTour: CoreML + OCR desktop clicks"></a></p>
<p><strong><a href="cases/2026-09-18-coreml-ocr/README.en.md">TipTour: CoreML + OCR desktop clicks</a></strong><br>Recognize buttons and labels on a Mac, then ask Jev which one to click.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#coreml-ocr">Clearer mechanism</a> · <a href="cases/2026-09-18-coreml-ocr/README.en.md">Details</a><br><a href="https://x.com/milindlabs/status/2100631847155994852">X · 564 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/mdlahfir/status/2100359236924637349"><img src="https://pbs.twimg.com/amplify_video_thumb/2100358791321755648/img/t6Bd787flQiGeoJ_.jpg" width="320" alt="OpenCode + agent-desktop"></a></p>
<p><strong><a href="cases/2026-09-18-agent-desktop/README.en.md">OpenCode + agent-desktop</a></strong><br>One model remembers the task while Jev helps choose desktop targets quickly.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#agent-desktop">Effectiveness unverified</a> · <a href="cases/2026-09-18-agent-desktop/README.en.md">Details</a><br><a href="https://x.com/mdlahfir/status/2100359236924637349">X · 870 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/stevekrouse/status/2100321685081559542"><img src="https://pbs.twimg.com/amplify_video_thumb/2100321453455425537/img/hVYy_d3Nuw9XhSwg.jpg" width="320" alt="Kernel browser demo"></a></p>
<p><strong><a href="cases/2026-09-18-kernel-browser/README.en.md">Kernel browser demo</a></strong><br>Try a web demo of Jev controlling a browser.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#kernel-browser">Effectiveness unverified</a> · <a href="cases/2026-09-18-kernel-browser/README.en.md">Details</a><br><a href="https://x.com/stevekrouse/status/2100321685081559542">X · 235 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/moritzkremb/status/2100577979021832365"><img src="https://pbs.twimg.com/amplify_video_thumb/2100577954338373633/img/tbH43kHpUotE3hzK.jpg" width="320" alt="Voice-controlled browser"></a></p>
<p><strong><a href="cases/2026-09-18-voice-browser/README.en.md">Voice-controlled browser</a></strong><br>Speak a command, such as “go back,” and let the browser act.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#voice-browser">Effectiveness unverified</a> · <a href="cases/2026-09-18-voice-browser/README.en.md">Details</a><br><a href="https://x.com/moritzkremb/status/2100577979021832365">X · 1,829 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/Neriousy/status/2100287208166969746"><img src="https://pbs.twimg.com/amplify_video_thumb/2100286679386873857/img/vlw6EBlSVZ9uAoHc.jpg" width="320" alt="OpenCode app testing"></a></p>
<p><strong><a href="cases/2026-09-18-opencode-qa/README.en.md">OpenCode app testing</a></strong><br>Let a coding assistant interact with an app to help check it after development.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#opencode-qa">Effectiveness unverified</a> · <a href="cases/2026-09-18-opencode-qa/README.en.md">Details</a><br><a href="https://x.com/Neriousy/status/2100287208166969746">X · 1,133 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/rafalwilinski/status/2100882207879434359"><img src="https://pbs.twimg.com/amplify_video_thumb/2100881920343105536/img/c1y4THiGwA2GfXGa.jpg" width="320" alt="Runlayer: parallel adversarial browser testing"></a></p>
<p><strong><a href="cases/2026-09-18-runlayer-adversarial-testing/README.en.md">Runlayer: parallel adversarial browser testing</a></strong><br>Run multiple browser sessions to explore how a new release might fail during use.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#runlayer-adversarial-testing">Effectiveness unverified</a> · <a href="cases/2026-09-18-runlayer-adversarial-testing/README.en.md">Details</a><br><a href="https://x.com/rafalwilinski/status/2100882207879434359">X · 820 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/Saccc_c/status/2100864907046768890"><img src="https://pbs.twimg.com/amplify_video_thumb/2100853279089647616/img/H6altwjZQ28_1bfY.jpg" width="320" alt="Sac: Codex + Jev for Mac Calendar"></a></p>
<p><strong><a href="cases/2026-09-18-sac-calendar-computer-use/README.en.md">Sac: Codex + Jev for Mac Calendar</a></strong><br>Add a Jev decision layer to Codex computer use and compare creating a calendar event side by side.</p>
<p><a href="references/2026-09-19-increment7-audit.en.md#sac-calendar-computer-use">Claims lack support</a> · <a href="cases/2026-09-18-sac-calendar-computer-use/README.en.md">Details</a><br><a href="https://x.com/Saccc_c/status/2100864907046768890">X · 217 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/ego_agent/status/2100970015977804008"><img src="https://pbs.twimg.com/amplify_video_thumb/2100969567715790848/img/IXAgXZrtsLGyeYRA.jpg" width="320" alt="ego lite: filter Amazon products"></a></p>
<p><strong><a href="cases/2026-09-19-ego-product-decisions/README.en.md">ego lite: filter Amazon products</a></strong><br>Combine browser tooling and models to filter products on a webpage.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#ego-product-decisions">Effectiveness unverified</a> · <a href="cases/2026-09-19-ego-product-decisions/README.en.md">Details</a><br><a href="https://x.com/ego_agent/status/2100970015977804008">X · 366 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/o_kwasniewski/status/2100966838905585687"><img src="https://pbs.twimg.com/amplify_video_thumb/2100966360192868352/img/8GCSVzX1AYF4caav.jpg" width="320" alt="Tester Army: web and mobile end-to-end testing"></a></p>
<p><strong><a href="cases/2026-09-19-tester-army-e2e/README.en.md">Tester Army: web and mobile end-to-end testing</a></strong><br>Explore agent-driven interface tests in a framework targeting web and mobile.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#tester-army-e2e">Effectiveness unverified</a> · <a href="cases/2026-09-19-tester-army-e2e/README.en.md">Details</a><br><a href="https://x.com/o_kwasniewski/status/2100966838905585687">X · 505 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/sxhivs/status/2101367048223982065"><img src="https://pbs.twimg.com/amplify_video_thumb/2101364408870109184/img/w93wxuq73naZx36A.jpg" width="320" alt="Third Hand / arc-cua: choose actions on a Mac"></a></p>
<p><strong><a href="cases/2026-09-20-third-hand/README.en.md">Third Hand / arc-cua: choose actions on a Mac</a></strong><br>Read controls and screen text, choose actions and enter request- or planner-supplied text.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#third-hand">Clearer mechanism</a> · <a href="cases/2026-09-20-third-hand/README.en.md">Details</a><br><a href="https://x.com/sxhivs/status/2101367048223982065">X · 549 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="routing"></a>

<details>
<summary><strong>Choose an assistant for the task</strong> · 11</summary>

Models, skills and tools serve different needs; Jev helps assign work. Model routing affects cost and quality, while skill routing finds capabilities. The two can work together.

[Compare approaches](breakdowns/2026-09-18-routing.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/eve/status/2100430918762832180"><img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" width="320" alt="Eve criteria-based model router"></a></p>
<p><strong><a href="cases/2026-09-18-eve-router/README.en.md">Eve criteria-based model router</a></strong><br>Choose which model should handle a request before sending it there.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#eve-router">Effectiveness unverified</a> · <a href="cases/2026-09-18-eve-router/README.en.md">Details</a><br><a href="https://x.com/eve/status/2100430918762832180">X · 821 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/ephraimduncan/status/2100454070536351824"><img src="https://pbs.twimg.com/amplify_video_thumb/2100454021852954624/img/hqULLONlXw40573G.jpg" width="320" alt="Request-to-model router"></a></p>
<p><strong><a href="cases/2026-09-18-ephraim-router/README.en.md">Request-to-model router</a></strong><br>Pick a model for each question and send the request automatically.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#ephraim-router">Effectiveness unverified</a> · <a href="cases/2026-09-18-ephraim-router/README.en.md">Details</a><br><a href="https://x.com/ephraimduncan/status/2100454070536351824">X · 1,503 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/kunchenguid/status/2100468943853085061"><img src="https://pbs.twimg.com/media/HSYK_gbagAAqKqr.jpg?name=orig" width="320" alt="Firstmate task dispatch"></a></p>
<p><strong><a href="cases/2026-09-18-firstmate/README.en.md">Firstmate task dispatch</a></strong><br>Choose an AI worker and effort level based on the task and user preferences.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#firstmate">Effectiveness unverified</a> · <a href="cases/2026-09-18-firstmate/README.en.md">Details</a><br><a href="https://x.com/kunchenguid/status/2100468943853085061">X · 1,615 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/mdlahfir/status/2100314182201802811"><img src="https://pbs.twimg.com/amplify_video_thumb/2100314084990414848/img/iePXR9Edae7YVCT_.jpg" width="320" alt="Local coding-agent delegation"></a></p>
<p><strong><a href="cases/2026-09-18-local-delegation/README.en.md">Local coding-agent delegation</a></strong><br>Send routine work, hard questions and long coding tasks to different AI assistants.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#local-delegation">Effectiveness unverified</a> · <a href="cases/2026-09-18-local-delegation/README.en.md">Details</a><br><a href="https://x.com/mdlahfir/status/2100314182201802811">X · 777 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/thekitze/status/2096598298220277856"><img src="https://pbs.twimg.com/media/HRidCpLaMAAqV-7.jpg?name=orig" width="320" alt="Skillbox skill selection"></a></p>
<p><strong><a href="cases/2026-09-18-skillbox/README.en.md">Skillbox skill selection</a></strong><br>Find useful skills for the current task in a large AI skill library.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#skillbox">Effectiveness unverified</a> · <a href="cases/2026-09-18-skillbox/README.en.md">Details</a><br><a href="https://x.com/thekitze/status/2100556122570792999">X · 724 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/CodingGarden/status/2100665210419950031"><img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" width="320" alt="Coding Garden tool assistant"></a></p>
<p><strong><a href="cases/2026-09-18-coding-garden-assistant/README.en.md">Coding Garden tool assistant</a></strong><br>Ask for weather, information or to-do actions and let an assistant call the right tool.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#coding-garden-assistant">Claims lack support</a> · <a href="cases/2026-09-18-coding-garden-assistant/README.en.md">Details</a><br><a href="https://x.com/CodingGarden/status/2100665210419950031">X · 334 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/oviniciuslana/status/2100457622407168509"><img src="https://pbs.twimg.com/media/HSZSqLGXwAA1jSL.jpg?name=orig" width="320" alt="Eve tool-calling agent"></a></p>
<p><strong><a href="cases/2026-09-18-eve-tool-agent/README.en.md">Eve tool-calling agent</a></strong><br>Let Jev choose an agent&#x27;s next tool to reduce selection overhead.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#eve-tool-agent">Effectiveness unverified</a> · <a href="cases/2026-09-18-eve-tool-agent/README.en.md">Details</a><br><a href="https://x.com/oviniciuslana/status/2100457622407168509">X · 1,117 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/ctatedev/status/2100584917092409479"><img src="https://pbs.twimg.com/media/HSbG2YLWkAAPqmU.jpg?name=orig" width="320" alt="ai-cli decision interface"></a></p>
<p><strong><a href="cases/2026-09-18-ai-cli/README.en.md">ai-cli decision interface</a></strong><br>Give terminal-based assistants access to Jev judgments, choices and scores.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#ai-cli">Clearer mechanism</a> · <a href="cases/2026-09-18-ai-cli/README.en.md">Details</a><br><a href="https://x.com/ctatedev/status/2100584917092409479">X · 874 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/yusukebe/status/2100871075743859182"><img src="https://pbs.twimg.com/media/HSfKgItbcAAwVIl.jpg?name=orig" width="320" alt="Hono JevRouter: route requests by meaning"></a></p>
<p><strong><a href="cases/2026-09-18-hono-semantic-router/README.en.md">Hono JevRouter: route requests by meaning</a></strong><br>Choose responses such as HTML or Markdown based on whether a request appears to come from a person or an AI.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#hono-semantic-router">Clearer mechanism</a> · <a href="cases/2026-09-18-hono-semantic-router/README.en.md">Details</a><br><a href="https://x.com/yusukebe/status/2100871075743859182">X · 405 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/antonioleivag/status/2100962426439000484"><img src="https://pbs.twimg.com/media/HSgeLlIX0AAjedL.png?name=orig" width="320" alt="Codex Model Router: choose a model each turn"></a></p>
<p><strong><a href="cases/2026-09-19-codex-model-router/README.en.md">Codex Model Router: choose a model each turn</a></strong><br>Select a model and reasoning settings for each Codex task.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#codex-model-router">Clearer mechanism</a> · <a href="cases/2026-09-19-codex-model-router/README.en.md">Details</a><br><a href="https://x.com/antonioleivag/status/2100962426439000484">X · 437 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/dani_avila7/status/2101176629745561686"><img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" width="320" alt="Claude Code Mod: model and effort routing"></a></p>
<p><strong><a href="cases/2026-09-19-claude-code-jev-router/README.en.md">Claude Code Mod: model and effort routing</a></strong><br>Choose subagent models and adjust reasoning effort in the main conversation.</p>
<p><a href="references/2026-09-19-increment7-audit.en.md#claude-code-jev-router">Clearer mechanism</a> · <a href="cases/2026-09-19-claude-code-jev-router/README.en.md">Details</a><br><a href="https://x.com/dani_avila7/status/2101176629745561686">X · 417 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="review"></a>

<details>
<summary><strong>Check code and risky actions</strong> · 13</summary>

Break a broad review into specific judgments. Code review looks for defects; permission checks govern actions. Both false alarms and missed problems matter, and scores do not replace tests.

[Compare approaches](breakdowns/2026-09-18-review.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/niazmorshed_/status/2100465662867218857"><img src="https://pbs.twimg.com/amplify_video_thumb/2100465308519759872/img/2uIG43VFGvWzku0s.jpg" width="320" alt="jev-review MCP"></a></p>
<p><strong><a href="cases/2026-09-18-jev-review/README.en.md">jev-review MCP</a></strong><br>Score AI-written code and let the coding agent revise it using feedback.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#jev-review">Effectiveness unverified</a> · <a href="cases/2026-09-18-jev-review/README.en.md">Details</a><br><a href="https://x.com/niazmorshed_/status/2100465662867218857">X · 445 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/redp314/status/2100585126652481915"><img src="https://pbs.twimg.com/amplify_video_thumb/2100585029533372416/img/ZcrsntW2yWgtB_HD.jpg" width="320" alt="14-check PR risk review"></a></p>
<p><strong><a href="cases/2026-09-18-typed-pr-review/README.en.md">14-check PR risk review</a></strong><br>Screen code changes for risks such as exposed secrets or removed tests, and escalate uncertainty.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#typed-pr-review">Effectiveness unverified</a> · <a href="cases/2026-09-18-typed-pr-review/README.en.md">Details</a><br><a href="https://x.com/redp314/status/2100585126652481915">X · 1,927 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/thekitze/status/2100616530275029139"><img src="https://pbs.twimg.com/media/HSbjmhQbQAA4G5A.jpg?name=orig" width="320" alt="jev-rabbit natural-language rules"></a></p>
<p><strong><a href="cases/2026-09-18-jev-rabbit/README.en.md">jev-rabbit natural-language rules</a></strong><br>Write code-review rules in plain language and have a bot check changes against them.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#jev-rabbit">Effectiveness unverified</a> · <a href="cases/2026-09-18-jev-rabbit/README.en.md">Details</a><br><a href="https://x.com/thekitze/status/2100616530275029139">X · 327 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/ryanvogel/status/2100068006592123055"><img src="https://pbs.twimg.com/amplify_video_thumb/2100067392223076352/img/BqXd-11SCr3_ff8q.jpg" width="320" alt="Codebase complexity classifier"></a></p>
<p><strong><a href="cases/2026-09-18-codebase-classifier/README.en.md">Codebase complexity classifier</a></strong><br>Explore whether a codebase makes simple things unnecessarily complicated.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#codebase-classifier">Effectiveness unverified</a> · <a href="cases/2026-09-18-codebase-classifier/README.en.md">Details</a><br><a href="https://x.com/ryanvogel/status/2100068006592123055">X · 1,165 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/fazxes/status/2100300097695232164"><img src="https://pbs.twimg.com/media/HSW-E8wWgAAyw9O.jpg?name=orig" width="320" alt="fx auto mode safety classifier"></a></p>
<p><strong><a href="cases/2026-09-18-fx-safety/README.en.md">fx auto mode safety classifier</a></strong><br>Check a command&#x27;s potential risk before an agent executes it automatically.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#fx-safety">Effectiveness unverified</a> · <a href="cases/2026-09-18-fx-safety/README.en.md">Details</a><br><a href="https://x.com/fazxes/status/2100300097695232164">X · 591 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/mayfer/status/2100343452865265747"><img src="https://pbs.twimg.com/media/HSXq9mqbsAAtHoT.jpg?name=orig" width="320" alt="Jailbreak prompt prescreen"></a></p>
<p><strong><a href="cases/2026-09-18-jailbreak-screen/README.en.md">Jailbreak prompt prescreen</a></strong><br>Prescreen prompts for attempts to bypass an AI system&#x27;s rules.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#jailbreak-screen">Effectiveness unverified</a> · <a href="cases/2026-09-18-jailbreak-screen/README.en.md">Details</a><br><a href="https://x.com/mayfer/status/2100343452865265747">X · 264 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/iwasakoya/status/2100471523358474709"><img src="https://pbs.twimg.com/amplify_video_thumb/2100471095627591680/img/jQewHJZ85th2EEv3.jpg" width="320" alt="Document upload checker"></a></p>
<p><strong><a href="cases/2026-09-18-upload-check/README.en.md">Document upload checker</a></strong><br>Before uploading a document, check whether its contents should be shared.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#upload-check">Effectiveness unverified</a> · <a href="cases/2026-09-18-upload-check/README.en.md">Details</a><br><a href="https://x.com/iwasakoya/status/2100471523358474709">X · 284 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/mizchi/status/2100765201385869434"><img src="https://pbs.twimg.com/media/HSdqjcJa8AAGjPE.jpg?name=orig" width="320" alt="Code judgments from ESLint rule descriptions"></a></p>
<p><strong><a href="cases/2026-09-18-eslint-rule-judgments/README.en.md">Code judgments from ESLint rule descriptions</a></strong><br>Give Jev a rule’s text description and ask whether a small code snippet complies.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#eslint-rule-judgments">Effectiveness unverified</a> · <a href="cases/2026-09-18-eslint-rule-judgments/README.en.md">Details</a><br><a href="https://x.com/mizchi/status/2100765201385869434">X · 351 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/OpeOginni/status/2100702649834188855"><img src="https://pbs.twimg.com/amplify_video_thumb/2100701224920129536/img/-vzxHYoZxMjXKOKh.jpg" width="320" alt="OpenCode intent-aware permissions"></a></p>
<p><strong><a href="cases/2026-09-18-opencode-intent-permissions/README.en.md">OpenCode intent-aware permissions</a></strong><br>Check an agent’s actions across tools using policies such as “only access Google.”</p>
<p><a href="references/2026-09-19-claims-audit.en.md#opencode-intent-permissions">Effectiveness unverified</a> · <a href="cases/2026-09-18-opencode-intent-permissions/README.en.md">Details</a><br><a href="https://x.com/OpeOginni/status/2100702649834188855">X · 235 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/markjaquith/status/2100359340087501296"><img src="https://pbs.twimg.com/media/HSX4qrBWcAAA3K4.jpg?name=orig" width="320" alt="Code comments: accuracy and usefulness scores"></a></p>
<p><strong><a href="cases/2026-09-18-code-comment-scoring/README.en.md">Code comments: accuracy and usefulness scores</a></strong><br>Check whether a comment is correct and whether it adds useful information beyond the code.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#code-comment-scoring">Effectiveness unverified</a> · <a href="cases/2026-09-18-code-comment-scoring/README.en.md">Details</a><br><a href="https://x.com/markjaquith/status/2100359340087501296">X · 1,777 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/liorshkiller/status/2100936106615140757"><img src="https://pbs.twimg.com/media/HSgGI1wWQAAY5zl.jpg?name=orig" width="320" alt="Script.it: flag issues before writing review comments"></a></p>
<p><strong><a href="cases/2026-09-19-script-code-review/README.en.md">Script.it: flag issues before writing review comments</a></strong><br>Score a git diff first, then ask a language model for explanations only when issues are flagged.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#script-code-review">Effectiveness unverified</a> · <a href="cases/2026-09-19-script-code-review/README.en.md">Details</a><br><a href="https://x.com/liorshkiller/status/2100936106615140757">X · 202 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/omarsar0/status/2101443311454036477"><img src="https://pbs.twimg.com/amplify_video_thumb/2101443076828925952/img/zVy7_B-F8UmXFdKK.jpg" width="320" alt="Agent goal verifier: check completion after each turn"></a></p>
<p><strong><a href="cases/2026-09-20-agent-goal-verifier/README.en.md">Agent goal verifier: check completion after each turn</a></strong><br>Check whether an agent has actually achieved its goal after every turn.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#agent-goal-verifier">Effectiveness unverified</a> · <a href="cases/2026-09-20-agent-goal-verifier/README.en.md">Details</a><br><a href="https://x.com/omarsar0/status/2101443311454036477">X · 317 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/sethkimmel3/status/2101357768640987302"><img src="https://pbs.twimg.com/amplify_video_thumb/2101357265253212160/img/yMWnsAPk5D4HinBv.jpg" width="320" alt="jev-align: refine decision criteria with human feedback"></a></p>
<p><strong><a href="cases/2026-09-20-jev-align/README.en.md">jev-align: refine decision criteria with human feedback</a></strong><br>Label boundary cases and iteratively improve Jev’s decision instructions.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#jev-align">Clearer mechanism</a> · <a href="cases/2026-09-20-jev-align/README.en.md">Details</a><br><a href="https://x.com/sethkimmel3/status/2101357768640987302">X · 511 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="data"></a>

<details>
<summary><strong>Organize files and information</strong> · 23</summary>

Label emails, identify forms or find relevant files. Classification, retrieval and numerical estimates fail in different ways; one speed ranking cannot compare them fairly.

[Compare approaches](breakdowns/2026-09-18-data.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/nutlope/status/2100426999546184123"><img src="https://pbs.twimg.com/amplify_video_thumb/2100425141947604992/img/AITyHwcOWq1jw-3Z.jpg" width="320" alt="1kpapers research classification"></a></p>
<p><strong><a href="cases/2026-09-18-papers/README.en.md">1kpapers research classification</a></strong><br>Organize over a thousand AI papers so readers can browse them by topic.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#papers">Effectiveness unverified</a> · <a href="cases/2026-09-18-papers/README.en.md">Details</a><br><a href="https://x.com/nutlope/status/2100426999546184123">X · 1,684 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/hamiltonulmer/status/2100370557405667768"><img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" width="320" alt="DuckDB semantic classification"></a></p>
<p><strong><a href="cases/2026-09-18-duckdb/README.en.md">DuckDB semantic classification</a></strong><br>Classify text rows while working with a table.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#duckdb">Effectiveness unverified</a> · <a href="cases/2026-09-18-duckdb/README.en.md">Details</a><br><a href="https://x.com/hamiltonulmer/status/2100370557405667768">X · 1,310 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/rileybrown/status/2100404532119269426"><img src="https://pbs.twimg.com/amplify_video_thumb/2100403183533125632/img/54ZFO-CHvDeC-rw-.jpg" width="320" alt="Batch classification of 500 emails"></a></p>
<p><strong><a href="cases/2026-09-18-email-batch/README.en.md">Batch classification of 500 emails</a></strong><br>Sort a large batch of emails into categories instead of filing them one by one.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#email-batch">Effectiveness unverified</a> · <a href="cases/2026-09-18-email-batch/README.en.md">Details</a><br><a href="https://x.com/rileybrown/status/2100404532119269426">X · 3,161 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/nutlope/status/2100614659690713543"><img src="https://pbs.twimg.com/amplify_video_thumb/2100608348219478016/img/23vFEVMegwLrMa8g.jpg" width="320" alt="Jev + Kimi email fraud detection"></a></p>
<p><strong><a href="cases/2026-09-18-email-fraud/README.en.md">Jev + Kimi email fraud detection</a></strong><br>Screen emails for fraud quickly, then send uncertain cases to a larger model.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#email-fraud">Effectiveness unverified</a> · <a href="cases/2026-09-18-email-fraud/README.en.md">Details</a><br><a href="https://x.com/nutlope/status/2100614659690713543">X · 542 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/jlongster/status/2100179852053639236"><img src="https://pbs.twimg.com/media/HSVWcZ9WcAAcwPe.jpg?name=orig" width="320" alt="Bank transaction payee cleanup"></a></p>
<p><strong><a href="cases/2026-09-18-bank-payee/README.en.md">Bank transaction payee cleanup</a></strong><br>Turn messy bank transaction descriptions into recognizable merchant names.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#bank-payee">Effectiveness unverified</a> · <a href="cases/2026-09-18-bank-payee/README.en.md">Details</a><br><a href="https://x.com/jlongster/status/2100179852053639236">X · 633 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/ku_suke/status/2100392430805856469"><img src="https://pbs.twimg.com/media/HSYXuW5aoAAghbD.jpg?name=orig" width="320" alt="Japanese support escalation intent"></a></p>
<p><strong><a href="cases/2026-09-18-support-intent/README.en.md">Japanese support escalation intent</a></strong><br>Detect whether a Japanese support message asks for a human or mentions repeated contact.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#support-intent">Clearer mechanism</a> · <a href="cases/2026-09-18-support-intent/README.en.md">Details</a><br><a href="https://x.com/ku_suke/status/2100392430805856469">X · 351 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/dabit3/status/2100780008193020049"><img src="https://pbs.twimg.com/amplify_video_thumb/2100779722447667200/img/gvsEg2-3oD6FRZhc.jpg" width="320" alt="Intent-driven spreadsheet ratings"></a></p>
<p><strong><a href="cases/2026-09-18-predictive-spreadsheet/README.en.md">Intent-driven spreadsheet ratings</a></strong><br>Name a column “Urgency” and have the text in each row receive a corresponding rating.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#predictive-spreadsheet">Effectiveness unverified</a> · <a href="cases/2026-09-18-predictive-spreadsheet/README.en.md">Details</a><br><a href="https://x.com/dabit3/status/2100780008193020049">X · 337 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/usutaku_channel/status/2100829343954173965"><img src="https://pbs.twimg.com/amplify_video_thumb/2100829070514864128/img/V3ix1we5Euhs8DsY.jpg" width="320" alt="Email classification: four-model speed comparison"></a></p>
<p><strong><a href="cases/2026-09-18-email-speed-race/README.en.md">Email classification: four-model speed comparison</a></strong><br>Classify a set of emails with four models and compare progress and elapsed time on one screen.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#email-speed-race">Effectiveness unverified</a> · <a href="cases/2026-09-18-email-speed-race/README.en.md">Details</a><br><a href="https://x.com/usutaku_channel/status/2100829343954173965">X · 445 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/thekitze/status/2100857642566758849"><img src="https://pbs.twimg.com/amplify_video_thumb/2100857416984477696/img/RAMEV-YddA05BR1X.jpg" width="320" alt="Calorie Notebook: text-based food logging"></a></p>
<p><strong><a href="cases/2026-09-18-calorie-notebook/README.en.md">Calorie Notebook: text-based food logging</a></strong><br>Write down what you ate and receive quick calorie, nutrient and total values in the interface.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#calorie-notebook">Effectiveness unverified</a> · <a href="cases/2026-09-18-calorie-notebook/README.en.md">Details</a><br><a href="https://x.com/thekitze/status/2100857642566758849">X · 326 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/levie/status/2101007708044574906"><img src="https://pbs.twimg.com/amplify_video_thumb/2100999115949953024/img/6D1_NvmSfMLGDstw.jpg" width="320" alt="Box: triage and file incident reports"></a></p>
<p><strong><a href="cases/2026-09-19-box-incident-triage/README.en.md">Box: triage and file incident reports</a></strong><br>Read incident reports, judge impact and severity, and route them to handling folders.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#box-incident-triage">Effectiveness unverified</a> · <a href="cases/2026-09-19-box-incident-triage/README.en.md">Details</a><br><a href="https://x.com/levie/status/2101007708044574906">X · 317 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/nikunj/status/2101006585481073093"><img src="https://pbs.twimg.com/amplify_video_thumb/2101005796603809792/img/19SyyiWW5wotfFfW.jpg" width="320" alt="NoSugarForKids: multi-criterion snack scoring"></a></p>
<p><strong><a href="cases/2026-09-19-snack-scoring/README.en.md">NoSugarForKids: multi-criterion snack scoring</a></strong><br>Score children’s snacks in batches to organize a product catalog.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#snack-scoring">Effectiveness unverified</a> · <a href="cases/2026-09-19-snack-scoring/README.en.md">Details</a><br><a href="https://x.com/nikunj/status/2101006585481073093">X · 312 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/nedwize/status/2100973868324417852"><img src="https://pbs.twimg.com/amplify_video_thumb/2100973360989773825/img/yMtL6CxrKMVXQEHV.jpg" width="320" alt="Tax Doc Classifier: label tax PDF pages"></a></p>
<p><strong><a href="cases/2026-09-19-tax-doc-classifier/README.en.md">Tax Doc Classifier: label tax PDF pages</a></strong><br>Identify which tax form each PDF page belongs to for downstream organization.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#tax-doc-classifier">Clearer mechanism</a> · <a href="cases/2026-09-19-tax-doc-classifier/README.en.md">Details</a><br><a href="https://x.com/nedwize/status/2100973868324417852">X · 1,506 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/dabit3/status/2100960281769738433"><img src="https://pbs.twimg.com/amplify_video_thumb/2100959260616151040/img/nb1GFqB_cwNesugB.jpg" width="320" alt="Gmail: search by intent"></a></p>
<p><strong><a href="cases/2026-09-19-gmail-intent-search/README.en.md">Gmail: search by intent</a></strong><br>Filter relevant messages from a natural-language request instead of relying only on keywords.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#gmail-intent-search">Effectiveness unverified</a> · <a href="cases/2026-09-19-gmail-intent-search/README.en.md">Details</a><br><a href="https://x.com/dabit3/status/2100960281769738433">X · 574 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/fayazara/status/2100953838891192789"><img src="https://pbs.twimg.com/amplify_video_thumb/2100953271238320128/img/vzUjAo15Bg8tVa_q.jpg" width="320" alt="OCR + Jev: organize images"></a></p>
<p><strong><a href="cases/2026-09-19-ocr-image-organizer/README.en.md">OCR + Jev: organize images</a></strong><br>Read text from images, then categorize them by content.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#ocr-image-organizer">Effectiveness unverified</a> · <a href="cases/2026-09-19-ocr-image-organizer/README.en.md">Details</a><br><a href="https://x.com/fayazara/status/2100953838891192789">X · 246 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/marcelpociot/status/2100906882365788167"><img src="https://pbs.twimg.com/amplify_video_thumb/2100906588626173952/img/1KnNI3B3aUJEwFvI.jpg" width="320" alt="macOS Downloads: organize files by rules"></a></p>
<p><strong><a href="cases/2026-09-19-downloads-organizer/README.en.md">macOS Downloads: organize files by rules</a></strong><br>Watch Downloads and move matching files to destinations defined by custom rules.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#downloads-organizer">Effectiveness unverified</a> · <a href="cases/2026-09-19-downloads-organizer/README.en.md">Details</a><br><a href="https://x.com/marcelpociot/status/2100906882365788167">X · 889 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/masa_okamura108/status/2101206603240477030"><img src="https://pbs.twimg.com/amplify_video_thumb/2101206578284380160/img/WUIj3LeQ4Nrch8yD.jpg" width="320" alt="Synthetic interview notes: batch classification and scoring"></a></p>
<p><strong><a href="cases/2026-09-19-synthetic-interview-classifier/README.en.md">Synthetic interview notes: batch classification and scoring</a></strong><br>Sort 100 fictional interview records into advance, hold or decline and assign component scores.</p>
<p><a href="references/2026-09-19-increment7-audit.en.md#synthetic-interview-classifier">Effectiveness unverified</a> · <a href="cases/2026-09-19-synthetic-interview-classifier/README.en.md">Details</a><br><a href="https://x.com/masa_okamura108/status/2101206603240477030">X · 278 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/venturetwins/status/2101393861667115437"><img src="https://pbs.twimg.com/amplify_video_thumb/2101393799234871296/img/oBhawR0JczN9WT1k.jpg" width="320" alt="Goodreads: predict personal five-star books"></a></p>
<p><strong><a href="cases/2026-09-20-goodreads-taste-prediction/README.en.md">Goodreads: predict personal five-star books</a></strong><br>Use past ratings to predict which books one reader might award five stars.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#goodreads-taste-prediction">Effectiveness unverified</a> · <a href="cases/2026-09-20-goodreads-taste-prediction/README.en.md">Details</a><br><a href="https://x.com/venturetwins/status/2101393861667115437">X · 238 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/venturetwins/status/2101341075684434245"><img src="https://pbs.twimg.com/amplify_video_thumb/2101339712464326656/img/A8yq5IoXQuhJAi32.jpg" width="320" alt="Zillow listings: natural-language filters"></a></p>
<p><strong><a href="cases/2026-09-20-zillow-semantic-filters/README.en.md">Zillow listings: natural-language filters</a></strong><br>Organize listings by architecture, renovation status and other nonstandard filters.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#zillow-semantic-filters">Effectiveness unverified</a> · <a href="cases/2026-09-20-zillow-semantic-filters/README.en.md">Details</a><br><a href="https://x.com/venturetwins/status/2101341075684434245">X · 527 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/brian_lovin/status/2101321554130809156"><img src="https://pbs.twimg.com/amplify_video_thumb/2101321495351799809/img/4KIZYG3NZtHjWnZB.jpg" width="320" alt="Shiori: automatic bookmark tags"></a></p>
<p><strong><a href="cases/2026-09-20-shiori-link-tagging/README.en.md">Shiori: automatic bookmark tags</a></strong><br>Categorize saved links so they are easier to find by topic later.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#shiori-link-tagging">Effectiveness unverified</a> · <a href="cases/2026-09-20-shiori-link-tagging/README.en.md">Details</a><br><a href="https://x.com/brian_lovin/status/2101321554130809156">X · 327 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/OpenRouter/status/2101412965765529853"><img src="https://pbs.twimg.com/media/HSm39ISbsAAEPfg.png?name=orig" width="320" alt="Ori Eval: compare 30-way request classification"></a></p>
<p><strong><a href="cases/2026-09-20-ori-task-classification/README.en.md">Ori Eval: compare 30-way request classification</a></strong><br>Classify requests into 30 task types and compare five models on speed, cost and correctness.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#ori-task-classification">Effectiveness unverified</a> · <a href="cases/2026-09-20-ori-task-classification/README.en.md">Details</a><br><a href="https://x.com/OpenRouter/status/2101412965765529853">X · 329 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/jerryjliu0/status/2101738281046294552"><img src="https://pbs.twimg.com/amplify_video_thumb/2101738161546391552/img/aTJ-mBG_YeF98yMQ.jpg" width="320" alt="DocJev: classify documents and split bundles"></a></p>
<p><strong><a href="cases/2026-09-21-docjev/README.en.md">DocJev: classify documents and split bundles</a></strong><br>Identify document types and boundaries inside a combined PDF.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#docjev">Clearer mechanism</a> · <a href="cases/2026-09-21-docjev/README.en.md">Details</a><br><a href="https://x.com/jerryjliu0/status/2101738281046294552">X · 695 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/oguzhankayancom/status/2101667801274478707"><img src="https://pbs.twimg.com/amplify_video_thumb/2101667558847856640/img/ueDe_Ess6ATvRcz8.jpg" width="320" alt="Reddit Radar MCP: filter discussions by your criteria"></a></p>
<p><strong><a href="cases/2026-09-21-reddit-radar-mcp/README.en.md">Reddit Radar MCP: filter discussions by your criteria</a></strong><br>Find Reddit discussions matching custom criteria from Claude Code or Codex.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#reddit-radar-mcp">Effectiveness unverified</a> · <a href="cases/2026-09-21-reddit-radar-mcp/README.en.md">Details</a><br><a href="https://x.com/oguzhankayancom/status/2101667801274478707">X · 295 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/omarsar0/status/2101696753749655863"><img src="https://pbs.twimg.com/amplify_video_thumb/2101692387160358912/img/2uCGZ2BKwoQEFC1k.jpg" width="320" alt="Jev Field Notes: curate Jev examples with Jev"></a></p>
<p><strong><a href="cases/2026-09-21-jev-field-notes-curation/README.en.md">Jev Field Notes: curate Jev examples with Jev</a></strong><br>Select X application demos for a community collection.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#jev-field-notes-curation">Effectiveness unverified</a> · <a href="cases/2026-09-21-jev-field-notes-curation/README.en.md">Details</a><br><a href="https://x.com/omarsar0/status/2101696753749655863">X · 298 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="content"></a>

<details>
<summary><strong>Analyze content and reach</strong> · 11</summary>

Some tools label ads; others connect articles or predict reach. Describing content differs from predicting the future, and a high score does not guarantee traffic or citations.

[Compare approaches](breakdowns/2026-09-18-content.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/rileybrown/status/2100425868053008758"><img src="https://pbs.twimg.com/amplify_video_thumb/2100424897491070976/img/kKnsb68jNUZZzSBi.jpg" width="320" alt="Live post-potential analyzer"></a></p>
<p><strong><a href="cases/2026-09-18-live-viral/README.en.md">Live post-potential analyzer</a></strong><br>Get feedback on a post&#x27;s type and potential reach as you write.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#live-viral">Effectiveness unverified</a> · <a href="cases/2026-09-18-live-viral/README.en.md">Details</a><br><a href="https://x.com/rileybrown/status/2100425868053008758">X · 830 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/robj3d3/status/2100631889585606959"><img src="https://pbs.twimg.com/media/HSbxP15bMAA1LaU.jpg?name=orig" width="320" alt="Viral-post classifier"></a></p>
<p><strong><a href="cases/2026-09-18-viral-classifier/README.en.md">Viral-post classifier</a></strong><br>Try to identify posts that may attract more attention.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#viral-classifier">Claims lack support</a> · <a href="cases/2026-09-18-viral-classifier/README.en.md">Details</a><br><a href="https://x.com/robj3d3/status/2100631889585606959">X · 387 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/leojrr/status/2100470174130250127"><img src="https://pbs.twimg.com/amplify_video_thumb/2100467692117295104/img/01ZWSKAA75eSiFlc.jpg" width="320" alt="X reach-score simulator"></a></p>
<p><strong><a href="cases/2026-09-18-x-algorithm-sim/README.en.md">X reach-score simulator</a></strong><br>Simulate reach scores to compare different ways of writing a post.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#x-algorithm-sim">Claims lack support</a> · <a href="cases/2026-09-18-x-algorithm-sim/README.en.md">Details</a><br><a href="https://x.com/leojrr/status/2100470174130250127">X · 877 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/AM09_21/status/2100430480642642395"><img src="https://pbs.twimg.com/media/HSYtFVgaoAIPpi5.jpg?name=orig" width="320" alt="Bookmark-percentile prediction"></a></p>
<p><strong><a href="cases/2026-09-18-bookmark-prediction/README.en.md">Bookmark-percentile prediction</a></strong><br>Predict whether a post ranks in the top quarter for bookmarks among nearby dates.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#bookmark-prediction">Effectiveness unverified</a> · <a href="cases/2026-09-18-bookmark-prediction/README.en.md">Details</a><br><a href="https://x.com/AM09_21/status/2100430480642642395">X · 287 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/iannuttall/status/2100668908227162567"><img src="https://pbs.twimg.com/amplify_video_thumb/2100668725737213952/img/m210oIkCyuGX5Dqr.jpg" width="320" alt="Analysis of 3,282 historical posts"></a></p>
<p><strong><a href="cases/2026-09-18-post-analytics/README.en.md">Analysis of 3,282 historical posts</a></strong><br>Review thousands of past posts to see which topics and styles performed well.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#post-analytics">Effectiveness unverified</a> · <a href="cases/2026-09-18-post-analytics/README.en.md">Details</a><br><a href="https://x.com/iannuttall/status/2100668908227162567">X · 262 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/TheMattBerman/status/2100654891756589230"><img src="https://pbs.twimg.com/amplify_video_thumb/2100654321792684032/img/cXvU50KmCe6QFu86.jpg" width="320" alt="StealAds ad-analysis preview"></a></p>
<p><strong><a href="cases/2026-09-18-ad-analysis/README.en.md">StealAds ad-analysis preview</a></strong><br>Break many ads into hooks, offers and calls to action for creative research.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#ad-analysis">Effectiveness unverified</a> · <a href="cases/2026-09-18-ad-analysis/README.en.md">Details</a><br><a href="https://x.com/TheMattBerman/status/2100654891756589230">X · 1,678 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/chetaslua/status/2100473581251748216"><img src="https://pbs.twimg.com/amplify_video_thumb/2100473445868003328/img/1ukjahQYLgbIEmyI.jpg" width="320" alt="JevMeter speech-analysis dashboard"></a></p>
<p><strong><a href="cases/2026-09-18-jevmeter/README.en.md">JevMeter speech-analysis dashboard</a></strong><br>Score sentences in debates or interviews to examine speech patterns and content features.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#jevmeter">Claims lack support</a> · <a href="cases/2026-09-18-jevmeter/README.en.md">Details</a><br><a href="https://x.com/chetaslua/status/2100473581251748216">X · 1,017 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/borjafat/status/2101018783976722479"><img src="https://pbs.twimg.com/amplify_video_thumb/2101018477087592448/img/9YlAHKLLo_h6rgtK.jpg" width="320" alt="SEO internal links: match existing text to relevant pages"></a></p>
<p><strong><a href="cases/2026-09-19-seo-internal-links/README.en.md">SEO internal links: match existing text to relevant pages</a></strong><br>Scan site articles and suggest relevant internal links using text already present.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#seo-internal-links">Effectiveness unverified</a> · <a href="cases/2026-09-19-seo-internal-links/README.en.md">Details</a><br><a href="https://x.com/borjafat/status/2101018783976722479">X · 721 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/OriSilver/status/2100941251478458871"><img src="https://pbs.twimg.com/amplify_video_thumb/2100940464870301696/img/g-uzVt-FDP21an26.jpg" width="320" alt="MaxFusion: classify advertising creatives"></a></p>
<p><strong><a href="cases/2026-09-19-maxfusion-ad-classifier/README.en.md">MaxFusion: classify advertising creatives</a></strong><br>Label ads by style and customer-journey stage for account-level analysis.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#maxfusion-ad-classifier">Effectiveness unverified</a> · <a href="cases/2026-09-19-maxfusion-ad-classifier/README.en.md">Details</a><br><a href="https://x.com/OriSilver/status/2100941251478458871">X · 320 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/irabukht/status/2101090579127951694"><img src="https://pbs.twimg.com/amplify_video_thumb/2101089408099516416/img/Smzn-jtE8prvdY90.jpg" width="320" alt="Ryze AI: SEO/GEO audits and fixes"></a></p>
<p><strong><a href="cases/2026-09-19-ryze-seo-geo/README.en.md">Ryze AI: SEO/GEO audits and fixes</a></strong><br>Add Jev to website visibility audits, analyzing pages and AI-search citations to guide fixes.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#ryze-seo-geo">Claims lack support</a> · <a href="cases/2026-09-19-ryze-seo-geo/README.en.md">Details</a><br><a href="https://x.com/irabukht/status/2101090579127951694">X · 790 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/unsu0707/status/2101249913099375058"><img src="https://pbs.twimg.com/amplify_video_thumb/2101248847444078592/img/mGFrlyfBgnJWT-p8.jpg" width="320" alt="X draft check: flag overhyped wording before posting"></a></p>
<p><strong><a href="cases/2026-09-20-x-draft-hype-check/README.en.md">X draft check: flag overhyped wording before posting</a></strong><br>Warn when a draft sounds like exaggerated marketing or a sales pitch.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#x-draft-hype-check">Effectiveness unverified</a> · <a href="cases/2026-09-20-x-draft-hype-check/README.en.md">Details</a><br><a href="https://x.com/unsu0707/status/2101249913099375058">X · 446 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="filter"></a>

<details>
<summary><strong>Filter unwanted content</strong> · 5</summary>

Turn preferences into filtering rules. Feed tools judge posts, page cleaners judge elements, and video tools locate time segments. Each needs a way to correct mistakes.

[Compare approaches](breakdowns/2026-09-18-filter.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/marcelpociot/status/2100520134481735729"><img src="https://pbs.twimg.com/amplify_video_thumb/2100519256425140224/img/-A44e4qCo8mVP8ws.jpg" width="320" alt="Natural-language X content filter"></a></p>
<p><strong><a href="cases/2026-09-18-x-filter/README.en.md">Natural-language X content filter</a></strong><br>Tell the browser in your own words which X posts you would rather not see.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#x-filter">Effectiveness unverified</a> · <a href="cases/2026-09-18-x-filter/README.en.md">Details</a><br><a href="https://x.com/marcelpociot/status/2100520134481735729">X · 950 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/thekitze/status/2100595129874817340"><img src="https://pbs.twimg.com/amplify_video_thumb/2100595059041370112/img/cyfF5qMMKBPQTMAG.jpg" width="320" alt="Unclutter page cleanup"></a></p>
<p><strong><a href="cases/2026-09-18-unclutter/README.en.md">Unclutter page cleanup</a></strong><br>Clear ads, promotional dialogs and similar clutter to make webpages easier to read.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#unclutter">Effectiveness unverified</a> · <a href="cases/2026-09-18-unclutter/README.en.md">Details</a><br><a href="https://x.com/thekitze/status/2100595129874817340">X · 497 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/tdinh_me/status/2100793777103466615"><img src="https://pbs.twimg.com/amplify_video_thumb/2100792834526007296/img/8AFbjqEeZrJUEHid.jpg" width="320" alt="YouTube sponsor-segment skipping"></a></p>
<p><strong><a href="cases/2026-09-18-youtube-sponsor-skip/README.en.md">YouTube sponsor-segment skipping</a></strong><br>Detect spoken sponsor segments while watching YouTube and jump past them.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#youtube-sponsor-skip">Clearer mechanism</a> · <a href="cases/2026-09-18-youtube-sponsor-skip/README.en.md">Details</a><br><a href="https://x.com/tdinh_me/status/2100793777103466615">X · 238 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/iannuttall/status/2100888635943883244"><img src="https://pbs.twimg.com/amplify_video_thumb/2100888448118759424/img/MafhEAfm3BlPst1X.jpg" width="320" alt="X reply cleanup: flag low-value comments"></a></p>
<p><strong><a href="cases/2026-09-19-x-reply-cleanup/README.en.md">X reply cleanup: flag low-value comments</a></strong><br>Identify suspected low-value replies to help clean up a post’s discussion.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#x-reply-cleanup">Effectiveness unverified</a> · <a href="cases/2026-09-19-x-reply-cleanup/README.en.md">Details</a><br><a href="https://x.com/iannuttall/status/2100888635943883244">X · 223 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114"><img src="https://pbs.twimg.com/amplify_video_thumb/2101576307352203264/img/THdpZUHOSRsSoTVr.jpg" width="320" alt="Needle: find webpage passages by meaning"></a></p>
<p><strong><a href="cases/2026-09-21-needle-semantic-find/README.en.md">Needle: find webpage passages by meaning</a></strong><br>Use your own words to find relevant sentences without remembering exact keywords.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#needle-semantic-find">Clearer mechanism</a> · <a href="cases/2026-09-21-needle-semantic-find/README.en.md">Details</a><br><a href="https://x.com/Saboo_Shubham_/status/2101576462042366114">X · 1,658 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="memory"></a>

<details>
<summary><strong>Help AI keep useful context</strong> · 3</summary>

As conversations grow, what should stay? These tools decide when to compact, what to keep or what to retrieve. Fewer tokens are useful only if later work still succeeds.

[Compare approaches](breakdowns/2026-09-18-memory.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/tamarajtran/status/2100694549362553153"><img src="https://pbs.twimg.com/amplify_video_thumb/2100694537672998912/img/OF8vottg6-45ZgNl.jpg" width="320" alt="Tool-history context compaction"></a></p>
<p><strong><a href="cases/2026-09-18-context-compaction/README.en.md">Tool-history context compaction</a></strong><br>Trim an AI assistant&#x27;s work history to retain what matters now.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#context-compaction">Claims lack support</a> · <a href="cases/2026-09-18-context-compaction/README.en.md">Details</a><br><a href="https://x.com/tamarajtran/status/2100694549362553153">X · 1,646 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/moritzkremb/status/2100566009312940457"><img src="https://pbs.twimg.com/amplify_video_thumb/2100565973376061440/img/jeTib61RNpwXn853.jpg" width="320" alt="Memory retrieval filtering"></a></p>
<p><strong><a href="cases/2026-09-18-memory-retrieval/README.en.md">Memory retrieval filtering</a></strong><br>Filter an AI memory store so the next model sees relevant material.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#memory-retrieval">Effectiveness unverified</a> · <a href="cases/2026-09-18-memory-retrieval/README.en.md">Details</a><br><a href="https://x.com/moritzkremb/status/2100566009312940457">X · 335 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/kunchenguid/status/2101032677940117875"><img src="https://pbs.twimg.com/media/HShbIHcbcAAJvsR.jpg?name=orig" width="320" alt="Compact Adviser: choose when to compact"></a></p>
<p><strong><a href="cases/2026-09-19-compact-adviser/README.en.md">Compact Adviser: choose when to compact</a></strong><br>Suggest when a coding conversation has reached a suitable point for context compaction.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#compact-adviser">Effectiveness unverified</a> · <a href="cases/2026-09-19-compact-adviser/README.en.md">Details</a><br><a href="https://x.com/kunchenguid/status/2101032677940117875">X · 242 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="games"></a>

<details>
<summary><strong>Play games and solve puzzles</strong> · 20</summary>

Turn game state into choices and watch small decisions add up. Some systems only select actions; others use planners or predefined solutions. Smooth footage does not establish strong play.

[Compare approaches](breakdowns/2026-09-18-games.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/CompleteSkeptic/status/2099925687465570372"><img src="https://pbs.twimg.com/amplify_video_thumb/2099924592534183936/img/hBGk8j8MRxBgPyg9.jpg" width="320" alt="Official Doom demo"></a></p>
<p><strong><a href="cases/2026-09-18-doom/README.en.md">Official Doom demo</a></strong><br>Use Jev to choose game actions repeatedly in a Doom demo.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#doom">Effectiveness unverified</a> · <a href="cases/2026-09-18-doom/README.en.md">Details</a><br><a href="https://x.com/CompleteSkeptic/status/2099925687465570372">X · 4,585 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/faadilhshaik/status/2100086301894881578"><img src="https://pbs.twimg.com/amplify_video_thumb/2100085174826647552/img/6YMRQKKZYBPsW2oo.jpg" width="320" alt="Super Mario · @faadilhshaik"></a></p>
<p><strong><a href="cases/2026-09-18-mario-faadhil/README.en.md">Super Mario · @faadilhshaik</a></strong><br>Let Jev control Super Mario to demonstrate fast action selection.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#mario-faadhil">Effectiveness unverified</a> · <a href="cases/2026-09-18-mario-faadhil/README.en.md">Details</a><br><a href="https://x.com/faadilhshaik/status/2100086301894881578">X · 2,686 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/karaage0703/status/2100569924238471355"><img src="https://pbs.twimg.com/amplify_video_thumb/2100567975317454849/img/UjFbLkeMH5RdOrlS.jpg" width="320" alt="Super Mario · Jev / Qwen comparison"></a></p>
<p><strong><a href="cases/2026-09-18-mario-comparison/README.en.md">Super Mario · Jev / Qwen comparison</a></strong><br>Give Jev and Qwen the same Mario information and compare action choices.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#mario-comparison">Clearer mechanism</a> · <a href="cases/2026-09-18-mario-comparison/README.en.md">Details</a><br><a href="https://x.com/karaage0703/status/2100569924238471355">X · 284 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/shantanugoel/status/2100455295801827769"><img src="https://pbs.twimg.com/amplify_video_thumb/2100454863335501825/img/RbCmluMnOGM4rHPb.jpg" width="320" alt="Super Mario · World 1-1"></a></p>
<p><strong><a href="cases/2026-09-18-mario-ppo/README.en.md">Super Mario · World 1-1</a></strong><br>Demonstrate Jev on Mario&#x27;s first level alongside the author&#x27;s earlier game-AI training experience.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#mario-ppo">Effectiveness unverified</a> · <a href="cases/2026-09-18-mario-ppo/README.en.md">Details</a><br><a href="https://x.com/shantanugoel/status/2100455295801827769">X · 248 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/daniel_mac8/status/2100335929273524541"><img src="https://pbs.twimg.com/amplify_video_thumb/2100335842451492864/img/gC9HxZoXRIgMLKrW.jpg" width="320" alt="Astra + Jev Pac-Man"></a></p>
<p><strong><a href="cases/2026-09-18-pacman/README.en.md">Astra + Jev Pac-Man</a></strong><br>One model plans while Jev chooses quick local moves to play Pac-Man.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#pacman">Effectiveness unverified</a> · <a href="cases/2026-09-18-pacman/README.en.md">Details</a><br><a href="https://x.com/daniel_mac8/status/2100335929273524541">X · 860 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/chenchengpro/status/2100516953496670430"><img src="https://pbs.twimg.com/amplify_video_thumb/2100516335155646464/img/pow4ZDKeRwkBVSvy.jpg" width="320" alt="Step-by-step Snake"></a></p>
<p><strong><a href="cases/2026-09-18-snake/README.en.md">Step-by-step Snake</a></strong><br>Ask Jev for the next move at every step of Snake.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#snake">Effectiveness unverified</a> · <a href="cases/2026-09-18-snake/README.en.md">Details</a><br><a href="https://x.com/chenchengpro/status/2100516953496670430">X · 204 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/marcus_lowe/status/2100315518930661861"><img src="https://pbs.twimg.com/amplify_video_thumb/2100315393860730880/img/u0iH2SHQny2hkd4Q.jpg" width="320" alt="Tetris"></a></p>
<p><strong><a href="cases/2026-09-18-tetris/README.en.md">Tetris</a></strong><br>Let Jev make Tetris decisions and observe how blocks are placed.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#tetris">Effectiveness unverified</a> · <a href="cases/2026-09-18-tetris/README.en.md">Details</a><br><a href="https://x.com/marcus_lowe/status/2100315518930661861">X · 956 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/0xBOYD/status/2100539883836018697"><img src="https://pbs.twimg.com/amplify_video_thumb/2100539819172544512/img/0EZ7yznRwL7qi4K8.jpg" width="320" alt="Jev Plays Pokémon"></a></p>
<p><strong><a href="cases/2026-09-18-pokemon/README.en.md">Jev Plays Pokémon</a></strong><br>Let Jev play Pokémon over time and track progress and decision costs.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#pokemon">Effectiveness unverified</a> · <a href="cases/2026-09-18-pokemon/README.en.md">Details</a><br><a href="https://x.com/0xBOYD/status/2100539883836018697">X · 220 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/coolish/status/2100570517954838897"><img src="https://pbs.twimg.com/amplify_video_thumb/2100569632482746369/img/TPuOBiHYCWUWxNOc.jpg" width="320" alt="Slay the Spire 2 agent"></a></p>
<p><strong><a href="cases/2026-09-18-slay-spire/README.en.md">Slay the Spire 2 agent</a></strong><br>Use Jev to choose card-game actions with less waiting between decisions.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#slay-spire">Effectiveness unverified</a> · <a href="cases/2026-09-18-slay-spire/README.en.md">Details</a><br><a href="https://x.com/coolish/status/2100570517954838897">X · 598 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/aimlapi/status/2100372930282573876"><img src="https://pbs.twimg.com/amplify_video_thumb/2100371773275406336/img/NmHPy0pAprSsC6Gi.jpg" width="320" alt="5+0 blitz chess"></a></p>
<p><strong><a href="cases/2026-09-18-chess/README.en.md">5+0 blitz chess</a></strong><br>Compare model playing strength and decision speed in timed chess.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#chess">Clearer mechanism</a> · <a href="cases/2026-09-18-chess/README.en.md">Details</a><br><a href="https://x.com/aimlapi/status/2100372930282573876">X · 1,985 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/_MaxBlade/status/2100634359099232678"><img src="https://pbs.twimg.com/amplify_video_thumb/2100633400717565952/img/KlytLNSLCQA-yY2E.jpg" width="320" alt="Parallel Subway Surfers demo"></a></p>
<p><strong><a href="cases/2026-09-18-subway-runners/README.en.md">Parallel Subway Surfers demo</a></strong><br>Demonstrate Jev controlling multiple runner-style games at once.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#subway-runners">Effectiveness unverified</a> · <a href="cases/2026-09-18-subway-runners/README.en.md">Details</a><br><a href="https://x.com/_MaxBlade/status/2100634359099232678">X · 1,474 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/redp314/status/2100489858951073858"><img src="https://pbs.twimg.com/amplify_video_thumb/2100479486382809088/img/r6daGpDnvsCr3LyL.jpg" width="320" alt="Staged Rubik&#x27;s Cube solver"></a></p>
<p><strong><a href="cases/2026-09-18-rubiks-cube/README.en.md">Staged Rubik&#x27;s Cube solver</a></strong><br>Code knows the cube-solving methods; Jev identifies which case to apply.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#rubiks-cube">Clearer mechanism</a> · <a href="cases/2026-09-18-rubiks-cube/README.en.md">Details</a><br><a href="https://x.com/redp314/status/2100489858951073858">X · 494 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/shreypandya/status/2100606445758898287"><img src="https://pbs.twimg.com/amplify_video_thumb/2100605130869784576/img/gdGysXaHMdzFOU8W.jpg" width="320" alt="Mario Kart 64"></a></p>
<p><strong><a href="cases/2026-09-18-mario-kart/README.en.md">Mario Kart 64</a></strong><br>Watch Jev control Mario Kart in a continuous-driving demo.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#mario-kart">Claims lack support</a> · <a href="cases/2026-09-18-mario-kart/README.en.md">Details</a><br><a href="https://x.com/shreypandya/status/2100606445758898287">X · 204 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/wuyang_zhou/status/2100727660875808913"><img src="https://pbs.twimg.com/amplify_video_thumb/2100727359569530880/img/IGuQpzilRkIsw1Wb.jpg" width="320" alt="Minecraft with Jev, Astra and local policies"></a></p>
<p><strong><a href="cases/2026-09-18-minecraft-hybrid/README.en.md">Minecraft with Jev, Astra and local policies</a></strong><br>Split Minecraft play across models: long-term planning, quick reactions, and local movement and aiming.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#minecraft-hybrid">Effectiveness unverified</a> · <a href="cases/2026-09-18-minecraft-hybrid/README.en.md">Details</a><br><a href="https://x.com/wuyang_zhou/status/2100727660875808913">X · 354 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/HugoDuprez/status/2100953089003921543"><img src="https://pbs.twimg.com/amplify_video_thumb/2100952449661992960/img/GEVdw9BvAW7Dv2Gx.jpg" width="320" alt="Sprite Fusion: generate runner terrain in real time"></a></p>
<p><strong><a href="cases/2026-09-19-game-level-generation/README.en.md">Sprite Fusion: generate runner terrain in real time</a></strong><br>Select new platforms and gaps ahead of a moving player.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#game-level-generation">Clearer mechanism</a> · <a href="cases/2026-09-19-game-level-generation/README.en.md">Details</a><br><a href="https://x.com/HugoDuprez/status/2100953089003921543">X · 1,289 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/thymikee/status/2100937960115838984"><img src="https://pbs.twimg.com/amplify_video_thumb/2100937854813700096/img/AlsBUETn77dLd0r8.jpg" width="320" alt="Flappy Bird: navigate obstacles"></a></p>
<p><strong><a href="cases/2026-09-19-flappy-bird/README.en.md">Flappy Bird: navigate obstacles</a></strong><br>Use Jev in controlling a bird through obstacles.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#flappy-bird">Effectiveness unverified</a> · <a href="cases/2026-09-19-flappy-bird/README.en.md">Details</a><br><a href="https://x.com/thymikee/status/2100937960115838984">X · 254 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/izumisatoshi05/status/2101287104030609624"><img src="https://pbs.twimg.com/amplify_video_thumb/2101283892556972032/img/VZM3g2req3zV_HAd.jpg" width="320" alt="Voice-spell game: turn a spoken chant into magic"></a></p>
<p><strong><a href="cases/2026-09-20-voice-spell-game/README.en.md">Voice-spell game: turn a spoken chant into magic</a></strong><br>Let semantic judgments determine the type and power of a player’s invented spell.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#voice-spell-game">Effectiveness unverified</a> · <a href="cases/2026-09-20-voice-spell-game/README.en.md">Details</a><br><a href="https://x.com/izumisatoshi05/status/2101287104030609624">X · 576 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/gigabit_million/status/2101285853859545263"><img src="https://pbs.twimg.com/amplify_video_thumb/2101283748440616960/img/zi6EL5MsWikz9suI.jpg" width="320" alt="Chat game: classify emotion and topic"></a></p>
<p><strong><a href="cases/2026-09-20-emotion-topic-chat-game/README.en.md">Chat game: classify emotion and topic</a></strong><br>Classify a player’s emotion and topic to drive a chat game’s response.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#emotion-topic-chat-game">Effectiveness unverified</a> · <a href="cases/2026-09-20-emotion-topic-chat-game/README.en.md">Details</a><br><a href="https://x.com/gigabit_million/status/2101285853859545263">X · 391 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/nwnwnyo/status/2101605150242849140"><img src="https://pbs.twimg.com/amplify_video_thumb/2101595622608687104/img/0WizOSDnwuaCFE80.jpg" width="320" alt="Mario teacher data: Jev demonstrates, LightGBM takes over"></a></p>
<p><strong><a href="cases/2026-09-21-mario-lightgbm-teacher/README.en.md">Mario teacher data: Jev demonstrates, LightGBM takes over</a></strong><br>Generate training examples with Jev, then control Mario with local LightGBM.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#mario-lightgbm-teacher">Effectiveness unverified</a> · <a href="cases/2026-09-21-mario-lightgbm-teacher/README.en.md">Details</a><br><a href="https://x.com/nwnwnyo/status/2101605150242849140">X · 945 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/rronak_/status/2101544156757950697"><img src="https://pbs.twimg.com/amplify_video_thumb/2101542497042481152/img/edco8P9wl-DUp5z8.jpg" width="320" alt="Minecraft fixed route: planning plus bounded actions"></a></p>
<p><strong><a href="cases/2026-09-21-minecraft-fixed-route/README.en.md">Minecraft fixed route: planning plus bounded actions</a></strong><br>Combine a planner, Jev and pathfinding code on a known route to the dragon.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#minecraft-fixed-route">Claims lack support</a> · <a href="cases/2026-09-21-minecraft-fixed-route/README.en.md">Details</a><br><a href="https://x.com/rronak_/status/2101544156757950697">X · 6,861 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
</tr>
</table>

</details>

<a id="simulation"></a>

<details>
<summary><strong>Experiment in simulated worlds</strong> · 11</summary>

Explore decisions in traffic, robotics and virtual characters. Code usually handles physics and movement. Success in a simulation still needs validation in the real world.

[Compare approaches](breakdowns/2026-09-18-simulation.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/m_iraji/status/2100394212743159944"><img src="https://pbs.twimg.com/amplify_video_thumb/2100394190643355648/img/52O-mJZSxj4IGHos.jpg" width="320" alt="Needs-driven NPCs"></a></p>
<p><strong><a href="cases/2026-09-18-npc-needs/README.en.md">Needs-driven NPCs</a></strong><br>Let game characters choose objects or activities that meet their needs.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#npc-needs">Effectiveness unverified</a> · <a href="cases/2026-09-18-npc-needs/README.en.md">Details</a><br><a href="https://x.com/m_iraji/status/2100394212743159944">X · 201 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/crislenta/status/2100457614073327754"><img src="https://pbs.twimg.com/amplify_video_thumb/2100457262372560897/img/zSIVGvaQhEZLMd9-.jpg" width="320" alt="500 agents in a 3D environment"></a></p>
<p><strong><a href="cases/2026-09-18-npc-500/README.en.md">500 agents in a 3D environment</a></strong><br>Run decisions for many virtual characters in one 3D world.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#npc-500">Claims lack support</a> · <a href="cases/2026-09-18-npc-500/README.en.md">Details</a><br><a href="https://x.com/crislenta/status/2100457614073327754">X · 572 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/jpschroeder/status/2100347770867458384"><img src="https://pbs.twimg.com/amplify_video_thumb/2100347372844756992/img/CaExDBw3MTf0ia58.jpg" width="320" alt="“FSD” driving simulation"></a></p>
<p><strong><a href="cases/2026-09-18-driving-toy/README.en.md">“FSD” driving simulation</a></strong><br>A small driving simulation that the author calls “rebuilding FSD.”</p>
<p><a href="references/2026-09-19-claims-audit.en.md#driving-toy">Claims lack support</a> · <a href="cases/2026-09-18-driving-toy/README.en.md">Details</a><br><a href="https://x.com/jpschroeder/status/2100347770867458384">X · 3,993 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/SigGravitas/status/2100325221932958134"><img src="https://pbs.twimg.com/amplify_video_thumb/2100323655389474816/img/LLOAJ3wie1phk45K.jpg" width="320" alt="Unpaused real-time driving"></a></p>
<p><strong><a href="cases/2026-09-18-realtime-driving/README.en.md">Unpaused real-time driving</a></strong><br>Keep the car moving while Jev thinks to test real-time simulated driving.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#realtime-driving">Effectiveness unverified</a> · <a href="cases/2026-09-18-realtime-driving/README.en.md">Details</a><br><a href="https://x.com/SigGravitas/status/2100325221932958134">X · 270 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/RomanSlack1/status/2100335978229690683"><img src="https://pbs.twimg.com/amplify_video_thumb/2100335726097494016/img/EljFdjduS88MyP9d.jpg" width="320" alt="Jev drone simulation"></a></p>
<p><strong><a href="cases/2026-09-18-drone-sim/README.en.md">Jev drone simulation</a></strong><br>Fly through simulated obstacles with Jev choosing tactics and code stabilizing the drone.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#drone-sim">Clearer mechanism</a> · <a href="cases/2026-09-18-drone-sim/README.en.md">Details</a><br><a href="https://x.com/RomanSlack1/status/2100335978229690683">X · 330 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/threepointone/status/2100576921629163848"><img src="https://pbs.twimg.com/amplify_video_thumb/2100576552849117184/img/fdEy6tirVMqee5pe.jpg" width="320" alt="Unstable Government town"></a></p>
<p><strong><a href="cases/2026-09-18-unstable-government/README.en.md">Unstable Government town</a></strong><br>Introduce a law in a fictional town and watch residents react before a newspaper is generated.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#unstable-government">Effectiveness unverified</a> · <a href="cases/2026-09-18-unstable-government/README.en.md">Details</a><br><a href="https://x.com/threepointone/status/2100576921629163848">X · 395 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/ytiskw/status/2100474943154827344"><img src="https://pbs.twimg.com/amplify_video_thumb/2100474178457698304/img/DXGnHg-iUrEhsFgE.jpg" width="320" alt="150 fictional user personas"></a></p>
<p><strong><a href="cases/2026-09-18-synthetic-personas/README.en.md">150 fictional user personas</a></strong><br>Ask fictional users about product interest to explore early ideas.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#synthetic-personas">Effectiveness unverified</a> · <a href="cases/2026-09-18-synthetic-personas/README.en.md">Details</a><br><a href="https://x.com/ytiskw/status/2100474943154827344">X · 792 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/leojrr/status/2101161666410893328"><img src="https://pbs.twimg.com/amplify_video_thumb/2101161072447180800/img/sRIOALT11TUpdAdU.jpg" width="320" alt="Jev City: nine-intersection traffic simulation"></a></p>
<p><strong><a href="cases/2026-09-19-traffic-light-city/README.en.md">Jev City: nine-intersection traffic simulation</a></strong><br>Choose signal directions in a virtual road network and observe queues and waiting time.</p>
<p><a href="references/2026-09-19-increment7-audit.en.md#traffic-light-city">Claims lack support</a> · <a href="cases/2026-09-19-traffic-light-city/README.en.md">Details</a><br><a href="https://x.com/leojrr/status/2101161666410893328">X · 1,081 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/roiyaruRIZ/status/2101130711067431018"><img src="https://pbs.twimg.com/amplify_video_thumb/2101125501234630656/img/pxMddfrpMLTvBhaR.jpg" width="320" alt="Vital-sign simulation: judging state changes"></a></p>
<p><strong><a href="cases/2026-09-19-vital-signs-simulator/README.en.md">Vital-sign simulation: judging state changes</a></strong><br>Compare rule alarms with Jev judgments in normal-state and slow-heart-rate simulations.</p>
<p><a href="references/2026-09-19-increment7-audit.en.md#vital-signs-simulator">Claims lack support</a> · <a href="cases/2026-09-19-vital-signs-simulator/README.en.md">Details</a><br><a href="https://x.com/roiyaruRIZ/status/2101130711067431018">X · 216 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/Raptor_zip/status/2101091398447505567"><img src="https://pbs.twimg.com/amplify_video_thumb/2101070240444772353/img/Ci_PCLcMigmoAdks.jpg" width="320" alt="Dual-arm robot simulation: layered action decisions"></a></p>
<p><strong><a href="cases/2026-09-19-dual-arm-robot-sim/README.en.md">Dual-arm robot simulation: layered action decisions</a></strong><br>Manipulate blocks in simulation, with Jev handling the middle decision layer.</p>
<p><a href="references/2026-09-19-increment7-audit.en.md#dual-arm-robot-sim">Effectiveness unverified</a> · <a href="cases/2026-09-19-dual-arm-robot-sim/README.en.md">Details</a><br><a href="https://x.com/Raptor_zip/status/2101091398447505567">X · 229 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/openroboto/status/2101310974359941332"><img src="https://pbs.twimg.com/amplify_video_thumb/2101310940260270080/img/mCYBqjSwjUf4UV6d.jpg" width="320" alt="MuJoCo: three-model apple pick-and-place comparison"></a></p>
<p><strong><a href="cases/2026-09-20-mujoco-apple-control/README.en.md">MuJoCo: three-model apple pick-and-place comparison</a></strong><br>Move an apple onto a plate with a simulated arm and compare direction and gripper decisions.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#mujoco-apple-control">Clearer mechanism</a> · <a href="cases/2026-09-20-mujoco-apple-control/README.en.md">Details</a><br><a href="https://x.com/openroboto/status/2101310974359941332">X · 272 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="interaction"></a>

<details>
<summary><strong>Turn judgments into interactions</strong> · 23</summary>

Choose a color or component, or decide whether speech needs a response. Small judgments can create new interfaces. Compare meaning, structure and false activations as well as latency.

[Compare approaches](breakdowns/2026-09-18-interaction.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/reczko_konrad/status/2100646448324833512"><img src="https://pbs.twimg.com/amplify_video_thumb/2100644432211062784/img/iduKHYZdESQ5FBR7.jpg" width="320" alt="TypeGPU real-time semantic effects"></a></p>
<p><strong><a href="cases/2026-09-18-typegpu-realtime/README.en.md">TypeGPU real-time semantic effects</a></strong><br>Let camera and microphone input influence lighting and visual effects.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#typegpu-realtime">Effectiveness unverified</a> · <a href="cases/2026-09-18-typegpu-realtime/README.en.md">Details</a><br><a href="https://x.com/reczko_konrad/status/2100646448324833512">X · 251 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/waynesutton/status/2100487878992388279"><img src="https://pbs.twimg.com/amplify_video_thumb/2100486117325955072/img/_QailXRTsMGQ_atc.jpg" width="320" alt="Ask Jev"></a></p>
<p><strong><a href="cases/2026-09-18-ask-jev/README.en.md">Ask Jev</a></strong><br>Enter a question and see Jev&#x27;s judgment instead of a long written answer.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#ask-jev">Effectiveness unverified</a> · <a href="cases/2026-09-18-ask-jev/README.en.md">Details</a><br><a href="https://x.com/waynesutton/status/2100487878992388279">X · 423 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/hi_im_isaac_/status/2100408276949385668"><img src="https://pbs.twimg.com/amplify_video_thumb/2100407646226649088/img/qVPomAIwJ_lKpO2J.jpg" width="320" alt="Finite-vocabulary chat"></a></p>
<p><strong><a href="cases/2026-09-18-word-chat/README.en.md">Finite-vocabulary chat</a></strong><br>Give Jev a common-word list and let it build a conversation one word at a time.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#word-chat">Clearer mechanism</a> · <a href="cases/2026-09-18-word-chat/README.en.md">Details</a><br><a href="https://x.com/hi_im_isaac_/status/2100408276949385668">X · 2,644 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/ryanvogel/status/2100218045549412499"><img src="https://pbs.twimg.com/amplify_video_thumb/2100217973000617984/img/AFareJummI08B_QB.jpg" width="320" alt="29-option character generation"></a></p>
<p><strong><a href="cases/2026-09-18-character-chat/README.en.md">29-option character generation</a></strong><br>Let Jev choose one letter or punctuation mark at a time to build text.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#character-chat">Clearer mechanism</a> · <a href="cases/2026-09-18-character-chat/README.en.md">Details</a><br><a href="https://x.com/ryanvogel/status/2100218045549412499">X · 866 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/anshuc/status/2100246929611411501"><img src="https://pbs.twimg.com/amplify_video_thumb/2100245288183066624/img/ARkl8CTLZxp1KXSa.jpg" width="320" alt="Parallel pixel drawing"></a></p>
<p><strong><a href="cases/2026-09-18-pixel-drawing/README.en.md">Parallel pixel drawing</a></strong><br>Combine many pixel-level judgments to experiment with drawing through Jev.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#pixel-drawing">Effectiveness unverified</a> · <a href="cases/2026-09-18-pixel-drawing/README.en.md">Details</a><br><a href="https://x.com/anshuc/status/2100246929611411501">X · 1,461 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/i2cjak/status/2100454307405365673"><img src="https://pbs.twimg.com/amplify_video_thumb/2100454137695469568/img/pGRTotN_ZQaAuc4V.jpg" width="320" alt="RISC-jeV logic-gate experiment"></a></p>
<p><strong><a href="cases/2026-09-18-riscv/README.en.md">RISC-jeV logic-gate experiment</a></strong><br>Use Jev for simple logic decisions and compose them into small computer instructions.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#riscv">Effectiveness unverified</a> · <a href="cases/2026-09-18-riscv/README.en.md">Details</a><br><a href="https://x.com/i2cjak/status/2100454307405365673">X · 208 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/dabit3/status/2100756930054504776"><img src="https://pbs.twimg.com/amplify_video_thumb/2100756324845862913/img/8ew1NdHs6k5cReoF.jpg" width="320" alt="Intent-aware predictive launcher"></a></p>
<p><strong><a href="cases/2026-09-18-predictive-launcher/README.en.md">Intent-aware predictive launcher</a></strong><br>Find files without remembering names: type “the PDF I just downloaded” and rank relevant matches first.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#predictive-launcher">Effectiveness unverified</a> · <a href="cases/2026-09-18-predictive-launcher/README.en.md">Details</a><br><a href="https://x.com/dabit3/status/2100756930054504776">X · 252 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/rinte0321/status/2100736454850908344"><img src="https://pbs.twimg.com/amplify_video_thumb/2100735518963355648/img/o0S0IxXnxWjnlNOG.jpg" width="320" alt="Live shopping assistant and avatar expressions"></a></p>
<p><strong><a href="cases/2026-09-18-live-commerce-assistant/README.en.md">Live shopping assistant and avatar expressions</a></strong><br>Recommend products during a conversation and change a virtual shop assistant’s expression with the dialogue.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#live-commerce-assistant">Effectiveness unverified</a> · <a href="cases/2026-09-18-live-commerce-assistant/README.en.md">Details</a><br><a href="https://x.com/rinte0321/status/2100736454850908344">X · 217 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/riku720720/status/2100705558512963602"><img src="https://pbs.twimg.com/amplify_video_thumb/2100705222016520192/img/BxzTN_rxkA_FLvwe.jpg" width="320" alt="Live emoji suggestions"></a></p>
<p><strong><a href="cases/2026-09-18-emoji-suggestions/README.en.md">Live emoji suggestions</a></strong><br>Suggest emoji that fit the meaning of text as it is entered.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#emoji-suggestions">Effectiveness unverified</a> · <a href="cases/2026-09-18-emoji-suggestions/README.en.md">Details</a><br><a href="https://x.com/riku720720/status/2100705558512963602">X · 230 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/jackcheng/status/2100729670991802386"><img src="https://pbs.twimg.com/amplify_video_thumb/2100729243185324032/img/YNw8njfnSXu-Tbyr.jpg" width="320" alt="Voice-and-pointing canvas control"></a></p>
<p><strong><a href="cases/2026-09-18-voice-gesture-canvas/README.en.md">Voice-and-pointing canvas control</a></strong><br>Use speech and pointing together to say “put that over there” on a canvas.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#voice-gesture-canvas">Effectiveness unverified</a> · <a href="cases/2026-09-18-voice-gesture-canvas/README.en.md">Details</a><br><a href="https://x.com/jackcheng/status/2100729670991802386">X · 915 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/southpolesteve/status/2100767781868150938"><img src="https://pbs.twimg.com/media/HSdr-ILWUAAN29Y.jpg?name=orig" width="320" alt="Probably: semantic judgments as program control"></a></p>
<p><strong><a href="cases/2026-09-18-probably-language/README.en.md">Probably: semantic judgments as program control</a></strong><br>Write judgments such as “is this email urgent?” into branches, then ask a text model to draft a reply.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#probably-language">Clearer mechanism</a> · <a href="cases/2026-09-18-probably-language/README.en.md">Details</a><br><a href="https://x.com/southpolesteve/status/2100767781868150938">X · 894 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/thorstenball/status/2100858434904109099"><img src="https://pbs.twimg.com/amplify_video_thumb/2100858390683475969/img/PRKkLSCaQKsfoXRI.jpg" width="320" alt="Shell history: semantic command suggestions"></a></p>
<p><strong><a href="cases/2026-09-18-shell-history-suggestions/README.en.md">Shell history: semantic command suggestions</a></strong><br>Type part of a command or describe an intent to select a suggestion from past commands.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#shell-history-suggestions">Clearer mechanism</a> · <a href="cases/2026-09-18-shell-history-suggestions/README.en.md">Details</a><br><a href="https://x.com/thorstenball/status/2100858434904109099">X · 396 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/ctatedev/status/2101022101750571357"><img src="https://pbs.twimg.com/amplify_video_thumb/2101022081810911232/img/3tKdQ3Y2_ZGSg3Q7.jpg" width="320" alt="json-render: assemble interfaces from component choices"></a></p>
<p><strong><a href="cases/2026-09-19-json-render-ui/README.en.md">json-render: assemble interfaces from component choices</a></strong><br>Turn interface requests into constrained component layouts, including additions, removals and moves.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#json-render-ui">Clearer mechanism</a> · <a href="cases/2026-09-19-json-render-ui/README.en.md">Details</a><br><a href="https://x.com/ctatedev/status/2101022101750571357">X · 3,341 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/_MaxBlade/status/2100967959879471519"><img src="https://pbs.twimg.com/amplify_video_thumb/2100966551826444288/img/i2s52ZeMNTOO-IRD.jpg" width="320" alt="CNVS: gate voice commands without a wake word"></a></p>
<p><strong><a href="cases/2026-09-19-cnvs-voice-gate/README.en.md">CNVS: gate voice commands without a wake word</a></strong><br>Decide whether a spoken utterance is directed at the computer.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#cnvs-voice-gate">Effectiveness unverified</a> · <a href="cases/2026-09-19-cnvs-voice-gate/README.en.md">Details</a><br><a href="https://x.com/_MaxBlade/status/2100967959879471519">X · 1,053 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/mattdesl/status/2100899669802963060"><img src="https://pbs.twimg.com/amplify_video_thumb/2100898643117068288/img/p9Jp61lJyiq-UoWK.jpg" width="320" alt="Words and colors: visualize 16-color judgments"></a></p>
<p><strong><a href="cases/2026-09-19-color-judgments/README.en.md">Words and colors: visualize 16-color judgments</a></strong><br>Enter words and visualize the model’s judgments about colors.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#color-judgments">Clearer mechanism</a> · <a href="cases/2026-09-19-color-judgments/README.en.md">Details</a><br><a href="https://x.com/mattdesl/status/2100899669802963060">X · 3,441 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/masa_okamura108/status/2101446065526632473"><img src="https://pbs.twimg.com/amplify_video_thumb/2101445734306586624/img/OtIwp0JbQ9jrtce0.jpg" width="320" alt="Meeting-to-flowchart: organize a process as people talk"></a></p>
<p><strong><a href="cases/2026-09-20-meeting-flowchart/README.en.md">Meeting-to-flowchart: organize a process as people talk</a></strong><br>Extract business steps from meeting remarks into an editable flowchart.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#meeting-flowchart">Effectiveness unverified</a> · <a href="cases/2026-09-20-meeting-flowchart/README.en.md">Details</a><br><a href="https://x.com/masa_okamura108/status/2101446065526632473">X · 439 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/nailthy62/status/2101388186916454439"><img src="https://pbs.twimg.com/amplify_video_thumb/2101384523124740096/img/1Q6moTMdLcZ-mJ3r.jpg" width="320" alt="Drape try-on experiment: select outfits from speech"></a></p>
<p><strong><a href="cases/2026-09-20-drape-outfit-selection/README.en.md">Drape try-on experiment: select outfits from speech</a></strong><br>Choose clothes from speech and wardrobe information, then display the change through a video system.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#drape-outfit-selection">Effectiveness unverified</a> · <a href="cases/2026-09-20-drape-outfit-selection/README.en.md">Details</a><br><a href="https://x.com/nailthy62/status/2101388186916454439">X · 1,379 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/measure_plan/status/2101315424247820309"><img src="https://pbs.twimg.com/amplify_video_thumb/2101314739296993280/img/2s3V7uUsqvcHi9AX.jpg" width="320" alt="Canada word map: visualize regional associations"></a></p>
<p><strong><a href="cases/2026-09-20-canada-word-map/README.en.md">Canada word map: visualize regional associations</a></strong><br>Enter a word and display Canadian regions the model associates with it.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#canada-word-map">Effectiveness unverified</a> · <a href="cases/2026-09-20-canada-word-map/README.en.md">Details</a><br><a href="https://x.com/measure_plan/status/2101315424247820309">X · 219 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/CoooolXyh/status/2101284346640654362"><img src="https://pbs.twimg.com/media/HSlCWGybcAA1AiJ.jpg?name=orig" width="320" alt="Contextual clipboard: choose what to paste now"></a></p>
<p><strong><a href="cases/2026-09-20-contextual-clipboard/README.en.md">Contextual clipboard: choose what to paste now</a></strong><br>Use the active field and app context to select an item from clipboard history.</p>
<p><a href="references/2026-09-20-increment8-audit.en.md#contextual-clipboard">Effectiveness unverified</a> · <a href="cases/2026-09-20-contextual-clipboard/README.en.md">Details</a><br><a href="https://x.com/CoooolXyh/status/2101284346640654362">X · 207 likes snapshot</a><br><sub>Content updated: 2026-09-20</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/wquguru/status/2101711235628810669"><img src="https://pbs.twimg.com/amplify_video_thumb/2101707450797932544/img/AZFZnwRm5949VkO1.jpg" width="320" alt="ReadAloud: check missing words and changed meaning"></a></p>
<p><strong><a href="cases/2026-09-21-dasheng-reading/README.en.md">ReadAloud: check missing words and changed meaning</a></strong><br>Transcribe reading and mark omissions or questionable substitutions for practice.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#dasheng-reading">Claims lack support</a> · <a href="cases/2026-09-21-dasheng-reading/README.en.md">Details</a><br><a href="https://x.com/wquguru/status/2101711235628810669">X · 351 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/ashutoshpuro97/status/2101660362882085299"><img src="https://pbs.twimg.com/amplify_video_thumb/2101659226607321089/img/iDIVp1YnUasEtGo9.jpg" width="320" alt="Toothless: decide whether speech addresses the assistant"></a></p>
<p><strong><a href="cases/2026-09-21-toothless-voice-gate/README.en.md">Toothless: decide whether speech addresses the assistant</a></strong><br>Separate assistant-directed remarks from people talking to each other.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#toothless-voice-gate">Effectiveness unverified</a> · <a href="cases/2026-09-21-toothless-voice-gate/README.en.md">Details</a><br><a href="https://x.com/ashutoshpuro97/status/2101660362882085299">X · 266 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/erikdunteman/status/2101533797527454109"><img src="https://pbs.twimg.com/amplify_video_thumb/2101533698042785792/img/qrWkmPUgmo0GVwUK.jpg" width="320" alt="Token-choice loop: assemble text through repeated decisions"></a></p>
<p><strong><a href="cases/2026-09-21-token-choice-loop/README.en.md">Token-choice loop: assemble text through repeated decisions</a></strong><br>Repeatedly ask Jev to choose the next token from candidates.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#token-choice-loop">Effectiveness unverified</a> · <a href="cases/2026-09-21-token-choice-loop/README.en.md">Details</a><br><a href="https://x.com/erikdunteman/status/2101533797527454109">X · 211 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/frombit_jp/status/2101298040741253195"><img src="https://pbs.twimg.com/amplify_video_thumb/2101297718199250944/img/ZfHi6yxmGhGWvSPC.jpg" width="320" alt="AnimeAct: connect dialogue to character acting"></a></p>
<p><strong><a href="cases/2026-09-21-animeact-jev-demo/README.en.md">AnimeAct: connect dialogue to character acting</a></strong><br>Connect dialogue intent to a 3D acting system for responsive expressions and motion.</p>
<p><a href="references/2026-09-21-increment9-audit.en.md#animeact-jev-demo">Effectiveness unverified</a> · <a href="cases/2026-09-21-animeact-jev-demo/README.en.md">Details</a><br><a href="https://x.com/frombit_jp/status/2101298040741253195">X · 2,014 likes snapshot</a><br><sub>Content updated: 2026-09-21</sub></p>
</td>
<td width="50%"></td>
</tr>
</table>

</details>

<a id="finance"></a>

<details>
<summary><strong>Explore trading and backtests</strong> · 4</summary>

Some examples test strategies on historical data; others demonstrate execution. Backtests need time-valid data, while execution needs fill and risk checks. Speed and low cost do not establish profit.

[Compare approaches](breakdowns/2026-09-18-finance.en.md)

<table>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/jarrodwatts/status/2100356151468585346"><img src="https://pbs.twimg.com/amplify_video_thumb/2100355999064379392/img/BiAbeDjN57avf2VK.jpg" width="320" alt="Monad / Kuru trading bot"></a></p>
<p><strong><a href="cases/2026-09-18-trading-bot/README.en.md">Monad / Kuru trading bot</a></strong><br>Let Jev choose buy or sell from price information and have code submit the order.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#trading-bot">Effectiveness unverified</a> · <a href="cases/2026-09-18-trading-bot/README.en.md">Details</a><br><a href="https://x.com/jarrodwatts/status/2100356151468585346">X · 4,142 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/virattt/status/2100959848623899005"><img src="https://pbs.twimg.com/amplify_video_thumb/2100959729350561792/img/wc-JtyIBGa_9qgNL.jpg" width="320" alt="AI Hedge Fund: strategy backtesting"></a></p>
<p><strong><a href="cases/2026-09-19-ai-hedge-fund-backtest/README.en.md">AI Hedge Fund: strategy backtesting</a></strong><br>Choose a strategy and stock tickers to run an experiment on historical data.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#ai-hedge-fund-backtest">Claims lack support</a> · <a href="cases/2026-09-19-ai-hedge-fund-backtest/README.en.md">Details</a><br><a href="https://x.com/virattt/status/2100959848623899005">X · 613 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<p><a href="https://x.com/tommy_jepsen/status/2100939646653903063"><img src="https://pbs.twimg.com/amplify_video_thumb/2100938100272746496/img/8yisuerchTVTcFTn.jpg" width="320" alt="Danish equities: a full-year historical strategy experiment"></a></p>
<p><strong><a href="cases/2026-09-19-danish-stock-backtest/README.en.md">Danish equities: a full-year historical strategy experiment</a></strong><br>Experiment with trading decisions on 2025 market data using news and other signals.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#danish-stock-backtest">Effectiveness unverified</a> · <a href="cases/2026-09-19-danish-stock-backtest/README.en.md">Details</a><br><a href="https://x.com/tommy_jepsen/status/2100939646653903063">X · 269 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
<td width="50%" valign="top">
<p><a href="https://x.com/IndraVahan/status/2100929105382564113"><img src="https://pbs.twimg.com/amplify_video_thumb/2100928264831410176/img/VP6eszCSb95ePMo4.jpg" width="320" alt="Nifty intraday trading: an account demo with a stop-loss report"></a></p>
<p><strong><a href="cases/2026-09-19-nifty-trading/README.en.md">Nifty intraday trading: an account demo with a stop-loss report</a></strong><br>Demonstrate Jev-connected Nifty trading and report a triggered stop loss.</p>
<p><a href="references/2026-09-19-claims-audit.en.md#nifty-trading">Effectiveness unverified</a> · <a href="cases/2026-09-19-nifty-trading/README.en.md">Details</a><br><a href="https://x.com/IndraVahan/status/2100929105382564113">X · 673 likes snapshot</a><br><sub>Content updated: 2026-09-19</sub></p>
</td>
</tr>
</table>

</details>

## About this collection

Original application posts must have at least **200 likes** and relevant media. Updates to one project are merged; independent implementations are grouped for comparison. Counts are snapshots, not credibility scores, and this is not an exhaustive inventory of X.

Exact metric timestamps, technical details and assessment grades are kept in the linked records. Media remains with its original creators; click through if a preview stops working.

[Case index](cases/README.en.md) · [Sources & method](references/README.en.md) · [Pending evidence](inbox/README.en.md) · [Contribute a case](CONTRIBUTING.en.md)
