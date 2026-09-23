# StarCraft II: plan globally and control squads with Jev

[简体中文](README.md) | **English**

> Use a planning model for tactics and multiple Jev loops for unit decisions.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A bounded StarCraft II prototype; quoted games are not conflated, and success/generalization remain unverified.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#starcraft2-squads)

## How it works, in plain English

A coach sets the plan; squads choose their next moves as the situation changes.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@GZhan57](https://x.com/GZhan57) |
| Main post | [Source post](https://x.com/GZhan57/status/2102126922688012410) |
| Published (UTC) | 2026-09-21T20:04:48+00:00 |
| Main-post likes snapshot | **709** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:31:26+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102126922688012410); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102121853624184832/img/GMYdvXYpr-xFZziV.jpg" width="640" alt="StarCraft II: plan globally and control squads with Jev preview">](https://x.com/GZhan57/status/2102126922688012410)<br>[Video](https://x.com/GZhan57/status/2102126922688012410)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2102121853624184832/vid/avc1/2500x1080/d49JmBwkLEPXGVEB.mp4?tag=29) (metadata duration: 17.5s)

Media source: [original publishing page](https://x.com/GZhan57/status/2102126922688012410). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use a planning model for tactics and multiple Jev loops for unit decisions.

**Useful aspect (analysis):** Separates long-term planning from short-term control for hybrid-architecture comparisons.

## Inputs, steps and outputs

The author says Astra plans once before combat and each squad/key unit gets Jev decisions about twice per second. State encoding and candidate actions are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A combat video and stated decision frequency, not a standard gaming benchmark. | Author report | [Post and attached media](https://x.com/GZhan57/status/2102126922688012410) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102126922688012410) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Maps, opponents, repeated win rates and full costs are missing. The quoted Warcraft experiment has another author and is not this project’s result.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
