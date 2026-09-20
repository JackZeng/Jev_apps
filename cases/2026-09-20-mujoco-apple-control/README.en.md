# MuJoCo: three-model apple pick-and-place comparison

[简体中文](README.md) | **English**

> Move an apple onto a plate with a simulated arm and compare direction and gripper decisions.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Pinned sources disclose single-trial limits, controller responsibilities and replay timing. A indicates inspectability; this catalog ran neither verification nor physical robots.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#mujoco-apple-control)

## How it works, in plain English

The model directs movement and grasping; code solves joints and advances physics.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@openroboto](https://x.com/openroboto) |
| Main post | [Source post](https://x.com/openroboto/status/2101310974359941332) |
| Published (UTC) | 2026-09-19T14:02:31+00:00 |
| Main-post likes snapshot | **272** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:47:32+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101310974359941332); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101310940260270080/img/mCYBqjSwjUf4UV6d.jpg" width="640" alt="MuJoCo: three-model apple pick-and-place comparison preview">](https://x.com/openroboto/status/2101310974359941332)<br>[Video](https://x.com/openroboto/status/2101310974359941332)

The minute-long comparison and protocol replies form one case. Mini came from an earlier paired run with the same initial scene, not one simultaneous three-model run.

- [Direct video 1](https://video.twimg.com/amplify_video/2101310940260270080/vid/avc1/1280x720/7XlK_MEooTisJ5Ry.mp4?tag=29) (metadata duration: 59.2s)

Media source: [original publishing page](https://x.com/openroboto/status/2101310974359941332). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Move an apple onto a plate with a simulated arm and compare direction and gripper decisions.

**Useful aspect (analysis):** Unlike a short dual-arm demo, this publishes responses, trajectories, source snapshots, success criteria and an offline verification entry point.

## Inputs, steps and outputs

Each pinned-version cycle makes two requests: intent, then XYZ signs and open/hold/close. Inputs are simulator geometry and contact feedback. Shared code handles step size, IK and physics, not camera perception or generated joint torques.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| Recorded results: Jev completed in 181.847s for $0.018825; GPT-6 Astra in 707.274s for $5.933624; GPT-4.1 mini reached 160 cycles. The roughly 1/315 cost applies only to these records. | Author report | [Results documentation](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/README.md) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101310974359941332) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @openroboto](https://x.com/openroboto/status/2101310978856276075): published 2026-09-19T14:02:32+00:00; 16 likes retrieved 2026-09-20T02:53:28+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101310978856276075).
- [Supporting post by @openroboto](https://x.com/openroboto/status/2101310983931040038): published 2026-09-19T14:02:33+00:00; 13 likes retrieved 2026-09-20T02:53:28+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101310983931040038).
- [Supporting post by @openroboto](https://x.com/openroboto/status/2101382220690895046): published 2026-09-19T18:45:37+00:00; 8 likes retrieved 2026-09-20T02:53:28+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101382220690895046).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/README.md)
- [Project / demo link 2](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/docs/RESULTS.md)
- [Project / demo link 3](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/incremental_policy.py)
- [Project / demo link 4](https://github.com/openroboto-ai/jev-robot-control/blob/7a4ed8b72c3c17d7aa790678ed9660df67c10dd3/verify_replay.py)

## Mechanism and comparison

Only one seed-0 trial per controller, so success rates are unknown. Replay synchronizes simulation time and removes API waits; video duration is not task wall time.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
