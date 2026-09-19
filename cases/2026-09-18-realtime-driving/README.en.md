# Unpaused real-time driving

[简体中文](README.md) | **English**

> Keep the car moving while Jev thinks to test real-time simulated driving.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author explicitly bounds the work to an unpaused driving simulator. Timing logs and broad reliability are missing, but the source does not claim validated physical autonomy.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#realtime-driving)

## How it works, in plain English

Pausing the simulator for every model call hides latency. Here it keeps moving, so the observed state may already be outdated when an answer arrives.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@SigGravitas](https://x.com/SigGravitas) |
| Main post | [Source post](https://x.com/SigGravitas/status/2100325221932958134) |
| Published (UTC) | 2026-09-16T20:45:29+00:00 |
| Main-post likes snapshot | **270** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:29.336350+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100325221932958134); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100323655389474816/img/LLOAJ3wie1phk45K.jpg" width="640" alt="Unpaused real-time driving preview">](https://x.com/SigGravitas/status/2100325221932958134)<br>[Video](https://x.com/SigGravitas/status/2100325221932958134)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100323655389474816/vid/avc1/1920x1080/jEAtGJpNs6PA23Ob.mp4?tag=29) (metadata duration: 78.9s)

Media source: [original publishing page](https://x.com/SigGravitas/status/2100325221932958134). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Keep the car moving while Jev thinks to test real-time simulated driving.

**Useful aspect (analysis):** Explicitly exposes latency and stale-state constraints rather than pausing the simulation.

## Inputs, steps and outputs

Continuously advancing simulator state → Jev → raw control inputs; physics does not pause during network waits.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author explicitly states that the simulator runs without pausing for the model. | Author report | [Post and attached media](https://x.com/SigGravitas/status/2100325221932958134) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100325221932958134) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Still a simulator, without coverage, crash-rate or long-duration stability data.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
