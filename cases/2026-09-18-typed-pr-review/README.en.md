# 14-check PR risk review

[简体中文](README.md) | **English**

> Screen code changes for risks such as exposed secrets or removed tests, and escalate uncertainty.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The six-PR typed-check demo and escalation rule are concrete. The price comparison does not establish equivalent coverage to a full Claude review; no general accuracy claim is justified.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#typed-pr-review)

## How it works, in plain English

Split review into 14 specific questions and ask Jev in one call. Code combines the answers; uncertain critical findings go to a person or larger model.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@redp314](https://x.com/redp314) |
| Main post | [Source post](https://x.com/redp314/status/2100585126652481915) |
| Published (UTC) | 2026-09-17T13:58:15+00:00 |
| Main-post likes snapshot | **1,927** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:24.549579+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100585126652481915); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100585029533372416/img/ZcrsntW2yWgtB_HD.jpg" width="640" alt="14-check PR risk review preview">](https://x.com/redp314/status/2100585126652481915)<br>[Video](https://x.com/redp314/status/2100585126652481915)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100585029533372416/vid/avc1/1920x1080/DH6WHlp4Tg6UUi3j.mp4?tag=29) (metadata duration: 32.4s)

Media source: [original publishing page](https://x.com/redp314/status/2100585126652481915). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Screen code changes for risks such as exposed secrets or removed tests, and escalate uncertainty.

**Useful aspect (analysis):** Explicit checks and escalation rules are easier to inspect than a single overall code-quality score.

## Inputs, steps and outputs

Diff → one Jev call returns 14 probabilities → code produces a verdict; critical checks between 0.35 and 0.65 go to a human or larger model.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports about 0.5 seconds and $0.00007 per PR. This repository has not reproduced the cost comparison. | Author report | [Post and attached media](https://x.com/redp314/status/2100585126652481915) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100585126652481915) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Only six PRs are shown; semantic risk classification does not establish comprehensive vulnerability detection.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
