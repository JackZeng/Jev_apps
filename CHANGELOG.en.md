# Collection updates

[简体中文](CHANGELOG.md) | **English**

## 2026-09-21 · Ninth incremental update

Reviewed through **2026-09-21 11:02:26 Beijing time**. **10 new cases**, **2 merged updates**, **137 cases in 11 groups** (A 25 / B 96 / C 16). Every new original has at least 200 likes in its recorded snapshot and corresponding media.

| New case | Like snapshot |
| --- | ---: |
| [DocJev: classify documents and split bundles](cases/2026-09-21-docjev/README.en.md) | [695](https://x.com/jerryjliu0/status/2101738281046294552) |
| [ReadAloud: check missing words and changed meaning](cases/2026-09-21-dasheng-reading/README.en.md) | [351](https://x.com/wquguru/status/2101711235628810669) |
| [Needle: find webpage passages by meaning](cases/2026-09-21-needle-semantic-find/README.en.md) | [1658](https://x.com/Saboo_Shubham_/status/2101576462042366114) |
| [Reddit Radar MCP: filter discussions by your criteria](cases/2026-09-21-reddit-radar-mcp/README.en.md) | [295](https://x.com/oguzhankayancom/status/2101667801274478707) |
| [Toothless: decide whether speech addresses the assistant](cases/2026-09-21-toothless-voice-gate/README.en.md) | [266](https://x.com/ashutoshpuro97/status/2101660362882085299) |
| [Mario teacher data: Jev demonstrates, LightGBM takes over](cases/2026-09-21-mario-lightgbm-teacher/README.en.md) | [945](https://x.com/nwnwnyo/status/2101605150242849140) |
| [Minecraft fixed route: planning plus bounded actions](cases/2026-09-21-minecraft-fixed-route/README.en.md) | [6861](https://x.com/rronak_/status/2101544156757950697) |
| [Token-choice loop: assemble text through repeated decisions](cases/2026-09-21-token-choice-loop/README.en.md) | [211](https://x.com/erikdunteman/status/2101533797527454109) |
| [Jev Field Notes: curate Jev examples with Jev](cases/2026-09-21-jev-field-notes-curation/README.en.md) | [298](https://x.com/omarsar0/status/2101696753749655863) |
| [AnimeAct: connect dialogue to character acting](cases/2026-09-21-animeact-jev-demo/README.en.md) | [2014](https://x.com/frombit_jp/status/2101298040741253195) |

Merged the DuckDB extension rewrite and the related Third Hand/arc-cua executor. DocJev and Needle have pinned implementation evidence; ReadAloud’s full-product/offline wording and Minecraft’s low-level-control claim exceed the inspected implementation. All remain unreproduced. Both languages preserve cards and original snapshots; only changed cases receive new content-update times. See the [evidence report](references/2026-09-21-increment9-audit.en.md).

## 2026-09-20 · Eighth incremental update

Reviewed through **2026-09-20 11:01:10 Beijing time**. Added **15** cases and merged **4** updates, for **127 cases in 11 groups**. A 23 / B 90 / C 14. Every new original post has at least 200 likes in its snapshot and corresponding media.

| New case | Like snapshot |
| --- | ---: |
| [Meeting-to-flowchart: organize a process as people talk](cases/2026-09-20-meeting-flowchart/README.en.md) | [439](https://x.com/masa_okamura108/status/2101446065526632473) |
| [Agent goal verifier: check completion after each turn](cases/2026-09-20-agent-goal-verifier/README.en.md) | [317](https://x.com/omarsar0/status/2101443311454036477) |
| [Drape try-on experiment: select outfits from speech](cases/2026-09-20-drape-outfit-selection/README.en.md) | [1379](https://x.com/nailthy62/status/2101388186916454439) |
| [Goodreads: predict personal five-star books](cases/2026-09-20-goodreads-taste-prediction/README.en.md) | [238](https://x.com/venturetwins/status/2101393861667115437) |
| [Zillow listings: natural-language filters](cases/2026-09-20-zillow-semantic-filters/README.en.md) | [527](https://x.com/venturetwins/status/2101341075684434245) |
| [Shiori: automatic bookmark tags](cases/2026-09-20-shiori-link-tagging/README.en.md) | [327](https://x.com/brian_lovin/status/2101321554130809156) |
| [jev-align: refine decision criteria with human feedback](cases/2026-09-20-jev-align/README.en.md) | [511](https://x.com/sethkimmel3/status/2101357768640987302) |
| [Third Hand: control a Mac using text from your request](cases/2026-09-20-third-hand/README.en.md) | [549](https://x.com/sxhivs/status/2101367048223982065) |
| [MuJoCo: three-model apple pick-and-place comparison](cases/2026-09-20-mujoco-apple-control/README.en.md) | [272](https://x.com/openroboto/status/2101310974359941332) |
| [Voice-spell game: turn a spoken chant into magic](cases/2026-09-20-voice-spell-game/README.en.md) | [576](https://x.com/izumisatoshi05/status/2101287104030609624) |
| [Chat game: classify emotion and topic](cases/2026-09-20-emotion-topic-chat-game/README.en.md) | [391](https://x.com/gigabit_million/status/2101285853859545263) |
| [Canada word map: visualize regional associations](cases/2026-09-20-canada-word-map/README.en.md) | [219](https://x.com/measure_plan/status/2101315424247820309) |
| [Contextual clipboard: choose what to paste now](cases/2026-09-20-contextual-clipboard/README.en.md) | [207](https://x.com/CoooolXyh/status/2101284346640654362) |
| [X draft check: flag overhyped wording before posting](cases/2026-09-20-x-draft-hype-check/README.en.md) | [446](https://x.com/unsu0707/status/2101249913099375058) |
| [Ori Eval: compare 30-way request classification](cases/2026-09-20-ori-task-classification/README.en.md) | [329](https://x.com/OpenRouter/status/2101412965765529853) |

Merged TipTour’s source release, the Hermes compaction evaluation, additional Ryze workflow details and a 12306 Ultrafast demonstration into their existing cases. TipTour moves to A for implementation clarity; performance remains unverified. New tools are compared within existing categories. Both languages preserve the two-column cards, original snapshots and first-added times; only the 19 changed cases receive new content-update times. See the [evidence report](references/2026-09-20-increment8-audit.en.md).

## 2026-09-19 · Two-column application cards

Changed the 11 collapsible categories to two-column cards. Each card places its thumbnail above the application name and purpose, followed by evidence, details, source and content-update date. Odd categories leave the final cell empty; images retain their aspect ratios. Both languages retain all 112 cases and existing historical data.

## 2026-09-19 · Field-guide homepage

Redesigned the homepage as a field guide: three introductory sentences, six highlights, 11 collapsible categories and a short collection policy. All 112 cases retain summaries, media, evidence links and content-update dates; exact timestamps, technical details and A/B/C reports remain in the records. Added bilingual homepage copy and a shared renderer. This presentation change adds no cases and changes no recorded assessments or content timestamps.

## 2026-09-19 · Increment 7

Checked through **2026-09-19 17:48:49 Beijing time**. Added **6** cases and merged **1** existing project update: **112 cases, 11 categories**. A 19 / B 79 / C 14. All new main posts have ≥200 likes and media at their recorded snapshots.

| Case | Likes |
| --- | ---: |
| [Claude Code Mod: model and effort routing](cases/2026-09-19-claude-code-jev-router/README.en.md) | [417](https://x.com/dani_avila7/status/2101176629745561686) |
| [Synthetic interview notes: batch classification and scoring](cases/2026-09-19-synthetic-interview-classifier/README.en.md) | [278](https://x.com/masa_okamura108/status/2101206603240477030) |
| [Jev City: nine-intersection traffic simulation](cases/2026-09-19-traffic-light-city/README.en.md) | [1081](https://x.com/leojrr/status/2101161666410893328) |
| [Vital-sign simulation: judging state changes](cases/2026-09-19-vital-signs-simulator/README.en.md) | [216](https://x.com/roiyaruRIZ/status/2101130711067431018) |
| [Dual-arm robot simulation: layered action decisions](cases/2026-09-19-dual-arm-robot-sim/README.en.md) | [229](https://x.com/Raptor_zip/status/2101091398447505567) |
| [Ryze AI: SEO/GEO audits and fixes](cases/2026-09-19-ryze-seo-geo/README.en.md) | [790](https://x.com/irabukht/status/2101090579127951694) |

Sac’s Jev-cu release is merged into its Calendar case. Original timestamps and evidence snapshots remain intact; only the six new cases and Sac update receive new content-update times. Both languages include mechanisms, comparisons, media and evidence labels. See [sources and assessments](references/2026-09-19-increment7-audit.en.md)。

## 2026-09-19 · Simpler application timestamps

Application introductions now display only **Content updated**, consistently across both homepages, indexes and detail pages. First-added and per-case assessment timestamps no longer appear beside introductions. Historical data and existing content-update values are preserved; this is a presentation-only change.

## 2026-09-19 · Claim assessment labels

Added the completed 106-case audit to both READMEs, case indexes and detail pages: **A 18, B 78, C 10**. Each case shows its assessment, a short reason and a direct link to its evidence row in the [audit report](references/2026-09-19-claims-audit.en.md). Labels assess public claims and do not change reproduction status.

The underlying audit was completed at 11:30 Beijing time; publishing the annotations updates content timestamps while preserving first-added times, main-post snapshots and media. No cases were added or removed. Shared assessment metadata and bilingual explanations are generated from the catalog; future unassessed additions receive an explicit neutral label.

## 2026-09-19 · Sixth increment

Review cutoff: **2026-09-19 07:03:22 Beijing time (2026-09-18 23:03:22 UTC)**. The catalog grows from 84 to **106 cases in 11 categories**: 22 independent additions and one existing entry supplemented. Every new main post had at least 200 likes and associated media at retrieval. Exact retrieval times are recorded per case; later visible increases do not overwrite snapshots.

| Addition | Main-post likes snapshot |
| --- | ---: |
| [Compact Adviser: choose when to compact](cases/2026-09-19-compact-adviser/README.en.md) | [242](https://x.com/kunchenguid/status/2101032677940117875) |
| [json-render: assemble interfaces from component choices](cases/2026-09-19-json-render-ui/README.en.md) | [3,341](https://x.com/ctatedev/status/2101022101750571357) |
| [SEO internal links: match existing text to relevant pages](cases/2026-09-19-seo-internal-links/README.en.md) | [721](https://x.com/borjafat/status/2101018783976722479) |
| [Box: triage and file incident reports](cases/2026-09-19-box-incident-triage/README.en.md) | [317](https://x.com/levie/status/2101007708044574906) |
| [NoSugarForKids: multi-criterion snack scoring](cases/2026-09-19-snack-scoring/README.en.md) | [312](https://x.com/nikunj/status/2101006585481073093) |
| [Tax Doc Classifier: label tax PDF pages](cases/2026-09-19-tax-doc-classifier/README.en.md) | [1,506](https://x.com/nedwize/status/2100973868324417852) |
| [ego lite: filter Amazon products](cases/2026-09-19-ego-product-decisions/README.en.md) | [366](https://x.com/ego_agent/status/2100970015977804008) |
| [CNVS: gate voice commands without a wake word](cases/2026-09-19-cnvs-voice-gate/README.en.md) | [1,053](https://x.com/_MaxBlade/status/2100967959879471519) |
| [Tester Army: web and mobile end-to-end testing](cases/2026-09-19-tester-army-e2e/README.en.md) | [505](https://x.com/o_kwasniewski/status/2100966838905585687) |
| [Codex Model Router: choose a model each turn](cases/2026-09-19-codex-model-router/README.en.md) | [437](https://x.com/antonioleivag/status/2100962426439000484) |
| [Gmail: search by intent](cases/2026-09-19-gmail-intent-search/README.en.md) | [574](https://x.com/dabit3/status/2100960281769738433) |
| [AI Hedge Fund: strategy backtesting](cases/2026-09-19-ai-hedge-fund-backtest/README.en.md) | [613](https://x.com/virattt/status/2100959848623899005) |
| [OCR + Jev: organize images](cases/2026-09-19-ocr-image-organizer/README.en.md) | [246](https://x.com/fayazara/status/2100953838891192789) |
| [Sprite Fusion: generate runner terrain in real time](cases/2026-09-19-game-level-generation/README.en.md) | [1,289](https://x.com/HugoDuprez/status/2100953089003921543) |
| [MaxFusion: classify advertising creatives](cases/2026-09-19-maxfusion-ad-classifier/README.en.md) | [320](https://x.com/OriSilver/status/2100941251478458871) |
| [Danish equities: a full-year historical strategy experiment](cases/2026-09-19-danish-stock-backtest/README.en.md) | [269](https://x.com/tommy_jepsen/status/2100939646653903063) |
| [Flappy Bird: navigate obstacles](cases/2026-09-19-flappy-bird/README.en.md) | [254](https://x.com/thymikee/status/2100937960115838984) |
| [Script.it: flag issues before writing review comments](cases/2026-09-19-script-code-review/README.en.md) | [202](https://x.com/liorshkiller/status/2100936106615140757) |
| [Nifty intraday trading: an account demo with a stop-loss report](cases/2026-09-19-nifty-trading/README.en.md) | [673](https://x.com/IndraVahan/status/2100929105382564113) |
| [macOS Downloads: organize files by rules](cases/2026-09-19-downloads-organizer/README.en.md) | [889](https://x.com/marcelpociot/status/2100906882365788167) |
| [Words and colors: visualize 16-color judgments](cases/2026-09-19-color-judgments/README.en.md) | [3,441](https://x.com/mattdesl/status/2100899669802963060) |
| [X reply cleanup: flag low-value comments](cases/2026-09-19-x-reply-cleanup/README.en.md) | [223](https://x.com/iannuttall/status/2100888635943883244) |

**Merging and deduplication:** The [WebMCP post](https://x.com/0xidanlevin/status/2100937437325205568) explicitly uses modified Ultrafast and is merged into [Browser Use](cases/2026-09-18-browser-use/README.en.md). Its original main-post snapshot and first-added timestamp remain; only its content timestamp advances. json-render quote-posts are not counted again. NoSugarForKids launch history remains one project. Color, reply-cleanup and terrain-generation follow-ups are merged with their main posts. Independent implementations are grouped and compared, without counting components, windows or platforms separately.

**Evidence boundaries:** WebMCP’s 49/49 task coverage includes 141/147 successful attempts, not success on every attempt. Tax classification retains 38 low-confidence strict-mode failures. SEO full-site comparator costs are extrapolated. Script.it retains its 75% bug recall. Trading entries distinguish historical experiments, author-claimed live use and the reported stop loss. Every case remains unreproduced.

**Deferred and excluded:** Flowsery replay analysis, Backdoor job matching, Gojiberry lead scoring, humor judgments, form autofill and DeepAPI abuse screening need clearer task definitions or component roles; see the [inbox](inbox/README.en.md). The Skittles-sorting repost exceeds 200 likes but its original application post has only **103** in this snapshot, so it is not admitted using repost engagement. Other models (including CUA-S1, Kev, SimpleJev, djev, Bespoke Nimble and GLiFormer), tutorials, opinions and roundups are not new Jev applications.

**Scope and method:** X latest search `Jev min_faves:200 since:2026-09-18`, from the newest results back toward the previous review window around Ian’s reply filter, Gojiberry and Runlayer. Reviewed posts, author replies, original media metadata and selected interface screenshots. Read pinned Compact Adviser, json-render, tax-classifier and Codex Router documentation, the Sprite Fusion article and WebMCP benchmark. Deduplication uses IDs, authors, purpose, repositories, quote chains and media, without claiming exhaustive X coverage.

**Maintenance:** New paths use each case’s first-added Beijing date; old paths stay stable. The homepage shows the new review date without refreshing unreviewed cases. Bilingual timestamps, lists, previews and comparisons are synchronized, with cross-midnight generation checks. Raw research stays ignored. No media was downloaded, external application executed, account connected or paid model API called.

## 2026-09-18 · Fifth incremental pass

Reviewed through **2026-09-18 19:42:10 Beijing time (11:42:10 UTC)**. The catalog grows from 79 to **84 cases in 11 categories**, adding five independent implementations. All 79 previous cases retain their content, timestamps and main-post like snapshots; none is counted again.

| Newly included | Main-post like snapshot | Evidence and deduplication |
| --- | ---: | --- |
| [Runlayer parallel browser testing](cases/2026-09-18-runlayer-adversarial-testing/README.en.md) | [820](https://x.com/rafalwilinski/status/2100882207879434359) | Author replies identify Runlayer agents, agent-browser and Chromium. A distinct multi-window video; sessions are not separate applications |
| [Hono JevRouter](cases/2026-09-18-hono-semantic-router/README.en.md) | [405](https://x.com/yusukebe/status/2100871075743859182) | Semantic HTTP routing, distinct from model selection. Pinned code selects the first qualifying registered route, not the highest score |
| [Sac’s Mac Calendar comparison](cases/2026-09-18-sac-calendar-computer-use/README.en.md) | [217](https://x.com/Saccc_c/status/2100864907046768890) | Called Jev Use, but with a different author and video from Cua. This main post reports similar token usage; broader savings in the quoted introductory post are not carried over |
| [Semantic shell-history suggestions](cases/2026-09-18-shell-history-suggestions/README.en.md) | [396](https://x.com/thorstenball/status/2100858434904109099) | Main demo and Amp production video merged. Pinned documentation explains candidate filtering, two-question gating and fabricated demo history |
| [Calorie Notebook food logging](cases/2026-09-18-calorie-notebook/README.en.md) | [326](https://x.com/thekitze/status/2100857642566758849) | Distinct text-based food interface. The author’s other projects are not recounted, and undisclosed estimation mechanics remain unknown |

Main-post snapshots were retrieved between 11:39:02 and 11:39:31 UTC; exact timestamps are retained per record. Every addition has bilingual descriptions, plain-language mechanisms, comparisons, media and README timestamps. None was reproduced. No plugin was installed, local history transmitted, external project executed or paid API called.

**Deduplication and exclusions:** [Rob Hallam’s quote](https://x.com/robj3d3/status/2100876506549645608) points to the included [Jack Cheng canvas](cases/2026-09-18-voice-gesture-canvas/README.en.md) and adds opinion only. [Sac’s introductory roundup](https://x.com/Saccc_c/status/2100833094291087773) lists already included browser, compaction, routing and review cases; the roundup is not counted again. Study sessions, article collections, generic use-case suggestions and imitations using other models are not new applications.

**Pending review:** Jev QA tester’s original post has 756 likes in this pass but still provides minimal text and a video without resolving its assertions or implementation relationship to the existing OpenCode demo. It remains pending. Runlayer has explicit author-provided tooling evidence and is not merged solely because both involve QA.

**Scope:** X Latest search `Jev min_faves:200 since:2026-09-18`, reaching the previously reviewed Kun Chen post and Sac roundup area. Read discussions for all five additions, Hono’s pinned README/router implementation, and the shell plugin’s pinned README. Deduplication uses post IDs, quote chains, authors, tasks, repositories and media; coverage is not exhaustive. No test was submitted to the Hono playground; reading code is not runtime verification.

## 2026-09-18 · Fourth incremental pass

Reviewed through **2026-09-18 16:15:58 Beijing time (08:15:58 UTC)**. The catalog grows from 77 to **79 cases in 11 categories**: two independent experiments, including one promoted after pending-evidence review. No existing project is counted again. Existing case content timestamps and like snapshots remain unchanged.

| Newly included | Main-post like snapshot | Evidence and deduplication |
| --- | ---: | --- |
| [Email classification: four-model speed comparison](cases/2026-09-18-email-speed-race/README.en.md) | [445](https://x.com/usutaku_channel/status/2100829343954173965) | Distinct author, interface and video; compared within the same category as the 500-email case. The author reports Jev as faster, but accuracy, version and configuration evidence is incomplete; no universal speed ranking is claimed |
| [Code comments: accuracy and usefulness scores](cases/2026-09-18-code-comment-scoring/README.en.md) | [1,777](https://x.com/markjaquith/status/2100359340087501296) | An earlier lead now supported by image inspection and two author replies establishing the scoring dimensions and screening role; distinct from ESLint-rule judgments and full PR review |

Both main-post snapshots were retrieved at **08:11:40 UTC**; the comment-scoring replies at **08:15:58 UTC**. Both cases include bilingual descriptions, plain-language mechanisms, trade-offs, original media and README inclusion/content-update timestamps. Neither was reproduced. A 99/100 example score is not treated as 99% test accuracy, and video length is not treated as execution time.

**Duplicates and exclusions:**

- [Tony’s sponsor-skipping video](https://x.com/tdinh_me/status/2100793777103466615) is already included; resurfacing in search does not add a case.
- The [OpenCode local-classifier discussion](https://x.com/thdxr/status/2100814192919929259) proposes Jev as a possible substitute without an implemented integration. An [access tutorial](https://x.com/harrisonitsme/status/2100799749192569167), learning materials, opinions and jokes do not become separate applications.
- Foreman’s main post had 685 likes in this pass. Reading its [pinned README](https://github.com/thruwire/foreman/blob/2c439828b9fe45ee5d40f6f57be81f7ff1f8a140/README.md) and repository tree clarified the supervision loop, but corresponding runtime image/video evidence was still not found; it remains pending.

**Scope:** X Latest search `Jev min_faves:200 since:2026-09-18`, reaching the previously included sponsor-skipping post, plus focused follow-up on Foreman and code-comment leads. New discoveries and older evidence promotions are identified separately; this is not exhaustive coverage of X. Deduplication checks main-post IDs, authors, tasks, videos and the existing catalog. Category comparisons are updated in both languages.

## 2026-09-18 · README timestamps

Added first-inclusion and latest-content-update times to all 77 bilingual introductions, indexes and detail pages, using Beijing time. Historical values come from Git content commits; regeneration does not advance them. No new cases or metric refreshes in this change. [Provenance](references/README.en.md#readme-times)

## 2026-09-18 · Third collection pass

Source-review cutoff: **2026-09-18 06:12:09 UTC (14:12:09 Asia/Shanghai)**. The catalog grows from 72 to **77 cases across 11 categories**: 5 new cases and 1 existing entry supplemented. The second-pass record below remains historical evidence rather than being overwritten.

| New application | Main-post likes snapshot | Deduplication and evidence |
| --- | ---: | --- |
| [YouTube sponsor skipping](cases/2026-09-18-youtube-sponsor-skip/README.en.md) | [238](https://x.com/tdinh_me/status/2100793777103466615) | Extension and same-repository web app are one project; distinct from hiding page ads. Pinned source reviewed; transcription adds cost |
| [Intent-driven spreadsheet](cases/2026-09-18-predictive-spreadsheet/README.en.md) | [337](https://x.com/dabit3/status/2100780008193020049) | Quotes the same author’s launcher but supplies its own video and row-rating task; author or quote identity alone does not make a duplicate |
| [Probably experimental language](cases/2026-09-18-probably-language/README.en.md) | [894](https://x.com/southpolesteve/status/2100767781868150938) | Combines judgments, branches and generation. Hosted examples replay recordings; custom programs need local model connections |
| [ESLint-description judgments](cases/2026-09-18-eslint-rule-judgments/README.en.md) | [351](https://x.com/mizchi/status/2100765201385869434) | A rule-level snippet experiment, distinct from PR review. The author’s reply limits the evaluation scope |
| [OpenCode intent permissions](cases/2026-09-18-opencode-intent-permissions/README.en.md) | [235](https://x.com/OpeOginni/status/2100702649834188855) | Previously pending at 160 likes; now promoted using the author’s qualifying main post. High-engagement reposts are not separately counted |

Main-post retrieval times: permissions, 06:07:34 UTC; sponsor skipping, Probably and ESLint, 06:08:49 UTC; spreadsheet, 06:08:50 UTC. See individual records and the shared catalog for exact sources and supplementary timestamps. Main posts and media are not duplicated. None of the new cases has been independently reproduced.

**Merged into an existing case:** [Teknium’s Cua quote](https://x.com/Teknium/status/2100783833419505941) announces planned testing only. It supplements [Cua · jev-use](cases/2026-09-18-cua-jev-use/README.en.md), without creating a “new integration.” GitHub API checks show #3916 still open and unmerged; #3943 remains an open, unmerged draft.

**Not counted as new applications:**

- [Chinese](https://x.com/SUOHA_AI/status/2100780634734002230) and [Japanese](https://x.com/k_matsumaru/status/2100767258415157493) compaction commentary points to the existing `fast-jev-compaction` project without a new independent implementation.
- [Sydney’s LangChain tutorial](https://x.com/sydneyrunkle/status/2100754364545761643) and [Harrison’s quote](https://x.com/hwchase17/status/2100773130041950570) cover one tutorial, retained as reference material. The article and its classification/routing examples are not each repackaged as separate applications.
- General opinions, stream announcements and other models that do not use TypeSafe Jev are excluded.

**Search scope:** X Latest search `Jev min_faves:200 since:2026-09-18`, scrolling back to the previously included launcher; revisited the below-threshold permissions lead. Read the ESLint and permissions threads, Sponsor Skip’s pinned source, Probably’s website and npm documentation. This includes earlier posts newly discovered or newly eligible in this pass and is not an exhaustive search.

All old main-post snapshots are preserved. An `updates` history field now prevents later generation from removing earlier case-update records.

## 2026-09-18 · Second collection pass

Source-review cutoff: **2026-09-18 02:43:33 UTC (10:43:33 Asia/Shanghai)**. The catalog grows from 67 to **72 cases across 11 categories**: 5 new cases and 4 existing entries supplemented. Likes are per-post retrieval snapshots, not live counts; existing main-post metrics were not refreshed in bulk.

### New cases

| Application | Why it is a separate case | Main-post likes snapshot |
| --- | --- | ---: |
| [Intent-aware predictive launcher](cases/2026-09-18-predictive-launcher/README.en.md) | Ranks file candidates by intent, a different task from browser clicks or OCR control | [252](https://x.com/dabit3/status/2100756930054504776) |
| [Live shopping assistant](cases/2026-09-18-live-commerce-assistant/README.en.md) | In-conversation recommendations and avatar expressions, distinct from offline support-intent classification | [217](https://x.com/rinte0321/status/2100736454850908344) |
| [Three-layer Minecraft system](cases/2026-09-18-minecraft-hybrid/README.en.md) | A separate game system combining Jev reactions, Astra planning and local policies | [354](https://x.com/wuyang_zhou/status/2100727660875808913) |
| [Live emoji suggestions](cases/2026-09-18-emoji-suggestions/README.en.md) | Chooses from an emoji set, distinct from character chat or pixel drawing | [230](https://x.com/riku720720/status/2100705558512963602) |
| [Voice-and-pointing canvas](cases/2026-09-18-voice-gesture-canvas/README.en.md) | Resolves spoken references through pointing to manipulate objects, distinct from TypeGPU audiovisual effects | [915](https://x.com/jackcheng/status/2100729670991802386) |

Each includes bilingual introductions, plain-language mechanisms, limitations and original source media. None has been independently reproduced. Minecraft’s main video is approximately 2× speed; the author’s original-speed version and explanation of the layers are included as supporting sources.

### Merged updates — no increase in case count

| Existing case | Update and deduplication basis |
| --- | --- |
| [Tool-history compaction](cases/2026-09-18-context-compaction/README.en.md) | The [author’s repository link](https://x.com/tamarajtran/status/2100694552369897539), [Alex’s usage report](https://x.com/altryne/status/2100739055923425589) and [Theo’s critique](https://x.com/theo/status/2100762304862384257) point to the same source or `tamaratran/fast-jev-compaction`. A pinned source revision clarifies budget fitting, omitted tool outputs and the recording animation that makes no API calls |
| [Viral-post classifier](cases/2026-09-18-viral-classifier/README.en.md) | The [author’s new video](https://x.com/robj3d3/status/2100722975645598191) quotes the original. Added the 61-question design, sample-size and cost claims; Jev + SuperX is not counted separately |
| [Voice-controlled browser](cases/2026-09-18-voice-browser/README.en.md) | The author’s [tutorial](https://x.com/moritzkremb/status/2100715237267660873) identifies the same use case at 5:59; merged as a supporting source |
| [Memory retrieval filtering](cases/2026-09-18-memory-retrieval/README.en.md) | The same tutorial identifies this use case at 11:33. A multi-example tutorial may support two existing records without becoming a new “tutorial app” |

[Rikuo’s compaction commentary](https://x.com/riku720720/status/2100716449568596261) also quotes the same original and supplies no new implementation evidence, so it receives no separate record.

### Pending evidence and integration news

- [OpenCode intent-aware permissions](https://x.com/OpeOginni/status/2100702649834188855): the author’s main post had **160 likes** at retrieval. A [repost](https://x.com/thdxr/status/2100723765718008238) exceeding a thousand likes does not replace the threshold. Kept in the inbox.
- The tutorial’s [YouTube predictor](https://x.com/moritzkremb/status/2100715237267660873) at 17:27 is a lead; its inputs, outputs and distinct implementation still need review before separate inclusion.
- [RAG-filtering suggestion](https://x.com/kushbhuwalka/status/2100731050075050485): 405 likes at retrieval but no concrete implementation media. A suggestion does not establish that RAG precision is “solved.”
- The [OpenRouter beta announcement](https://x.com/OpenRouter/status/2100744709589316009) and [TypeSafe repost](https://x.com/typesafeai/status/2100747035746193598) describe one integration, not two apps. The [Laravel AI SDK announcement](https://x.com/taylorotwell/status/2100700952923713641) links to merged [PR #1010](https://github.com/laravel/ai/pull/1010): developer support material, not an additional end-user application. No live service calls were tested.

### Search and deduplication scope

Used X Latest search `Jev min_faves:200 since:2026-09-17`, reviewing new results since the previous collection and scrolling back to the already-included compaction post. Checked post IDs, quote relationships, authors, project links and tasks. Examined the Minecraft, canvas and emoji threads. Metadata comes from the public FxTwitter API and may be cached. This is not exhaustive coverage of the search period, nor a claim that every video frame was reviewed.

New and updated slugs live in `latest_update` in the [shared catalog](data/catalog.json). Individual main and supporting posts retain exact retrieval timestamps. Future passes should compare these IDs and projects before adding records.

[All applications](README.en.md) · [Inbox](inbox/README.en.md) · [Evidence method](references/README.en.md)
