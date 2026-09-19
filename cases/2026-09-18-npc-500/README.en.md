# 500 agents in a 3D environment

[简体中文](README.md) | **English**

> Run decisions for many virtual characters in one 3D world.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟠 C · Claims exceed evidence**<br>500 entities, 500ms request latency and 35 total calls/s do not establish every entity’s decision rate or remove latency as a bottleneck. Under one call per agent, a full sweep would take about 14.3s; batching is unspecified, so that calculation is conditional.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#npc-500) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Send characters' questions to Jev and execute their choices in the simulation. An overall rate of 35 requests/second does not mean each of 500 characters updates 35 times/second.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@crislenta](https://x.com/crislenta) |
| Main post | [Source post](https://x.com/crislenta/status/2100457614073327754) |
| Published (UTC) | 2026-09-17T05:31:34+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **572** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:28.758741+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100457614073327754); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100457262372560897/img/zSIVGvaQhEZLMd9-.jpg" width="640" alt="500 agents in a 3D environment preview">](https://x.com/crislenta/status/2100457614073327754)<br>[Video](https://x.com/crislenta/status/2100457614073327754)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100457262372560897/vid/avc1/2096x1080/9GTTLqvWoY0P0gzy.mp4?tag=29) (metadata duration: 23.6s)

Media source: [original publishing page](https://x.com/crislenta/status/2100457614073327754). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Run decisions for many virtual characters in one 3D world.

**Useful aspect (analysis):** Focuses on population scale and throughput under simulation load.

## Inputs, steps and outputs

Agents request Jev decisions and the simulator executes them; scheduling and batching details are unknown.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports 500 agents, 500ms average latency and 35 API calls/second for an initial implementation. | Author report | [Post and attached media](https://x.com/crislenta/status/2100457614073327754) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100457614073327754) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

35 calls/second is not 35 updates per second for every agent; per-agent update frequency is absent.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
