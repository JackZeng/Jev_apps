# Tax Doc Classifier: label tax PDF pages

[简体中文](README.md) | **English**

> Identify which tax form each PDF page belongs to for downstream organization.

**Added to README:** 2026-09-19 07:04:48<br>**Content updated:** 2026-09-19 07:08:57 (Beijing time, UTC+08:00)

## How it works, in plain English

Like reading the header, body and footer before attaching a form label, while reporting uncertainty instead of pretending every page is recognized.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@nedwize](https://x.com/nedwize) |
| Main post | [Source post](https://x.com/nedwize/status/2100973868324417852) |
| Published (UTC) | 2026-09-18T15:42:59+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-19 07:04:48 / 2026-09-19 07:08:57 |
| Main-post likes snapshot | **1,506** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T22:49:18+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100973868324417852); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100973360989773825/img/yMtL6CxrKMVXQEHV.jpg" width="640" alt="Tax Doc Classifier: label tax PDF pages preview">](https://x.com/nedwize/status/2100973868324417852)<br>[Video](https://x.com/nedwize/status/2100973868324417852)

The source has a video; pinned README figures define the evaluation scope. Page classification is not tax filing.

- [Direct video 1](https://video.twimg.com/amplify_video/2100973360989773825/vid/avc1/2360x1864/9o-fXACEXud024Pi.mp4?tag=29) (metadata duration: 12.6s)

Media source: [original publishing page](https://x.com/nedwize/status/2100973868324417852). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Identify which tax form each PDF page belongs to for downstream organization.

**Useful aspect (analysis):** More explicit than general file sorting: documented coverage of 261 forms, test counts and rejection conditions.

## Inputs, steps and outputs

Pinned documentation extracts text with pdftotext, then classifies form and page types. Corporate forms have a follow-up question; the default confidence gate is 0.95 and blank text skips the model.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| Documentation reports no errors across 314 filled pages spanning 15 forms. A separate 753-page, 261-form blank set had no misclassifications but 38 low-confidence strict-mode failures. | Author report | [Results documentation](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/README.md) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100973868324417852) | Snapshot at the recorded time, not a live count |

**Documentation review:** Read the [pinned documentation](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/README.md). Implementation descriptions above come from documentation, not installation, execution or independent reproduction.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/kyotofin/tax-doc-classifier)
- [Project / demo link 2](https://github.com/kyotofin/tax-doc-classifier/blob/6afcf701395466d7c936ec8178daf017b9d96b0c/README.md)

## Mechanism and comparison

Scans require separate OCR; pages without text can appear blank. Evaluation mainly covers English federal forms, and low-confidence failures must not disappear behind a “100%” headline.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
