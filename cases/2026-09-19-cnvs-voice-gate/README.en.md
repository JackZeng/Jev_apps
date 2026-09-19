# CNVS: gate voice commands without a wake word

[简体中文](README.md) | **English**

> Decide whether a spoken utterance is directed at the computer.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The video supports an intent-gating experiment within a speech/action pipeline. Long-term false activations, missed commands and transcription details are unknown; an ambient Jarvis remains a vision rather than demonstrated full autonomy.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#cnvs-voice-gate)

## How it works, in plain English

Like a listener distinguishing conversation from a request: only accepted utterances enter the action workflow. Speech recognition and execution remain surrounding-system responsibilities.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@_MaxBlade](https://x.com/_MaxBlade) |
| Main post | [Source post](https://x.com/_MaxBlade/status/2100967959879471519) |
| Published (UTC) | 2026-09-18T15:19:30+00:00 |
| Main-post likes snapshot | **1,053** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T22:49:18+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100967959879471519); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100966551826444288/img/i2s52ZeMNTOO-IRD.jpg" width="640" alt="CNVS: gate voice commands without a wake word preview">](https://x.com/_MaxBlade/status/2100967959879471519)<br>[Video](https://x.com/_MaxBlade/status/2100967959879471519)

Separate from this author’s game demo and another author’s voice canvas because the tasks and videos differ.

- [Direct video 1](https://video.twimg.com/amplify_video/2100966551826444288/vid/avc1/3808x2160/-l1FkaXsmJs5BGfK.mp4?tag=29) (metadata duration: 83.6s)

Media source: [original publishing page](https://x.com/_MaxBlade/status/2100967959879471519). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Decide whether a spoken utterance is directed at the computer.

**Useful aspect (analysis):** Unlike the voice-and-gesture canvas, this focuses on deciding whether to respond, without a fixed activation phrase.

## Inputs, steps and outputs

The author uses Jev probabilities to distinguish commands from incidental speech in CNVS without a wake word. Transcription components, thresholds and execution interfaces are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares roughly 84 seconds of interaction, without an independent activation-accuracy comparison. | Author report | [Post and attached media](https://x.com/_MaxBlade/status/2100967959879471519) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100967959879471519) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

False activations, missed commands, recording handling and end-to-end latency lack evaluation. A text decision model should not be described as directly understanding raw audio.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
