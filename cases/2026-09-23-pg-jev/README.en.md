# pg-jev: filter database rows in everyday language

[简体中文](README.md) | **English**

> Use semantic conditions inside PostgreSQL to classify, score or filter rows.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A covers public batching and caching, not unlimited scale or error-free search without a vector index.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#pg-jev)

## How it works, in plain English

Give SQL a filter that reads descriptions; the database still handles sorting and aggregation.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@iam_zachi](https://x.com/iam_zachi) |
| Main post | [Source post](https://x.com/iam_zachi/status/2100679300756435135) |
| Published (UTC) | 2026-09-17T20:12:28+00:00 |
| Main-post likes snapshot | **2,832** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:47+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100679300756435135); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100674729216524288/img/ZqaCccSfzuzlrdro.jpg" width="640" alt="pg-jev: filter database rows in everyday language preview">](https://x.com/iam_zachi/status/2100679300756435135)<br>[Video](https://x.com/iam_zachi/status/2100679300756435135)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2100674729216524288/vid/avc1/1662x1080/dqifvKIL8-ktKzRk.mp4?tag=29) (metadata duration: 44.9s)

Media source: [original publishing page](https://x.com/iam_zachi/status/2100679300756435135). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use semantic conditions inside PostgreSQL to classify, score or filter rows.

**Useful aspect (analysis):** A PostgreSQL counterpart to DuckDB integration, composing judgments with ordinary queries.

## Inputs, steps and outputs

The extension batches rows into shared state with per-row questions, defaults to 20 rows per batch and caches answers by row content within a session. Probability, choice and score functions are exposed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The original reports 129 rows in about 1s/$0.0009 and a 6ms cached rerun. Repository measurements use other dataset sizes. | Author report | [Post and attached media](https://x.com/iam_zachi/status/2100679300756435135) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100679300756435135) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/realZachi/pg-jev/blob/afd11fa856d7a2b831a1bfd8ee7f869ce8efcd62/README.md)
- [Project / demo link 2](https://github.com/realZachi/pg-jev/blob/afd11fa856d7a2b831a1bfd8ee7f869ce8efcd62/sql/jev--0.2.0.sql)

## Mechanism and comparison

Requires plpython3u and superuser access, unavailable on many managed hosts. First-pass large-table queries incur calls; cached milliseconds are not fresh inference speed.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
