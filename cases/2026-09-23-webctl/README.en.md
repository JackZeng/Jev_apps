# webctl: filter web results before the research assistant reads them

[简体中文](README.md) | **English**

> Remove irrelevant and near-duplicate search material before it reaches an assistant.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A reflects inspectable filtering and evaluation boundaries. Small samples, single runs and separate billing do not establish universal accuracy or cost gains.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#webctl)

## How it works, in plain English

Sort a stack of clippings first: pick relevant pages, merge repeats and pass useful passages to the answer-writing model.

[Back to catalog](../../README.en.md#filter) · [Compare similar examples](../../breakdowns/2026-09-18-filter.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Webpage and feed filtering |
| Platform / author | X / [@dorkitude](https://x.com/dorkitude) |
| Main post | [Source post](https://x.com/dorkitude/status/2102194028704092585) |
| Published (UTC) | 2026-09-22T00:31:27+00:00 |
| Main-post likes snapshot | **357** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T03:56:00+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102194028704092585); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSx-UqEaIAEjR4L.jpg?name=orig" width="640" alt="webctl: filter web results before the research assistant reads them preview">](https://x.com/dorkitude/status/2102194028704092585)<br>[Image](https://x.com/dorkitude/status/2102194028704092585)

Original image plus pinned code and evaluation; no search or model APIs were run.

- [Original image 1](https://pbs.twimg.com/media/HSx-UqEaIAEjR4L.jpg?name=orig)

Media source: [original publishing page](https://x.com/dorkitude/status/2102194028704092585). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Remove irrelevant and near-duplicate search material before it reaches an assistant.

**Useful aspect (analysis):** Targets multi-page research, complementing Needle’s source-sentence highlighting on one page; code and a small evaluation are inspectable.

## Inputs, steps and outputs

Search providers retrieve results; code collapses identical URLs/titles, and Jev scores relevance and confirms near-duplicates. Optional scraping adds chunk filtering; a separate model can summarize.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The report shows lower costs and higher judge scores for three Claude Code configurations. The same Kimi model judges pi answers, introducing bias. | Author report | [Results documentation](https://github.com/dorkitude/webctl/blob/ab99fe743a8f30ad26437eaf8c15d1965ae46d4d/benchmarks/RESULTS.md) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102194028704092585) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/dorkitude/webctl/blob/ab99fe743a8f30ad26437eaf8c15d1965ae46d4d/README.md)
- [Project / demo link 2](https://github.com/dorkitude/webctl/blob/ab99fe743a8f30ad26437eaf8c15d1965ae46d4d/internal/jev/chunks.go)
- [Project / demo link 3](https://github.com/dorkitude/webctl/blob/ab99fe743a8f30ad26437eaf8c15d1965ae46d4d/benchmarks/RESULTS.md)

## Mechanism and comparison

Only 30 questions and one run per cell, with a model judge rather than human ground truth. Jev and summarizer calls are separately billed and excluded from token counts; context reduction is not full-stack savings.

See the [category analysis](../../breakdowns/2026-09-18-filter.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
