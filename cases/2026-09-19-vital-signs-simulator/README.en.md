# Vital-sign simulation: judging state changes

[简体中文](README.md) | **English**

> Compare rule alarms with Jev judgments in normal-state and slow-heart-rate simulations.

**Content updated:** 2026-09-19 17:48:49 (Beijing time, UTC+08:00)

**🟠 C · Claims exceed evidence**<br>Two simulations do not support readiness for practical use. Repeatability, confidence and clinical event probability are different validation targets.<br>[Assessment and sources](../../references/2026-09-19-increment7-audit.en.md#vital-signs-simulator)

## How it works, in plain English

Like a practice drill for a monitor: compare judgments on simulated measurements. Model confidence is not a clinically validated event probability.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@roiyaruRIZ](https://x.com/roiyaruRIZ) |
| Main post | [Source post](https://x.com/roiyaruRIZ/status/2101130711067431018) |
| Published (UTC) | 2026-09-19T02:06:13+00:00 |
| Main-post likes snapshot | **216** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-19T09:41:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101130711067431018); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101125501234630656/img/pxMddfrpMLTvBhaR.jpg" width="640" alt="Vital-sign simulation: judging state changes preview">](https://x.com/roiyaruRIZ/status/2101130711067431018)<br>[Video](https://x.com/roiyaruRIZ/status/2101130711067431018)

Both videos belong to one simulator. Replies about practical use and calibration support the assessment, not separate cases.

- [Direct video 1](https://video.twimg.com/amplify_video/2101125501234630656/vid/avc1/1920x1080/xuiPCOamd2CeqyKA.mp4?tag=29) (metadata duration: 44.0s)
- [Direct video 2](https://video.twimg.com/amplify_video/2101125604217442304/vid/avc1/1920x1080/J2CRrrXoNgVF0g-P.mp4?tag=29) (metadata duration: 45.9s)

Media source: [original publishing page](https://x.com/roiyaruRIZ/status/2101130711067431018). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Compare rule alarms with Jev judgments in normal-state and slow-heart-rate simulations.

**Useful aspect (analysis):** Unlike traffic or robotics control, this explores state assessment and false alarms; scenarios can inform later evaluation questions.

## Inputs, steps and outputs

Two clips include movement artifacts and a slow-heart-rate scenario. Complete inputs, prediction horizon, reference labels and thresholds are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports better simulated behavior and says in a reply that it could be used in practice. Evidence is limited to two roughly 44/46-second simulation clips. | Author report | [Post and attached media](https://x.com/roiyaruRIZ/status/2101130711067431018) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101130711067431018) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @roiyaruRIZ](https://x.com/roiyaruRIZ/status/2101131147346690267): published 2026-09-19T02:07:57+00:00; 2 likes retrieved 2026-09-19T09:45:18+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101131147346690267).
- [Supporting post by @roiyaruRIZ](https://x.com/roiyaruRIZ/status/2101179451291947185): published 2026-09-19T05:19:53+00:00; 4 likes retrieved 2026-09-19T09:45:18+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101179451291947185).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://docs.typesafe.ai/confidence)

## Mechanism and comparison

No clinical dataset, independent validation or missed-event statistics was provided. The author’s repeatability-based explanation of calibration does not establish risk-probability validity.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
