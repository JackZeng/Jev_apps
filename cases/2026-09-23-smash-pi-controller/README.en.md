# Smash Bros.: Raspberry Pi inputs and Jev move selection

[简体中文](README.md) | **English**

> Read captured gameplay, select moves with Jev and execute controller inputs through hardware.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author reports weaknesses; supports limited control, not high-level competitive play.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#smash-pi-controller)

## How it works, in plain English

An observer reports positions, a controller chooses a move and the gamepad executes it.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@aokiti_tech](https://x.com/aokiti_tech) |
| Main post | [Source post](https://x.com/aokiti_tech/status/2102123079912808849) |
| Published (UTC) | 2026-09-21T19:49:32+00:00 |
| Main-post likes snapshot | **249** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:31:26+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102123079912808849); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102119468684206080/img/i92SVpUsgqxaubUr.jpg" width="640" alt="Smash Bros.: Raspberry Pi inputs and Jev move selection preview">](https://x.com/aokiti_tech/status/2102123079912808849)<br>[Video](https://x.com/aokiti_tech/status/2102123079912808849)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2102119468684206080/vid/avc1/1226x720/QXnO__ZCDmQeGlrb.mp4?tag=14) (metadata duration: 41.5s)

Media source: [original publishing page](https://x.com/aokiti_tech/status/2102123079912808849). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Read captured gameplay, select moves with Jev and execute controller inputs through hardware.

**Useful aspect (analysis):** Connects perception, decisions and physical inputs for studying hardware-loop latency.

## Inputs, steps and outputs

The earlier post describes Pi 5 controller operation and OpenCV capture detection. The follow-up reports 2–3 Jev decisions per second using distance and direction.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| Hardware preparation and the later Jev gameplay demo are grouped as one project. | Author report | [Post and attached media](https://x.com/aokiti_tech/status/2102123079912808849) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102123079912808849) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @aokiti_tech](https://x.com/aokiti_tech/status/2101506737417363546): published 2026-09-20T03:00:24+00:00; 31 likes retrieved 2026-09-23T04:32:45+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101506737417363546). [Supplementary media 1](https://pbs.twimg.com/media/HSoMQJKbYAAqZoG.jpg?name=orig)

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The author says it is very weak against CPU level 8. Exact features, action candidates and sustained win rates are undisclosed.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
