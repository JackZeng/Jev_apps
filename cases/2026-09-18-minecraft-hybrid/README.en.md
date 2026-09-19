# Minecraft with Jev, Astra and local policies

[简体中文](README.md) | **English**

> Split Minecraft play across models: long-term planning, quick reactions, and local movement and aiming.

**Added to README:** 2026-09-18 10:50:59<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author discloses planning, judgment and local movement policies plus an original-speed clip. The sped-up main clip cannot measure reaction time, and combined combat performance cannot be attributed to Jev alone.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#minecraft-hybrid) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Like a captain, field coordinator and players sharing work: Astra plans, Jev reacts to immediate events, and local policies turn decisions into movement and aiming. The footage reflects the entire system.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@wuyang_zhou](https://x.com/wuyang_zhou) |
| Main post | [Source post](https://x.com/wuyang_zhou/status/2100727660875808913) |
| Published (UTC) | 2026-09-17T23:24:38+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 10:50:59 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **354** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T02:36:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100727660875808913); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100727359569530880/img/IGuQpzilRkIsw1Wb.jpg" width="640" alt="Minecraft with Jev, Astra and local policies preview">](https://x.com/wuyang_zhou/status/2100727660875808913)<br>[Video](https://x.com/wuyang_zhou/status/2100727660875808913)

The main video is about 192 seconds; the author-labeled original-speed version is about 384 seconds. Use the latter when judging responsiveness rather than inferring speed from the main clip.

- [Direct video 1](https://video.twimg.com/amplify_video/2100727359569530880/vid/avc1/1276x648/GRtnLHSbO6-kzVjo.mp4?tag=29) (metadata duration: 192.0s)

Media source: [original publishing page](https://x.com/wuyang_zhou/status/2100727660875808913). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Split Minecraft play across models: long-term planning, quick reactions, and local movement and aiming.

**Useful aspect (analysis):** Makes the planning, reactive-decision and low-level-control split explicit; useful to compare with the layered Pac-Man implementation.

## Inputs, steps and outputs

The author explains that GPT-6 Astra handles longer-term goals, Jev reacts to events such as zombie attacks, and local policy models handle movement and aiming. Observation encoding, model frequencies and execution libraries are undisclosed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author demonstrates encounters with multiple zombies, explains the three layers in a reply and posts an original-speed version of the same footage. | Author report | [Post and attached media](https://x.com/wuyang_zhou/status/2100727660875808913) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100727660875808913) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @wuyang_zhou](https://x.com/wuyang_zhou/status/2100727859400622158): published 2026-09-17T23:25:25+00:00; 34 likes retrieved 2026-09-18T02:41:19+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100727859400622158).
- [Supporting post by @wuyang_zhou](https://x.com/wuyang_zhou/status/2100741909790490764): published 2026-09-18T00:21:15+00:00; 7 likes retrieved 2026-09-18T02:41:19+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100741909790490764). [Supplementary media 1](https://video.twimg.com/amplify_video/2100741480226721792/vid/avc1/1276x648/Je0yf35SKPhCagLO.mp4?tag=29)

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Combat performance cannot be attributed to Jev alone. No Jev-only, Astra-only or combined-system comparison is available. The main video is approximately 2× speed; an original-speed version is supplied separately. No completion or speedrun result is established.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
