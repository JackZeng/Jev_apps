# JevMeter speech-analysis dashboard

[简体中文](README.md) | **English**

> Score sentences in debates or interviews to examine speech patterns and content features.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟠 C · Claims exceed evidence**<br>The implementation supports rhetorical sentence scoring, while the follow-up fact-checking claim contradicts its own README disclaimer. The 200 authored-sentence evaluation measures preset classification, not truth verification.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#jevmeter)

## How it works, in plain English

Ask the same five questions about each sentence and visualize the results. Consistent criteria help comparisons, but without external evidence checks they do not determine truth.

[Back to catalog](../../README.en.md#content) · [Compare similar examples](../../breakdowns/2026-09-18-content.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Content and advertising analysis |
| Platform / author | X / [@chetaslua](https://x.com/chetaslua) |
| Main post | [Source post](https://x.com/chetaslua/status/2100473581251748216) |
| Published (UTC) | 2026-09-17T06:35:01+00:00 |
| Main-post likes snapshot | **1,017** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.874127+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100473581251748216); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100473445868003328/img/1ukjahQYLgbIEmyI.jpg" width="640" alt="JevMeter speech-analysis dashboard preview">](https://x.com/chetaslua/status/2100473581251748216)<br>[Video](https://x.com/chetaslua/status/2100473581251748216)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100473445868003328/vid/avc1/1920x1080/aPuEpkmSR4nxTOf7.mp4?tag=29) (metadata duration: 116.9s)

Media source: [original publishing page](https://x.com/chetaslua/status/2100473581251748216). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Score sentences in debates or interviews to examine speech patterns and content features.

**Useful aspect (analysis):** Fixed questions support applying the same criteria to the material.

## Inputs, steps and outputs

Sentences → five yes/no questions per sentence → aggregate and display indicators; code was later released.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports 1,191 calls, 415ms median latency and $0.0497 for the debate experiment. | Author report | [Post and attached media](https://x.com/chetaslua/status/2100473581251748216) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100473581251748216) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @chetaslua](https://x.com/chetaslua/status/2100602714204049588): published 2026-09-17T15:08:09+00:00; 231 likes retrieved 2026-09-17T22:42:26.950354+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100602714204049588). [Supplementary media 1](https://video.twimg.com/amplify_video/2100602569987121152/vid/avc1/1920x1080/fvF0p2eL9x5cK2yn.mp4?tag=29)

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/ChetasLua/jevmeter)

## Mechanism and comparison

The first post explicitly says it is not fact-checking. Later promotional wording does not establish verification of truth.

See the [category analysis](../../breakdowns/2026-09-18-content.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
