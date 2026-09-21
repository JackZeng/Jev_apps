# Token-choice loop: assemble text through repeated decisions

[简体中文](README.md) | **English**

> Repeatedly ask Jev to choose the next token from candidates.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A sourced loop and prototype, with text quality and efficiency still unverified.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#token-choice-loop)

## How it works, in plain English

Build a sentence by choosing one piece from a tray at each step.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@erikdunteman](https://x.com/erikdunteman) |
| Main post | [Source post](https://x.com/erikdunteman/status/2101533797527454109) |
| Published (UTC) | 2026-09-20T04:47:56+00:00 |
| Main-post likes snapshot | **211** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-21T02:50:32+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101533797527454109); may be cached |
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101533698042785792/img/qrWkmPUgmo0GVwUK.jpg" width="640" alt="Token-choice loop: assemble text through repeated decisions preview">](https://x.com/erikdunteman/status/2101533797527454109)<br>[Video](https://x.com/erikdunteman/status/2101533797527454109)

Independent author and media, grouped with word/character loops; reposts are not separate cases.

- [Direct video 1](https://video.twimg.com/amplify_video/2101533698042785792/vid/avc1/1712x1216/vsoeAn2rMIZ5X9ti.mp4?tag=29) (metadata duration: 22.0s)

Media source: [original publishing page](https://x.com/erikdunteman/status/2101533797527454109). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Repeatedly ask Jev to choose the next token from candidates.

**Useful aspect (analysis):** Complements word- and character-choice experiments, illustrating how candidate granularity affects assembled text.

## Inputs, steps and outputs

The author places Jev in an autoregressive loop with possible next tokens. The full vocabulary, stopping rule and sampling procedure are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A roughly 22-second demo; the author cautiously says it partly works, without general performance conclusions. | Author report | [Post and attached media](https://x.com/erikdunteman/status/2101533797527454109) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101533797527454109) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No language-quality, total-call or full-response latency comparison. This is not a native generation endpoint or established chat model.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
