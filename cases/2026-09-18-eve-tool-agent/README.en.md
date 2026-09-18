# Eve tool-calling agent

[简体中文](README.md) | **English**

> Let Jev choose an agent's next tool to reduce selection overhead.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 07:24:03 (Beijing time, UTC+08:00)

## How it works, in plain English

The original agent reasons about which tool to use. This experiment hands that choice to Jev while retaining the tools and downstream processing.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@oviniciuslana](https://x.com/oviniciuslana) |
| Main post | [Source post](https://x.com/oviniciuslana/status/2100457622407168509) |
| Published (UTC) | 2026-09-17T05:31:36+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 07:24:03 |
| Main-post likes snapshot | **1,117** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:23.913443+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100457622407168509); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSZSqLGXwAA1jSL.jpg?name=orig" width="640" alt="Eve tool-calling agent preview">](https://x.com/oviniciuslana/status/2100457622407168509)<br>[Image](https://x.com/oviniciuslana/status/2100457622407168509)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Original image 1](https://pbs.twimg.com/media/HSZSqLGXwAA1jSL.jpg?name=orig)
- [Original image 2](https://pbs.twimg.com/media/HSZS8p0XMAA0_s2.png?name=orig)

Media source: [original publishing page](https://x.com/oviniciuslana/status/2100457622407168509). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Let Jev choose an agent's next tool to reduce selection overhead.

**Useful aspect (analysis):** A targeted substitution for existing tool agents without rebuilding the whole system.

## Inputs, steps and outputs

Keep the agent execution flow while handing tool selection to Jev; compare combinations with several larger models.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| An earlier update reports roughly one-eighth the cost with similar execution time and output quality. | Author report | [Post and attached media](https://x.com/oviniciuslana/status/2100457622407168509) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100457622407168509) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @oviniciuslana](https://x.com/oviniciuslana/status/2100423271128715387): published 2026-09-17T03:15:06+00:00; 223 likes retrieved 2026-09-17T22:42:24.020491+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100423271128715387). [Supplementary media 1](https://pbs.twimg.com/media/HSYzx4UXIAAzwwy.jpg?name=orig)

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

The author describes similar results but provides insufficient samples or a shared quality score; savings do not imply complete LLM replacement.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
