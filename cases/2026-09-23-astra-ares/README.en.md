# Astra-Ares: adjust reasoning effort as work progresses

[简体中文](README.md) | **English**

> Give Codex more reasoning effort for difficult steps and less for routine ones.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A covers the inspectable controller. Savings and faster runs remain author measurements; preserving prompt structure does not establish cache hit rates.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#astra-ares)

## How it works, in plain English

Like changing gears for the same problem solver: Jev reads the task and recent tool feedback to select the next effort level.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@miu21590](https://x.com/miu21590) |
| Main post | [Source post](https://x.com/miu21590/status/2101857866378362926) |
| Published (UTC) | 2026-09-21T02:15:40+00:00 |
| Main-post likes snapshot | **3,466** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T03:53:20+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101857866378362926); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101857791967178752/img/MiCcd9s5hrptUHqe.jpg" width="640" alt="Astra-Ares: adjust reasoning effort as work progresses preview">](https://x.com/miu21590/status/2101857866378362926)<br>[Video](https://x.com/miu21590/status/2101857866378362926)

The 23-second original and source-release reply are one case; pinned code was read, not installed.

- [Direct video 1](https://video.twimg.com/amplify_video/2101857791967178752/vid/avc1/2560x1440/CTWUFtPEHb3pYnBj.mp4?tag=29) (metadata duration: 23.1s)

Media source: [original publishing page](https://x.com/miu21590/status/2101857866378362926). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Give Codex more reasoning effort for difficult steps and less for routine ones.

**Useful aspect (analysis):** Finer control than choosing a model once per task, with inspectable switching conditions and context boundaries.

## Inputs, steps and outputs

A patched Codex CLI asks Jev through a local bridge before the next model generation. It selects effort and a 1/2/5/10-step lease, rechecking after new input or tool failures while keeping model identity fixed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The post reports 50% lower Astra cost. Repository validation covers native settings application and prefix preservation, not a controlled savings benchmark. | Author report | [Post and attached media](https://x.com/miu21590/status/2101857866378362926) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101857866378362926) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @miu21590](https://x.com/miu21590/status/2102404547587318081): published 2026-09-22T14:27:59+00:00; 283 likes retrieved 2026-09-23T03:52:52+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2102404547587318081).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/miuuyy/Astra-Ares/blob/a1dbc976103e300419cb0b4ab54150ad6a3e0b4b/README.md)
- [Project / demo link 2](https://github.com/miuuyy/Astra-Ares/blob/a1dbc976103e300419cb0b4ab54150ad6a3e0b4b/src/bridge.mjs)
- [Project / demo link 3](https://github.com/miuuyy/Astra-Ares/blob/a1dbc976103e300419cb0b4ab54150ad6a3e0b4b/docs/validation.md)

## Mechanism and comparison

An early preview requiring a patched CLI, not intervention inside one generation. Validation explicitly excludes workload savings and cache hit rates; halving cost is not guaranteed.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
