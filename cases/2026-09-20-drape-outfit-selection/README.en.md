# Drape try-on experiment: select outfits from speech

[简体中文](README.md) | **English**

> Choose clothes from speech and wardrobe information, then display the change through a video system.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author separates outfit decisions from video rendering; decision timing alone does not establish end-to-end realtime performance.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#drape-outfit-selection)

## How it works, in plain English

Like a stylist choosing from a wardrobe list: Jev selects clothes and a separate video stage puts them on screen.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@nailthy62](https://x.com/nailthy62) |
| Main post | [Source post](https://x.com/nailthy62/status/2101388186916454439) |
| Published (UTC) | 2026-09-19T19:09:20+00:00 |
| Main-post likes snapshot | **1,379** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:45:54+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101388186916454439); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101384523124740096/img/1Q6moTMdLcZ-mJ3r.jpg" width="640" alt="Drape try-on experiment: select outfits from speech preview">](https://x.com/nailthy62/status/2101388186916454439)<br>[Video](https://x.com/nailthy62/status/2101388186916454439)

The 31-second clip is combined with author replies about metadata, rendering and the lack of app integration.

- [Direct video 1](https://video.twimg.com/amplify_video/2101384523124740096/vid/avc1/1688x950/f3zLUWk8IRp9Xhdx.mp4?tag=29) (metadata duration: 31.2s)

Media source: [original publishing page](https://x.com/nailthy62/status/2101388186916454439). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Choose clothes from speech and wardrobe information, then display the change through a video system.

**Useful aspect (analysis):** Adds conversational selection and current-outfit context to ordinary product recommendation, with visual feedback.

## Inputs, steps and outputs

Author replies describe transcripts and existing clothing metadata as inputs, with reference garment images used by a realtime video-to-video stage. The experiment was not actually integrated into Drape.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports about 620ms and $0.0011 per Jev decision, excluding creation of pre-existing metadata. | Author report | [Post and attached media](https://x.com/nailthy62/status/2101388186916454439) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101388186916454439) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @nailthy62](https://x.com/nailthy62/status/2101459808587284818): published 2026-09-19T23:53:56+00:00; 3 likes retrieved 2026-09-20T02:54:51+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101459808587284818).
- [Supporting post by @nailthy62](https://x.com/nailthy62/status/2101420612485103693): published 2026-09-19T21:18:11+00:00; 8 likes retrieved 2026-09-20T02:54:51+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101420612485103693).
- [Supporting post by @nailthy62](https://x.com/nailthy62/status/2101401929842831381): published 2026-09-19T20:03:56+00:00; 5 likes retrieved 2026-09-20T02:54:51+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101401929842831381).

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The full video model, transcription pipeline and end-to-end bill are undisclosed. Selection latency and cost are not full try-on measurements.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
