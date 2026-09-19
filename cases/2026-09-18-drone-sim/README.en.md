# Jev drone simulation

[简体中文](README.md) | **English**

> Fly through simulated obstacles with Jev choosing tactics and code stabilizing the drone.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>The pinned documentation separates symbolic perception, classical control, safety vetoes and Jev advice, and discloses failures. It supports a narrow simulated hybrid-system result, not physical deployment or general superiority.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#drone-sim) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Like a navigator working with a flight controller, code summarizes camera information, Jev chooses maneuvers, and faster control/safety loops constrain the actions.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@RomanSlack1](https://x.com/RomanSlack1) |
| Main post | [Source post](https://x.com/RomanSlack1/status/2100335978229690683) |
| Published (UTC) | 2026-09-16T21:28:14+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **330** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:29.328700+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100335978229690683); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100335726097494016/img/EljFdjduS88MyP9d.jpg" width="640" alt="Jev drone simulation preview">](https://x.com/RomanSlack1/status/2100335978229690683)<br>[Video](https://x.com/RomanSlack1/status/2100335978229690683)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100335726097494016/vid/avc1/1324x720/349M_-yqAXZTf5Yd.mp4?tag=14) (metadata duration: 48.0s)

Media source: [original publishing page](https://x.com/RomanSlack1/status/2100335978229690683). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Fly through simulated obstacles with Jev choosing tactics and code stabilizing the drone.

**Useful aspect (analysis):** Publishes perception, tactical decision and flight-control layers, including a baseline and failure boundaries.

## Inputs, steps and outputs

Project README: local code converts camera depth/segmentation buffers to symbolic scenes → Jev judges maneuvers, risk and target loss → ordinary code executes; control and safety run independently at higher rates.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports about 15 minutes of setup and $0.10 spent. | Author report | [Post and attached media](https://x.com/RomanSlack1/status/2100335978229690683) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100335978229690683) | Snapshot at the recorded time, not a live count |

**Repository cross-check (2026-09-18)**: The [pinned README](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/README.md) specifies MuJoCo, symbolic camera scenes and layered control. Jev does not receive images directly, and safety code can override its actions in the main setup. The author also discloses a single-run result, an earlier comparison with no advantage and an unreliable tunnel experiment. This is a documentation review, not a reproduction.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/RomanSlack/jev-drone)
- [Project / demo link 2](https://github.com/RomanSlack/jev-drone/blob/cbeb53ce4f17a06ea490ae43effcdad231143610/README.md)

## Mechanism and comparison

MuJoCo simulation, not a real flight. The main successful comparison is a single run; an earlier seed-matched test showed no advantage over the baseline.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
