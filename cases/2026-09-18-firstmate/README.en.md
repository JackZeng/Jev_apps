# Firstmate task dispatch

[简体中文](README.md) | **English**

> Choose an AI worker and effort level based on the task and user preferences.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author discloses 25 matching dispatch decisions and separates dispatch overhead. This is bounded self-reported evidence, not proof of equivalent task quality or whole-agent savings.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#firstmate)

## How it works, in plain English

A dispatcher chooses the worker, tool setup and effort level. Jev replaces that dispatch step; other agents still perform the task.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@kunchenguid](https://x.com/kunchenguid) |
| Main post | [Source post](https://x.com/kunchenguid/status/2100468943853085061) |
| Published (UTC) | 2026-09-17T06:16:35+00:00 |
| Main-post likes snapshot | **1,615** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:23.394737+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100468943853085061); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSYK_gbagAAqKqr.jpg?name=orig" width="640" alt="Firstmate task dispatch preview">](https://x.com/kunchenguid/status/2100468943853085061)<br>[Image](https://x.com/kunchenguid/status/2100468943853085061)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Original image 1](https://pbs.twimg.com/media/HSYK_gbagAAqKqr.jpg?name=orig)

Media source: [original publishing page](https://x.com/kunchenguid/status/2100468943853085061). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Choose an AI worker and effort level based on the task and user preferences.

**Useful aspect (analysis):** Routes both execution environment and model configuration within an existing agent orchestrator.

## Inputs, steps and outputs

Jev replaces the LLM-driven rule-reading and dispatch step; the parent agent still invokes Jev through a tool call.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports agreement on 25 tasks and reductions of 71% in cost and 90% in elapsed time for the entire dispatch stage. | Author report | [Post and attached media](https://x.com/kunchenguid/status/2100468943853085061) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100468943853085061) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Agreement with Fable on 25 tasks is small-sample decision agreement, not task-outcome accuracy.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
