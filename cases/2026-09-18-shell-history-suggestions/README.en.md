# Shell history: semantic command suggestions

[简体中文](README.md) | **English**

> Type part of a command or describe an intent to select a suggestion from past commands.

**Added to README:** 2026-09-18 19:44:51<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Pinned docs specify history candidates, prefix filtering, Choice/Noul gates and stale-result rejection. The demo uses fabricated history and reports 0.7–0.9 s latency; everyday adoption and long-term acceptance are not established.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#shell-history-suggestions) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Like a history menu that understands meaning: code lists previous commands and Jev picks the closest to your intent. Code controls candidates, matching and display; the user accepts a suggestion into the command line.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@thorstenball](https://x.com/thorstenball) |
| Main post | [Source post](https://x.com/thorstenball/status/2100858434904109099) |
| Published (UTC) | 2026-09-18T08:04:17+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 19:44:51 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **396** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T11:39:31+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100858434904109099); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100858390683475969/img/PRKkLSCaQKsfoXRI.jpg" width="640" alt="Shell history: semantic command suggestions preview">](https://x.com/thorstenball/status/2100858434904109099)<br>[Video](https://x.com/thorstenball/status/2100858434904109099)

The main video and the author’s Amp production video are one project. A demonstration with fabricated history is not a real-user-log evaluation.

- [Direct video 1](https://video.twimg.com/amplify_video/2100858390683475969/vid/avc1/1280x720/12nAuetEpzApPuvX.mp4?tag=29) (metadata duration: 22.2s)

Media source: [original publishing page](https://x.com/thorstenball/status/2100858434904109099). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Type part of a command or describe an intent to select a suggestion from past commands.

**Useful aspect (analysis):** Supports intent descriptions beyond literal prefixes while restricting outputs to historical candidates. Like the predictive launcher it selects candidates, but operates on commands rather than files.

## Inputs, steps and outputs

The pinned README describes a zsh plugin using the latest 100 distinct history entries, narrowing to prefix matches when available. A single prefix candidate skips the model. Otherwise Choice selects a command ID and Noul judges whether any candidate fits; thresholds gate suggestions and stale responses are discarded after input changes.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a roughly 22-second demo and repository, then states that Amp produced the demo. The repository README explicitly says it uses fabricated command history. | Author report | [Post and attached media](https://x.com/thorstenball/status/2100858434904109099) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100858434904109099) | Snapshot at the recorded time, not a live count |

**Documentation review:** Read the [README at 4b2b75d](https://github.com/mrnugget/jev-shell-history/blob/4b2b75d26c0ccf5726263904514a22a8e11659ea/README.md), distinguishing prefix filtering, Jev candidate judgments and zsh acceptance. The plugin was not installed and local shell history was not transmitted.

Updates and deduplicated supporting sources:

- [Supporting post by @thorstenball](https://x.com/thorstenball/status/2100860748175921398): published 2026-09-18T08:13:29+00:00; 25 likes retrieved 2026-09-18T11:41:16+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100860748175921398).
- [Supporting post by @thorstenball](https://x.com/thorstenball/status/2100891804136505584): published 2026-09-18T10:16:53+00:00; 12 likes retrieved 2026-09-18T11:41:16+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100891804136505584). [Supplementary media 1](https://video.twimg.com/amplify_video/2100891117461925888/vid/avc1/3480x2160/LON1FWy2jhqMJuVU.mp4?tag=29)
- [Supporting post by @thorstenball](https://x.com/thorstenball/status/2100867609549848659): published 2026-09-18T08:40:45+00:00; 3 likes retrieved 2026-09-18T11:41:16+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100867609549848659).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/mrnugget/jev-shell-history)

## Mechanism and comparison

History can be stale or sensitive and is sent to the service as candidate data. A suitable suggestion does not establish safe execution; user review remains necessary. The README reports roughly 0.7–0.9 seconds per request, not the millisecond claims from other demos. The author presents an experiment, not evidence of daily use.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
