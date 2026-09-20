# Third Hand: control a Mac using text from your request

[简体中文](README.md) | **English**

> Read app controls, click them and enter text already supplied in the request.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Pinned source explains text entry without an extra LLM as selection/extraction, not general generation. Speed and cost remain independently unverified.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#third-hand)

## How it works, in plain English

Like using a button list and a note: Jev chooses a target and picks words from the note; it cannot freely write a new article.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@sxhivs](https://x.com/sxhivs) |
| Main post | [Source post](https://x.com/sxhivs/status/2101367048223982065) |
| Published (UTC) | 2026-09-19T17:45:20+00:00 |
| Main-post likes snapshot | **549** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-20T02:46:29+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101367048223982065); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101364408870109184/img/w93wxuq73naZx36A.jpg" width="640" alt="Third Hand: control a Mac using text from your request preview">](https://x.com/sxhivs/status/2101367048223982065)<br>[Video](https://x.com/sxhivs/status/2101367048223982065)

A separate Swift repository and author, not another Ultrafast demo; release reply and source form one case.

- [Direct video 1](https://video.twimg.com/amplify_video/2101364408870109184/vid/avc1/3024x1964/ywaIWwbhUYD5NIOm.mp4?tag=29) (metadata duration: 31.1s)

Media source: [original publishing page](https://x.com/sxhivs/status/2101367048223982065). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Read app controls, click them and enter text already supplied in the request.

**Useful aspect (analysis):** More constrained than Ultrafast’s small-LLM text entry but requires no extra generator; unlike click-only TipTour, it can enter explicitly supplied text.

## Inputs, steps and outputs

Pinned code reads accessibility controls with local Apple Vision OCR when needed. Jev selects actions and candidate text extracted from the request, then the app checks state. Tasks, labels and values go to TypeSafe even though pixels stay local.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shows a 31-second demo and claims subsecond latency. Documentation calls it experimental and says completion still needs human judgment. | Author report | [Post and attached media](https://x.com/sxhivs/status/2101367048223982065) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101367048223982065) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @sxhivs](https://x.com/sxhivs/status/2101367050207981608): published 2026-09-19T17:45:20+00:00; 50 likes retrieved 2026-09-20T02:53:28+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101367050207981608).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/README.md)
- [Project / demo link 2](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/TextEntryPlan.swift)
- [Project / demo link 3](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/JevClient.swift)

## Mechanism and comparison

No free-form writing or arbitrary command generation. Icons, complex editors and gestures can fail; subsecond and near-free claims lack full-task benchmarks.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
