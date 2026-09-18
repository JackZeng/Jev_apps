# Viral-post classifier

[简体中文](README.md) | **English**

> Try to identify posts that may attract more attention.

## How it works, in plain English

Jev acts as a fast first-pass classifier. The author does not publish the full criteria or evaluation, so reliable virality prediction is not established.

[Back to catalog](../../README.en.md#content) · [Compare similar examples](../../breakdowns/2026-09-18-content.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Content and advertising analysis |
| Platform / author | X / [@robj3d3](https://x.com/robj3d3) |
| Main post | [Source post](https://x.com/robj3d3/status/2100631889585606959) |
| Published (UTC) | 2026-09-17T17:04:04+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **387** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.294732+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100631889585606959); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSbxP15bMAA1LaU.jpg?name=orig" width="640" alt="Viral-post classifier preview">](https://x.com/robj3d3/status/2100631889585606959)<br>[Image](https://x.com/robj3d3/status/2100631889585606959)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Original image 1](https://pbs.twimg.com/media/HSbxP15bMAA1LaU.jpg?name=orig)

Media source: [original publishing page](https://x.com/robj3d3/status/2100631889585606959). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Try to identify posts that may attract more attention.

**Useful aspect (analysis):** A classification-focused counterpart to live writing feedback.

## Inputs, steps and outputs

The update describes 61 Jev questions per post and a scoring approach fitted using SuperX post data, followed by a write–score–rewrite loop. Exact features, fitting method and independent test split remain undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author says it was built in about eight hours and shares a results screenshot. | Author report | [Post and attached media](https://x.com/robj3d3/status/2100631889585606959) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100631889585606959) | Snapshot at the recorded time, not a live count |

**Same-project demonstration update:** [The author’s new post](https://x.com/robj3d3/status/2100722975645598191) quotes the original and reports fitting on 9,481 posts from 207 creators, 61 questions per post, roughly one second / $0.0004, and selecting the viral post about two out of three times. These are author reports. The new 45-second video is supplementary media, not a separately counted “SuperX app.”

Updates and deduplicated supporting sources:

- [Supporting post by @robj3d3](https://x.com/robj3d3/status/2100722975645598191): published 2026-09-17T23:06:01+00:00; 250 likes retrieved 2026-09-18T02:38:04+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100722975645598191). [Supplementary media 1](https://video.twimg.com/amplify_video/2100722766362406912/vid/avc1/3840x2160/QJqYHBR15YiMvQC8.mp4?tag=29)

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The update provides sample size and per-post cost, but “two out of three” lacks a disclosed independent test split, baseline and cross-author validation. It does not guarantee virality; fitting data should not be described as Jev’s training data.

See the [category analysis](../../breakdowns/2026-09-18-content.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-18T02:43:33+00:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
