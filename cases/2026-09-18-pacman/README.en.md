# Astra + Jev Pac-Man

[简体中文](README.md) | **English**

> One model plans while Jev chooses quick local moves to play Pac-Man.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author discloses a planning/action split. Local decision latency does not establish end-to-end cost, speed or win rate.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#pacman) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Think of a coach and player: Astra supplies the strategy, and Jev handles local choices. Assess the combined system, not just Jev's speed.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@daniel_mac8](https://x.com/daniel_mac8) |
| Main post | [Source post](https://x.com/daniel_mac8/status/2100335929273524541) |
| Published (UTC) | 2026-09-16T21:28:02+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **860** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:27.561323+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100335929273524541); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100335842451492864/img/gC9HxZoXRIgMLKrW.jpg" width="640" alt="Astra + Jev Pac-Man preview">](https://x.com/daniel_mac8/status/2100335929273524541)<br>[Video](https://x.com/daniel_mac8/status/2100335929273524541)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100335842451492864/vid/avc1/1920x1240/tv-voEIcPAD8LoM8.mp4?tag=29) (metadata duration: 28.0s)

Media source: [original publishing page](https://x.com/daniel_mac8/status/2100335929273524541). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

One model plans while Jev chooses quick local moves to play Pac-Man.

**Useful aspect (analysis):** A clear planning/execution split that may apply to longer tasks.

## Inputs, steps and outputs

Astra planning → Jev follows the strategy through local decisions → game feedback.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares hierarchical-control footage, without standardized win rates. | Author report | [Post and attached media](https://x.com/daniel_mac8/status/2100335929273524541) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100335929273524541) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Both models affect outcomes; Jev latency alone does not represent total cost or quality.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
