# Tool-history context compaction

[简体中文](README.md) | **English**

> Trim an AI assistant's work history to retain what matters now.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 10:50:59 (Beijing time, UTC+08:00)

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
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 10:50:59 |
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

At source revision e3f262a: pair tool calls with results, pin the first and recent messages, and fit conversation state to a budget. Tool-output bodies become status/length notes. Jev judges whether to retain each call and result; code keeps, truncates or removes them by thresholds. The Claude Code hook falls back to built-in summarization on errors or insufficient reduction.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a short demo claiming instant compaction, without a full quality evaluation. | Author report | [Post and attached media](https://x.com/tamarajtran/status/2100694549362553153) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100694549362553153) | Snapshot at the recorded time, not a live count |

**2026-09-18 update — merged into the same project:**

- [Alex’s usage report](https://x.com/altryne/status/2100739055923425589) cites the original post and repository, reporting about one second to reduce nearly one million tokens to roughly 86,000. This is another user’s single report, not our reproduction.
- [Theo’s critique](https://x.com/theo/status/2100762304862384257) raises information-loss, reasoning-state and cache-cost concerns. These are a reviewer’s arguments, not uniformly verified findings.
- The [pinned README](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/README.md) and [state.ts](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/state.ts) show budget-fitted conversation context rather than completely isolated calls. However, tool-output bodies are replaced by status/length notes. “Whole conversation” does not mean every original detail is visible.
- That revision explicitly describes `demo/JevDemo` as a scripted recording animation with no API calls. The animation alone is not a live-inference measurement; this also does not negate the separate real API implementation in the library. The plugin was not run.

Updates and deduplicated supporting sources:

- [Supporting post by @tamarajtran](https://x.com/tamarajtran/status/2100694552369897539): published 2026-09-17T21:13:04+00:00; 500 likes retrieved 2026-09-18T02:41:19+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100694552369897539).
- [Supporting post by @altryne](https://x.com/altryne/status/2100739055923425589): published 2026-09-18T00:09:55+00:00; 1,836 likes retrieved 2026-09-18T02:36:40+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100739055923425589). [Supplementary media 1](https://pbs.twimg.com/media/HSdTBk8bAAAPtk8.png?name=orig) [Supplementary media 2](https://pbs.twimg.com/media/HSdTCa_a0AAKYLw.png?name=orig)
- [Supporting post by @theo](https://x.com/theo/status/2100762304862384257): published 2026-09-18T01:42:18+00:00; 347 likes retrieved 2026-09-18T02:36:40+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100762304862384257).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/tamaratran/fast-jev-compaction)

## Mechanism and comparison

No long-task retention or total-cost comparison is available. The state shown to Jev omits tool-output bodies, so filtering may miss important results; history edits also need cache-rebuild evaluation. The new usage report does not establish downstream task quality, and the repository’s recording demo explicitly makes no API calls.

See the [category analysis](../../breakdowns/2026-09-18-memory.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-18T02:43:33+00:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
