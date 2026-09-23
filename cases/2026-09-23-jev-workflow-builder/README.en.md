# Jev Workflow Builder: connect decisions into a workflow

[简体中文](README.md) | **English**

> Connect classification, scoring, yes/no checks and text-generation nodes on a canvas.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A concerns inspectable execution and model roles, not proven workflow effectiveness or production readiness.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#jev-workflow-builder)

## How it works, in plain English

Draw a flowchart where later nodes receive earlier decisions and continue the work.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@ctnicholasdev](https://x.com/ctnicholasdev) |
| Main post | [Source post](https://x.com/ctnicholasdev/status/2102070640589279318) |
| Published (UTC) | 2026-09-21T16:21:09+00:00 |
| Main-post likes snapshot | **638** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:31:24+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102070640589279318); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102070615926771715/img/PueMU1HUq0WB86ZG.jpg" width="640" alt="Jev Workflow Builder: connect decisions into a workflow preview">](https://x.com/ctnicholasdev/status/2102070640589279318)<br>[Video](https://x.com/ctnicholasdev/status/2102070640589279318)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2102070615926771715/vid/avc1/1060x720/s3eKlPvK1XUESV-r.mp4?tag=14) (metadata duration: 41.8s)

Media source: [original publishing page](https://x.com/ctnicholasdev/status/2102070640589279318). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Connect classification, scoring, yes/no checks and text-generation nodes on a canvas.

**Useful aspect (analysis):** Run previews and REST access make multi-step support-routing experiments easier to inspect.

## Inputs, steps and outputs

Liveblocks supports collaborative editing. Server code converts node settings into Jev primitives and passes upstream answers; separate LLM nodes generate text.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The original demos a support workflow; pinned source separates real API calls from mock mode. | Author report | [Post and attached media](https://x.com/ctnicholasdev/status/2102070640589279318) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102070640589279318) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/README.md)
- [Project / demo link 2](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/app/workflow/server/typesafe.ts)
- [Project / demo link 3](https://github.com/CTNicholas/jev-workflow-builder/blob/9a652d22216028a64ccaa7468754e45e1860618b/app/workflow/server/executor.ts)

## Mechanism and comparison

Without a key, code explicitly returns keyword-based mock results, not Jev inference. Production concurrency and reliability are untested.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
