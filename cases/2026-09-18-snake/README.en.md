# Step-by-step Snake

[简体中文](README.md) | **English**

> Ask Jev for the next move at every step of Snake.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The per-step loop and arithmetic are coherent as an author-reported run; the extrapolated price and gameplay quality are not independently established.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#snake) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Repeat a simple loop: read the state, ask for a direction, move one step. Each extra move adds a request, so costs grow with game length.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@chenchengpro](https://x.com/chenchengpro) |
| Main post | [Source post](https://x.com/chenchengpro/status/2100516953496670430) |
| Published (UTC) | 2026-09-17T09:27:22+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **204** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:27.634923+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100516953496670430); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100516335155646464/img/pow4ZDKeRwkBVSvy.jpg" width="640" alt="Step-by-step Snake preview">](https://x.com/chenchengpro/status/2100516953496670430)<br>[Video](https://x.com/chenchengpro/status/2100516953496670430)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100516335155646464/vid/avc1/1260x1080/k8rDO956Lzrwy1tt.mp4?tag=29) (metadata duration: 27.3s)

Media source: [original publishing page](https://x.com/chenchengpro/status/2100516953496670430). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Ask Jev for the next move at every step of Snake.

**Useful aspect (analysis):** A simple loop for studying action costs and failure conditions.

## Inputs, steps and outputs

Current game state → Jev decision → move one step → repeat.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports $0.02 for 200 requests. | Author report | [Post and attached media](https://x.com/chenchengpro/status/2100516953496670430) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100516953496670430) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Request count grows with moves; maximum length and multi-game success rates are absent.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
