# DuckDB semantic classification

[简体中文](README.md) | **English**

> Classify text rows while working with a table.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 07:24:03 (Beijing time, UTC+08:00)

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
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 07:24:03 |
| Main-post likes snapshot | **1,310** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:25.668728+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100370557405667768); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
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
| The author reports roughly 10 seconds for 1,000 rows, without a full reproduction configuration. | Author report | [Post and attached media](https://x.com/hamiltonulmer/status/2100370557405667768) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100370557405667768) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Throughput depends on concurrency, row length and API limits; it is not directly comparable with single-request latency.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
