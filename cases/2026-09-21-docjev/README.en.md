# DocJev: classify documents and split bundles

[简体中文](README.md) | **English**

> Identify document types and boundaries inside a combined PDF.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Implementation and timing scope are clear. Equal accuracy and roughly sixfold speed claims need qualification: splitting differs and OCR is excluded.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#docjev)

## How it works, in plain English

OCR reads the pages; Jev decides their categories and where another document starts.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@jerryjliu0](https://x.com/jerryjliu0) |
| Main post | [Source post](https://x.com/jerryjliu0/status/2101738281046294552) |
| Published (UTC) | 2026-09-20T18:20:29+00:00 |
| Main-post likes snapshot | **695** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-21T02:44:57+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101738281046294552); may be cached |
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101738161546391552/img/aTJ-mBG_YeF98yMQ.jpg" width="640" alt="DocJev: classify documents and split bundles preview">](https://x.com/jerryjliu0/status/2101738281046294552)<br>[Video](https://x.com/jerryjliu0/status/2101738281046294552)

A 24-second post video plus pinned code and evaluation.

- [Direct video 1](https://video.twimg.com/amplify_video/2101738161546391552/vid/avc1/1920x1080/nBgVsuxAS-XY62FK.mp4?tag=29) (metadata duration: 24.1s)

Media source: [original publishing page](https://x.com/jerryjliu0/status/2101738281046294552). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Identify document types and boundaries inside a combined PDF.

**Useful aspect (analysis):** Adds page-boundary detection to ordinary document classification, with an inspectable small evaluation.

## Inputs, steps and outputs

Pinned code uses Choice for categories and Noul for page boundaries. LiteParse can parse locally; Jev decisions remain hosted, with LlamaParse optional.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| Published results: both classify 40/40; packet exact match is 7/8 for Jev and 8/8 for Luna. Decision medians are 138.6/794.3ms and 209.6/1352.3ms, excluding OCR. | Author report | [Results documentation](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/benchmarks/results/real-small-v1-run01/report.md) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101738281046294552) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/README.md)
- [Project / demo link 2](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/src/jev_docs/engines/jev.py)
- [Project / demo link 3](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/benchmarks/results/real-small-v1-run01/report.md)

## Mechanism and comparison

Only 40 short English PDFs and eight constructed packets; labels lack human review. This does not establish scan, long-document or production accuracy.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
