# OpenCode + agent-desktop

[简体中文](README.md) | **English**

> One model remembers the task while Jev helps choose desktop targets quickly.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 07:24:03 (Beijing time, UTC+08:00)

## How it works, in plain English

Think of a coordinator and an operator: the language model keeps context and passes desktop information to Jev for target selection. The post does not explain the exact representation.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@mdlahfir](https://x.com/mdlahfir) |
| Main post | [Source post](https://x.com/mdlahfir/status/2100359236924637349) |
| Published (UTC) | 2026-09-16T23:00:39+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 07:24:03 |
| Main-post likes snapshot | **870** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:22.762217+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100359236924637349); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100358791321755648/img/t6Bd787flQiGeoJ_.jpg" width="640" alt="OpenCode + agent-desktop preview">](https://x.com/mdlahfir/status/2100359236924637349)<br>[Video](https://x.com/mdlahfir/status/2100359236924637349)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100358791321755648/vid/avc1/2992x1682/Qt4A9BBV9Hu0rbyI.mp4?tag=29) (metadata duration: 47.1s)

Media source: [original publishing page](https://x.com/mdlahfir/status/2100359236924637349). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

One model remembers the task while Jev helps choose desktop targets quickly.

**Useful aspect (analysis):** Separates long-term context management from fast action selection.

## Inputs, steps and outputs

The LLM maintains memory and requests agent-desktop snapshots, then sends them to Jev to select an element.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a desktop-control demo with a visible cursor. | Author report | [Post and attached media](https://x.com/mdlahfir/status/2100359236924637349) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100359236924637349) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Still depends on an LLM. Snapshot encoding is unspecified; this does not establish native image input to Jev.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
