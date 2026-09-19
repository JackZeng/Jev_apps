# Unclutter page cleanup

[简体中文](README.md) | **English**

> Clear ads, promotional dialogs and similar clutter to make webpages easier to read.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The page-cleanup prototype is demonstrated and explicitly BYOK; cross-site safety and compatibility are untested, and a free extension does not mean free inference.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#unclutter) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Code identifies candidate page elements and asks Jev to judge them. The challenge is not only finding clutter but avoiding removal of useful controls such as login dialogs.

[Back to catalog](../../README.en.md#filter) · [Compare similar examples](../../breakdowns/2026-09-18-filter.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Webpage and feed filtering |
| Platform / author | X / [@thekitze](https://x.com/thekitze) |
| Main post | [Source post](https://x.com/thekitze/status/2100595129874817340) |
| Published (UTC) | 2026-09-17T14:38:00+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **497** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:26.941693+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100595129874817340); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100595059041370112/img/cyfF5qMMKBPQTMAG.jpg" width="640" alt="Unclutter page cleanup preview">](https://x.com/thekitze/status/2100595129874817340)<br>[Video](https://x.com/thekitze/status/2100595129874817340)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100595059041370112/vid/avc1/1718x1080/Ar4lfNzo_oThuG2K.mp4?tag=16) (metadata duration: 25.3s)

Media source: [original publishing page](https://x.com/thekitze/status/2100595129874817340). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Clear ads, promotional dialogs and similar clutter to make webpages easier to read.

**Useful aspect (analysis):** Targets page clutter beyond individual X posts.

## Inputs, steps and outputs

Candidate page elements → Jev identifies cleanup targets → extension applies changes; extraction details are unknown.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares an approximately 25-second demo and describes it as free, open source and BYOK. | Author report | [Post and attached media](https://x.com/thekitze/status/2100595129874817340) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100595129874817340) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Requires the user's API key; mistaken element classification may affect legitimate dialogs or page behavior.

See the [category analysis](../../breakdowns/2026-09-18-filter.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
