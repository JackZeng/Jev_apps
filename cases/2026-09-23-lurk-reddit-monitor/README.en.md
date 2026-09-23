# Lurk: monitor Reddit discussions worth following

[简体中文](README.md) | **English**

> Screen Reddit topics and send relevant discussions to notification channels.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>An identifiable product and screening task, with marketing outcomes and sustained operation unverified.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#lurk-reddit-monitor)

## How it works, in plain English

A topic watcher continually selects potentially relevant conversations.

[Back to catalog](../../README.en.md#filter) · [Compare similar examples](../../breakdowns/2026-09-18-filter.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Webpage and feed filtering |
| Platform / author | X / [@mxfp4](https://x.com/mxfp4) |
| Main post | [Source post](https://x.com/mxfp4/status/2101070906852298910) |
| Published (UTC) | 2026-09-18T22:08:34+00:00 |
| Main-post likes snapshot | **751** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:30+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101070906852298910); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101070204654456832/img/ixTfmBca9GY8Xyhf.jpg" width="640" alt="Lurk: monitor Reddit discussions worth following preview">](https://x.com/mxfp4/status/2101070906852298910)<br>[Video](https://x.com/mxfp4/status/2101070906852298910)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2101070204654456832/vid/avc1/1920x1080/79RTzXqLXezVQGuK.mp4?tag=29) (metadata duration: 16.3s)

Media source: [original publishing page](https://x.com/mxfp4/status/2101070906852298910). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Screen Reddit topics and send relevant discussions to notification channels.

**Useful aspect (analysis):** Emphasizes ongoing discovery and alerts compared with Reddit Radar’s on-demand queries.

## Inputs, steps and outputs

The author combines Jev and AnyAPI for thread scanning, with email, Discord and Slack notifications. Coverage, prompts and ranking details are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The original reports scanning 4,000 threads, not complete Reddit coverage. | Author report | [Post and attached media](https://x.com/mxfp4/status/2101070906852298910) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101070906852298910) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://lurk.so)

## Mechanism and comparison

Finding threads does not guarantee AI citations for a brand. Coverage, false alerts, notification delay and free allowances are unverified.

See the [category analysis](../../breakdowns/2026-09-18-filter.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
