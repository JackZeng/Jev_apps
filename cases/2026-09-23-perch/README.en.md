# Perch: check code against natural-language rules

[简体中文](README.md) | **English**

> Check behavioral expectations and rank suspicious defects for human or agent review.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A covers inspectable scanning and rules. Confidence does not establish a real bug; diagnosis, reproduction and regression checks remain necessary.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#perch)

## How it works, in plain English

Read code with a checklist: map functions and calls, then ask whether each expectation is satisfied.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@joshuafbrown](https://x.com/joshuafbrown) |
| Main post | [Source post](https://x.com/joshuafbrown/status/2102085153015451695) |
| Published (UTC) | 2026-09-21T17:18:49+00:00 |
| Main-post likes snapshot | **229** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T03:58:14+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102085153015451695); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102085145339842560/img/sRjfu4DinUQLEad8.jpg" width="640" alt="Perch: check code against natural-language rules preview">](https://x.com/joshuafbrown/status/2102085153015451695)<br>[Video](https://x.com/joshuafbrown/status/2102085153015451695)

Independent author/repository, compared with existing ESLint experiments; no project was scanned.

- [Direct video 1](https://video.twimg.com/amplify_video/2102085145339842560/vid/avc1/1280x900/g-ITrnzpxvbYOeF_.mp4?tag=29) (metadata duration: 13.7s)

Media source: [original publishing page](https://x.com/joshuafbrown/status/2102085153015451695). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Check behavioral expectations and rank suspicious defects for human or agent review.

**Useful aspect (analysis):** Addresses behavioral requirements that ordinary syntax rules struggle to express, beyond comment scoring.

## Inputs, steps and outputs

tree-sitter builds a method/call graph. Jev uses Noul, Choice and Score for defect likelihood, location and severity; natural-language ensure rules join checks and changes can be rechecked.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A roughly 13-second behavior-driven development demo, with public scan code and documented scoring and coverage. | Author report | [Post and attached media](https://x.com/joshuafbrown/status/2102085153015451695) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102085153015451695) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/lakeday-org/perch/blob/69b519d903e5528ca32557fce61d0e2e7d90ced6/README.md)
- [Project / demo link 2](https://github.com/lakeday-org/perch/blob/69b519d903e5528ca32557fce61d0e2e7d90ced6/src/scan.js)
- [Project / demo link 3](https://github.com/lakeday-org/perch/blob/69b519d903e5528ca32557fce61d0e2e7d90ced6/docs/scan.md)

## Mechanism and comparison

Probability rankings are not defect proofs; independent detection benchmarks are absent. Neighbor context is bounded and long methods have an eight-pass cap; inspect partial-read and failure records.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
