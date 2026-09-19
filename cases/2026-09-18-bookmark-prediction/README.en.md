# Bookmark-percentile prediction

[简体中文](README.md) | **English**

> Predict whether a post ranks in the top quarter for bookmarks among nearby dates.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The personal historical benchmark has a concrete label, but undisclosed splits and configurations prevent validating generalization or the 200-fold cost comparison; a future-looking label alone is not proof of leakage.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#bookmark-prediction) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Replace vague virality with a checkable target: top 25% within a defined date window. Jev predicts that outcome and the author compares predictions with historical data.

[Back to catalog](../../README.en.md#content) · [Compare similar examples](../../breakdowns/2026-09-18-content.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Content and advertising analysis |
| Platform / author | X / [@AM09_21](https://x.com/AM09_21) |
| Main post | [Source post](https://x.com/AM09_21/status/2100430480642642395) |
| Published (UTC) | 2026-09-17T03:43:45+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **287** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.368585+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100430480642642395); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSYtFVgaoAIPpi5.jpg?name=orig" width="640" alt="Bookmark-percentile prediction preview">](https://x.com/AM09_21/status/2100430480642642395)<br>[Image](https://x.com/AM09_21/status/2100430480642642395)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Original image 1](https://pbs.twimg.com/media/HSYtFVgaoAIPpi5.jpg?name=orig)

Media source: [original publishing page](https://x.com/AM09_21/status/2100430480642642395). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Predict whether a post ranks in the top quarter for bookmarks among nearby dates.

**Useful aspect (analysis):** A more specific target than vaguely predicting virality; the author describes sample size and objective.

## Inputs, steps and outputs

Historical posts → Jev top-percentile prediction → comparison with other models.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports using about 5,000 personal posts from June–August and plots cost against accuracy. | Author report | [Post and attached media](https://x.com/AM09_21/status/2100430480642642395) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100430480642642395) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Single-account data with incomplete time-split and leakage details; not a general X ranking model.

See the [category analysis](../../breakdowns/2026-09-18-content.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
