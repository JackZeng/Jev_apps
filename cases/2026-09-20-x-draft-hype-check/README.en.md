# X draft check: flag overhyped wording before posting

[简体中文](README.md) | **English**

> Warn when a draft sounds like exaggerated marketing or a sales pitch.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Supports a draft-style reminder, not fact-checking or reliable judgments about people.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#x-draft-hype-check)

## How it works, in plain English

Like an editor checking whether a draft overdoes its tone; this judges style, not factual truth.

[Back to catalog](../../README.en.md#content) · [Compare similar examples](../../breakdowns/2026-09-18-content.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Content and advertising analysis |
| Platform / author | X / [@unsu0707](https://x.com/unsu0707) |
| Main post | [Source post](https://x.com/unsu0707/status/2101249913099375058) |
| Published (UTC) | 2026-09-19T09:59:53+00:00 |
| Main-post likes snapshot | **446** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:51:41+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101249913099375058); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101248847444078592/img/mGFrlyfBgnJWT-p8.jpg" width="640" alt="X draft check: flag overhyped wording before posting preview">](https://x.com/unsu0707/status/2101249913099375058)<br>[Video](https://x.com/unsu0707/status/2101249913099375058)

An original implementation and video, distinct from feed filtering and virality prediction.

- [Direct video 1](https://video.twimg.com/amplify_video/2101248847444078592/vid/avc1/874x720/9i5mvIyhW-EIe-LA.mp4?tag=14) (metadata duration: 44.1s)

Media source: [original publishing page](https://x.com/unsu0707/status/2101249913099375058). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Warn when a draft sounds like exaggerated marketing or a sales pitch.

**Useful aspect (analysis):** Supports revision before publication, rather than trying to predict reach.

## Inputs, steps and outputs

The author built a browser extension using Jev to assess the style of an X draft. Labels, prompts and trigger frequency are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A roughly 44-second extension demo, without reproducible accuracy or cost figures. | Author report | [Post and attached media](https://x.com/unsu0707/status/2101249913099375058) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101249913099375058) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Style is subjective and does not establish profession, motives or factual accuracy. Human agreement and false-positive rates are missing.

See the [category analysis](../../breakdowns/2026-09-18-content.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
