# Ori Eval: compare 30-way request classification

[简体中文](README.md) | **English**

> Classify requests into 30 task types and compare five models on speed, cost and correctness.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The task and important limits are stated, but a small synthetic set and incomplete reproduction materials restrict the conclusions.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#ori-task-classification)

## How it works, in plain English

Like sorting the same letters into 30 inboxes and comparing mistakes and time.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@OpenRouter](https://x.com/OpenRouter) |
| Main post | [Source post](https://x.com/OpenRouter/status/2101412965765529853) |
| Published (UTC) | 2026-09-19T20:47:48+00:00 |
| Main-post likes snapshot | **329** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:45:53+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101412965765529853); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSm39ISbsAAEPfg.png?name=orig" width="640" alt="Ori Eval: compare 30-way request classification preview">](https://x.com/OpenRouter/status/2101412965765529853)<br>[Image](https://x.com/OpenRouter/status/2101412965765529853)

The main chart and four methodological/results replies form one request-classification experiment, not a general agent-quality judge.

- [Original image 1](https://pbs.twimg.com/media/HSm39ISbsAAEPfg.png?name=orig)

Media source: [original publishing page](https://x.com/OpenRouter/status/2101412965765529853). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Classify requests into 30 task types and compare five models on speed, cost and correctness.

**Useful aspect (analysis):** Discloses the task, sample size, synthetic origin and some settings, and acknowledges that Jev is not the cheapest model.

## Inputs, steps and outputs

OpenRouter describes sequential, stateless evaluation on the same 200 synthetic cases. LLM reasoning was off except for GLM 5.3 Flash, which ran at low effort.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports over five times the speed of the runner-up, accuracy within a few cases across models, and second-lowest cost behind Qwen3.8 Flash. | Author report | [Post and attached media](https://x.com/OpenRouter/status/2101412965765529853) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101412965765529853) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @OpenRouter](https://x.com/OpenRouter/status/2101412983297778130): published 2026-09-19T20:47:52+00:00; 29 likes retrieved 2026-09-20T02:53:54+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101412983297778130). [Supplementary media 1](https://pbs.twimg.com/media/HSm3-K6acAAqfK-.png?name=orig)
- [Supporting post by @OpenRouter](https://x.com/OpenRouter/status/2101413000725074212): published 2026-09-19T20:47:56+00:00; 23 likes retrieved 2026-09-20T02:53:54+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101413000725074212). [Supplementary media 1](https://pbs.twimg.com/media/HSm3_MDbUAAfPs4.png?name=orig)
- [Supporting post by @OpenRouter](https://x.com/OpenRouter/status/2101413013941330371): published 2026-09-19T20:47:59+00:00; 13 likes retrieved 2026-09-20T02:53:54+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101413013941330371).
- [Supporting post by @OpenRouter](https://x.com/OpenRouter/status/2101413025572172201): published 2026-09-19T20:48:02+00:00; 9 likes retrieved 2026-09-20T02:53:54+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101413025572172201).

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Complete examples, per-case labels and repeated runs are absent. Default provider routing affects some tail latencies, limiting production generalization.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
