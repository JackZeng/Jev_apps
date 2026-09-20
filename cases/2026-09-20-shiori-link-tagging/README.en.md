# Shiori: automatic bookmark tags

[简体中文](README.md) | **English**

> Categorize saved links so they are easier to find by topic later.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The task and comparison media are clear, but superiority over Haiku or production-quality classification is unproven.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#shiori-link-tagging)

## How it works, in plain English

Like organizing a bookmark drawer: read the available page information and choose topic compartments.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@brian_lovin](https://x.com/brian_lovin) |
| Main post | [Source post](https://x.com/brian_lovin/status/2101321554130809156) |
| Published (UTC) | 2026-09-19T14:44:33+00:00 |
| Main-post likes snapshot | **327** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:47:32+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101321554130809156); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101321495351799809/img/4KIZYG3NZtHjWnZB.jpg" width="640" alt="Shiori: automatic bookmark tags preview">](https://x.com/brian_lovin/status/2101321554130809156)<br>[Video](https://x.com/brian_lovin/status/2101321554130809156)

Only the tagging feature is collected; other Shiori features are not assumed to use Jev.

- [Direct video 1](https://video.twimg.com/amplify_video/2101321495351799809/vid/avc1/3456x2084/fUL_3DbDaWbBCtNL.mp4?tag=29) (metadata duration: 25.6s)

Media source: [original publishing page](https://x.com/brian_lovin/status/2101321554130809156). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Categorize saved links so they are easier to find by topic later.

**Useful aspect (analysis):** Applies classification directly to bookmark retrieval; speed, incorrect tags and missing tags can be evaluated separately.

## Inputs, steps and outputs

The author shows Jev versus Haiku for Shiori link tagging. Page extraction, label vocabulary and multilabel rules were not established.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A roughly 25-second comparison clip, without reproducible accuracy, cost or speedup figures. | Author report | [Post and attached media](https://x.com/brian_lovin/status/2101321554130809156) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101321554130809156) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The video lacks labeled data and matched-condition statistics. Faster interface updates do not establish equal tag quality.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
