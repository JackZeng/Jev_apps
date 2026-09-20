# Agent goal verifier: check completion after each turn

[简体中文](README.md) | **English**

> Check whether an agent has actually achieved its goal after every turn.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Supports an early verifier prototype, not universal verification suitability or proven long-horizon gains.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#agent-goal-verifier)

## How it works, in plain English

Like a checker beside a task list: the agent acts and Jev judges whether requirements remain unmet.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@omarsar0](https://x.com/omarsar0) |
| Main post | [Source post](https://x.com/omarsar0/status/2101443311454036477) |
| Published (UTC) | 2026-09-19T22:48:23+00:00 |
| Main-post likes snapshot | **317** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:45:24+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101443311454036477); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101443076828925952/img/zVy7_B-F8UmXFdKK.jpg" width="640" alt="Agent goal verifier: check completion after each turn preview">](https://x.com/omarsar0/status/2101443311454036477)<br>[Video](https://x.com/omarsar0/status/2101443311454036477)

The main post has a roughly 17-second video. A promised guide is not treated as already delivered.

- [Direct video 1](https://video.twimg.com/amplify_video/2101443076828925952/vid/avc1/3700x2160/cRyok3dsTXg65u7u.mp4?tag=29) (metadata duration: 17.5s)

Media source: [original publishing page](https://x.com/omarsar0/status/2101443311454036477). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Check whether an agent has actually achieved its goal after every turn.

**Useful aspect (analysis):** Narrower and more frequent than whole-PR review, making it useful for exploring inexpensive continuous checks.

## Inputs, steps and outputs

A custom verifier is integrated into the harness’s /goal feature. Full inputs, criteria and failure handling are not yet public.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author says Jev replaces a more expensive reasoning model and permits more frequent checks, without a complete quality/cost comparison. | Author report | [Post and attached media](https://x.com/omarsar0/status/2101443311454036477) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101443311454036477) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The author explicitly calls this early experimentation with benchmarking still to come. A completion judgment is not a passed test; false-stop and missed-error rates are unknown.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
