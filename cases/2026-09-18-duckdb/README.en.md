# DuckDB semantic classification

[简体中文](README.md) | **English**

> Classify text rows while working with a table.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The new figures describe software optimization of the same DuckDB integration. The author acknowledges the earlier inefficiency; no public matched benchmark, so B is retained and the update merged.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#duckdb)

## How it works, in plain English

DuckDB processes tabular data. This extension connects it to Jev so queries can include classifications without manually copying rows into a chat window.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@hamiltonulmer](https://x.com/hamiltonulmer) |
| Main post | [Source post](https://x.com/hamiltonulmer/status/2100370557405667768) |
| Published (UTC) | 2026-09-16T23:45:38+00:00 |
| Main-post likes snapshot | **1,310** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:25.668728+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100370557405667768); may be cached |
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" width="640" alt="DuckDB semantic classification preview">](https://x.com/hamiltonulmer/status/2100370557405667768)<br>[Image](https://x.com/hamiltonulmer/status/2100370557405667768)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Original image 1](https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig)

Media source: [original publishing page](https://x.com/hamiltonulmer/status/2100370557405667768). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Classify text rows while working with a table.

**Useful aspect (analysis):** Keeps semantic classification inside a SQL analysis workflow.

## Inputs, steps and outputs

A DuckDB extension calls Jev on table data and returns queryable classifications.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The original reports 1,000 rows in about 10 seconds. A new post claims a 20–40-fold speedup after rewriting the extension, relative to the author’s inefficient earlier extension, not another model. | Author report | [Results documentation](https://x.com/hamiltonulmer/status/2101700765656264896) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100370557405667768) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @hamiltonulmer](https://x.com/hamiltonulmer/status/2101700765656264896): published 2026-09-20T15:51:24+00:00; 503 likes retrieved 2026-09-21T02:45:54+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101700765656264896).

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The update lacks full configuration, data and accuracy results. Throughput depends on concurrency, row length and API limits; this is not an intrinsic Jev model speedup.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-21T11:02:26+08:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
