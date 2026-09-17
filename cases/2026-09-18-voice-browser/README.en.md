# Voice-controlled browser

[简体中文](README.md) | **English**

> Speak a command, such as “go back,” and let the browser act.

## How it works, in plain English

Speech is first transcribed. Jev maps the text to an action, then the browser executes it. Jev chooses what to do; a separate component handles the audio.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@moritzkremb](https://x.com/moritzkremb) |
| Main post | [Source post](https://x.com/moritzkremb/status/2100577979021832365) |
| Published (UTC) | 2026-09-17T13:29:51+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **1,829** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:22.752244+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100577979021832365); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100577954338373633/img/tbH43kHpUotE3hzK.jpg" width="640" alt="Voice-controlled browser preview">](https://x.com/moritzkremb/status/2100577979021832365)<br>[Video](https://x.com/moritzkremb/status/2100577979021832365)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100577954338373633/vid/avc1/1920x1080/f30FtLe23N2iCgyX.mp4?tag=16) (metadata duration: 39.5s)

Media source: [original publishing page](https://x.com/moritzkremb/status/2100577979021832365). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Speak a command, such as “go back,” and let the browser act.

**Useful aspect (analysis):** Hands-free interaction for short, explicit commands.

## Inputs, steps and outputs

Speech transcription → Jev interprets the action → browser execution.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports about 300ms and $0.0002 per decision. | Author report | [Post and attached media](https://x.com/moritzkremb/status/2100577979021832365) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100577979021832365) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Transcription, targeting and browser execution add overhead; decision latency is not end-to-end latency.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
