# 2026-09-20 · Eighth incremental intake and evidence review

[简体中文](2026-09-20-increment8-audit.md) | **English**

Reviewed through **2026-09-20 11:01:10 Beijing time**. **15 new cases**, **4 merged updates**, **127 cases in 11 groups**. Catalog totals: A 23 / B 90 / C 14. All remain **not independently reproduced**.

Searched forward from the previous review cutoff (2026-09-19 17:48:49 Beijing time), with overlap, using X Latest search `Jev min_faves:200 since:2026-09-19`. Follow-up work read author threads, pinned documentation and relevant code. X indexing is incomplete; this is not an exhaustive export.

Likes and media use per-post snapshots from the public FxTwitter API, which can be cached. Exact retrieval times are retained below and in shared data. Reply/quote likes are not added to the original application post. Author claims, inspectable source, published evaluations and independent reproduction are distinct; no model calls or third-party execution were performed.

A means relatively clear implementation and limits; B means a concrete task/prototype with unverified outcomes; C means central claims exceed the evidence. A is not independent verification. New cases: A 3 / B 12. TipTour moves from B to A with pinned source; other updated ratings remain unchanged.

## Deduplication decisions

| Lead | Decision and reason |
| --- | --- |
| TipTour source release | Same author quoting the original CoreML/OCR demo: merged. |
| Hermes compaction evaluation | Evaluates a port of the existing plugin; added as evidence, not a new app. |
| Seven Ryze workflows | More detail for one product, not seven projects; copied claims do not count again. |
| 12306 train query | Explicitly uses Ultrafast: merged into Browser Use. A new website does not create another project. |
| Meeting diagrams and interview scoring | Same author but different tasks, outputs, posts and media: separate cases. |
| Third Hand and other computer-use tools | Independent Swift repository and request-text extraction; compare with generated text in Ultrafast and click-only TipTour. |
| Canada map and color experiment | Quotes inspiration but has a distinct geographic task and video: grouped for comparison. |
| Book prediction and property tagging | Same author, different data, tasks and media: separate data cases. |

## Per-case evidence

<a id="meeting-flowchart"></a>

## Meeting-to-flowchart: organize a process as people talk · B

The described workflow and original demo support a prototype, not established accuracy or completeness on complex meetings.

**Evidence:** The author describes per-utterance business relevance and add/edit/delete/no-op decisions. Utterances at 50% confidence or above reach an LLM; Jev then checks grounding, duplication and ownership before code updates draw.io.

**Limits:** The 50% cutoff is an author-set threshold, not an accuracy guarantee. Full transcripts, omission rates and human-diagram comparisons are missing.

**Reported result:** A roughly two-minute fictional real-estate interview is described as normal-speed footage. Low-confidence material is skipped or marked for confirmation.

Case: [Meeting-to-flowchart: organize a process as people talk](../cases/2026-09-20-meeting-flowchart/README.en.md)

Sources: [X @masa_okamura108](https://x.com/masa_okamura108/status/2101446065526632473)

Main-post snapshot: **439 likes**, 2026-09-20T02:45:24+00:00; [retrieval source](https://api.fxtwitter.com/status/2101446065526632473).

<a id="agent-goal-verifier"></a>

## Agent goal verifier: check completion after each turn · B

Supports an early verifier prototype, not universal verification suitability or proven long-horizon gains.

**Evidence:** A custom verifier is integrated into the harness’s /goal feature. Full inputs, criteria and failure handling are not yet public.

**Limits:** The author explicitly calls this early experimentation with benchmarking still to come. A completion judgment is not a passed test; false-stop and missed-error rates are unknown.

**Reported result:** The author says Jev replaces a more expensive reasoning model and permits more frequent checks, without a complete quality/cost comparison.

Case: [Agent goal verifier: check completion after each turn](../cases/2026-09-20-agent-goal-verifier/README.en.md)

Sources: [X @omarsar0](https://x.com/omarsar0/status/2101443311454036477)

Main-post snapshot: **317 likes**, 2026-09-20T02:45:24+00:00; [retrieval source](https://api.fxtwitter.com/status/2101443311454036477).

<a id="drape-outfit-selection"></a>

## Drape try-on experiment: select outfits from speech · B

The author separates outfit decisions from video rendering; decision timing alone does not establish end-to-end realtime performance.

**Evidence:** Author replies describe transcripts and existing clothing metadata as inputs, with reference garment images used by a realtime video-to-video stage. The experiment was not actually integrated into Drape.

**Limits:** The full video model, transcription pipeline and end-to-end bill are undisclosed. Selection latency and cost are not full try-on measurements.

**Reported result:** The author reports about 620ms and $0.0011 per Jev decision, excluding creation of pre-existing metadata.

Case: [Drape try-on experiment: select outfits from speech](../cases/2026-09-20-drape-outfit-selection/README.en.md)

Sources: [X @nailthy62](https://x.com/nailthy62/status/2101388186916454439) · [X @nailthy62](https://x.com/nailthy62/status/2101459808587284818) · [X @nailthy62](https://x.com/nailthy62/status/2101420612485103693) · [X @nailthy62](https://x.com/nailthy62/status/2101401929842831381)

Main-post snapshot: **1379 likes**, 2026-09-20T02:45:54+00:00; [retrieval source](https://api.fxtwitter.com/status/2101388186916454439).

<a id="goodreads-taste-prediction"></a>

## Goodreads: predict personal five-star books · B

Data and holdout sizes are stated, but the full protocol is missing; the ratios do not generalize to other readers or tasks.

**Evidence:** The author starts with roughly 1,000 personal Goodreads ratings, holds out 100, and compares Jev with GPT-5.6 on five-star prediction. Prompts, split details and class balance are not established.

**Limits:** A 100-item single-reader test does not establish general recommendation quality. Majority-class baselines, leakage, precision and recall still need checking.

**Reported result:** The author reports slightly better accuracy, 53-fold lower cost and 25-fold greater speed for this setup; not independently reproduced.

Case: [Goodreads: predict personal five-star books](../cases/2026-09-20-goodreads-taste-prediction/README.en.md)

Sources: [X @venturetwins](https://x.com/venturetwins/status/2101393861667115437)

Main-post snapshot: **238 likes**, 2026-09-20T02:45:53+00:00; [retrieval source](https://api.fxtwitter.com/status/2101393861667115437).

<a id="zillow-semantic-filters"></a>

## Zillow listings: natural-language filters · B

Supports custom property tagging, with accuracy, input provenance and full billing boundaries still unresolved.

**Evidence:** The author describes semantic classification by style, renovation and freeway proximity. Raw fields, geographic inputs and any image-to-text preparation are undisclosed.

**Limits:** No labeled test set or error breakdown. This does not establish direct photo input to Jev or verified map-distance measurement.

**Reported result:** The author reports thousands of listings in under 20 seconds for $0.18; inclusion of retrieval and preprocessing is unknown.

Case: [Zillow listings: natural-language filters](../cases/2026-09-20-zillow-semantic-filters/README.en.md)

Sources: [X @venturetwins](https://x.com/venturetwins/status/2101341075684434245)

Main-post snapshot: **527 likes**, 2026-09-20T02:47:09+00:00; [retrieval source](https://api.fxtwitter.com/status/2101341075684434245).

<a id="shiori-link-tagging"></a>

## Shiori: automatic bookmark tags · B

The task and comparison media are clear, but superiority over Haiku or production-quality classification is unproven.

**Evidence:** The author shows Jev versus Haiku for Shiori link tagging. Page extraction, label vocabulary and multilabel rules were not established.

**Limits:** The video lacks labeled data and matched-condition statistics. Faster interface updates do not establish equal tag quality.

**Reported result:** A roughly 25-second comparison clip, without reproducible accuracy, cost or speedup figures.

Case: [Shiori: automatic bookmark tags](../cases/2026-09-20-shiori-link-tagging/README.en.md)

Sources: [X @brian_lovin](https://x.com/brian_lovin/status/2101321554130809156)

Main-post snapshot: **327 likes**, 2026-09-20T02:47:32+00:00; [retrieval source](https://api.fxtwitter.com/status/2101321554130809156).

<a id="jev-align"></a>

## jev-align: refine decision criteria with human feedback · A

Code exposes labeling, GEPA’s optimization target and human acceptance. A denotes clear implementation evidence, not proven generalization gains.

**Evidence:** The pinned CLI samples uncertain examples and random audit rows. GEPA optimizes task specifications against human labels using a separate reflection model; it does not fine-tune Jev weights.

**Limits:** Training gains do not guarantee generalization. Held-out evaluation is optional; annotation, reflection and repeated evaluation costs must also be counted.

**Reported result:** Source and a roughly two-minute demo support the workflow; this catalog has not reproduced it or established a universal gain.

Case: [jev-align: refine decision criteria with human feedback](../cases/2026-09-20-jev-align/README.en.md)

Sources: [X @sethkimmel3](https://x.com/sethkimmel3/status/2101357768640987302)

Implementation / method: [README.md](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/README.md) · [optimizer.py](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/src/jev_align/optimizer.py)

Main-post snapshot: **511 likes**, 2026-09-20T02:47:09+00:00; [retrieval source](https://api.fxtwitter.com/status/2101357768640987302).

<a id="third-hand"></a>

## Third Hand: control a Mac using text from your request · A

Pinned source explains text entry without an extra LLM as selection/extraction, not general generation. Speed and cost remain independently unverified.

**Evidence:** Pinned code reads accessibility controls with local Apple Vision OCR when needed. Jev selects actions and candidate text extracted from the request, then the app checks state. Tasks, labels and values go to TypeSafe even though pixels stay local.

**Limits:** No free-form writing or arbitrary command generation. Icons, complex editors and gestures can fail; subsecond and near-free claims lack full-task benchmarks.

**Reported result:** The author shows a 31-second demo and claims subsecond latency. Documentation calls it experimental and says completion still needs human judgment.

Case: [Third Hand: control a Mac using text from your request](../cases/2026-09-20-third-hand/README.en.md)

Sources: [X @sxhivs](https://x.com/sxhivs/status/2101367048223982065) · [X @sxhivs](https://x.com/sxhivs/status/2101367050207981608)

Implementation / method: [README.md](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/README.md) · [TextEntryPlan.swift](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/TextEntryPlan.swift) · [JevClient.swift](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/JevClient.swift)

Main-post snapshot: **549 likes**, 2026-09-20T02:46:29+00:00; [retrieval source](https://api.fxtwitter.com/status/2101367048223982065).

<a id="mujoco-apple-control"></a>

## MuJoCo: three-model apple pick-and-place comparison · A

Pinned sources disclose single-trial limits, controller responsibilities and replay timing. A indicates inspectability; this catalog ran neither verification nor physical robots.

**Evidence:** Each pinned-version cycle makes two requests: intent, then XYZ signs and open/hold/close. Inputs are simulator geometry and contact feedback. Shared code handles step size, IK and physics, not camera perception or generated joint torques.

**Limits:** Only one seed-0 trial per controller, so success rates are unknown. Replay synchronizes simulation time and removes API waits; video duration is not task wall time.

**Reported result:** Recorded results: Jev completed in 181.847s for $0.018825; GPT-6 Astra in 707.274s for $5.933624; GPT-4.1 mini reached 160 cycles. The roughly 1/315 cost applies only to these records.

Case: [MuJoCo: three-model apple pick-and-place comparison](../cases/2026-09-20-mujoco-apple-control/README.en.md)

Sources: [X @openroboto](https://x.com/openroboto/status/2101310974359941332) · [X @openroboto](https://x.com/openroboto/status/2101310978856276075) · [X @openroboto](https://x.com/openroboto/status/2101310983931040038) · [X @openroboto](https://x.com/openroboto/status/2101382220690895046)

Implementation / method: [README.md](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/README.md) · [RESULTS.md](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/docs/RESULTS.md) · [incremental_policy.py](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/incremental_policy.py) · [verify_replay.py](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/verify_replay.py)

Main-post snapshot: **272 likes**, 2026-09-20T02:47:32+00:00; [retrieval source](https://api.fxtwitter.com/status/2101310974359941332).

<a id="voice-spell-game"></a>

## Voice-spell game: turn a spoken chant into magic · B

The post specifies judgment dimensions and parameter mapping; playability, recognition quality and stability remain unverified.

**Evidence:** The author assigns spell validity, element, form and power to Jev, then maps results to game parameters. Speech transcription and rendering are surrounding stages whose implementations were not established.

**Limits:** Scoring rules, false activations and consistency need testing. No evidence that Jev directly processes audio or generates visual effects.

**Reported result:** A roughly 75-second proof-of-concept clip without reproducible end-to-end latency or cost measurements.

Case: [Voice-spell game: turn a spoken chant into magic](../cases/2026-09-20-voice-spell-game/README.en.md)

Sources: [X @izumisatoshi05](https://x.com/izumisatoshi05/status/2101287104030609624)

Main-post snapshot: **576 likes**, 2026-09-20T02:48:04+00:00; [retrieval source](https://api.fxtwitter.com/status/2101287104030609624).

<a id="emotion-topic-chat-game"></a>

## Chat game: classify emotion and topic · B

Supports an emotion/topic-driven prototype; sustainable free operation and long-term dialogue quality are not established.

**Evidence:** The author explicitly assigns emotion/topic classification to Jev and provides a Cloudflare-hosted entry point. Response-text sources, branching rules and candidate counts are unestablished.

**Limits:** A free public page does not imply permanently free underlying service. Full costs, classification errors and long-dialogue consistency are unknown; replies are not assumed to be generated by Jev.

**Reported result:** The author describes low costs and provides a 21-second clip and public demo. This catalog did not run it or call the model.

Case: [Chat game: classify emotion and topic](../cases/2026-09-20-emotion-topic-chat-game/README.en.md)

Sources: [X @gigabit_million](https://x.com/gigabit_million/status/2101285853859545263)

Implementation / method: [](https://jev-chat.gigabitmillion-games.workers.dev/)

Main-post snapshot: **391 likes**, 2026-09-20T02:48:04+00:00; [retrieval source](https://api.fxtwitter.com/status/2101285853859545263).

<a id="canada-word-map"></a>

## Canada word map: visualize regional associations · B

Shows model associations; understanding Canada is not an established geography or social-knowledge capability.

**Evidence:** The author describes Jev predicting word-associated regions for a map display. Geographic candidates, prompts and score normalization are undisclosed.

**Limits:** Subjective associations are not demographic, cultural or regional facts. No reference set or calibration is provided.

**Reported result:** The author reports instant responses and under one cent, without call counts or timing boundaries.

Case: [Canada word map: visualize regional associations](../cases/2026-09-20-canada-word-map/README.en.md)

Sources: [X @measure_plan](https://x.com/measure_plan/status/2101315424247820309)

Main-post snapshot: **219 likes**, 2026-09-20T02:47:32+00:00; [retrieval source](https://api.fxtwitter.com/status/2101315424247820309).

<a id="contextual-clipboard"></a>

## Contextual clipboard: choose what to paste now · B

Task, input sources and media are clear; accuracy, privacy handling and cross-app reliability remain unresolved.

**Evidence:** The author supplies clipboard history plus field/app context to Jev. Capture interfaces, candidate lengths and execution confirmation are unknown.

**Limits:** Only a prototype and subjective accuracy impression; similar candidates, errors and sensitive-content filtering need testing. It is not established as offline.

**Reported result:** The author calls it a travel-time toy that seems accurate, without measured hit rate or cost.

Case: [Contextual clipboard: choose what to paste now](../cases/2026-09-20-contextual-clipboard/README.en.md)

Sources: [X @CoooolXyh](https://x.com/CoooolXyh/status/2101284346640654362)

Main-post snapshot: **207 likes**, 2026-09-20T02:48:04+00:00; [retrieval source](https://api.fxtwitter.com/status/2101284346640654362).

<a id="x-draft-hype-check"></a>

## X draft check: flag overhyped wording before posting · B

Supports a draft-style reminder, not fact-checking or reliable judgments about people.

**Evidence:** The author built a browser extension using Jev to assess the style of an X draft. Labels, prompts and trigger frequency are undisclosed.

**Limits:** Style is subjective and does not establish profession, motives or factual accuracy. Human agreement and false-positive rates are missing.

**Reported result:** A roughly 44-second extension demo, without reproducible accuracy or cost figures.

Case: [X draft check: flag overhyped wording before posting](../cases/2026-09-20-x-draft-hype-check/README.en.md)

Sources: [X @unsu0707](https://x.com/unsu0707/status/2101249913099375058)

Main-post snapshot: **446 likes**, 2026-09-20T02:51:41+00:00; [retrieval source](https://api.fxtwitter.com/status/2101249913099375058).

<a id="ori-task-classification"></a>

## Ori Eval: compare 30-way request classification · B

The task and important limits are stated, but a small synthetic set and incomplete reproduction materials restrict the conclusions.

**Evidence:** OpenRouter describes sequential, stateless evaluation on the same 200 synthetic cases. LLM reasoning was off except for GLM 5.3 Flash, which ran at low effort.

**Limits:** Complete examples, per-case labels and repeated runs are absent. Default provider routing affects some tail latencies, limiting production generalization.

**Reported result:** The author reports over five times the speed of the runner-up, accuracy within a few cases across models, and second-lowest cost behind Qwen3.8 Flash.

Case: [Ori Eval: compare 30-way request classification](../cases/2026-09-20-ori-task-classification/README.en.md)

Sources: [X @OpenRouter](https://x.com/OpenRouter/status/2101412965765529853) · [X @OpenRouter](https://x.com/OpenRouter/status/2101412983297778130) · [X @OpenRouter](https://x.com/OpenRouter/status/2101413000725074212) · [X @OpenRouter](https://x.com/OpenRouter/status/2101413013941330371) · [X @OpenRouter](https://x.com/OpenRouter/status/2101413025572172201)

Main-post snapshot: **329 likes**, 2026-09-20T02:45:53+00:00; [retrieval source](https://api.fxtwitter.com/status/2101412965765529853).

<a id="coreml-ocr"></a>

## TipTour: CoreML + OCR desktop clicks · A

Pinned code exposes local perception, click limits and the 12-action budget. The 90ms figure remains an author-reported step timing; A denotes inspectability, not verified performance.

**Evidence:** Now open-source as TipTour. The pinned version detects controls/labels locally, lets Jev choose single/double/right-click targets and observes again after execution, with a default 12-action budget. Tasks, labels, positions and recent actions go to Jev; screenshots do not.

**Limits:** Detection errors affect clicks. Jev chooses the top-ranked target without a target-confidence cutoff and cannot freely write text. Gemini mode may send audio/screenshots, so local-image handling is not a blanket property of both modes.

**Reported result:** The original reports roughly 90ms per decision. The source release provides no new complete task set, success rate or end-to-end speed evaluation.

Case: [TipTour: CoreML + OCR desktop clicks](../cases/2026-09-18-coreml-ocr/README.en.md)

Sources: [X @milindlabs](https://x.com/milindlabs/status/2100631847155994852) · [X @milindlabs](https://x.com/milindlabs/status/2101260711645372886)

Implementation / method: [README.md](https://github.com/milind-soni/tiptour-macos/blob/52582467c883d66484542f3be8e259340eb524f1/README.md) · [JevPointerLoop.swift](https://github.com/milind-soni/tiptour-macos/blob/52582467c883d66484542f3be8e259340eb524f1/TipTour/Jev/JevPointerLoop.swift)

Main-post snapshot: **564 likes**, 2026-09-17T22:42:22.793465+00:00; [retrieval source](https://api.fxtwitter.com/status/2100631847155994852).

<a id="context-compaction"></a>

## Tool-history context compaction · C

A public adverse evaluation separates fast compaction from long-term savings. Three transcripts, a port and a recovery-enabled baseline are essential limits; the original recording animation is not realtime API measurement.

**Evidence:** At source revision e3f262a: pair tool calls with results, pin the first and recent messages, and fit conversation state to a budget. Tool-output bodies become status/length notes. Jev judges whether to retain each call and result; code keeps, truncates or removes them by thresholds. The Claude Code hook falls back to built-in summarization on errors or insufficient reduction.

**Limits:** A new Hermes evaluation exposes retention and long-session limits: its port dropped all 851 unpinned candidates at the default threshold, while repeated compaction retained a growing text floor. Findings apply to this adaptation, sample and budget, not all Jev memory designs.

**Reported result:** The original claims instant compaction. A three-transcript Hermes evaluation reports roughly 1.4s per Jev compaction, 115K retained tokens and 75.5% recall versus 55K and 78.9% for production summarization plus search recovery. This catalog did not run the evaluation.

Case: [Tool-history context compaction](../cases/2026-09-18-context-compaction/README.en.md)

Sources: [X @tamarajtran](https://x.com/tamarajtran/status/2100694549362553153) · [X @tamarajtran](https://x.com/tamarajtran/status/2100694552369897539) · [X @altryne](https://x.com/altryne/status/2100739055923425589) · [X @theo](https://x.com/theo/status/2100762304862384257) · [X @Teknium](https://x.com/Teknium/status/2101398453578555898)

Implementation / method: [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) · [116246](https://github.com/NousResearch/hermes-agent/pull/116246) · [SCORECARD-2026-09-19-jev.md](https://github.com/NousResearch/hermes-agent/blob/dba815e7ad800dad19f921ca9ad028eba027e8a4/evals/compaction/results/SCORECARD-2026-09-19-jev.md) · [jev_arm.py](https://github.com/NousResearch/hermes-agent/blob/dba815e7ad800dad19f921ca9ad028eba027e8a4/evals/compaction/jev_arm.py)

Main-post snapshot: **1646 likes**, 2026-09-17T22:42:26.956952+00:00; [retrieval source](https://api.fxtwitter.com/status/2100694549362553153).

<a id="ryze-seo-geo"></a>

## Ryze AI: SEO/GEO audits and fixes · C

Seven additional judgment workflows still belong to one Ryze product. The 90% savings, 20–30-fold speedups and citation effects lack reproducible controls; workflow count does not increase case count.

**Evidence:** The update details seven judgments in the same product: competitor-page scoring, keep/change decisions for page elements, question-to-page matching, citation-chance scoring, buyer-query classification, screening 15 internal-link candidates and 20 draft checks before human review. Retrieval, writing and execution still require surrounding components.

**Limits:** The detail clarifies workflow but does not provide full baseline, quality or billing comparisons. Citation-chance scores are not calibrated citation probabilities or guarantees of rankings/conversions.

**Reported result:** The author claims a 90% cost reduction from roughly $250, 30-fold gains across several stages and 20-fold faster page creation. A six-second interface clip does not establish those comparisons.

Case: [Ryze AI: SEO/GEO audits and fixes](../cases/2026-09-19-ryze-seo-geo/README.en.md)

Sources: [X @irabukht](https://x.com/irabukht/status/2101090579127951694) · [X @irabukht](https://x.com/irabukht/status/2101123317327372487) · [X @irabukht](https://x.com/irabukht/status/2101375295152652372)

Main-post snapshot: **790 likes**, 2026-09-19T09:42:43+00:00; [retrieval source](https://api.fxtwitter.com/status/2101090579127951694).

<a id="browser-use"></a>

## Browser Use · Ultrafast · A

Pinned docs and a public benchmark expose implementation and timing conditions. The new 12306 clip is another use report for the same project, not a separate app or proof of arbitrary-site reliability.

**Evidence:** Each step builds a fresh action space from the DOM. Jev selects an action; a small LLM supplies text when needed.

**Limits:** Still uses an LLM for text. The MVP excludes shadow DOM, iframes, canvas and uploads; a few repeated tasks do not establish cross-site reliability.

**Reported result:** The original author reports roughly 7s and $0.0039 for flight search. A new user shows a roughly 93-second 12306 train-query video using Ultrafast with Pi + DeepSeek, without controlled timing or billing comparisons.

Case: [Browser Use · Ultrafast](../cases/2026-09-18-browser-use/README.en.md)

Sources: [X @gregpr07](https://x.com/gregpr07/status/2100411066966749359) · [X @0xidanlevin](https://x.com/0xidanlevin/status/2100937437325205568) · [X @yanhua1010](https://x.com/yanhua1010/status/2101257759497089171)

Implementation / method: [jev-ultrafast](https://github.com/browser-use/jev-ultrafast) · [README.md](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/README.md) · [benchmark](https://webmcp.com/benchmark) · [WindTunnel](https://github.com/nekuda-ai/WindTunnel)

Main-post snapshot: **6891 likes**, 2026-09-17T22:32:51.243200+00:00; [retrieval source](https://api.fxtwitter.com/status/2100411066966749359).

## Scope and pending leads

Unclear implementations, unverified media and secondary reposts remain outside the formal count. See the [inbox](../inbox/README.en.md). Existing main-post snapshots and first-added times remain unchanged; only these 19 cases receive a new content-update time.
