# 29-option character generation

[简体中文](README.md) | **English**

> Let Jev choose one letter or punctuation mark at a time to build text.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>The post specifies 29 yes/no character questions and appending the highest-probability result. The substantiated claim is an autoregressive selection loop, not training a new general-purpose language model.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#character-chat) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Each round asks 29 yes/no questions, picks the strongest character and appends it. Producing text this way does not establish an advantage over a dedicated text model.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@ryanvogel](https://x.com/ryanvogel) |
| Main post | [Source post](https://x.com/ryanvogel/status/2100218045549412499) |
| Published (UTC) | 2026-09-16T13:39:36+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **866** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:29.946918+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100218045549412499); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100217973000617984/img/AFareJummI08B_QB.jpg" width="640" alt="29-option character generation preview">](https://x.com/ryanvogel/status/2100218045549412499)<br>[Video](https://x.com/ryanvogel/status/2100218045549412499)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100217973000617984/vid/avc1/2204x2160/WurTrR1KHjrK3FZ6.mp4?tag=29) (metadata duration: 15.7s)

Media source: [original publishing page](https://x.com/ryanvogel/status/2100218045549412499). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Let Jev choose one letter or punctuation mark at a time to build text.

**Useful aspect (analysis):** An explicit control loop with more freedom than a fixed word list.

## Inputs, steps and outputs

Evaluate a–z, space, comma and period → append the highest-probability character → feed the updated text back.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author describes 29 character candidates and shares an approximately 15-second demo. | Author report | [Post and attached media](https://x.com/ryanvogel/status/2100218045549412499) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100218045549412499) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Character-level loops require many calls and do not establish a native text-generation API.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
