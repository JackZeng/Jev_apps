# Sprite Fusion: generate runner terrain in real time

[简体中文](README.md) | **English**

> Select new platforms and gaps ahead of a moving player.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>The implementation article specifies state, finite terrain choices and code placement, with five measured requests at 319–375ms. This supports bounded terrain assembly, not asset generation, unrestricted game creation or long-term playability.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#game-level-generation)

## How it works, in plain English

Like giving a level designer a box of fixed-size tiles: Jev chooses width, gap, height and surface type, and game code places them.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@HugoDuprez](https://x.com/HugoDuprez) |
| Main post | [Source post](https://x.com/HugoDuprez/status/2100953089003921543) |
| Published (UTC) | 2026-09-18T14:20:24+00:00 |
| Main-post likes snapshot | **1,289** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T22:50:12+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100953089003921543); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100952449661992960/img/GEVdw9BvAW7Dv2Gx.jpg" width="640" alt="Sprite Fusion: generate runner terrain in real time preview">](https://x.com/HugoDuprez/status/2100953089003921543)<br>[Video](https://x.com/HugoDuprez/status/2100953089003921543)

The main video, implementation article and author’s state clarification form one case.

- [Direct video 1](https://video.twimg.com/amplify_video/2100952449661992960/vid/avc1/960x640/PpGr_QrlTEiPpCeb.mp4?tag=29) (metadata duration: 10.2s)

Media source: [original publishing page](https://x.com/HugoDuprez/status/2100953089003921543). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Select new platforms and gaps ahead of a moving player.

**Useful aspect (analysis):** Unlike Mario or Flappy Bird action selection, this creates the environment. Bounded tile choices support collision and reachability checks.

## Inputs, steps and outputs

The author’s article supplies player position, velocity, dash state and terrain, then asks parallel choice questions for the next four surfaces. PhaserJS builds terrain; Sprite Fusion separately provides graphical assets.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author records five requests at 319–375 ms Jev latency and an estimated $0.00057 each, not a measured sub-100 ms system. | Author report | [Results documentation](https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100953089003921543) | Snapshot at the recorded time, not a live count |

**Author article:** The [implementation write-up](https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev) documents allowed surface types, widths, gaps, heights and a recorded response. This is public-design analysis; the game was not run.

Updates and deduplicated supporting sources:

- [Supporting post by @HugoDuprez](https://x.com/HugoDuprez/status/2100960962392018992): published 2026-09-18T14:51:42+00:00; 47 likes retrieved 2026-09-18T22:56:39+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100960962392018992).
- [Supporting post by @HugoDuprez](https://x.com/HugoDuprez/status/2101011373136200058): published 2026-09-18T18:12:00+00:00; 2 likes retrieved 2026-09-18T22:56:40+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101011373136200058).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://www.spritefusion.com/blog/generating-game-level-in-real-time-with-jev)

## Mechanism and comparison

A simple runner prototype without long-horizon playability or adaptive-difficulty evaluation. Asset generation and terrain decisions are separate stages.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
