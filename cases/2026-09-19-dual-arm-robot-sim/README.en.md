# Dual-arm robot simulation: layered action decisions

[简体中文](README.md) | **English**

> Manipulate blocks in simulation, with Jev handling the middle decision layer.

**Content updated:** 2026-09-19 17:48:49 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Layer descriptions and simulation media support a prototype; speed, cost and transfer to hardware remain unverified.<br>[Assessment and sources](../../references/2026-09-19-increment7-audit.en.md#dual-arm-robot-sim)

## How it works, in plain English

Like a supervisor choosing which block to move while an engineer calculates arm motion: decisions, joint solving and physics have separate roles.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@Raptor_zip](https://x.com/Raptor_zip) |
| Main post | [Source post](https://x.com/Raptor_zip/status/2101091398447505567) |
| Published (UTC) | 2026-09-18T23:30:00+00:00 |
| Main-post likes snapshot | **229** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-19T09:42:43+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101091398447505567); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101070240444772353/img/Ci_PCLcMigmoAdks.jpg" width="640" alt="Dual-arm robot simulation: layered action decisions preview">](https://x.com/Raptor_zip/status/2101091398447505567)<br>[Video](https://x.com/Raptor_zip/status/2101091398447505567)

An approximately 87-second video and three explanatory images form one case; physical deployment is not claimed by this catalog.

- [Direct video 1](https://video.twimg.com/amplify_video/2101070240444772353/vid/avc1/1280x610/Euxtwn2wm6-HBwU3.mp4?tag=29) (metadata duration: 87.1s)
- [Original image 2](https://pbs.twimg.com/media/HSiAQHCawAALmiU.jpg?name=orig)
- [Original image 3](https://pbs.twimg.com/media/HSiAQHLbIAAHYLu.jpg?name=orig)
- [Original image 4](https://pbs.twimg.com/media/HSiAQGyagAAlj5V.jpg?name=orig)

Media source: [original publishing page](https://x.com/Raptor_zip/status/2101091398447505567). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Manipulate blocks in simulation, with Jev handling the middle decision layer.

**Useful aspect (analysis):** Like drone simulation, this separates decisions from motion computation, but explores object selection and dual-arm manipulation.

## Inputs, steps and outputs

The author assigns layer two of three to Jev, with inverse kinematics and physics in code. Media shows simulated arms, blocks and an instruction panel.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports roughly 500ms response and ¥0.5 per trial; timing and full cost were not independently checked. | Author report | [Post and attached media](https://x.com/Raptor_zip/status/2101091398447505567) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101091398447505567) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No physical-robot deployment or complete success-rate evaluation. A roughly 500ms response is not a joint-control period or full task duration.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
