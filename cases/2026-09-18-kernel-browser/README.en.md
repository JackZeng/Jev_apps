# Kernel browser demo

[简体中文](README.md) | **English**

> Try a web demo of Jev controlling a browser.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A short integration demo supports plausibility, while mechanism detail, recovery behavior and a task-level evaluation are missing.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#kernel-browser)

## How it works, in plain English

The author connects Jev to the Kernel browser service in an observe–choose–act loop. The post does not detail how pages become model inputs or how errors are recovered.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@stevekrouse](https://x.com/stevekrouse) |
| Main post | [Source post](https://x.com/stevekrouse/status/2100321685081559542) |
| Published (UTC) | 2026-09-16T20:31:26+00:00 |
| Main-post likes snapshot | **235** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:22.741898+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100321685081559542); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100321453455425537/img/hVYy_d3Nuw9XhSwg.jpg" width="640" alt="Kernel browser demo preview">](https://x.com/stevekrouse/status/2100321685081559542)<br>[Video](https://x.com/stevekrouse/status/2100321685081559542)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100321453455425537/vid/avc1/1644x1080/KUCCykm9Yri3B8wZ.mp4?tag=29) (metadata duration: 22.6s)

Media source: [original publishing page](https://x.com/stevekrouse/status/2100321685081559542). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Try a web demo of Jev controlling a browser.

**Useful aspect (analysis):** A public entry point supports further reproduction of the interaction.

## Inputs, steps and outputs

The author provides a Jev + Kernel integration and demo URL; state representation, action constraints and fallback details are not disclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares an approximately 22-second demo, without a comparable benchmark. | Author report | [Post and attached media](https://x.com/stevekrouse/status/2100321685081559542) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100321685081559542) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://jev-browser-use.val.run)

## Mechanism and comparison

Only a short demo; complex pages, recovery and completion rates are undocumented.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
