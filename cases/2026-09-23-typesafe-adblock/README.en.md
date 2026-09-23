# TypeSafe AdBlock: judge suspected webpage ads by meaning

[简体中文](README.md) | **English**

> Identify ad-like elements, then decide whether to remove or highlight them.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A covers implementation, not undetectability or universal blocking effectiveness; coverage depends on candidate rules and test conditions.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#typesafe-adblock)

## How it works, in plain English

Circle suspected ads first, ask for a judgment and let code hide the element.

[Back to catalog](../../README.en.md#filter) · [Compare similar examples](../../breakdowns/2026-09-18-filter.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Webpage and feed filtering |
| Platform / author | X / [@iam_zachi](https://x.com/iam_zachi) |
| Main post | [Source post](https://x.com/iam_zachi/status/2100529273186472318) |
| Published (UTC) | 2026-09-17T10:16:19+00:00 |
| Main-post likes snapshot | **3,889** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:49+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100529273186472318); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100529029761642496/img/OY0Ltm7v7lXv5-y6.jpg" width="640" alt="TypeSafe AdBlock: judge suspected webpage ads by meaning preview">](https://x.com/iam_zachi/status/2100529273186472318)<br>[Video](https://x.com/iam_zachi/status/2100529273186472318)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2100529029761642496/vid/avc1/3324x2160/plhiVvyd13nRhuHR.mp4?tag=29) (metadata duration: 27.5s)

Media source: [original publishing page](https://x.com/iam_zachi/status/2100529273186472318). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Identify ad-like elements, then decide whether to remove or highlight them.

**Useful aspect (analysis):** Adds semantic checks to candidates, comparable with Unclutter’s broader page cleanup.

## Inputs, steps and outputs

Heuristics extract candidate DOM descriptions; Jev batches Noul questions, with a default 0.70 removal threshold and page-mutation monitoring.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The post calls it realtime and undetectable; the repository reports only small fixtures and explicitly calls it an experimental side project. | Author report | [Post and attached media](https://x.com/iam_zachi/status/2100529273186472318) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100529273186472318) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/README.md)
- [Project / demo link 2](https://github.com/realZachi/typesafe-adblock/blob/7e067d243d87b7fe4d511653c0ddcd77b9beee18/src/typesafe.js)

## Mechanism and comparison

Code does not inspect every element. Ads outside candidate rules can be missed and content wrongly removed. The repository excludes tracking, malware and video-ad protection.

See the [category analysis](../../breakdowns/2026-09-18-filter.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
