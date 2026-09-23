# BTC paper trading: estimate five-minute direction from an order book

[简体中文](README.md) | **English**

> Read market order-book data, estimate direction and simulate trades against prediction-market prices.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>B supports a concrete paper-trading experiment only; predictive accuracy and profitability are unverified.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#btc-polymarket-paper)

## How it works, in plain English

Estimate a reference price, then compare it with a quoted price; faster execution cannot make a wrong estimate correct.

[Back to catalog](../../README.en.md#finance) · [Compare similar examples](../../breakdowns/2026-09-18-finance.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Trading and historical backtests |
| Platform / author | X / [@FrankDa18249347](https://x.com/FrankDa18249347) |
| Main post | [Source post](https://x.com/FrankDa18249347/status/2102197241331290121) |
| Published (UTC) | 2026-09-22T00:44:13+00:00 |
| Main-post likes snapshot | **356** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T03:55:29+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102197241331290121); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102196000005963776/img/J_7eFuDjznhJL_6l.jpg" width="640" alt="BTC paper trading: estimate five-minute direction from an order book preview">](https://x.com/FrankDa18249347/status/2102197241331290121)<br>[Video](https://x.com/FrankDa18249347/status/2102197241331290121)

Original author video and a read-only demo link; no orders or bot runs were performed.

- [Direct video 1](https://video.twimg.com/amplify_video/2102196000005963776/vid/avc1/2876x1532/6XSoFiCFZOZ5iv9n.mp4?tag=29) (metadata duration: 28.1s)

Media source: [original publishing page](https://x.com/FrankDa18249347/status/2102197241331290121). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Read market order-book data, estimate direction and simulate trades against prediction-market prices.

**Useful aspect (analysis):** Connects decisions to explicit input and trading rules while clearly identifying paper trading, separate from live capital.

## Inputs, steps and outputs

The author uses Binance BTC futures order-book data for Jev estimates of Polymarket five-minute directional-market fair value, trading on differences from quoted prices in a simulation.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A 1,000u paper account and roughly 28-second demo, not verified real returns or live-fund trading. | Author report | [Post and attached media](https://x.com/FrankDa18249347/status/2102197241331290121) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102197241331290121) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](http://jev-poly-crypto-demo-black.vercel.app/)

## Mechanism and comparison

No probability calibration, out-of-sample results or comparison including fees, latency and slippage. A model score is not established fair value, and a short demo cannot show profitability.

See the [category analysis](../../breakdowns/2026-09-18-finance.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
