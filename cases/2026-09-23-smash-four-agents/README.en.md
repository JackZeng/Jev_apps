# Smash with four agents: simultaneous character decisions

[简体中文](README.md) | **English**

> Let Jev control four characters fighting in the same match.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Independent author/media, compared with the Pi controller. Behavior is demonstrated; cost and playing strength remain unverified.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#smash-four-agents)

## How it works, in plain English

Four players each choose moves while the game engine executes them.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@maubaron](https://x.com/maubaron) |
| Main post | [Source post](https://x.com/maubaron/status/2100738237237002706) |
| Published (UTC) | 2026-09-18T00:06:40+00:00 |
| Main-post likes snapshot | **3,680** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:46+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100738237237002706); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100731665513349120/img/j4DcB9CxjN8DX4qe.jpg" width="640" alt="Smash with four agents: simultaneous character decisions preview">](https://x.com/maubaron/status/2100738237237002706)<br>[Video](https://x.com/maubaron/status/2100738237237002706)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2100731665513349120/vid/avc1/2560x1440/fmGbOoeSxjYD1X86.mp4?tag=29) (metadata duration: 107.5s)

Media source: [original publishing page](https://x.com/maubaron/status/2100738237237002706). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Let Jev control four characters fighting in the same match.

**Useful aspect (analysis):** Shows interacting parallel agents rather than one character against a CPU.

## Inputs, steps and outputs

The author describes per-character decisions; observation format, move candidates, update rate and controller interface are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The post reports over 22M tokens for a few cents, without a bill, model version or complete accounting; that cost is not independently confirmed. | Author report | [Post and attached media](https://x.com/maubaron/status/2100738237237002706) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100738237237002706) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No strong-opponent comparison, win rate or latency distribution. Visible activity does not establish tactical strength.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
