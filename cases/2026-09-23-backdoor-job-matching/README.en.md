# Backdoor: compare a profile with job opportunities

[简体中文](README.md) | **English**

> Compare candidate information with companies/jobs and flag matches or mismatches.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟠 C · Claims exceed evidence**<br>C concerns presenting semantic fit as predicted hiring chances; retain the screening prototype without validating that probability interpretation.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#backdoor-job-matching)

## How it works, in plain English

Organize a job-search list by checking where experience matches descriptions.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@sarvagya_kul](https://x.com/sarvagya_kul) |
| Main post | [Source post](https://x.com/sarvagya_kul/status/2100980770206879849) |
| Published (UTC) | 2026-09-18T16:10:24+00:00 |
| Main-post likes snapshot | **1,770** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:30:00+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100980770206879849); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100980671640645632/img/19dyomYRhfAONg7S.jpg" width="640" alt="Backdoor: compare a profile with job opportunities preview">](https://x.com/sarvagya_kul/status/2100980770206879849)<br>[Video](https://x.com/sarvagya_kul/status/2100980770206879849)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2100980671640645632/vid/avc1/3016x1646/3ezS0dXo24Hninas.mp4?tag=29) (metadata duration: 11.7s)

Media source: [original publishing page](https://x.com/sarvagya_kul/status/2100980770206879849). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Compare candidate information with companies/jobs and flag matches or mismatches.

**Useful aspect (analysis):** Bulk organization can support subsequent human review.

## Inputs, steps and outputs

The author shows Jev scoring profile/company fit, without disclosed features, job data, rubric or calibration.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The post reports 400 companies and one profile in 12s/$0.0005, with release still forthcoming. | Author report | [Post and attached media](https://x.com/sarvagya_kul/status/2100980770206879849) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100980770206879849) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Fit scores are not hiring probabilities. Real hiring outcomes and bias evaluation are absent, so likely-to-get-the-job claims are unsupported.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
