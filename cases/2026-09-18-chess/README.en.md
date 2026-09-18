# 5+0 blitz chess

[简体中文](README.md) | **English**

> Compare model playing strength and decision speed in timed chess.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 07:24:03 (Beijing time, UTC+08:00)

## How it works, in plain English

Every model call consumes time on the chess clock. Jev wins one game on time but is checkmated in another, separating speed from playing strength.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@aimlapi](https://x.com/aimlapi) |
| Main post | [Source post](https://x.com/aimlapi/status/2100372930282573876) |
| Published (UTC) | 2026-09-16T23:55:04+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 07:24:03 |
| Main-post likes snapshot | **1,985** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:28.166587+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100372930282573876); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | V13 (as labeled by the author) |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100371773275406336/img/NmHPy0pAprSsC6Gi.jpg" width="640" alt="5+0 blitz chess preview">](https://x.com/aimlapi/status/2100372930282573876)<br>[Video](https://x.com/aimlapi/status/2100372930282573876)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100371773275406336/vid/avc1/1080x1920/uIu9G9yNLoxTTYIE.mp4?tag=29) (metadata duration: 99.7s)

Media source: [original publishing page](https://x.com/aimlapi/status/2100372930282573876). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Compare model playing strength and decision speed in timed chess.

**Useful aspect (analysis):** Exposes the trade-off between speed and playing strength, including a losing game.

## Inputs, steps and outputs

One model API call per move under a five-minute, no-increment time control.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author says Jev beat Fable on time from a losing position, then was checkmated by Astra on move 18. | Author report | [Post and attached media](https://x.com/aimlapi/status/2100372930282573876) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100372930282573876) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Limited games and opponent configurations; winning on time does not establish superior chess strength.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
