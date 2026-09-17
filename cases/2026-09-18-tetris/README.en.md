# Tetris

[简体中文](README.md) | **English**

> Let Jev make Tetris decisions and observe how blocks are placed.

## How it works, in plain English

Code must pass board information to the model and execute its choices. The post does not say whether Jev chooses final placements or individual keys, which matters for comparisons.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@marcus_lowe](https://x.com/marcus_lowe) |
| Main post | [Source post](https://x.com/marcus_lowe/status/2100315518930661861) |
| Published (UTC) | 2026-09-16T20:06:56+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **956** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:28.080664+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100315518930661861); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100315393860730880/img/u0iH2SHQny2hkd4Q.jpg" width="640" alt="Tetris preview">](https://x.com/marcus_lowe/status/2100315518930661861)<br>[Video](https://x.com/marcus_lowe/status/2100315518930661861)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100315393860730880/vid/avc1/1776x1514/GkyZllakpiJ_nMHe.mp4?tag=29) (metadata duration: 28.4s)

Media source: [original publishing page](https://x.com/marcus_lowe/status/2100315518930661861). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Let Jev make Tetris decisions and observe how blocks are placed.

**Useful aspect (analysis):** Useful for contrasting landing-position selection with continuous key presses.

## Inputs, steps and outputs

The game loop calls Jev; board encoding and action granularity are unspecified.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares an approximately 28-second demo without score benchmarks. | Author report | [Post and attached media](https://x.com/marcus_lowe/status/2100315518930661861) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100315518930661861) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The post does not identify which control method is used, so planning ability cannot be inferred.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
