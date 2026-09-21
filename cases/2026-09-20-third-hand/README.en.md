# Third Hand / arc-cua: choose actions on a Mac

[简体中文](README.md) | **English**

> Read controls and screen text, choose actions and enter request- or planner-supplied text.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A concerns inspectable implementation roles. arc-cua explicitly reuses Third Hand’s text-entry approach and is grouped as related work. Solved computer use and universal speed gains lack benchmarks.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#third-hand)

## How it works, in plain English

A planner supplies the task and a note, Jev chooses from a control list, and the executor handles clicks, typing and waiting.

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
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101364408870109184/img/w93wxuq73naZx36A.jpg" width="640" alt="Third Hand / arc-cua: choose actions on a Mac preview">](https://x.com/sxhivs/status/2101367048223982065)<br>[Video](https://x.com/sxhivs/status/2101367048223982065)

Preserves the Third Hand original snapshot, adding arc-cua’s 11-second demo, release reply and separate repository.

- [Direct video 1](https://video.twimg.com/amplify_video/2101364408870109184/vid/avc1/3024x1964/ywaIWwbhUYD5NIOm.mp4?tag=29) (metadata duration: 31.1s)

Media source: [original publishing page](https://x.com/sxhivs/status/2101367048223982065). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Read controls and screen text, choose actions and enter request- or planner-supplied text.

**Useful aspect (analysis):** Third Hand extracts text from requests without another generator; arc-cua accepts literals from an upstream planner for agent integration. Both separate action selection from local execution.

## Inputs, steps and outputs

Third Hand is a Swift app; the same author’s arc-cua is a separate Python executor reusing its text-entry approach. An upstream planner supplies goals, literal values and checks; AX/local OCR observes, Jev selects actions and input keys, and the runtime waits for UI stability.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shows a 31-second demo and claims subsecond latency. Documentation calls it experimental and says completion still needs human judgment. | Author report | [Post and attached media](https://x.com/sxhivs/status/2101367048223982065) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101367048223982065) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @sxhivs](https://x.com/sxhivs/status/2101367050207981608): published 2026-09-19T17:45:20+00:00; 50 likes retrieved 2026-09-20T02:53:28+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101367050207981608).
- [Supporting post by @sxhivs](https://x.com/sxhivs/status/2101729362194432184): published 2026-09-20T17:45:02+00:00; 505 likes retrieved 2026-09-21T02:45:24+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101729362194432184). [Supplementary media 1](https://video.twimg.com/amplify_video/2101728406949994496/vid/avc1/3024x1964/wsoMkHs40zGSxksi.mp4?tag=29)
- [Supporting post by @sxhivs](https://x.com/sxhivs/status/2101729364203475072): published 2026-09-20T17:45:03+00:00; 28 likes retrieved 2026-09-21T02:55:37+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101729364203475072).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/README.md)
- [Project / demo link 2](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/TextEntryPlan.swift)
- [Project / demo link 3](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/JevClient.swift)
- [Project / demo link 4](https://github.com/shhivv/arc-cua/blob/85fc321715e23f51c222d59d31461b75804ba4ac/README.md)
- [Project / demo link 5](https://github.com/shhivv/arc-cua/blob/85fc321715e23f51c222d59d31461b75804ba4ac/src/arc_cua/policies/typesafe.py)

## Mechanism and comparison

Separate repositories and programs are grouped as related work by one author. arc-cua still observes and calls Jev at each step; it has not established solved computer use. Unlabeled graphical interfaces and full-task success rates remain gaps.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-20 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-21T11:02:26+08:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
