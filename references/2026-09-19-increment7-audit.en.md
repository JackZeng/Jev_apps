# Increment 7: sources and claim assessments
 
[中文 / English](2026-09-19-increment7-audit.md)

**Review cutoff: 2026-09-19 17:48:49 Beijing time.**

Six independent additions and one merged update bring the catalog from 106 to 112 cases. Current assessments: A 19, B 79, C 14. These labels assess specific claims, not reproduction or overall authenticity. Nothing was independently run.

## Discovery and deduplication

Searched X Latest for `Jev min_faves:200 since:2026-09-18`, continuing into the prior cutoff overlap. Checked original posts, media, selected author replies and pinned code. Public FxTwitter metadata supplies exact like snapshots; it is a third-party mirror and can lag. This is a bounded search, not an exhaustive export.

Deduplication uses main-post IDs, author/project identity, repositories and media. Claude Code and Codex routers are independent implementations in one category. Sac’s source release is merged into the existing Calendar case, preserving its original post, likes and first-added timestamp. The robot’s four media attachments and the vital-sign simulator’s two clips each form one case.

Excluded local imitation models, gateway announcements, opinions, tutorial quote-posts and satire. Kun Chen’s “chat too” thread contains a humorous clip rather than evidence of a new implementation. Alan Daitch’s voice-control clip remains in the inbox until its original implementation is established.

<a id="claude-code-jev-router"></a>

## Claude Code Mod: model and effort routing · A

Pinned source exposes hooks, defaults and fallback. Main-model behavior differs from the post’s description; savings remain unverified.

**Evidence:** Pinned code classifies at prompt submission and applies decisions at model requests and subagent creation. Subagent-model and main-effort routing default on; main-model switching defaults off. This differs from the post’s session-start-only description; the pinned implementation takes precedence.

**Limits:** No complete quality, cache-cost or savings comparison. Without a Jev key, the host classifier is used, so that path is not evidence of Jev performance.

**Author report:** The post includes a roughly 25-second video; source supports TypeSafe or Vercel Gateway. It establishes a routing mechanism, not cheaper equivalent-quality completion.

Sources: [X @dani_avila7](https://x.com/dani_avila7/status/2101176629745561686) · [Reference 1](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/README.md) · [Reference 2](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/hooks/jev-model-router.ts)

Main-post snapshot: **417 likes**, 2026-09-19T09:41:40+00:00; [metadata source](https://api.fxtwitter.com/status/2101176629745561686).

<a id="synthetic-interview-classifier"></a>

## Synthetic interview notes: batch classification and scoring · B

Explicitly fictional data supports a batch-classification demo; independent labels and error statistics are missing.

**Evidence:** The author describes three outcomes, three scoring dimensions and serious-concern flags. Full prompts, rubrics and reference labels were not established.

**Limits:** No evidence of real hiring validity, fairness or label agreement; the demo does not justify automated personnel selection.

**Author report:** The author reports 12.8 seconds and $0.005 for 100 fictional records: one batch test, not an accuracy evaluation.

Sources: [X @masa_okamura108](https://x.com/masa_okamura108/status/2101206603240477030)

Main-post snapshot: **278 likes**, 2026-09-19T09:41:40+00:00; [metadata source](https://api.fxtwitter.com/status/2101206603240477030).

<a id="traffic-light-city"></a>

## Jev City: nine-intersection traffic simulation · C

The over-600% claim lacks matched controller baselines and repeated statistics. The simulation interface does not establish real-world traffic gains.

**Evidence:** The display shows nine junctions, north/south versus east/west decisions and confidence, an on/off control and wait curves. Full state encoding and the off-mode baseline were not established.

**Limits:** Matched traffic demand, seeds, repeated trials and fixed/adaptive rule baselines are missing. A virtual network does not establish real-city outcomes.

**Author report:** The author claims average waiting rises by over 600% when Jev is switched off; a 73-second clip and public entry point do not verify that ratio.

Sources: [X @leojrr](https://x.com/leojrr/status/2101161666410893328) · [X 2101165998086783170](https://x.com/leojrr/status/2101165998086783170) · [Reference 1](https://01a0b7a9-5619-7ec6-a0d8-fb357ed42aa3.skydive.app/)

Main-post snapshot: **1081 likes**, 2026-09-19T09:41:40+00:00; [metadata source](https://api.fxtwitter.com/status/2101161666410893328).

<a id="vital-signs-simulator"></a>

## Vital-sign simulation: judging state changes · C

Two simulations do not support readiness for practical use. Repeatability, confidence and clinical event probability are different validation targets.

**Evidence:** Two clips include movement artifacts and a slow-heart-rate scenario. Complete inputs, prediction horizon, reference labels and thresholds are undisclosed.

**Limits:** No clinical dataset, independent validation or missed-event statistics was provided. The author’s repeatability-based explanation of calibration does not establish risk-probability validity.

**Author report:** The author reports better simulated behavior and says in a reply that it could be used in practice. Evidence is limited to two roughly 44/46-second simulation clips.

Sources: [X @roiyaruRIZ](https://x.com/roiyaruRIZ/status/2101130711067431018) · [X 2101131147346690267](https://x.com/roiyaruRIZ/status/2101131147346690267) · [X 2101179451291947185](https://x.com/roiyaruRIZ/status/2101179451291947185) · [Reference 1](https://docs.typesafe.ai/confidence)

Main-post snapshot: **216 likes**, 2026-09-19T09:41:40+00:00; [metadata source](https://api.fxtwitter.com/status/2101130711067431018).

TypeSafe’s documentation describes confidence as a statistic derived from answer distributions and recommends task-specific validation. It does not certify probabilities of clinical deterioration; that distinction is this catalog’s inference from the documented definition and missing clinical evidence.

<a id="dual-arm-robot-sim"></a>

## Dual-arm robot simulation: layered action decisions · B

Layer descriptions and simulation media support a prototype; speed, cost and transfer to hardware remain unverified.

**Evidence:** The author assigns layer two of three to Jev, with inverse kinematics and physics in code. Media shows simulated arms, blocks and an instruction panel.

**Limits:** No physical-robot deployment or complete success-rate evaluation. A roughly 500ms response is not a joint-control period or full task duration.

**Author report:** The author reports roughly 500ms response and ¥0.5 per trial; timing and full cost were not independently checked.

Sources: [X @Raptor_zip](https://x.com/Raptor_zip/status/2101091398447505567)

Main-post snapshot: **229 likes**, 2026-09-19T09:42:43+00:00; [metadata source](https://api.fxtwitter.com/status/2101091398447505567).

<a id="ryze-seo-geo"></a>

## Ryze AI: SEO/GEO audits and fixes · C

The 90% savings, 20–30-fold speedups and citation claims lack complete controlled evidence; the short clip does not establish these outcomes.

**Evidence:** The author lists data reads, citation-source analysis, content gaps and page fixes, without specifying Jev calls or the division among retrieval, judgment, generation and execution.

**Limits:** Complete baselines, quality checks, end-to-end bills and search outcomes are absent. Classification alone does not establish faster page generation or guaranteed AI citations.

**Author report:** The author claims a 90% cost reduction from roughly $250, 30-fold gains across several stages and 20-fold faster page creation. A six-second interface clip does not establish those comparisons.

Sources: [X @irabukht](https://x.com/irabukht/status/2101090579127951694) · [X 2101123317327372487](https://x.com/irabukht/status/2101123317327372487)

Main-post snapshot: **790 likes**, 2026-09-19T09:42:43+00:00; [metadata source](https://api.fxtwitter.com/status/2101090579127951694).

<a id="sac-calendar-computer-use"></a>

## Sac: Codex + Jev for Mac Calendar · C

Text candidates and execution roles are inspectable, but the new fastest-in-Codex comparison lacks a matched benchmark. C addresses that superlative, not prototype existence.

**Evidence:** The newly published version extracts text candidates from the accessibility tree. Jev judges targets, actions, completion and risk; Codex Computer Use observes and executes. Code checks candidate validity, confidence and policy gates. Sending text instead of screenshots does not mean offline processing.

**Limits:** One calendar demo does not establish average speedup, success rate or total cost. Source improves inspectability, but the new fastest-in-Codex claim lacks a matched task benchmark. This catalog has not run the tool.

**Author report:** The author shares a roughly 51-second video labeled 1× playback, reports smoother operation with similar token usage, and clarifies in a reply that Jev makes judgments within existing computer use. The update publishes Jev-cu and claims larger gains for tasks with frequent decisions and tool calls, without a new reproducible timing comparison.

Sources: [X @Saccc_c](https://x.com/Saccc_c/status/2100864907046768890) · [X 2100895536119488734](https://x.com/Saccc_c/status/2100895536119488734) · [X 2100899012727673107](https://x.com/Saccc_c/status/2100899012727673107) · [X 2101152089598791845](https://x.com/Saccc_c/status/2101152089598791845) · [Reference 1](https://github.com/Sac-Y/Jev-cu) · [Reference 2](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/README.md) · [Reference 3](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/scripts/loop.mjs) · [Reference 4](https://github.com/Sac-Y/Jev-cu/blob/38fb31de7dfe6209bbe6e04057c00c6e885ba577/scripts/policy.mjs)

The earlier B assessment covered one Calendar demonstration. The new C assessment specifically addresses the source-release post’s strongest speed superlative; newly inspectable architecture is a positive evidence update.

The earlier [106-case audit](2026-09-19-claims-audit.en.md) remains a historical snapshot. Only these seven cases receive new content-update times.
