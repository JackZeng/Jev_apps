# Predictive keyboard: light up a likely next key

[简体中文](README.md) | **English**

> Use active-application context to highlight a likely next key.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Supports a hardware prototype, not proven typing gains or compatibility with every application.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#predictive-keyboard)

## How it works, in plain English

A small keyboard hint considers what you are doing and suggests where to press next.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@neogoose_btw](https://x.com/neogoose_btw) |
| Main post | [Source post](https://x.com/neogoose_btw/status/2101556786528760050) |
| Published (UTC) | 2026-09-20T06:19:17+00:00 |
| Main-post likes snapshot | **478** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:30:03+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101556786528760050); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101556538381139968/img/ILH0mqDphFwHNSZw.jpg" width="640" alt="Predictive keyboard: light up a likely next key preview">](https://x.com/neogoose_btw/status/2101556786528760050)<br>[Video](https://x.com/neogoose_btw/status/2101556786528760050)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2101556538381139968/vid/avc1/2022x3320/rMW0nIIEM7UkXmlQ.mp4?tag=29) (metadata duration: 35.2s)

Media source: [original publishing page](https://x.com/neogoose_btw/status/2101556786528760050). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use active-application context to highlight a likely next key.

**Useful aspect (analysis):** Hardware feedback differs from software launchers and history-completion suggestions.

## Inputs, steps and outputs

The author combines custom firmware with application context and Jev predictions for Vim commands, endings or phrases. Context capture and candidate encoding are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A described near-realtime key-light demo; full-loop latency remains unknown. | Author report | [Post and attached media](https://x.com/neogoose_btw/status/2101556786528760050) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101556786528760050) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

This is not offline Jev running on the keyboard. Prediction accuracy, distractions and typing-efficiency comparisons are absent.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
