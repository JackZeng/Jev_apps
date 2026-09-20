# Zillow listings: natural-language filters

[简体中文](README.md) | **English**

> Organize listings by architecture, renovation status and other nonstandard filters.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Supports custom property tagging, with accuracy, input provenance and full billing boundaries still unresolved.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#zillow-semantic-filters)

## How it works, in plain English

Like attaching labels to a stack of listings: translate a spoken requirement into questions, then keep matching properties.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@venturetwins](https://x.com/venturetwins) |
| Main post | [Source post](https://x.com/venturetwins/status/2101341075684434245) |
| Published (UTC) | 2026-09-19T16:02:08+00:00 |
| Main-post likes snapshot | **527** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:47:09+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101341075684434245); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101339712464326656/img/A8yq5IoXQuhJAi32.jpg" width="640" alt="Zillow listings: natural-language filters preview">](https://x.com/venturetwins/status/2101341075684434245)<br>[Video](https://x.com/venturetwins/status/2101341075684434245)

A roughly 23-second original demo, independent of the same author’s Goodreads prediction experiment.

- [Direct video 1](https://video.twimg.com/amplify_video/2101339712464326656/vid/avc1/1920x1226/fDU5LpduR2NheRzv.mp4?tag=29) (metadata duration: 23.3s)

Media source: [original publishing page](https://x.com/venturetwins/status/2101341075684434245). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Organize listings by architecture, renovation status and other nonstandard filters.

**Useful aspect (analysis):** More flexible than fixed checkboxes and better suited to bulk judgments than individual chats.

## Inputs, steps and outputs

The author describes semantic classification by style, renovation and freeway proximity. Raw fields, geographic inputs and any image-to-text preparation are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports thousands of listings in under 20 seconds for $0.18; inclusion of retrieval and preprocessing is unknown. | Author report | [Post and attached media](https://x.com/venturetwins/status/2101341075684434245) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101341075684434245) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No labeled test set or error breakdown. This does not establish direct photo input to Jev or verified map-distance measurement.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
