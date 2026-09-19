# 1kpapers research classification

[简体中文](README.md) | **English**

> Organize over a thousand AI papers so readers can browse them by topic.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The staged workflow and split costs are clearly described; $0.08 covers classification only, and the live site had not yet adopted the Jev labels.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#papers)

## How it works, in plain English

Another model summarizes each paper, then Jev picks from 24 topics. Think of making an index card first and then labeling it.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@nutlope](https://x.com/nutlope) |
| Main post | [Source post](https://x.com/nutlope/status/2100426999546184123) |
| Published (UTC) | 2026-09-17T03:29:55+00:00 |
| Main-post likes snapshot | **1,684** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:32:51.161171+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100426999546184123); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100425141947604992/img/AITyHwcOWq1jw-3Z.jpg" width="640" alt="1kpapers research classification preview">](https://x.com/nutlope/status/2100426999546184123)<br>[Video](https://x.com/nutlope/status/2100426999546184123)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100425141947604992/vid/avc1/2924x2160/S3xa37gd7_PiAL_I.mp4?tag=29) (metadata duration: 10.3s)

Media source: [original publishing page](https://x.com/nutlope/status/2100426999546184123). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Organize over a thousand AI papers so readers can browse them by topic.

**Useful aspect (analysis):** Separates generation and classification costs, useful for research indexes and document catalogs.

## Inputs, steps and outputs

DeepSeek V4 Flash summarizes papers → titles, summaries and candidate topics go to Jev → classifications support the site's visualization.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports $3.99 for summaries, $0.08 for classification and 256ms median end-to-end classification latency per paper. | Author report | [Post and attached media](https://x.com/nutlope/status/2100426999546184123) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100426999546184123) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://1kpapers.com)

## Mechanism and comparison

At posting, Jev labels were still under evaluation and had not replaced the site's existing labels. Summary quality affects classification.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
