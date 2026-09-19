# Coding Garden tool assistant

[简体中文](README.md) | **English**

> Ask for weather, information or to-do actions and let an assistant call the right tool.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟠 C · Claims exceed evidence**<br>The tool-based assistant demo is credible, but eliminating free-form generation does not guarantee error-free answers. Tool selection, arguments and retrieved sources can still be wrong, so the categorical no-hallucination claim is overstated.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#coding-garden-assistant)

## How it works, in plain English

Jev selects a tool and its arguments; the tool returns results and the interface displays them. Even sourced answers can be wrong if the wrong tool or arguments are chosen.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@CodingGarden](https://x.com/CodingGarden) |
| Main post | [Source post](https://x.com/CodingGarden/status/2100665210419950031) |
| Published (UTC) | 2026-09-17T19:16:29+00:00 |
| Main-post likes snapshot | **334** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:23.899501+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100665210419950031); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100664410935332864/img/KPApgq0AysL_SFeg.jpg" width="640" alt="Coding Garden tool assistant preview">](https://x.com/CodingGarden/status/2100665210419950031)<br>[Video](https://x.com/CodingGarden/status/2100665210419950031)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100664410935332864/vid/avc1/1920x1080/ismjaOhzadz-zS-J.mp4?tag=29) (metadata duration: 257.6s)

Media source: [original publishing page](https://x.com/CodingGarden/status/2100665210419950031). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Ask for weather, information or to-do actions and let an assistant call the right tool.

**Useful aspect (analysis):** Connects tool results to a conversational interface for common personal-assistant tasks.

## Inputs, steps and outputs

User prompt → Jev chooses a tool and arguments → tool returns results → assistant presents them with sources.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares an approximately four-minute demo and says no text-generating LLM is used. | Author report | [Post and attached media](https://x.com/CodingGarden/status/2100665210419950031) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100665210419950031) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Arguments and tool choices can still be wrong; the author's claim of no hallucinations is not established.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
