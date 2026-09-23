# Hacker News classification: organize 24,000 posts in bulk

[简体中文](README.md) | **English**

> Use Jev through Venice API to categorize technology-community posts.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Count the classification demo once, not the gateway announcement as another application.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#hn-venice-classification)

## How it works, in plain English

Attach topic labels to a stack of community entries for browsing by category.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@sabrinaesaquino](https://x.com/sabrinaesaquino) |
| Main post | [Source post](https://x.com/sabrinaesaquino/status/2101102660997017747) |
| Published (UTC) | 2026-09-19T00:14:45+00:00 |
| Main-post likes snapshot | **221** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:29+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101102660997017747); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101101845225865216/img/cubmkjzFZ8i2sPKp.jpg" width="640" alt="Hacker News classification: organize 24,000 posts in bulk preview">](https://x.com/sabrinaesaquino/status/2101102660997017747)<br>[Video](https://x.com/sabrinaesaquino/status/2101102660997017747)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2101101845225865216/vid/avc1/1920x1080/Kn6g02Aj1maQ-u97.mp4?tag=29) (metadata duration: 114.1s)

Media source: [original publishing page](https://x.com/sabrinaesaquino/status/2101102660997017747). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use Jev through Venice API to categorize technology-community posts.

**Useful aspect (analysis):** A concrete community-data classification task, comparable with email and paper labeling.

## Inputs, steps and outputs

The author demonstrates 12-way HN classification through Venice API. Label definitions, full-text inclusion and sampling are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The post reports roughly two minutes for 24,000 posts across 12 categories, without human-reference evaluation. | Author report | [Post and attached media](https://x.com/sabrinaesaquino/status/2101102660997017747) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101102660997017747) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Volume and speed do not measure label accuracy; gateway, collection and storage overhead should be separated.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
