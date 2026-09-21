# Minecraft fixed route: planning plus bounded actions

[简体中文](README.md) | **English**

> Combine a planner, Jev and pathfinding code on a known route to the dragon.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟠 C · Claims exceed evidence**<br>The WASD/mouse claim conflicts with documented structured-state, higher-level actions. Treat this as a bounded route experiment, not general autonomous completion.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#minecraft-fixed-route)

## How it works, in plain English

Follow a surveyed map: the planner sets objectives, Jev picks an operation and pathfinding handles movement.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@rronak_](https://x.com/rronak_) |
| Main post | [Source post](https://x.com/rronak_/status/2101544156757950697) |
| Published (UTC) | 2026-09-20T05:29:06+00:00 |
| Main-post likes snapshot | **6,861** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-21T02:51:31+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101544156757950697); may be cached |
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101542497042481152/img/edco8P9wl-DUp5z8.jpg" width="640" alt="Minecraft fixed route: planning plus bounded actions preview">](https://x.com/rronak_/status/2101544156757950697)<br>[Video](https://x.com/rronak_/status/2101544156757950697)

The 39-second post and author reply form one case; full run evidence is absent from the repository.

- [Direct video 1](https://video.twimg.com/amplify_video/2101542497042481152/vid/avc1/1280x720/bpYI_EL7c3mp10Oq.mp4?tag=29) (metadata duration: 39.1s)

Media source: [original publishing page](https://x.com/rronak_/status/2101544156757950697). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Combine a planner, Jev and pathfinding code on a known route to the dragon.

**Useful aspect (analysis):** Inspectable route and control roles; a separate implementation from the existing Minecraft hybrid controller.

## Inputs, steps and outputs

Astra plans, Jev selects bounded actions and Mineflayer executes. A fixed seed and Peaceful difficulty use configured supply/active-portal coordinates plus a read-only dragon-position sensor.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports 8m43s and $0.01 Jev plus $0.96 Astra. Documentation adds surveyed routes and scripts; this catalog has not reproduced it. | Author report | [Post and attached media](https://x.com/rronak_/status/2101544156757950697) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101544156757950697) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @rronak_](https://x.com/rronak_/status/2101544158502728002): published 2026-09-20T05:29:06+00:00; 545 likes retrieved 2026-09-21T02:50:32+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101544158502728002).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/rmalde/minecraft-agent/blob/78b40ed59514e5e2abde33a05ce398ecb2c39e05/README.md)
- [Project / demo link 2](https://github.com/rmalde/minecraft-agent/blob/78b40ed59514e5e2abde33a05ce398ecb2c39e05/optimization/nether/config.json)

## Mechanism and comparison

Neither random-world exploration nor individual-key/screenshot control. Full video and action logs remain local to the author; the short public clip cannot establish the complete run or bill.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
