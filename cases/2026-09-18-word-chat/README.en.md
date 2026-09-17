# Finite-vocabulary chat

[简体中文](README.md) | **English**

> Give Jev a common-word list and let it build a conversation one word at a time.

## How it works, in plain English

Jev chooses the next word from a finite list; code appends it and asks again. The loop constructs the text, and the vocabulary limits what it can say.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@hi_im_isaac_](https://x.com/hi_im_isaac_) |
| Main post | [Source post](https://x.com/hi_im_isaac_/status/2100408276949385668) |
| Published (UTC) | 2026-09-17T02:15:31+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **2,644** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:29.953529+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100408276949385668); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100407646226649088/img/qVPomAIwJ_lKpO2J.jpg" width="640" alt="Finite-vocabulary chat preview">](https://x.com/hi_im_isaac_/status/2100408276949385668)<br>[Video](https://x.com/hi_im_isaac_/status/2100408276949385668)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100407646226649088/vid/avc1/622x470/Z5SxcnGSKXO_pTc8.mp4?tag=29) (metadata duration: 28.9s)

Media source: [original publishing page](https://x.com/hi_im_isaac_/status/2100408276949385668). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Give Jev a common-word list and let it build a conversation one word at a time.

**Useful aspect (analysis):** Shows how choice outputs can be composed into a generative interaction.

## Inputs, steps and outputs

Existing text and a finite vocabulary → choose the next word → append → repeat.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author demonstrates chat built from common English words and punctuation choices. | Author report | [Post and attached media](https://x.com/hi_im_isaac_/status/2100408276949385668) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100408276949385668) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The vocabulary limits expression; per-word decision costs and latency are not directly comparable with a text model.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
