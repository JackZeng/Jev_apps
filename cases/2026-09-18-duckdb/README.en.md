# DuckDB / MotherDuck: classify text inside SQL

[简体中文](README.md) | **English**

> Call Jev while querying a table without exporting the text first.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The article adds data, queries and metric definitions, but remains vendor-reported; B is retained. Consider NULL exclusion and training-split provenance alongside the headline, not as a universal result.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#duckdb)

## How it works, in plain English

Add a sorting button to a table: SQL supplies rows, Jev judges categories, and results return for analysis.

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
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig" width="640" alt="DuckDB / MotherDuck: classify text inside SQL preview">](https://x.com/hamiltonulmer/status/2100370557405667768)<br>[Image](https://x.com/hamiltonulmer/status/2100370557405667768)

Preserves the DuckDB original snapshot, adding MotherDuck’s image and methods article; no SQL was executed.

- [Original image 1](https://pbs.twimg.com/media/HSYD5B1bsAAWqeg.jpg?name=orig)

Media source: [original publishing page](https://x.com/hamiltonulmer/status/2100370557405667768). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Call Jev while querying a table without exporting the text first.

**Useful aspect (analysis):** Keeps the SQL analysis workflow; the hosted version adds public queries and a larger classification comparison.

## Inputs, steps and outputs

The original DuckDB extension calls Jev. A MotherDuck article coauthored by the same developer describes hosted prompt_jev(), returning Choice, Noul or Score in SQL. Related deployments are grouped, not claimed to be one program.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| Earlier: 1,000 rows in about 10 seconds, with a 20–40-fold rewrite gain over the old extension. New vendor example, Jev/Terra: 89%/88%, 40s/31m59s, $0.50/$37.58, limited to that query setup. | Author report | [Results documentation](https://motherduck.com/blog/motherduck-supports-jev/) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100370557405667768) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @hamiltonulmer](https://x.com/hamiltonulmer/status/2101700765656264896): published 2026-09-20T15:51:24+00:00; 503 likes retrieved 2026-09-21T02:45:54+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101700765656264896).
- [Supporting post by @motherduck](https://x.com/motherduck/status/2102077291081896307): published 2026-09-21T16:47:35+00:00; 456 likes retrieved 2026-09-23T03:55:29+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2102077291081896307). [Supplementary media 1](https://pbs.twimg.com/media/HSwUH3TbAAAdWbK.jpg?name=orig)

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://motherduck.com/blog/motherduck-supports-jev/)

## Mechanism and comparison

MotherDuck support is for paid plans. The evaluation samples 100,000 rows from the AG News training split and excludes NULL predictions from accuracy. Concurrency and full-pipeline conditions do not establish universal accuracy parity or savings.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-21T11:02:26+08:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
| 2026-09-23T12:09:12+08:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
