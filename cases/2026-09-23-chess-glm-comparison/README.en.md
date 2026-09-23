# Chess comparison: moving faster is not playing better

[简体中文](README.md) | **English**

> Observe Jev and GLM 5.3 speed, cost and outcome in one game.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>B: a limited match, keeping speed and playing strength distinct.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#chess-glm-comparison)

## How it works, in plain English

Two players can differ in thinking time and playing strength; those are separate measures.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@nutlope](https://x.com/nutlope) |
| Main post | [Source post](https://x.com/nutlope/status/2101010773157761481) |
| Published (UTC) | 2026-09-18T18:09:37+00:00 |
| Main-post likes snapshot | **324** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:35+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101010773157761481); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101007875644506112/img/2KoYEIDaUkXehsRC.jpg" width="640" alt="Chess comparison: moving faster is not playing better preview">](https://x.com/nutlope/status/2101010773157761481)<br>[Video](https://x.com/nutlope/status/2101010773157761481)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2101007875644506112/vid/avc1/2636x2160/pUIb4Ym_5wIbmv9P.mp4?tag=29) (metadata duration: 15.6s)

Media source: [original publishing page](https://x.com/nutlope/status/2101010773157761481). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Observe Jev and GLM 5.3 speed, cost and outcome in one game.

**Useful aspect (analysis):** Records a Jev loss explicitly, separating execution efficiency from strategic strength.

## Inputs, steps and outputs

The author stages a match and reports per-move latency and cost. Board encoding, legal-move candidates and settings are not fully disclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports GLM checkmate on move 29, about 0.3s/move for Jev versus 5.8s for GLM, and $0.24 for the game. | Author report | [Post and attached media](https://x.com/nutlope/status/2101010773157761481) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101010773157761481) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

One game cannot establish a stable strength ranking; complete timing and billing logs are absent.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
