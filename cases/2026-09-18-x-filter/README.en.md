# Natural-language X content filter

[简体中文](README.md) | **English**

> Tell the browser in your own words which X posts you would rather not see.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A credible natural-language filtering demo; false positives, misses and ongoing cost are unmeasured, and the future-of-ad-blockers framing is a vision.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#x-filter)

## How it works, in plain English

The extension asks Jev whether a post matches your filtering rule, then hides or collapses it. The aim is meaning-based filtering rather than a keyword match.

[Back to catalog](../../README.en.md#filter) · [Compare similar examples](../../breakdowns/2026-09-18-filter.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Webpage and feed filtering |
| Platform / author | X / [@marcelpociot](https://x.com/marcelpociot) |
| Main post | [Source post](https://x.com/marcelpociot/status/2100520134481735729) |
| Published (UTC) | 2026-09-17T09:40:00+00:00 |
| Main-post likes snapshot | **950** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.919857+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100520134481735729); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100519256425140224/img/-A44e4qCo8mVP8ws.jpg" width="640" alt="Natural-language X content filter preview">](https://x.com/marcelpociot/status/2100520134481735729)<br>[Video](https://x.com/marcelpociot/status/2100520134481735729)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100519256425140224/vid/avc1/1502x1080/c5G0aEoBbk0xPR_k.mp4?tag=29) (metadata duration: 45.1s)
- [Original image 2](https://pbs.twimg.com/media/HSaLxuaW0AA-KC5.jpg?name=orig)

Media source: [original publishing page](https://x.com/marcelpociot/status/2100520134481735729). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Tell the browser in your own words which X posts you would rather not see.

**Useful aspect (analysis):** Can express semantic preferences that keyword filters miss.

## Inputs, steps and outputs

Browser extension reads posts → Jev checks them against a rule → hide or collapse.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares an extension video and configuration screenshot, without a standardized benchmark. | Author report | [Post and attached media](https://x.com/marcelpociot/status/2100520134481735729) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100520134481735729) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

False-positive rates are unmeasured; vague rules may remove useful content.

See the [category analysis](../../breakdowns/2026-09-18-filter.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
