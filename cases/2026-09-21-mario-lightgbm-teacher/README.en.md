# Mario teacher data: Jev demonstrates, LightGBM takes over

[简体中文](README.md) | **English**

> Generate examples with a teacher model, then let local LightGBM play Mario; the author later changed teachers.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Merge contrary follow-up evidence from the same author and harness. Preserve the original while identifying the switch to DeepSeek; its new completion claim cannot be credited to Jev.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#mario-lightgbm-teacher)

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
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101595622608687104/img/0WizOSDnwuaCFE80.jpg" width="640" alt="Mario teacher data: Jev demonstrates, LightGBM takes over preview">](https://x.com/nwnwnyo/status/2101605150242849140)<br>[Video](https://x.com/nwnwnyo/status/2101605150242849140)

Keep the original 22-second clip and add the 23-second teacher-switch demo, not another Jev application.

- [Direct video 1](https://video.twimg.com/amplify_video/2101595622608687104/vid/avc1/1280x720/B_00-HweMXR0qUSE.mp4?tag=14) (metadata duration: 22.1s)

Media source: [original publishing page](https://x.com/nwnwnyo/status/2101605150242849140). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Generate examples with a teacher model, then let local LightGBM play Mario; the author later changed teachers.

**Useful aspect (analysis):** Moves network waiting to preparation instead of every gameplay decision, unlike continuously calling Jev.

## Inputs, steps and outputs

The original uses Jev teacher data to train LightGBM. A follow-up reports better results with DeepSeek-4.1-Flash outputs in the same harness. LightGBM still runs gameplay; data and training code are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The earlier Jev-teacher version claimed over 300-fold speedup. The update reports repeated original failures, then over 1,000-fold speed and consistent completion with DeepSeek teaching. The latter is not a new Jev achievement; neither claim is independently verified. | Author report | [Results documentation](https://x.com/nwnwnyo/status/2102297736011997680) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101605150242849140) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @nwnwnyo](https://x.com/nwnwnyo/status/2102297736011997680): published 2026-09-22T07:23:33+00:00; 350 likes retrieved 2026-09-23T03:54:25+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2102297736011997680). [Supplementary media 1](https://video.twimg.com/amplify_video/2102297708744904704/vid/avc1/1280x720/BNY1gZ0OLmm3NiHj.mp4?tag=14)

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No matched dataset sizes, unseen-level evaluation or repeated-run records across teachers. These are not intrinsic Jev speedups; preparation and training costs are unknown.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-23T12:09:12+08:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
