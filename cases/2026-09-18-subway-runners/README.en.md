# Parallel Subway Surfers demo

[简体中文](README.md) | **English**

> Demonstrate Jev controlling multiple runner-style games at once.

## How it works, in plain English

Several game environments request decisions in parallel and execute them separately. The original client versus recreation is unspecified, so this is not evidence of general phone control.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@_MaxBlade](https://x.com/_MaxBlade) |
| Main post | [Source post](https://x.com/_MaxBlade/status/2100634359099232678) |
| Published (UTC) | 2026-09-17T17:13:53+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **1,474** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:28.213323+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100634359099232678); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100633400717565952/img/KlytLNSLCQA-yY2E.jpg" width="640" alt="Parallel Subway Surfers demo preview">](https://x.com/_MaxBlade/status/2100634359099232678)<br>[Video](https://x.com/_MaxBlade/status/2100634359099232678)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100633400717565952/vid/avc1/1920x1080/qYdwajEzKFl86kYo.mp4?tag=29) (metadata duration: 185.9s)

Media source: [original publishing page](https://x.com/_MaxBlade/status/2100634359099232678). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Demonstrate Jev controlling multiple runner-style games at once.

**Useful aspect (analysis):** Shows parallel-environment throughput for studying multi-instance control.

## Inputs, steps and outputs

Game environments and Jev form action loops; scheduling and game implementation details are not disclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports 50 simultaneous games and less than $0.01 for the run. | Author report | [Post and attached media](https://x.com/_MaxBlade/status/2100634359099232678) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100634359099232678) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

It is unclear whether this uses the original client, a recreation or a simulator; it is not evidence of general phone control.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
