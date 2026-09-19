# Voice-and-pointing canvas control

[简体中文](README.md) | **English**

> Use speech and pointing together to say “put that over there” on a canvas.

**Added to README:** 2026-09-18 10:50:59<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author explains keyword-timed pointing and several small judgments, explicitly admitting imperfect behavior. Perception libraries, success rates and recovery are unreported; the demo is a feasibility experiment.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#voice-gesture-canvas) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

The app records where you point when saying words such as “that” and “there,” then asks Jev a few separate questions. It avoids enumerating every object, action and position combination as one huge choice list.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@jackcheng](https://x.com/jackcheng) |
| Main post | [Source post](https://x.com/jackcheng/status/2100729670991802386) |
| Published (UTC) | 2026-09-17T23:32:37+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 10:50:59 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **915** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T02:36:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100729670991802386); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100729243185324032/img/YNw8njfnSXu-Tbyr.jpg" width="640" alt="Voice-and-pointing canvas control preview">](https://x.com/jackcheng/status/2100729670991802386)<br>[Video](https://x.com/jackcheng/status/2100729670991802386)

The video interface shows a canvas, camera and separate input/decision panels. Implementation details come from the author’s reply; this is not evidence that Jev directly recognizes video.

- [Direct video 1](https://video.twimg.com/amplify_video/2100729243185324032/vid/avc1/2316x1756/H3toCH4Ykl3HBkxA.mp4?tag=29) (metadata duration: 39.0s)

Media source: [original publishing page](https://x.com/jackcheng/status/2100729670991802386). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use speech and pointing together to say “put that over there” on a canvas.

**Useful aspect (analysis):** Combines language and pointing to resolve references missing from text alone. Compared with TypeGPU’s semantic effects, this example focuses on manipulating canvas objects.

## Inputs, steps and outputs

According to the author’s reply, the app captures pointing at key words and splits each sentence into a few small questions for Jev to confirm, then executes canvas actions. The video interface displays speech, finger and canvas state; perception libraries are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a roughly 39-second canvas demo and explains pointing capture and question decomposition in a reply. | Author report | [Post and attached media](https://x.com/jackcheng/status/2100729670991802386) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100729670991802386) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @jackcheng](https://x.com/jackcheng/status/2100769017115902136): published 2026-09-18T02:08:58+00:00; 0 likes retrieved 2026-09-18T02:43:03+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100769017115902136).

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The author explicitly describes an imperfect feasibility experiment. No pointing-error, speech-error or action-success evaluation is available, and separate decisions still require consistency checks.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
