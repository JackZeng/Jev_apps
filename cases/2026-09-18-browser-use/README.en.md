# Browser Use · Ultrafast

[简体中文](README.md) | **English**

> Describe a flight search and let the agent click, type and find results on the website.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 07:24:03 (Beijing time, UTC+08:00)

## How it works, in plain English

Think of an assistant with a constantly updated list of buttons. Code reads the page, Jev chooses the next action, and a text model helps fill in details such as city names.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@gregpr07](https://x.com/gregpr07) |
| Main post | [Source post](https://x.com/gregpr07/status/2100411066966749359) |
| Published (UTC) | 2026-09-17T02:26:36+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 07:24:03 |
| Main-post likes snapshot | **6,891** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:32:51.243200+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100411066966749359); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100410607807918080/img/lNfcykqoOvLoZHWa.jpg" width="640" alt="Browser Use · Ultrafast preview">](https://x.com/gregpr07/status/2100411066966749359)<br>[Video](https://x.com/gregpr07/status/2100411066966749359)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100410607807918080/vid/avc1/1536x1000/-_qOblr7l4zH2q3G.mp4?tag=29) (metadata duration: 7.6s)

Media source: [original publishing page](https://x.com/gregpr07/status/2100411066966749359). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Describe a flight search and let the agent click, type and find results on the website.

**Useful aspect (analysis):** Dynamic action candidates and public code make the complete browser loop worth studying.

## Inputs, steps and outputs

Each step builds a fresh action space from the DOM. Jev selects an action; a small LLM supplies text when needed.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports a flight search taking about 7 seconds and costing $0.0039, shown at normal speed. | Author report | [Post and attached media](https://x.com/gregpr07/status/2100411066966749359) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100411066966749359) | Snapshot at the recorded time, not a live count |

**Repository cross-check (2026-09-18)**: The [pinned README](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/README.md) describes separate operation and target judgments in one request, with code executing only the matching target. A small LLM is used for TYPE_TEXT. Its 7,073ms measurement starts after the initial page observation and lists unsupported page types; it is not a general time from browser launch to arbitrary task completion.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/browser-use/jev-ultrafast)
- [Project / demo link 2](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/README.md)

## Mechanism and comparison

Still uses an LLM for text. The MVP excludes shadow DOM, iframes, canvas and uploads; a few repeated tasks do not establish cross-site reliability.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
