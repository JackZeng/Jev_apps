# Tool-history context compaction

[简体中文](README.md) | **English**

> Trim an AI assistant's work history to retain what matters now.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟠 C · Claims exceed evidence**<br>A public adverse evaluation separates fast compaction from long-term savings. Three transcripts, a port and a recovery-enabled baseline are essential limits; the original recording animation is not realtime API measurement.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#context-compaction)

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
| Main-post likes snapshot | **1,646** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.956952+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100694549362553153); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
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
| The original claims instant compaction. A three-transcript Hermes evaluation reports roughly 1.4s per Jev compaction, 115K retained tokens and 75.5% recall versus 55K and 78.9% for production summarization plus search recovery. This catalog did not run the evaluation. | Author report | [Results documentation](https://github.com/NousResearch/hermes-agent/blob/dba815e7ad800dad19f921ca9ad028eba027e8a4/evals/compaction/results/SCORECARD-2026-09-19-jev.md) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100694549362553153) | Snapshot at the recorded time, not a live count |

**2026-09-18 update — merged into the same project:**

- [Alex’s usage report](https://x.com/altryne/status/2100739055923425589) cites the original post and repository, reporting about one second to reduce nearly one million tokens to roughly 86,000. This is another user’s single report, not our reproduction.
- [Theo’s critique](https://x.com/theo/status/2100762304862384257) raises information-loss, reasoning-state and cache-cost concerns. These are a reviewer’s arguments, not uniformly verified findings.
- The [pinned README](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/README.md) and [state.ts](https://github.com/tamaratran/fast-jev-compaction/blob/e3f262a7f4d42bd8dd32ced30d26176f7cb545b0/src/state.ts) show budget-fitted conversation context rather than completely isolated calls. However, tool-output bodies are replaced by status/length notes. “Whole conversation” does not mean every original detail is visible.
- That revision explicitly describes `demo/JevDemo` as a scripted recording animation with no API calls. The animation alone is not a live-inference measurement; this also does not negate the separate real API implementation in the library. The plugin was not run.

**2026-09-20 evaluation update:** The [pinned Hermes scorecard](https://github.com/NousResearch/hermes-agent/blob/dba815e7ad800dad19f921ca9ad028eba027e8a4/evals/compaction/results/SCORECARD-2026-09-19-jev.md) uses three 500K-token prefixes and 15 recall questions each; a fourth fell back because the state would not fit and was not scored. This is an OpenRouter-backed port, not a direct rerun inside Claude Code. The default dropped all unpinned tool candidates, not all history. Matched-budget Jev and recency rankings both scored 77.8%. Raw conversations were not committed and grading used a model. Repeated-compaction results concern a growing text floor consuming reclaimable space, not the permanent absence of new tool calls. These are evaluator-reported results; the post’s generic 10-fold cache-cost claim is not adopted as a universal fact.

Updates and deduplicated supporting sources:

- [Supporting post by @tamarajtran](https://x.com/tamarajtran/status/2100694552369897539): published 2026-09-17T21:13:04+00:00; 500 likes retrieved 2026-09-18T02:41:19+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100694552369897539).
- [Supporting post by @altryne](https://x.com/altryne/status/2100739055923425589): published 2026-09-18T00:09:55+00:00; 1,836 likes retrieved 2026-09-18T02:36:40+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100739055923425589). [Supplementary media 1](https://pbs.twimg.com/media/HSdTBk8bAAAPtk8.png?name=orig) [Supplementary media 2](https://pbs.twimg.com/media/HSdTCa_a0AAKYLw.png?name=orig)
- [Supporting post by @theo](https://x.com/theo/status/2100762304862384257): published 2026-09-18T01:42:18+00:00; 347 likes retrieved 2026-09-18T02:36:40+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100762304862384257).
- [Supporting post by @Teknium](https://x.com/Teknium/status/2101398453578555898): published 2026-09-19T19:50:08+00:00; 894 likes retrieved 2026-09-20T02:45:53+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101398453578555898). [Supplementary media 1](https://pbs.twimg.com/media/HSmb61xbMAAsTQj.jpg?name=orig)

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/tamaratran/fast-jev-compaction)
- [Project / demo link 2](https://github.com/NousResearch/hermes-agent/pull/116246)
- [Project / demo link 3](https://github.com/NousResearch/hermes-agent/blob/dba815e7ad800dad19f921ca9ad028eba027e8a4/evals/compaction/results/SCORECARD-2026-09-19-jev.md)
- [Project / demo link 4](https://github.com/NousResearch/hermes-agent/blob/dba815e7ad800dad19f921ca9ad028eba027e8a4/evals/compaction/jev_arm.py)

## Mechanism and comparison

A new Hermes evaluation exposes retention and long-session limits: its port dropped all 851 unpinned candidates at the default threshold, while repeated compaction retained a growing text floor. Findings apply to this adaptation, sample and budget, not all Jev memory designs.

See the [category analysis](../../breakdowns/2026-09-18-memory.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-18T02:43:33+00:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
| 2026-09-20T11:01:10+08:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
