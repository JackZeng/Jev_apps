# Script.it: flag issues before writing review comments

[简体中文](README.md) | **English**

> Score a git diff first, then ask a language model for explanations only when issues are flagged.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author discloses the workflow change and 75% recall trade-off. Private-data zero false positives and speed/cost ratios remain unverified, but are not presented as an equal-recall universal guarantee.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#script-code-review)

## How it works, in plain English

Like marking suspicious changes with a checklist before asking a reviewer to explain them. This can avoid lengthy exploration but may miss deeper issues.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@liorshkiller](https://x.com/liorshkiller) |
| Main post | [Source post](https://x.com/liorshkiller/status/2100936106615140757) |
| Published (UTC) | 2026-09-18T13:12:55+00:00 |
| Main-post likes snapshot | **202** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T22:50:12+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100936106615140757); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSgGI1wWQAAY5zl.jpg?name=orig" width="640" alt="Script.it: flag issues before writing review comments preview">](https://x.com/liorshkiller/status/2100936106615140757)<br>[Image](https://x.com/liorshkiller/status/2100936106615140757)

The source includes an image and workflow description. Results remain an internal author evaluation, not independent certification.

- [Original image 1](https://pbs.twimg.com/media/HSgGI1wWQAAY5zl.jpg?name=orig)

Media source: [original publishing page](https://x.com/liorshkiller/status/2100936106615140757). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Score a git diff first, then ask a language model for explanations only when issues are flagged.

**Useful aspect (analysis):** Explicitly separates detection from explanation compared with agent-led review, and discloses the recall tradeoff.

## Inputs, steps and outputs

The author replaces a multi-turn GLM/Grok/Gemini ensemble with direct Jev scoring of raw diffs, invoking an LLM for explanations after a flag.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports roughly 50× speed, 100× cost improvement and 75% confirmed-bug recall; the previous ensemble detected more bugs. | Author report | [Post and attached media](https://x.com/liorshkiller/status/2100936106615140757) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100936106615140757) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The private set’s size and labels are unavailable. Zero false positives refers to tested developer-disputed findings, not a guarantee of no production errors.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
