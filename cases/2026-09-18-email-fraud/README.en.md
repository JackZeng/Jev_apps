# Jev + Kimi email fraud detection

[简体中文](README.md) | **English**

> Screen emails for fraud quickly, then send uncertain cases to a larger model.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A transparent small-sample cascade, but 96/100 belongs to Jev plus Kimi; the confidence threshold and balanced sample do not establish production fraud detection.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#email-fraud) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

It is a two-stage check: Jev screens first and Kimi reviews 31 low-confidence emails. The 96/100 result belongs to the combined pipeline, not Jev alone.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@nutlope](https://x.com/nutlope) |
| Main post | [Source post](https://x.com/nutlope/status/2100614659690713543) |
| Published (UTC) | 2026-09-17T15:55:37+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **542** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:25.698324+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100614659690713543); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100608348219478016/img/23vFEVMegwLrMa8g.jpg" width="640" alt="Jev + Kimi email fraud detection preview">](https://x.com/nutlope/status/2100614659690713543)<br>[Video](https://x.com/nutlope/status/2100614659690713543)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100608348219478016/vid/avc1/2920x2160/8ivDmLmuHZ-ajKFq.mp4?tag=29) (metadata duration: 12.8s)

Media source: [original publishing page](https://x.com/nutlope/status/2100614659690713543). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Screen emails for fraud quickly, then send uncertain cases to a larger model.

**Useful aspect (analysis):** An explicit escalation route and itemized costs support studying a layered classifier.

## Inputs, steps and outputs

100 emails → Jev → 31 emails below the author's 95% threshold go to Kimi K3 → merge results.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports 1.42 seconds for Jev; the full pipeline took 16 seconds, cost about $0.07 and got 96/100 correct. | Author report | [Post and attached media](https://x.com/nutlope/status/2100614659690713543) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100614659690713543) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

96/100 is the combined pipeline result. A small 50:50 sample does not represent real-world fraud prevalence or deployment performance.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
