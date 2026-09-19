# Email classification: four-model speed comparison

[简体中文](README.md) | **English**

> Classify a set of emails with four models and compare progress and elapsed time on one screen.

**Added to README:** 2026-09-18 16:17:27<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A task-level speed demo is visible, but unspecified model versions, concurrency and accuracy prevent a general performance ranking.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#email-speed-race) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Like four sorting clerks handling the same stack of letters: each model assigns categories while the page tracks results and time. This demonstration focuses on speed; finishing first does not mean every label is correct.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@usutaku_channel](https://x.com/usutaku_channel) |
| Main post | [Source post](https://x.com/usutaku_channel/status/2100829343954173965) |
| Published (UTC) | 2026-09-18T06:08:41+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 16:17:27 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **445** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T08:11:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100829343954173965); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100829070514864128/img/V3ix1we5Euhs8DsY.jpg" width="640" alt="Email classification: four-model speed comparison preview">](https://x.com/usutaku_channel/status/2100829343954173965)<br>[Video](https://x.com/usutaku_channel/status/2100829343954173965)

Uses this post’s own video and thumbnail. The source interface and discussion were inspected; this is not a repost of the existing 500-email video.

- [Direct video 1](https://video.twimg.com/amplify_video/2100829070514864128/vid/avc1/3024x1964/ru396ddS-QlRgpgZ.mp4?tag=29) (metadata duration: 30.0s)

Media source: [original publishing page](https://x.com/usutaku_channel/status/2100829343954173965). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Classify a set of emails with four models and compare progress and elapsed time on one screen.

**Useful aspect (analysis):** Makes differences in waiting time across models more visible than a single-model batch demo. Compare it with the 500-email case to distinguish cross-model responsiveness from batch throughput.

## Inputs, steps and outputs

The source video’s JEV Speed Race interface places Jev, GPT Luna, Claude Sonnet and Gemini 3.5 Flash side by side, with matching email rows, progress counters and timers. This establishes a task-level speed comparison; request settings, full model versions and classification rules remain unverified.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a roughly 30-second comparison video and reports Jev as substantially faster. This repository has not reproduced that claim or treated video length as classification latency. | Author report | [Post and attached media](https://x.com/usutaku_channel/status/2100829343954173965) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100829343954173965) | Snapshot at the recorded time, not a live count |

**Deduplication and comparison:** The author, interface and source video differ from Riley Brown’s batch-email case, so this is a separate experiment in the same category. Without a shared complete test protocol, advertised times and costs should not be compared directly.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No independent accuracy, confusion-matrix or full-cost evaluation is available. Concurrency, batching and timing conditions remain unverified, and interface labels do not establish exact API versions. This is insufficient for a universal speed ranking or multiplier.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
