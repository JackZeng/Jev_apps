# Slay the Spire 2 agent

[简体中文](README.md) | **English**

> Use Jev to choose card-game actions with less waiting between decisions.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 07:24:03 (Beijing time, UTC+08:00)

## How it works, in plain English

Card games usually provide a set of currently legal choices that code can offer to a model. The post does not disclose the interface, and quicker moves do not necessarily win more games.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@coolish](https://x.com/coolish) |
| Main post | [Source post](https://x.com/coolish/status/2100570517954838897) |
| Published (UTC) | 2026-09-17T13:00:12+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 07:24:03 |
| Main-post likes snapshot | **598** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:28.210633+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100570517954838897); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100569632482746369/img/TPuOBiHYCWUWxNOc.jpg" width="640" alt="Slay the Spire 2 agent preview">](https://x.com/coolish/status/2100570517954838897)<br>[Video](https://x.com/coolish/status/2100570517954838897)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100569632482746369/vid/avc1/2160x3840/wSKmX_IAXY-wcRYM.mp4?tag=29) (metadata duration: 33.3s)

Media source: [original publishing page](https://x.com/coolish/status/2100570517954838897). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use Jev to choose card-game actions with less waiting between decisions.

**Useful aspect (analysis):** A setting with discrete legal actions suits studying decision selection.

## Inputs, steps and outputs

Game state → Jev action choice → execution; the state interface is unknown.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports roughly 0.7 seconds of decision time per action and shares a video. | Author report | [Post and attached media](https://x.com/coolish/status/2100570517954838897) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100570517954838897) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Fast play does not imply stronger strategy; full-run win rates are absent.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
