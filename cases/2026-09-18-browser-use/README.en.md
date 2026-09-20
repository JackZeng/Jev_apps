# Browser Use · Ultrafast

[简体中文](README.md) | **English**

> Describe a flight search and let the agent click, type and find results on the website.

**Content updated:** 2026-09-20 11:01:10 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Pinned docs and a public benchmark expose implementation and timing conditions. The new 12306 clip is another use report for the same project, not a separate app or proof of arbitrary-site reliability.<br>[Assessment and sources](../../references/2026-09-20-increment8-audit.en.md#browser-use)

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
| Main-post likes snapshot | **6,891** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:32:51.243200+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100411066966749359); may be cached |
| Last source review | 2026-09-20; public descriptions and metadata reviewed, application not run |
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

**2026-09-19 WebMCP comparison merged:** The author modifies Ultrafast: Jev selects website tools and Mercury 2.5 generates arguments. This is a benchmark variant of the existing project, not another entry. The [benchmark](https://webmcp.com/benchmark) covers 49 tasks on eight sites, with three attempts each. WebMCP solves 49/49 tasks but succeeds in 141/147 attempts; the DOM variant solves 25/49. Displayed median costs are $0.0011 and $0.0008 respectively, so the post’s 18% reduction does not directly describe those medians. These findings apply to this harness and test, without independent reproduction.

**2026-09-20 merged 12306 use report:** [@yanhua1010’s post](https://x.com/yanhua1010/status/2101257759497089171) explicitly uses Jev Ultrafast with Pi + DeepSeek to query trains. The roughly 93-second process video lacks full timing boundaries, bills and repeated tests; it is not a separate browser tool.

Updates and deduplicated supporting sources:

- [Supporting post by @0xidanlevin](https://x.com/0xidanlevin/status/2100937437325205568): published 2026-09-18T13:18:13+00:00; 1,407 likes retrieved 2026-09-18T22:50:12+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100937437325205568). [Supplementary media 1](https://pbs.twimg.com/media/HSf2OSVWQAAYUAE.jpg?name=orig)
- [Supporting post by @yanhua1010](https://x.com/yanhua1010/status/2101257759497089171): published 2026-09-19T10:31:04+00:00; 227 likes retrieved 2026-09-20T02:51:41+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101257759497089171). [Supplementary media 1](https://video.twimg.com/amplify_video/2101257016945819648/vid/avc1/2458x1440/F8vfvuaYZJ38VTOq.mp4?tag=29)

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/browser-use/jev-ultrafast)
- [Project / demo link 2](https://github.com/browser-use/jev-ultrafast/blob/452c1ad2dd628008f1d5608f28158d76e49e6cc0/README.md)
- [Project / demo link 3](https://webmcp.com/benchmark)
- [Project / demo link 4](https://github.com/nekuda-ai/WindTunnel)

## Mechanism and comparison

Still uses an LLM for text. The MVP excludes shadow DOM, iframes, canvas and uploads; a few repeated tasks do not establish cross-site reliability.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-18T23:03:22+00:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
| 2026-09-20T11:01:10+08:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
