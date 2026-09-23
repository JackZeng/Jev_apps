# OpenClaw: a shared decision interface for plugins

[简体中文](README.md) | **English**

> Let plugins or application code request classification, scoring and choices for later workflow steps.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Official support for interface progress, with production release and proposed-use outcomes unverified. This is opt-in, not automatic activation of every feature.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#openclaw-decisions)

## How it works, in plain English

Add a standard socket to a toolbox: code asks which option to choose, and an adapter sends the question to Jev.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@openclaw](https://x.com/openclaw) |
| Main post | [Source post](https://x.com/openclaw/status/2102488199486656862) |
| Published (UTC) | 2026-09-22T20:00:23+00:00 |
| Main-post likes snapshot | **438** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T03:51:47+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102488199486656862); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102486637041315840/img/FzZ0g52-3ocut6K2.jpg" width="640" alt="OpenClaw: a shared decision interface for plugins preview">](https://x.com/openclaw/status/2102488199486656862)<br>[Video](https://x.com/openclaw/status/2102488199486656862)

One Jev interface integration; another supported model and proposed plugins are not separate applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2102486637041315840/vid/avc1/1920x1080/qdoC_rPt1yepniSv.mp4?tag=29) (metadata duration: 411.1s)

Media source: [original publishing page](https://x.com/openclaw/status/2102488199486656862). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Let plugins or application code request classification, scoring and choices for later workflow steps.

**Useful aspect (analysis):** A common plugin interface makes decisions reusable without requiring a chat model to initiate every judgment.

## Inputs, steps and outputs

The official article exposes api.runtime.decisions.evaluate in the Plugin SDK, backed by a configured decision model. Application code can now call directly, alongside the earlier agent-facing decision tool.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| An official roughly 6-minute-51-second video and design article, without controlled throughput, cost or quality results. | Author report | [Post and attached media](https://x.com/openclaw/status/2102488199486656862) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102488199486656862) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://openclaw.ai/blog/decision-models-in-openclaw)

## Mechanism and comparison

Available in development checkouts; provider packages await a supporting release. Voice gating, tool filtering, compaction and routing are largely explorations or proposals, not all shipped features.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
