# Memory retrieval filtering

[简体中文](README.md) | **English**

> Filter an AI memory store so the next model sees relevant material.

## How it works, in plain English

Retrieve candidate memories, then use Jev for a second filter. It resembles picking useful search results; overly aggressive filtering can miss key evidence.

[Back to catalog](../../README.en.md#memory) · [Compare similar examples](../../breakdowns/2026-09-18-memory.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Context and memory filtering |
| Platform / author | X / [@moritzkremb](https://x.com/moritzkremb) |
| Main post | [Source post](https://x.com/moritzkremb/status/2100566009312940457) |
| Published (UTC) | 2026-09-17T12:42:17+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **335** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:27.020275+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100566009312940457); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100565973376061440/img/jeTib61RNpwXn853.jpg" width="640" alt="Memory retrieval filtering preview">](https://x.com/moritzkremb/status/2100566009312940457)<br>[Video](https://x.com/moritzkremb/status/2100566009312940457)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100565973376061440/vid/avc1/1920x1080/czw3cutAR-gg2PBL.mp4?tag=16) (metadata duration: 135.1s)

Media source: [original publishing page](https://x.com/moritzkremb/status/2100566009312940457). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Filter an AI memory store so the next model sees relevant material.

**Useful aspect (analysis):** A post-retrieval filter that can complement existing memory systems.

## Inputs, steps and outputs

Memory candidates → Jev relevance judgments → filtered content for the next model; retrieval details are unknown.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports 94% fewer tokens and 2–3× faster retrieval, not independently reproduced here. | Author report | [Post and attached media](https://x.com/moritzkremb/status/2100566009312940457) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100566009312940457) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Explicitly a quick test, without recall or long-task accuracy data.

See the [category analysis](../../breakdowns/2026-09-18-memory.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
