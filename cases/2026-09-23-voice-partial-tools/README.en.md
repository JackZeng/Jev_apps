# Partial-speech tool choice: decide before the utterance ends

[简体中文](README.md) | **English**

> Explore whether a tool can be selected from an unfinished speech transcript.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Clear task and substitution point; benefits and failures require real-conversation measurement.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#voice-partial-tools)

## How it works, in plain English

Infer the direction of a request early while later words complete it.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@BhosalePratim](https://x.com/BhosalePratim) |
| Main post | [Source post](https://x.com/BhosalePratim/status/2100986774742765991) |
| Published (UTC) | 2026-09-18T16:34:16+00:00 |
| Main-post likes snapshot | **477** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:36+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100986774742765991); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100986186219081728/img/LmAGU-0Pd5ZABGeb.jpg" width="640" alt="Partial-speech tool choice: decide before the utterance ends preview">](https://x.com/BhosalePratim/status/2100986774742765991)<br>[Video](https://x.com/BhosalePratim/status/2100986774742765991)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2100986186219081728/vid/avc1/2344x1722/sVStRPvpF00xcih6.mp4?tag=29) (metadata duration: 70.0s)

Media source: [original publishing page](https://x.com/BhosalePratim/status/2100986774742765991). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Explore whether a tool can be selected from an unfinished speech transcript.

**Useful aspect (analysis):** Unlike end-of-turn detection, asks whether enough information exists before speech finishes.

## Inputs, steps and outputs

The author replaces LLM tool selection in a voice agent with Jev decisions on partial transcripts. Execution thresholds and cancellation are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A tool-calling learning experiment, not a validated general voice agent. | Author report | [Post and attached media](https://x.com/BhosalePratim/status/2100986774742765991) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100986774742765991) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Self-corrections can invalidate early choices. No error, latency or completion comparison against waiting for full speech.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
