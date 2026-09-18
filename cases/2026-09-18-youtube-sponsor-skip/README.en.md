# YouTube sponsor-segment skipping

[简体中文](README.md) | **English**

> Detect spoken sponsor segments while watching YouTube and jump past them.

## How it works, in plain English

Like marking up captions: Jev identifies sponsor lines, code maps their IDs to playback times, then seeks the player. Listening modes first use a separate speech service to turn audio into text.

[Back to catalog](../../README.en.md#filter) · [Compare similar examples](../../breakdowns/2026-09-18-filter.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Webpage and feed filtering |
| Platform / author | X / [@tdinh_me](https://x.com/tdinh_me) |
| Main post | [Source post](https://x.com/tdinh_me/status/2100793777103466615) |
| Published (UTC) | 2026-09-18T03:47:21+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **238** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T06:08:49+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100793777103466615); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100792834526007296/img/8AFbjqEeZrJUEHid.jpg" width="640" alt="YouTube sponsor-segment skipping preview">](https://x.com/tdinh_me/status/2100793777103466615)<br>[Video](https://x.com/tdinh_me/status/2100793777103466615)

The source video demonstrates the extension prototype. The repository’s web app and extension are one project, not two catalog entries.

- [Direct video 1](https://video.twimg.com/amplify_video/2100792834526007296/vid/avc1/2440x1538/xKVx6zmwMQpQOfMS.mp4?tag=29) (metadata duration: 21.3s)

Media source: [original publishing page](https://x.com/tdinh_me/status/2100793777103466615). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Detect spoken sponsor segments while watching YouTube and jump past them.

**Useful aspect (analysis):** Handles spoken sponsorship inside a video rather than hiding webpage ads. Transcript, hybrid and listening modes accommodate different caption availability.

## Inputs, steps and outputs

The pinned source labels caption lines, scans windows for sponsor presence and boundaries with Jev, and maps selected lines to timestamps in code. Smart/Listen modes use Deepgram transcription and Jev judgments about the current segment. Code owns timestamp calculation and playback seeking.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a roughly 21-second Chrome-extension demo, reports real-time detection at about $0.005/video, and calls it an open-source BYOK prototype. | Author report | [Post and attached media](https://x.com/tdinh_me/status/2100793777103466615) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100793777103466615) | Snapshot at the recorded time, not a live count |

**Source review:** Read the pinned [README at de01f05](https://github.com/trungdq88/youtube-sponsor-detection/blob/de01f0568d043035889a296a61ce21e0accc8b16/README.md) and [src/jev.js](https://github.com/trungdq88/youtube-sponsor-detection/blob/de01f0568d043035889a296a61ce21e0accc8b16/src/jev.js). Documentation distinguishes hourly costs across modes and Deepgram’s per-minute charge. The post’s per-video estimate is not treated as a total-cost guarantee. No extension was installed or API called.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/trungdq88/youtube-sponsor-detection)

## Mechanism and comparison

Caption fetching can break; stepwise listening-mode seeks may overshoot into normal content. The author’s roughly $0.005/video claim is not universal across modes, and transcription adds cost. No accuracy or time-saving benchmark was run here.

See the [category analysis](../../breakdowns/2026-09-18-filter.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
