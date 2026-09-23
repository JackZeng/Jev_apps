# AgentRun: turn repeated work into reusable procedures

[简体中文](README.md) | **English**

> Learn from agent traces and move routine steps into code and Jev decisions.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Original methods support the workflow description. Performance, correctness and transfer to other tasks remain B, not independently reproduced.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#agentrun)

## How it works, in plain English

An experienced worker performs a task several times, writes a procedure and keeps experts for exceptions.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@_aj](https://x.com/_aj) |
| Main post | [Source post](https://x.com/_aj/status/2102061534956662818) |
| Published (UTC) | 2026-09-21T15:44:59+00:00 |
| Main-post likes snapshot | **2,142** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:31:25+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102061534956662818); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSwFAsyawAA4tst.jpg?name=orig" width="640" alt="AgentRun: turn repeated work into reusable procedures preview">](https://x.com/_aj/status/2102061534956662818)<br>[Image](https://x.com/_aj/status/2102061534956662818)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Original image 1](https://pbs.twimg.com/media/HSwFAsyawAA4tst.jpg?name=orig)

Media source: [original publishing page](https://x.com/_aj/status/2102061534956662818). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Learn from agent traces and move routine steps into code and Jev decisions.

**Useful aspect (analysis):** Separates research, decisions and execution so avoided work can be inspected.

## Inputs, steps and outputs

The author describes a Pi-based harness: agents research, Jev handles Route/Classify/Sift/Pick and evidence checks, code applies deterministic rules, and uncertain cases escalate.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports $2.89 to $0.25 per alert on 100 comparisons, a 1,000-alert adaptive run and costs over 100,000 alerts; these remain author-reported. | Author report | [Results documentation](https://x.com/i/article/2100840456200581120) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102061534956662818) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @MiguelriosEN](https://x.com/MiguelriosEN/status/2101029313906987422): published 2026-09-18T19:23:18+00:00; 394 likes retrieved 2026-09-23T04:32:45+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101029313906987422).
- [Supporting post by @MiguelriosEN](https://x.com/MiguelriosEN/status/2101033282414768456): published 2026-09-18T19:39:04+00:00; 312 likes retrieved 2026-09-23T04:32:32+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101033282414768456). [Supplementary media 1](https://video.twimg.com/amplify_video/2101032781270917120/vid/avc1/3840x2160/WQ2m025g9MHrPnYB.mp4?tag=29)

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://x.com/i/article/2100840456200581120)

## Mechanism and comparison

Comparisons concern the author’s compliance-alert workload, without complete public cases or independent audit. Skipping research can miss evidence; cost alone is insufficient.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
