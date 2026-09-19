# Monad / Kuru trading bot

[简体中文](README.md) | **English**

> Let Jev choose buy or sell from price information and have code submit the order.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The decision-to-order architecture is plausible, but trades and sustained end-to-end latency are unverified. A 300ms block interval is not a measured complete decision/execution cycle, and no profitable strategy is established.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#trading-bot) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

The model chooses an action and code connects to the blockchain order book. Fast orders do not imply profitable trading; complete returns and risk records are absent.

[Back to catalog](../../README.en.md#finance) · [Compare similar examples](../../breakdowns/2026-09-18-finance.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Trading and historical backtests |
| Platform / author | X / [@jarrodwatts](https://x.com/jarrodwatts) |
| Main post | [Source post](https://x.com/jarrodwatts/status/2100356151468585346) |
| Published (UTC) | 2026-09-16T22:48:23+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **4,142** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:32:51.243553+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100356151468585346); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100355999064379392/img/BiAbeDjN57avf2VK.jpg" width="640" alt="Monad / Kuru trading bot preview">](https://x.com/jarrodwatts/status/2100356151468585346)<br>[Video](https://x.com/jarrodwatts/status/2100356151468585346)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100355999064379392/vid/avc1/1812x1080/GZCpxi1k16gkuJyS.mp4?tag=29) (metadata duration: 10.3s)

Media source: [original publishing page](https://x.com/jarrodwatts/status/2100356151468585346). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Let Jev choose buy or sell from price information and have code submit the order.

**Useful aspect (analysis):** A clear decision-to-execution path for studying event-driven systems.

## Inputs, steps and outputs

Asset-pair prices → Jev buy/sell choice → Kuru order book on Monad.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author says it can execute trades in each roughly 300ms block and provides a demo URL. | Author report | [Post and attached media](https://x.com/jarrodwatts/status/2100356151468585346) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100356151468585346) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://jev-trader.vercel.app/)

## Mechanism and comparison

No return, drawdown or risk-control evaluation; fast execution does not establish profitability. The demo is not investment advice.

See the [category analysis](../../breakdowns/2026-09-18-finance.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
