# CoreML + OCR desktop clicks

[简体中文](README.md) | **English**

> Recognize buttons and labels on a Mac, then ask Jev which one to click.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Local OCR plus remote text decisions is technically coherent. The reported 90 ms is per decision, not end-to-end latency; the short demo and author report do not establish general desktop reliability.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#coreml-ocr) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Local recognition software does the screen-reading and lists the button labels. Jev chooses from that list. Images stay on the device, but recognized text is still sent to Jev.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@milindlabs](https://x.com/milindlabs) |
| Main post | [Source post](https://x.com/milindlabs/status/2100631847155994852) |
| Published (UTC) | 2026-09-17T17:03:54+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **564** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:22.793465+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100631847155994852); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100629037790183424/img/NR6wQpZiC-xjCEsC.jpg" width="640" alt="CoreML + OCR desktop clicks preview">](https://x.com/milindlabs/status/2100631847155994852)<br>[Video](https://x.com/milindlabs/status/2100631847155994852)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100629037790183424/vid/avc1/3324x2160/nTz-UJM8mYnHqARF.mp4?tag=29) (metadata duration: 133.9s)

Media source: [original publishing page](https://x.com/milindlabs/status/2100631847155994852). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Recognize buttons and labels on a Mac, then ask Jev which one to click.

**Useful aspect (analysis):** No DOM required. The author says screen pixels stay on the Mac, offering a route to native-app control.

## Inputs, steps and outputs

Local CoreML segments UI elements → on-device OCR reads labels → Jev assigns probabilities to elements → click and detect again.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports roughly 90ms per decision, without a full task benchmark. | Author report | [Post and attached media](https://x.com/milindlabs/status/2100631847155994852) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100631847155994852) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

OCR and detection errors affect results. Label text still leaves the device, so this is not fully offline.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
