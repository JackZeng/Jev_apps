# Corent: use different routing thresholds for different costs

[简体中文](README.md) | **English**

> Use workload, quality requirements and cost to select a model or fall back.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Clear component roles, but model count and probabilities do not prove optimal selection.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#corent-router)

## How it works, in plain English

Expensive production mistakes warrant different review thresholds from inexpensive ones.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@corentAI](https://x.com/corentAI) |
| Main post | [Source post](https://x.com/corentAI/status/2100965880242770423) |
| Published (UTC) | 2026-09-18T15:11:14+00:00 |
| Main-post likes snapshot | **326** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:38+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100965880242770423); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100964784581525504/img/S0fJrRk_X0OFZhdh.jpg" width="640" alt="Corent: use different routing thresholds for different costs preview">](https://x.com/corentAI/status/2100965880242770423)<br>[Video](https://x.com/corentAI/status/2100965880242770423)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2100964784581525504/vid/avc1/3840x2160/8UGaVvQfucoJ9qiX.mp4?tag=29) (metadata duration: 38.5s)

Media source: [original publishing page](https://x.com/corentAI/status/2100965880242770423). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use workload, quality requirements and cost to select a model or fall back.

**Useful aspect (analysis):** Emphasizes the cost of routing mistakes instead of one universal threshold.

## Inputs, steps and outputs

The official post describes Jev assessing prompts, workloads, quality and confidence, applying task-specific thresholds and fallback when confidence is low.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| Shows decisions preceding generation, without a public quality/cost comparison. | Author report | [Post and attached media](https://x.com/corentAI/status/2100965880242770423) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100965880242770423) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://corent.tech)

## Mechanism and comparison

A thousand-plus models describes platform scale, not validated routing coverage. Calibration, fallback targets and misrouting losses are undisclosed.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
