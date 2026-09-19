# Super Mario · Jev / Qwen comparison

[简体中文](README.md) | **English**

> Give Jev and Qwen the same Mario information and compare action choices.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>The bounded setup is unusually explicit: identical structured observations and five actions. This supports the comparison design, not a general ranking or independent reproduction.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#mario-comparison)

## How it works, in plain English

Convert the game state to structured data and give both models five choices. They take the same multiple-choice test rather than receiving different kinds of observations.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@karaage0703](https://x.com/karaage0703) |
| Main post | [Source post](https://x.com/karaage0703/status/2100569924238471355) |
| Published (UTC) | 2026-09-17T12:57:51+00:00 |
| Main-post likes snapshot | **284** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:27.523986+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100569924238471355); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100567975317454849/img/UjFbLkeMH5RdOrlS.jpg" width="640" alt="Super Mario · Jev / Qwen comparison preview">](https://x.com/karaage0703/status/2100569924238471355)<br>[Video](https://x.com/karaage0703/status/2100569924238471355)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100567975317454849/vid/avc1/1280x720/5LJQvGE0heT0eUwB.mp4?tag=29) (metadata duration: 39.7s)

Media source: [original publishing page](https://x.com/karaage0703/status/2100569924238471355). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Give Jev and Qwen the same Mario information and compare action choices.

**Useful aspect (analysis):** Explicitly controls input format and action count for comparing model choices.

## Inputs, steps and outputs

Convert game information to structured data → each model chooses one of five actions → execute in the game.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a same-condition demo and explicitly says Jev does not receive game images. | Author report | [Post and attached media](https://x.com/karaage0703/status/2100569924238471355) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100569924238471355) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Not a native-vision comparison; repeated-run success rates and network conditions are absent.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
