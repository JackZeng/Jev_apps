# Mario teacher data: Jev demonstrates, LightGBM takes over

[简体中文](README.md) | **English**

> Generate training examples with Jev, then control Mario with local LightGBM.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Teacher and runtime models are clearly distinguished, while generalization and reliable completion remain unverified.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#mario-lightgbm-teacher)

## How it works, in plain English

A coach demonstrates and a trainee takes over; the trainee runs during gameplay.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@nwnwnyo](https://x.com/nwnwnyo) |
| Main post | [Source post](https://x.com/nwnwnyo/status/2101605150242849140) |
| Published (UTC) | 2026-09-20T09:31:28+00:00 |
| Main-post likes snapshot | **945** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-21T02:49:26+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101605150242849140); may be cached |
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101595622608687104/img/0WizOSDnwuaCFE80.jpg" width="640" alt="Mario teacher data: Jev demonstrates, LightGBM takes over preview">](https://x.com/nwnwnyo/status/2101605150242849140)<br>[Video](https://x.com/nwnwnyo/status/2101605150242849140)

Compared with other Mario controllers by runtime architecture; reposts of this experiment are not new cases.

- [Direct video 1](https://video.twimg.com/amplify_video/2101595622608687104/vid/avc1/1280x720/B_00-HweMXR0qUSE.mp4?tag=14) (metadata duration: 22.1s)

Media source: [original publishing page](https://x.com/nwnwnyo/status/2101605150242849140). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Generate training examples with Jev, then control Mario with local LightGBM.

**Useful aspect (analysis):** Moves network waiting to preparation instead of every gameplay decision, unlike continuously calling Jev.

## Inputs, steps and outputs

The author reports excessive Jev latency from Japan, then generates teacher data and trains LightGBM to replace live decisions. Samples, features and training code are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author claims over 300-fold faster decisions and a completion, with a roughly 22-second clip; the ratio is specific to that reported setup. | Author report | [Post and attached media](https://x.com/nwnwnyo/status/2101605150242849140) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101605150242849140) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

This does not accelerate Jev itself. Dataset size, unseen-level results, repeated completion rates and full preparation costs are unknown.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
