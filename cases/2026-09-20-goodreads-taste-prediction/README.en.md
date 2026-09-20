# Goodreads: predict personal five-star books

[简体中文](README.md) | **English**

> Use past ratings to predict which books one reader might award five stars.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Data and holdout sizes are stated, but the full protocol is missing; the ratios do not generalize to other readers or tasks.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#goodreads-taste-prediction)

## How it works, in plain English

Like showing a bookseller your reading diary and asking for a guess; this tests one person’s taste.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@venturetwins](https://x.com/venturetwins) |
| Main post | [Source post](https://x.com/venturetwins/status/2101393861667115437) |
| Published (UTC) | 2026-09-19T19:31:53+00:00 |
| Main-post likes snapshot | **238** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:45:53+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101393861667115437); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101393799234871296/img/oBhawR0JczN9WT1k.jpg" width="640" alt="Goodreads: predict personal five-star books preview">](https://x.com/venturetwins/status/2101393861667115437)<br>[Video](https://x.com/venturetwins/status/2101393861667115437)

The post includes a roughly 12-second results demo; separate from the same author’s property-filtering task.

- [Direct video 1](https://video.twimg.com/amplify_video/2101393799234871296/vid/avc1/2796x2160/hDihdGgIjfEKCoWz.mp4?tag=29) (metadata duration: 12.2s)

Media source: [original publishing page](https://x.com/venturetwins/status/2101393861667115437). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use past ratings to predict which books one reader might award five stars.

**Useful aspect (analysis):** Uses personal preference labels and describes a holdout, unlike generic categorization; useful for exploring personalized decisions.

## Inputs, steps and outputs

The author starts with roughly 1,000 personal Goodreads ratings, holds out 100, and compares Jev with GPT-5.6 on five-star prediction. Prompts, split details and class balance are not established.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports slightly better accuracy, 53-fold lower cost and 25-fold greater speed for this setup; not independently reproduced. | Author report | [Post and attached media](https://x.com/venturetwins/status/2101393861667115437) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101393861667115437) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

A 100-item single-reader test does not establish general recommendation quality. Majority-class baselines, leakage, precision and recall still need checking.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
