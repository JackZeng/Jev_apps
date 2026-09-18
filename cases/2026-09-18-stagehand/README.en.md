# Stagehand browser control

[简体中文](README.md) | **English**

> Let Jev choose the next browser action and Stagehand carry it out.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 07:24:03 (Beijing time, UTC+08:00)

## How it works, in plain English

Webpages expose button names and other information to accessibility tools. This system gives that information to Jev, lets it choose an action, and uses Stagehand to execute it before checking the page again.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@kylejeong](https://x.com/kylejeong) |
| Main post | [Source post](https://x.com/kylejeong/status/2100622054945095934) |
| Published (UTC) | 2026-09-17T16:25:00+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 07:24:03 |
| Main-post likes snapshot | **393** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:22.761918+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100622054945095934); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100495119065722880/img/7A1mijkU3Z_Zj7PM.jpg" width="640" alt="Stagehand browser control preview">](https://x.com/kylejeong/status/2100622054945095934)<br>[Video](https://x.com/kylejeong/status/2100622054945095934)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100495119065722880/vid/avc1/3012x2160/ELaeOdE95fA4Ps2R.mp4?tag=29) (metadata duration: 14.3s)

Media source: [original publishing page](https://x.com/kylejeong/status/2100622054945095934). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Let Jev choose the next browser action and Stagehand carry it out.

**Useful aspect (analysis):** A clear division between observation and execution, useful for existing Stagehand projects.

## Inputs, steps and outputs

Observe the page → send the accessibility tree as state and actions as questions → Jev decides → Stagehand executes → observe again.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports $0.001 for this remote-browser task. | Author report | [Post and attached media](https://x.com/kylejeong/status/2100622054945095934) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100622054945095934) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Depends on page accessibility information; no success rate on a shared task set is published.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
