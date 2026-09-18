# X reach-score simulator

[简体中文](README.md) | **English**

> Simulate reach scores to compare different ways of writing a post.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 07:24:03 (Beijing time, UTC+08:00)

## How it works, in plain English

The author combines Jev judgments with weights. That scoring formula is a simplified model; resembling X does not establish recreation of its real recommendation system.

[Back to catalog](../../README.en.md#content) · [Compare similar examples](../../breakdowns/2026-09-18-content.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Content and advertising analysis |
| Platform / author | X / [@leojrr](https://x.com/leojrr) |
| Main post | [Source post](https://x.com/leojrr/status/2100470174130250127) |
| Published (UTC) | 2026-09-17T06:21:29+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 07:24:03 |
| Main-post likes snapshot | **877** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.298301+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100470174130250127); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100467692117295104/img/01ZWSKAA75eSiFlc.jpg" width="640" alt="X reach-score simulator preview">](https://x.com/leojrr/status/2100470174130250127)<br>[Video](https://x.com/leojrr/status/2100470174130250127)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100467692117295104/vid/avc1/1080x1080/rslLjcSg_pertU5S.mp4?tag=29) (metadata duration: 42.6s)

Media source: [original publishing page](https://x.com/leojrr/status/2100470174130250127). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Simulate reach scores to compare different ways of writing a post.

**Useful aspect (analysis):** Combines scoring with a feed to compare relative changes across text.

## Inputs, steps and outputs

Posts and weights enter a scoring pipeline, Jev supplies judgments, and the UI displays simulated results.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares an approximately 42-second demo and claims to use real weights. | Author report | [Post and attached media](https://x.com/leojrr/status/2100470174130250127) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100470174130250127) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Rebuilding the X algorithm is the author's framing; weight provenance and real recommendation accuracy are unverified.

See the [category analysis](../../breakdowns/2026-09-18-content.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
