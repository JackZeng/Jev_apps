# Kaku: tag notes using your existing organization

[简体中文](README.md) | **English**

> Organize notes with workspace tags and send uncertain matches for human review.

**Content updated:** 2026-09-23 12:09:12 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The task and review workflow have author support; large-scale quality, costs and exact model settings remain unverified.<br>[Assessment and sources](../../references/2026-09-23-increment10-audit.en.md#kaku-note-tags)

## How it works, in plain English

Like an archivist: apply obvious labels first and collect doubtful ones for you to check.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@gemama0](https://x.com/gemama0) |
| Main post | [Source post](https://x.com/gemama0/status/2102198046201086356) |
| Published (UTC) | 2026-09-22T00:47:25+00:00 |
| Main-post likes snapshot | **2,026** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T03:55:29+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2102198046201086356); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2102197556138684416/img/VOAFvXpPpUMtUKYH.jpg" width="640" alt="Kaku: tag notes using your existing organization preview">](https://x.com/gemama0/status/2102198046201086356)<br>[Video](https://x.com/gemama0/status/2102198046201086356)

Original, product link and workflow replies form one Kaku case; the app was not installed.

- [Direct video 1](https://video.twimg.com/amplify_video/2102197556138684416/vid/avc1/1250x720/6AxDsv51X3NUX8D4.mp4?tag=14) (metadata duration: 31.9s)

Media source: [original publishing page](https://x.com/gemama0/status/2102198046201086356). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Organize notes with workspace tags and send uncertain matches for human review.

**Useful aspect (analysis):** Keeps the user’s tag vocabulary. Unlike Shiori’s web bookmarks, Kaku targets note libraries.

## Inputs, steps and outputs

The author describes batch Jev judgments against existing tags, applying high-confidence matches and reviewing low-confidence cells in a matrix, with diff confirmation, discard and snapshot rollback.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| A roughly 31-second demo, with author replies describing batch judgments and review. | Author report | [Post and attached media](https://x.com/gemama0/status/2102198046201086356) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2102198046201086356) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

- [Supporting post by @gemama0](https://x.com/gemama0/status/2102198213067612337): published 2026-09-22T00:48:05+00:00; 78 likes retrieved 2026-09-23T03:59:43+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2102198213067612337).
- [Supporting post by @gemama0](https://x.com/gemama0/status/2102334807376367678): published 2026-09-22T09:50:52+00:00; 7 likes retrieved 2026-09-23T03:59:43+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2102334807376367678).
- [Supporting post by @gemama0](https://x.com/gemama0/status/2102360440353480999): published 2026-09-22T11:32:43+00:00; 5 likes retrieved 2026-09-23T03:59:43+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2102360440353480999).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://kaku.md)

## Mechanism and comparison

Confidence is not measured labeling accuracy. Human-reference comparisons, missed tags and cross-library validation are absent. Targeting Obsidian users does not establish an Obsidian plugin.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
