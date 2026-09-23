# Halite: compare strategic planning and ship-level execution

[简体中文](README.md) | **English**

> Compare a pure language-model agent with planning plus Jev execution in strategy games.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Related experiments by one author are grouped; timings and matches do not establish universal model superiority.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#halite-hybrid)

## How it works, in plain English

A fleet sets a strategy, then individual ships choose moves; different models can handle each layer.

[Back to catalog](../../README.en.md#games) · [Compare similar examples](../../breakdowns/2026-09-18-games.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Game decisions and solving |
| Platform / author | X / [@Sentdex](https://x.com/Sentdex) |
| Main post | [Source post](https://x.com/Sentdex/status/2101828851458293827) |
| Published (UTC) | 2026-09-21T00:20:22+00:00 |
| Main-post likes snapshot | **386** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:45+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101828851458293827); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101827235925590016/img/Z9-x2VHoe3B_rhqT.jpg" width="640" alt="Halite: compare strategic planning and ship-level execution preview">](https://x.com/Sentdex/status/2101828851458293827)<br>[Video](https://x.com/Sentdex/status/2101828851458293827)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2101827235925590016/vid/avc1/1440x1440/NDniQmrNfk0jMECF.mp4?tag=29) (metadata duration: 24.2s)

Media source: [original publishing page](https://x.com/Sentdex/status/2101828851458293827). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Compare a pure language-model agent with planning plus Jev execution in strategy games.

**Useful aspect (analysis):** Includes pure and hybrid comparisons, preserving follow-up results unfavorable to Jev.

## Inputs, steps and outputs

In Halite 2, GLM 5.3 Flash plans planets, expansion, combat and replanning; Jev executes ship actions. A later Halite 1 test compares Jev and OpenJev execution.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports 13-fold speed and 56% of pure-GLM cost; OpenJev performs better in a later small Halite 1 test. | Author report | [Post and attached media](https://x.com/Sentdex/status/2101828851458293827) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101828851458293827) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @Sentdex](https://x.com/Sentdex/status/2102192643480678651): published 2026-09-22T00:25:57+00:00; 340 likes retrieved 2026-09-23T04:31:26+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2102192643480678651). [Supplementary media 1](https://video.twimg.com/amplify_video/2102191703671111680/vid/avc1/1620x1620/agzJvBXrFgMtELYJ.mp4?tag=29)

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Different games/settings cannot be pooled into a ranking. Full schedules, seeds, logs and reproducible protocols are unavailable.

See the [category analysis](../../breakdowns/2026-09-18-games.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
