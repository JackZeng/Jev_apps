# jev-align: refine decision criteria with human feedback

[简体中文](README.md) | **English**

> Label boundary cases and iteratively improve Jev’s decision instructions.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Code exposes labeling, GEPA’s optimization target and human acceptance. A denotes clear implementation evidence, not proven generalization gains.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#jev-align)

## How it works, in plain English

Like revising a marking guide with an assistant: you supply answers, another model proposes wording, Jev evaluates it, and you accept or reject the change.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@sethkimmel3](https://x.com/sethkimmel3) |
| Main post | [Source post](https://x.com/sethkimmel3/status/2101357768640987302) |
| Published (UTC) | 2026-09-19T17:08:28+00:00 |
| Main-post likes snapshot | **511** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:47:09+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101357768640987302); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101357265253212160/img/yMWnsAPk5D4HinBv.jpg" width="640" alt="jev-align: refine decision criteria with human feedback preview">](https://x.com/sethkimmel3/status/2101357768640987302)<br>[Video](https://x.com/sethkimmel3/status/2101357768640987302)

Launch posts and quotes refer to one tool. Pinned sources preserve the inspected version.

- [Direct video 1](https://video.twimg.com/amplify_video/2101357265253212160/vid/avc1/3400x2160/w35QhvgnRKRBocQo.mp4?tag=29) (metadata duration: 129.0s)

Media source: [original publishing page](https://x.com/sethkimmel3/status/2101357768640987302). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Label boundary cases and iteratively improve Jev’s decision instructions.

**Useful aspect (analysis):** Adds feedback, diff inspection and rollback to manual prompting, supporting binary, multiclass, multilabel and ordered-score tasks.

## Inputs, steps and outputs

The pinned CLI samples uncertain examples and random audit rows. GEPA optimizes task specifications against human labels using a separate reflection model; it does not fine-tune Jev weights.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| Source and a roughly two-minute demo support the workflow; this catalog has not reproduced it or established a universal gain. | Author report | [Post and attached media](https://x.com/sethkimmel3/status/2101357768640987302) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101357768640987302) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/README.md)
- [Project / demo link 2](https://github.com/sutro-sh/jev-align/blob/49753df924d30c0d3642b58e0b9b1e89921dc102/src/jev_align/optimizer.py)

## Mechanism and comparison

Training gains do not guarantee generalization. Held-out evaluation is optional; annotation, reflection and repeated evaluation costs must also be counted.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
