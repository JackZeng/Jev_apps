# Jev City: nine-intersection traffic simulation

[简体中文](README.md) | **English**

> Choose signal directions in a virtual road network and observe queues and waiting time.

**Content updated:** 2026-09-19 17:48:49 (Beijing time, UTC+08:00)

**🟠 C · Claims exceed evidence**<br>The over-600% claim lacks matched controller baselines and repeated statistics. The simulation interface does not establish real-world traffic gains.<br>[Assessment and sources](../../references/2026-09-19-increment7-audit.en.md#traffic-light-city)

## How it works, in plain English

Like a dispatcher in a model city: code supplies junction state, Jev chooses a direction, and the simulator moves vehicles.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@leojrr](https://x.com/leojrr) |
| Main post | [Source post](https://x.com/leojrr/status/2101161666410893328) |
| Published (UTC) | 2026-09-19T04:09:13+00:00 |
| Main-post likes snapshot | **1,081** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-19T09:41:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101161666410893328); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101161072447180800/img/sRIOALT11TUpdAdU.jpg" width="640" alt="Jev City: nine-intersection traffic simulation preview">](https://x.com/leojrr/status/2101161666410893328)<br>[Video](https://x.com/leojrr/status/2101161666410893328)

The original simulation video and author’s entry-point reply form one case, distinct from this author’s X algorithm simulation.

- [Direct video 1](https://video.twimg.com/amplify_video/2101161072447180800/vid/avc1/2154x1864/la5a3xiJ95P9d7RI.mp4?tag=29) (metadata duration: 73.2s)

Media source: [original publishing page](https://x.com/leojrr/status/2101161666410893328). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Choose signal directions in a virtual road network and observe queues and waiting time.

**Useful aspect (analysis):** Unlike controlling one simulated car, this coordinates junctions to explore network-level congestion effects.

## Inputs, steps and outputs

The display shows nine junctions, north/south versus east/west decisions and confidence, an on/off control and wait curves. Full state encoding and the off-mode baseline were not established.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author claims average waiting rises by over 600% when Jev is switched off; a 73-second clip and public entry point do not verify that ratio. | Author report | [Post and attached media](https://x.com/leojrr/status/2101161666410893328) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101161666410893328) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @leojrr](https://x.com/leojrr/status/2101165998086783170): published 2026-09-19T04:26:26+00:00; 5 likes retrieved 2026-09-19T09:44:59+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101165998086783170).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://01a0b7a9-5619-7ec6-a0d8-fb357ed42aa3.skydive.app/)

## Mechanism and comparison

Matched traffic demand, seeds, repeated trials and fixed/adaptive rule baselines are missing. A virtual network does not establish real-city outcomes.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
