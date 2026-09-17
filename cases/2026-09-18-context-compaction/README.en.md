# Tool-history context compaction

[简体中文](README.md) | **English**

> Trim an AI assistant's work history to retain what matters now.

## How it works, in plain English

Rather than rewrite all history as a summary, score tool records for relevance and keep selected ones. This saves context but can omit information needed later.

[Back to catalog](../../README.en.md#memory) · [Compare similar examples](../../breakdowns/2026-09-18-memory.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Context and memory filtering |
| Platform / author | X / [@tamarajtran](https://x.com/tamarajtran) |
| Main post | [Source post](https://x.com/tamarajtran/status/2100694549362553153) |
| Published (UTC) | 2026-09-17T21:13:04+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **1,646** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.956952+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100694549362553153); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100694537672998912/img/OF8vottg6-45ZgNl.jpg" width="640" alt="Tool-history context compaction preview">](https://x.com/tamarajtran/status/2100694549362553153)<br>[Video](https://x.com/tamarajtran/status/2100694549362553153)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100694537672998912/vid/avc1/1180x932/IORPfdtj6gAeFPIH.mp4?tag=29) (metadata duration: 5.0s)

Media source: [original publishing page](https://x.com/tamarajtran/status/2100694549362553153). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Trim an AI assistant's work history to retain what matters now.

**Useful aspect (analysis):** Reduces context through selection without rewriting the entire history as a summary.

## Inputs, steps and outputs

Tool-call records → Jev relevance scores → select records for the context.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a short demo claiming instant compaction, without a full quality evaluation. | Author report | [Post and attached media](https://x.com/tamarajtran/status/2100694549362553153) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100694549362553153) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No long-task retention evaluation; discarded records may be needed later.

See the [category analysis](../../breakdowns/2026-09-18-memory.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
