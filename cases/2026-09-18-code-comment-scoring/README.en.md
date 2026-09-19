# Code comments: accuracy and usefulness scores

[简体中文](README.md) | **English**

> Check whether a comment is correct and whether it adds useful information beyond the code.

**Added to README:** 2026-09-18 16:17:27<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>Two simple examples illustrate separate accuracy and usefulness scores, and the author positions it as a gate. These scores are not evaluation accuracy or validation on complex code.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#code-comment-scoring) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Give each comment two report cards: it may correctly restate the code without explaining why it exists, or even misdescribe what the code does. Jev scores the dimensions separately to highlight comments worth reviewing.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@markjaquith](https://x.com/markjaquith) |
| Main post | [Source post](https://x.com/markjaquith/status/2100359340087501296) |
| Published (UTC) | 2026-09-16T23:01:04+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 16:17:27 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **1,777** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T08:11:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100359340087501296); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSX4qrBWcAAA3K4.jpg?name=orig" width="640" alt="Code comments: accuracy and usefulness scores preview">](https://x.com/markjaquith/status/2100359340087501296)<br>[Image](https://x.com/markjaquith/status/2100359340087501296)

The source image is the author’s terminal experiment output. Two author replies clarify the scores and proposed screening role.

- [Original image 1](https://pbs.twimg.com/media/HSX4qrBWcAAA3K4.jpg?name=orig)

Media source: [original publishing page](https://x.com/markjaquith/status/2100359340087501296). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Check whether a comment is correct and whether it adds useful information beyond the code.

**Useful aspect (analysis):** Separating factual correctness from informational value makes issues easier to interpret than a single overall code score. Like the ESLint experiment, it examines local code, but evaluates comment quality rather than rule compliance.

## Inputs, steps and outputs

The source terminal screenshot shows two small code/comment examples with 0–100 Accuracy and Usefulness scores and descriptions. The observable flow takes code plus comments into judgments and displays scores; prompts, parsing and score mapping are not established by the available evidence.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The screenshot gives a correct but redundant multiplication comment 99/100 for accuracy and 2/100 for usefulness. A comment describing division as multiplication receives 1/100 and 11/100. The author confirms both lack informational value and the second is also wrong. | Author report | [Post and attached media](https://x.com/markjaquith/status/2100359340087501296) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100359340087501296) | Snapshot at the recorded time, not a live count |

**Promoted after fourth-pass evidence review:** Previously pending because the label meanings were unclear. Image inspection and author replies establish two scoring dimensions and just two examples. Included as a concrete task experiment, not described as a shipped linter or mature product; no verifiable source-code entry point was obtained in this review.

Updates and deduplicated supporting sources:

- [Supporting post by @markjaquith](https://x.com/markjaquith/status/2100567922552742323): published 2026-09-17T12:49:54+00:00; 1 likes retrieved 2026-09-18T08:15:58+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100567922552742323).
- [Supporting post by @markjaquith](https://x.com/markjaquith/status/2100617693778923533): published 2026-09-17T16:07:40+00:00; 3 likes retrieved 2026-09-18T08:15:58+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100617693778923533).

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Two trivial examples do not establish performance on complex code. Scores are not independently measured test accuracy, and automatic comment deletion or rewriting is not demonstrated. The author describes a possible gate for reducing larger-model review, not a complete reviewer.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
