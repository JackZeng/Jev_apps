# Monid: add batch decisions to tool workflows

[简体中文](README.md) | **English**

> Connect lead scoring and video screening to an agent’s tool workflow.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Two authors’ Monid demos form one case; clear tasks, without general speed or quality guarantees.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#monid-jev-tools)

## How it works, in plain English

Tools gather material, Jev sorts it and the agent continues the task.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@shengkunye](https://x.com/shengkunye) |
| Main post | [Source post](https://x.com/shengkunye/status/2102112693041938825) |
| Published (UTC) | 2026-09-21T19:08:16+00:00 |
| Main-post likes snapshot | **238** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:31:25+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102112693041938825); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102112249112604672/img/3lR6gxILRYKTiMF_.jpg" width="640" alt="Monid: add batch decisions to tool workflows preview">](https://x.com/shengkunye/status/2102112693041938825)<br>[Video](https://x.com/shengkunye/status/2102112693041938825)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2102112249112604672/vid/avc1/1920x1080/2uBaqEr_8A6mJe4N.mp4?tag=29) (metadata duration: 32.3s)

Media source: [original publishing page](https://x.com/shengkunye/status/2102112693041938825). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Connect lead scoring and video screening to an agent’s tool workflow.

**Useful aspect (analysis):** Focuses on batch processing after tools retrieve data, rather than only model selection.

## Inputs, steps and outputs

The author explicitly says the agent selects tools. Jev accelerates decisions; another Monid demo scores 60 TikToks, with preprocessing unspecified.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The video-screening demo reports 1.9 seconds and $0.0022 for 60 items, retained only as author figures. | Author report | [Results documentation](https://x.com/Jasperli0122/status/2102140451763749077) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102112693041938825) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @Jasperli0122](https://x.com/Jasperli0122/status/2102140451763749077): published 2026-09-21T20:58:34+00:00; 204 likes retrieved 2026-09-23T04:31:26+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2102140451763749077). [Supplementary media 1](https://video.twimg.com/amplify_video/2102138973145706496/vid/avc1/3840x2160/TSFiq7OeulsdvSE2.mp4?tag=29)

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

2,000 describes the tool catalog, not verified task coverage. The 30-fold claim lacks a full baseline; transcription and visual-processing costs are unknown.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
