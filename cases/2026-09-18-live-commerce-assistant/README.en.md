# Live shopping assistant and avatar expressions

[简体中文](README.md) | **English**

> Recommend products during a conversation and change a virtual shop assistant’s expression with the dialogue.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author identifies a simple demo using Jev plus gpt-live-1. End-to-end behavior is not solely attributable to Jev, expression mapping is not proven unique to it, and recommendation/inventory accuracy is unmeasured.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#live-commerce-assistant)

## How it works, in plain English

Like a shop assistant listening and bringing over products: the conversation system talks, Jev contributes quick judgments, and the app updates recommendations and expressions. The author demonstrates two models together but does not disclose every interface.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@rinte0321](https://x.com/rinte0321) |
| Main post | [Source post](https://x.com/rinte0321/status/2100736454850908344) |
| Published (UTC) | 2026-09-17T23:59:35+00:00 |
| Main-post likes snapshot | **217** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T02:36:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100736454850908344); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100735518963355648/img/o0S0IxXnxWjnlNOG.jpg" width="640" alt="Live shopping assistant and avatar expressions preview">](https://x.com/rinte0321/status/2100736454850908344)<br>[Video](https://x.com/rinte0321/status/2100736454850908344)

The main post’s roughly 65-second video; demonstration footage does not establish recommendation quality or conversion gains.

- [Direct video 1](https://video.twimg.com/amplify_video/2100735518963355648/vid/avc1/1572x1080/729stTM98GihHYmI.mp4?tag=29) (metadata duration: 65.1s)

Media source: [original publishing page](https://x.com/rinte0321/status/2100736454850908344). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Recommend products during a conversation and change a virtual shop assistant’s expression with the dialogue.

**Useful aspect (analysis):** Places recommendations inside a live conversation; closer to a customer-facing shopping experience than offline intent labeling.

## Inputs, steps and outputs

The author combines Jev and gpt-live-1 to update product recommendations during a conversation and change avatar expressions with its content. The exact speech, ranking and expression-mapping responsibilities are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a roughly 65-second live shopping demo using Jev and gpt-live-1, describing the expression feature as a simple implementation. | Author report | [Post and attached media](https://x.com/rinte0321/status/2100736454850908344) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100736454850908344) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

A simple demo without recommendation-relevance, inventory-consistency or end-to-end latency evaluation. Expression mapping does not establish a capability exclusive to Jev.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
