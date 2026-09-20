# TipTour: CoreML + OCR desktop clicks

[简体中文](README.md) | **English**

> Recognize buttons and labels on a Mac, then ask Jev which one to click.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Pinned code exposes local perception, click limits and the 12-action budget. The 90ms figure remains an author-reported step timing; A denotes inspectability, not verified performance.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#coreml-ocr)

## How it works, in plain English

In Jev mode, local recognition software reads the screen and lists button labels. Jev chooses from that list. Images stay on the device, but recognized text is sent to Jev.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@milindlabs](https://x.com/milindlabs) |
| Main post | [Source post](https://x.com/milindlabs/status/2100631847155994852) |
| Published (UTC) | 2026-09-17T17:03:54+00:00 |
| Main-post likes snapshot | **564** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:22.793465+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100631847155994852); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100629037790183424/img/NR6wQpZiC-xjCEsC.jpg" width="640" alt="TipTour: CoreML + OCR desktop clicks preview">](https://x.com/milindlabs/status/2100631847155994852)<br>[Video](https://x.com/milindlabs/status/2100631847155994852)

Retains the original demo as the main post; the same author’s TipTour source release is merged here.

- [Direct video 1](https://video.twimg.com/amplify_video/2100629037790183424/vid/avc1/3324x2160/nTz-UJM8mYnHqARF.mp4?tag=29) (metadata duration: 133.9s)

Media source: [original publishing page](https://x.com/milindlabs/status/2100631847155994852). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Recognize buttons and labels on a Mac, then ask Jev which one to click.

**Useful aspect (analysis):** Inspectable native-Mac clicking without DOM. Unlike Third Hand, the Jev mode focuses on clicks; Gemini voice/text entry is a separate mode.

## Inputs, steps and outputs

Now open-source as TipTour. The pinned version detects controls/labels locally, lets Jev choose single/double/right-click targets and observes again after execution, with a default 12-action budget. Tasks, labels, positions and recent actions go to Jev; screenshots do not.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The original reports roughly 90ms per decision. The source release provides no new complete task set, success rate or end-to-end speed evaluation. | Author report | [Post and attached media](https://x.com/milindlabs/status/2100631847155994852) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100631847155994852) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @milindlabs](https://x.com/milindlabs/status/2101260711645372886): published 2026-09-19T10:42:47+00:00; 467 likes retrieved 2026-09-20T02:48:04+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101260711645372886).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/milind-soni/tiptour-macos/blob/52582467c883d66484542f3be8e259340eb524f1/README.md)
- [Project / demo link 2](https://github.com/milind-soni/tiptour-macos/blob/52582467c883d66484542f3be8e259340eb524f1/TipTour/Jev/JevPointerLoop.swift)

## Mechanism and comparison

Detection errors affect clicks. Jev chooses the top-ranked target without a target-confidence cutoff and cannot freely write text. Gemini mode may send audio/screenshots, so local-image handling is not a blanket property of both modes.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-20T11:01:10+08:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
