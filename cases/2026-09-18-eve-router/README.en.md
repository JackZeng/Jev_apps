# Eve criteria-based model router

[简体中文](README.md) | **English**

> Choose which model should handle a request before sending it there.

## How it works, in plain English

Like a receptionist routing calls, Jev sees the request and selection criteria, chooses a model, and lets code forward the work. The final task result is needed to judge the choice.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@eve](https://x.com/eve) |
| Main post | [Source post](https://x.com/eve/status/2100430918762832180) |
| Published (UTC) | 2026-09-17T03:45:29+00:00 |
| Collected / record updated | 2026-09-18 / 2026-09-18 |
| Main-post likes snapshot | **821** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:32:51.243424+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100430918762832180); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig" width="640" alt="Eve criteria-based model router preview">](https://x.com/eve/status/2100430918762832180)<br>[Image](https://x.com/eve/status/2100430918762832180)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Original image 1](https://pbs.twimg.com/media/HSY6yf5a8AA8NJi.jpg?name=orig)

Media source: [original publishing page](https://x.com/eve/status/2100430918762832180). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Choose which model should handle a request before sending it there.

**Useful aspect (analysis):** An explicit selection policy can serve as a separate routing layer.

## Inputs, steps and outputs

Jev receives the request and selection criteria, selects a candidate model, and the application invokes it.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a screenshot of criteria-based model routing. | Author report | [Post and attached media](https://x.com/eve/status/2100430918762832180) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100430918762832180) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The post provides no routing accuracy, quota policy or fallback evaluation; the evidence is a demo screenshot.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
