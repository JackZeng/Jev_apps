# Intent-driven spreadsheet ratings

[简体中文](README.md) | **English**

> Name a column “Urgency” and have the text in each row receive a corresponding rating.

**Added to README:** 2026-09-18 14:17:58<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A concrete intent-labelled spreadsheet demo; question construction, consistency and timing scope are unknown, so arbitrary-column reliability is not established.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#predictive-spreadsheet) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Ordinary formulas calculate numbers; this demo uses a column name to express a question. Jev judges each row’s urgency, and the app writes the result into the table.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@dabit3](https://x.com/dabit3) |
| Main post | [Source post](https://x.com/dabit3/status/2100780008193020049) |
| Published (UTC) | 2026-09-18T02:52:39+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 14:17:58 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **337** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T06:08:50+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100780008193020049); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100779722447667200/img/gvsEg2-3oD6FRZhc.jpg" width="640" alt="Intent-driven spreadsheet ratings preview">](https://x.com/dabit3/status/2100780008193020049)<br>[Video](https://x.com/dabit3/status/2100780008193020049)

Uses this spreadsheet post’s own video, not the launcher video it quotes.

- [Direct video 1](https://video.twimg.com/amplify_video/2100779722447667200/vid/avc1/1920x1080/z3QL0T2eNCZYQJ6N.mp4?tag=29) (metadata duration: 17.9s)

Media source: [original publishing page](https://x.com/dabit3/status/2100780008193020049). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Name a column “Urgency” and have the text in each row receive a corresponding rating.

**Useful aspect (analysis):** Brings semantic judgments into a familiar spreadsheet interface for experiments with ticket or text-record triage; emphasizes interaction beyond fixed-label batch classification.

## Inputs, steps and outputs

The author describes column intent and row content driving Jev ratings that update with typing. Question construction, score ranges, batching and caching are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a roughly 18-second video, reporting ratings from no follow-up needed to urgent after entering Urgency, in roughly 100ms. | Author report | [Post and attached media](https://x.com/dabit3/status/2100780008193020049) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100780008193020049) | Snapshot at the recorded time, not a live count |

**Deduplication:** This post quotes the same author’s launcher, but has its own video and a different task: rating spreadsheet rows rather than ranking files. It is a separate data-classification case; common authorship or a quote alone does not establish duplicate identity.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The roughly 100ms claim lacks row-count and timing-scope details. Ambiguous column names, rating consistency and large-table costs are unevaluated. Arbitrary headings are not proven to become reliable formulas.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
