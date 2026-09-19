# Nifty intraday trading: an account demo with a stop-loss report

[简体中文](README.md) | **English**

> Demonstrate Jev-connected Nifty trading and report a triggered stop loss.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The source reports a stop-loss after an initially green morning, not a profitable day. Account authenticity, executions and long-term risk controls remain unverified; the disclosure is more balanced than profit marketing.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#nifty-trading)

## How it works, in plain English

Like connecting decisions to orders with a stopping rule. Model judgments, broker execution and risk controls have separate roles; a video does not prove profitability.

[Back to catalog](../../README.en.md#finance) · [Compare similar examples](../../breakdowns/2026-09-18-finance.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Trading and historical backtests |
| Platform / author | X / [@IndraVahan](https://x.com/IndraVahan) |
| Main post | [Source post](https://x.com/IndraVahan/status/2100929105382564113) |
| Published (UTC) | 2026-09-18T12:45:06+00:00 |
| Main-post likes snapshot | **673** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T22:50:12+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100929105382564113); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100928264831410176/img/VP6eszCSb95ePMo4.jpg" width="640" alt="Nifty intraday trading: an account demo with a stop-loss report preview">](https://x.com/IndraVahan/status/2100929105382564113)<br>[Video](https://x.com/IndraVahan/status/2100929105382564113)

The roughly 38-second video has a different author, market and execution venue from the Monad/Kuru bot.

- [Direct video 1](https://video.twimg.com/amplify_video/2100928264831410176/vid/avc1/1920x1080/IsI9fz3yTp8KOeDw.mp4?tag=29) (metadata duration: 37.7s)

Media source: [original publishing page](https://x.com/IndraVahan/status/2100929105382564113). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Demonstrate Jev-connected Nifty trading and report a triggered stop loss.

**Useful aspect (analysis):** Unlike speed-only trading posts, this discloses a stopped-out day and an author-reported adverse outcome.

## Inputs, steps and outputs

The author claims a real Kotak account with ₹100,000 and 5× leverage. Strategy inputs, Jev candidates and order code are undisclosed; live-account status was not independently verified.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author says an initially profitable morning ended at the ₹1,000 hard stop, not an overall profitable day. | Author report | [Post and attached media](https://x.com/IndraVahan/status/2100929105382564113) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100929105382564113) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Accounts, fills and net returns are unverified. Leverage magnifies losses; one stop-loss report does not establish durable risk control.

See the [category analysis](../../breakdowns/2026-09-18-finance.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
