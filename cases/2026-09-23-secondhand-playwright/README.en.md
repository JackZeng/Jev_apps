# Second-hand shopping assistant: judge listings against requirements

[简体中文](README.md) | **English**

> Browse used-item listings, reject mismatches and demonstrate follow-up actions.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A concrete shopping-screening prototype; reported bidding/contact actions are not verified purchasing outcomes.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#secondhand-playwright)

## How it works, in plain English

Check listings against a shopping list and identify missing information.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@AlanDaitch](https://x.com/AlanDaitch) |
| Main post | [Source post](https://x.com/AlanDaitch/status/2100757989212754085) |
| Published (UTC) | 2026-09-18T01:25:09+00:00 |
| Main-post likes snapshot | **947** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:46+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100757989212754085); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/ext_tw_video_thumb/2100757808484438017/pu/img/bydnTNNexLUnwB63.jpg" width="640" alt="Second-hand shopping assistant: judge listings against requirements preview">](https://x.com/AlanDaitch/status/2100757989212754085)<br>[Video](https://x.com/AlanDaitch/status/2100757989212754085)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/ext_tw_video/2100757808484438017/pu/vid/avc1/1510x720/AKPTLyKiMAlH8Sw9.mp4?tag=12) (metadata duration: 55.2s)

Media source: [original publishing page](https://x.com/AlanDaitch/status/2100757989212754085). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Browse used-item listings, reject mismatches and demonstrate follow-up actions.

**Useful aspect (analysis):** A specific browsing task with clearer acceptance criteria than generic clicking.

## Inputs, steps and outputs

The author uses Claude to integrate Jev with Playwright. Jev judges matches; the browser filters, bids and asks questions. Message-generation roles are unspecified.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports about 26 listings/minute, 406ms decisions and $0.00085 for a search, unreplicated. | Author report | [Post and attached media](https://x.com/AlanDaitch/status/2100757989212754085) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100757989212754085) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

No seller responses, completed purchases or mistaken-bid records. Actions do not establish successful buying; full costs are unclear.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
