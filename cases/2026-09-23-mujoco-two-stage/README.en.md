# MuJoCo two-stage control: choose a goal, then move the arm

[简体中文](README.md) | **English**

> Separate task choice from robot-arm movement in simulation.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>An independent experiment retaining failure context and component roles, not another author’s MuJoCo demo.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#mujoco-two-stage)

## How it works, in plain English

First choose what to pick up, then decide how the arm and gripper should move.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@dimentary](https://x.com/dimentary) |
| Main post | [Source post](https://x.com/dimentary/status/2101018760371171420) |
| Published (UTC) | 2026-09-18T18:41:22+00:00 |
| Main-post likes snapshot | **626** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:34+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101018760371171420); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101017646154366976/img/02bH3Hxy9l0qEffS.jpg" width="640" alt="MuJoCo two-stage control: choose a goal, then move the arm preview">](https://x.com/dimentary/status/2101018760371171420)<br>[Video](https://x.com/dimentary/status/2101018760371171420)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2101017646154366976/vid/avc1/1600x900/SJmRemv2KFPa89oY.mp4?tag=29) (metadata duration: 20.3s)

Media source: [original publishing page](https://x.com/dimentary/status/2101018760371171420). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Separate task choice from robot-arm movement in simulation.

**Useful aspect (analysis):** Makes preprocessing and hierarchical control visible for comparison with single-step action selection.

## Inputs, steps and outputs

The author explicitly supplies simplified geometry and contacts as text, not images. Each update uses separate what-next and how-to-move calls.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports initial struggles and a two-call redesign, accompanied by a video. | Author report | [Post and attached media](https://x.com/dimentary/status/2101018760371171420) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101018760371171420) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No repeated grasp success, collision statistics or real-hardware results. Rendered simulation is not proof of visual control.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
