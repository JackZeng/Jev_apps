# Needle: find webpage passages by meaning

[简体中文](README.md) | **English**

> Use your own words to find relevant sentences without remembering exact keywords.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Pinned code establishes extraction, relevance and sentence selection. A reflects clear implementation, not verified search completeness.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#needle-semantic-find)

## How it works, in plain English

Like asking someone to highlight useful passages: read the page text and select the best source sentence.

[Back to catalog](../../README.en.md#filter) · [Compare similar examples](../../breakdowns/2026-09-18-filter.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Webpage and feed filtering |
| Platform / author | X / [@Saboo_Shubham_](https://x.com/Saboo_Shubham_) |
| Main post | [Source post](https://x.com/Saboo_Shubham_/status/2101576462042366114) |
| Published (UTC) | 2026-09-20T07:37:28+00:00 |
| Main-post likes snapshot | **1,658** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-21T02:50:32+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101576462042366114); may be cached |
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101576307352203264/img/THdpZUHOSRsSoTVr.jpg" width="640" alt="Needle: find webpage passages by meaning preview">](https://x.com/Saboo_Shubham_/status/2101576462042366114)<br>[Video](https://x.com/Saboo_Shubham_/status/2101576462042366114)

The author links the Needle subdirectory; the entire awesome-llm-apps repository is not counted as another application.

- [Direct video 1](https://video.twimg.com/amplify_video/2101576307352203264/vid/avc1/3584x2160/BhFo3Z_2xMkihnBB.mp4?tag=29) (metadata duration: 21.6s)

Media source: [original publishing page](https://x.com/Saboo_Shubham_/status/2101576462042366114). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use your own words to find relevant sentences without remembering exact keywords.

**Useful aspect (analysis):** Handles paraphrases while keeping results tied to inspectable source text.

## Inputs, steps and outputs

The extension extracts passages. A backend calls Jev through Vercel AI Gateway for relevance and sentence selection, then maps highlights back; the inclusion threshold is 0.58.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A roughly 21-second demo, without a standard retrieval benchmark. Temporary promotions are not permanent free access. | Author report | [Post and attached media](https://x.com/Saboo_Shubham_/status/2101576462042366114) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101576462042366114) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @Saboo_Shubham_](https://x.com/Saboo_Shubham_/status/2101577105809240488): published 2026-09-20T07:40:02+00:00; 72 likes retrieved 2026-09-21T02:55:37+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101577105809240488).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/9e860951aaf5c82801779e43e748dcf92042879a/advanced_llm_apps/needle/README.md)
- [Project / demo link 2](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/9e860951aaf5c82801779e43e748dcf92042879a/advanced_llm_apps/needle/server/search.mjs)

## Mechanism and comparison

Limited to 160 passages and 60,000 characters; PDF viewers and scans are unsupported. Long pages may be incomplete. Queries and captured passages go to hosted services; the threshold does not guarantee recall.

See the [category analysis](../../breakdowns/2026-09-18-filter.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
