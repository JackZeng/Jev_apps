# Intent-aware predictive launcher

[简体中文](README.md) | **English**

> Find files without remembering names: type “the PDF I just downloaded” and rank relevant matches first.

**Added to README:** 2026-09-18 10:50:59<br>**Content updated:** 2026-09-18 10:50:59 (Beijing time, UTC+08:00)

## How it works, in plain English

Like asking an assistant for the document you just downloaded: the app prepares candidates and context, Jev interprets the request, and the interface updates its ranking as you type. Indexing details are undisclosed.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@dabit3](https://x.com/dabit3) |
| Main post | [Source post](https://x.com/dabit3/status/2100756930054504776) |
| Published (UTC) | 2026-09-18T01:20:56+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 10:50:59 / 2026-09-18 10:50:59 |
| Main-post likes snapshot | **252** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T02:36:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100756930054504776); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100756324845862913/img/8ew1NdHs6k5cReoF.jpg" width="640" alt="Intent-aware predictive launcher preview">](https://x.com/dabit3/status/2100756930054504776)<br>[Video](https://x.com/dabit3/status/2100756930054504776)

The original 20-second demo video, with its source cover and direct video link.

- [Direct video 1](https://video.twimg.com/amplify_video/2100756324845862913/vid/avc1/1920x1080/h60Z77ixV33yGs9V.mp4?tag=29) (metadata duration: 20.0s)

Media source: [original publishing page](https://x.com/dabit3/status/2100756930054504776). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Find files without remembering names: type “the PDF I just downloaded” and rank relevant matches first.

**Useful aspect (analysis):** Explores contextual requests such as “just downloaded” beyond filename or alias matching; useful for selecting among file candidates.

## Inputs, steps and outputs

The author describes Jev interpreting a query while it is typed and the launcher updating its ranked matches. File indexing, context construction, request throttling and permission scope are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a 20-second launcher demo and reports roughly 100ms decisions per keystroke, ranking the newest downloaded PDF first. | Author report | [Post and attached media](https://x.com/dabit3/status/2100756930054504776) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100756930054504776) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The roughly 100ms figure is author-reported. No evaluation covers large file collections, duplicate names or ambiguous references. High model confidence does not guarantee a correct match.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
