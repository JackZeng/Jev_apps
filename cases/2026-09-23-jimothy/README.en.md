# Jimothy: teach a local classifier from Jev examples

[简体中文](README.md) | **English**

> Collect Jev decisions for a specific task and train a small classifier for local browser or server use.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A covers inspectable data and training roles. Student inference speed is not full-pipeline speed, and teacher errors may be inherited.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#jimothy)

## How it works, in plain English

A teacher marks examples, then a specialist apprentice learns that particular kind of question.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@AndrewPrifer](https://x.com/AndrewPrifer) |
| Main post | [Source post](https://x.com/AndrewPrifer/status/2102162296739099126) |
| Published (UTC) | 2026-09-21T22:25:22+00:00 |
| Main-post likes snapshot | **367** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T03:56:58+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102162296739099126); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102161913723691008/img/elm99ez4yx84JJO2.jpg" width="640" alt="Jimothy: teach a local classifier from Jev examples preview">](https://x.com/AndrewPrifer/status/2102162296739099126)<br>[Video](https://x.com/AndrewPrifer/status/2102162296739099126)

A 21-second demo with pinned teacher interface and training documentation; no training or exported inference was run.

- [Direct video 1](https://video.twimg.com/amplify_video/2102161913723691008/vid/avc1/908x714/hZWNZe-tLGn2woXE.mp4?tag=29) (metadata duration: 21.9s)

Media source: [original publishing page](https://x.com/AndrewPrifer/status/2102162296739099126). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Collect Jev decisions for a specific task and train a small classifier for local browser or server use.

**Useful aspect (analysis):** Useful for repetitive, stable classification tasks; provides training and export tooling beyond a one-off teacher-data experiment.

## Inputs, steps and outputs

Read saved labels or call Jev through Gateway with response caching. Train a head on MiniLM features or TF-IDF, separating model selection, calibration and acceptance-threshold evaluation.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The post claims 15–45MB and 10–20-fold speedups. Repository timing examples use warmed single-input inference on an M3 Max, excluding loading, teacher collection and training. | Author report | [Results documentation](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/README.md) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102162296739099126) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/README.md)
- [Project / demo link 2](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/src/teacher.ts)
- [Project / demo link 3](https://github.com/AndrewPrifer/jimothy/blob/f2ad9b40b88ea913d38fda758e564eac5f12fc0b/docs/automatic-training.md)

## Mechanism and comparison

The local student is not Jev weights. Applications must implement Jev fallback. Thresholds measure agreement with supplied labels, not guaranteed correctness or robustness to changed data.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
