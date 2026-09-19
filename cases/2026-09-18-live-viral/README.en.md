# Live post-potential analyzer

[简体中文](README.md) | **English**

> Get feedback on a post's type and potential reach as you write.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The interactive scoring demo is plausible and explicitly experimental. No evidence establishes predictive validity for future reach.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#live-viral)

## How it works, in plain English

After a half-second pause, code sends the draft to Jev and updates its labels and scores. This is immediate writing feedback, not proof that the post will spread.

[Back to catalog](../../README.en.md#content) · [Compare similar examples](../../breakdowns/2026-09-18-content.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Content and advertising analysis |
| Platform / author | X / [@rileybrown](https://x.com/rileybrown) |
| Main post | [Source post](https://x.com/rileybrown/status/2100425868053008758) |
| Published (UTC) | 2026-09-17T03:25:25+00:00 |
| Main-post likes snapshot | **830** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.282636+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100425868053008758); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100424897491070976/img/kKnsb68jNUZZzSBi.jpg" width="640" alt="Live post-potential analyzer preview">](https://x.com/rileybrown/status/2100425868053008758)<br>[Video](https://x.com/rileybrown/status/2100425868053008758)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100424897491070976/vid/avc1/3480x2160/YETjQWhRn81gBn5v.mp4?tag=29) (metadata duration: 44.6s)

Media source: [original publishing page](https://x.com/rileybrown/status/2100425868053008758). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Get feedback on a post's type and potential reach as you write.

**Useful aspect (analysis):** Fast feedback for comparing wording while writing.

## Inputs, steps and outputs

Edited text → debounce delay → Jev classification/scoring → live feedback.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author demonstrates live classification and calls it an experiment. | Author report | [Post and attached media](https://x.com/rileybrown/status/2100425868053008758) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100425868053008758) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The author says real X data still needs to be collected; predictive ability for future reach is unproven.

See the [category analysis](../../breakdowns/2026-09-18-content.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
