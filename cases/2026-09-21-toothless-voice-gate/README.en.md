# Toothless: decide whether speech addresses the assistant

[简体中文](README.md) | **English**

> Separate assistant-directed remarks from people talking to each other.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Supports an activation-gate prototype; natural turn-taking and persistent reliability remain unverified.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#toothless-voice-gate)

## How it works, in plain English

Like a considerate listener, use conversational context to decide whether to respond.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@ashutoshpuro97](https://x.com/ashutoshpuro97) |
| Main post | [Source post](https://x.com/ashutoshpuro97/status/2101660362882085299) |
| Published (UTC) | 2026-09-20T13:10:52+00:00 |
| Main-post likes snapshot | **266** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-21T02:48:14+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101660362882085299); may be cached |
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101659226607321089/img/iDIVp1YnUasEtGo9.jpg" width="640" alt="Toothless: decide whether speech addresses the assistant preview">](https://x.com/ashutoshpuro97/status/2101660362882085299)<br>[Video](https://x.com/ashutoshpuro97/status/2101660362882085299)

Independent author and media, grouped with CNVS rather than treated as its update.

- [Direct video 1](https://video.twimg.com/amplify_video/2101659226607321089/vid/avc1/1920x1080/VEQywvQopJ0O1No7.mp4?tag=29) (metadata duration: 220.9s)

Media source: [original publishing page](https://x.com/ashutoshpuro97/status/2101660362882085299). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Separate assistant-directed remarks from people talking to each other.

**Useful aspect (analysis):** Shares wake-word-free interaction with CNVS, emphasizing when to join a multi-person conversation.

## Inputs, steps and outputs

The author describes simultaneous checks for topic continuation, internet needs and potential assistant usefulness. Transcription, speaker information and the final activation rule are not fully disclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A roughly 3m40s prototype demo, without controlled latency, quality or all-day evaluation. | Author report | [Post and attached media](https://x.com/ashutoshpuro97/status/2101660362882085299) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101660362882085299) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No multi-speaker false-activation or miss rates. This does not establish direct audio understanding by Jev or reliable addressee recognition.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
