# json-render: assemble interfaces from component choices

[简体中文](README.md) | **English**

> Turn interface requests into constrained component layouts, including additions, removals and moves.

**Added to README:** 2026-09-19 07:04:48<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Pinned docs substantiate component selection, staged layout and JSON assembly in code, without full-page templates or freeform generation. “Instant” is not established for arbitrary UIs: candidates, text, batch size and depth are bounded, with no matched-quality end-to-end benchmark.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#json-render-ui) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Like choosing blocks and arranging them: Jev makes selections, while code builds and renders a valid interface specification.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@ctatedev](https://x.com/ctatedev) |
| Main post | [Source post](https://x.com/ctatedev/status/2101022101750571357) |
| Published (UTC) | 2026-09-18T18:54:38+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-19 07:04:48 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **3,341** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T22:48:32+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101022101750571357); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101022081810911232/img/3tKdQ3Y2_ZGSg3Q7.jpg" width="640" alt="json-render: assemble interfaces from component choices preview">](https://x.com/ctatedev/status/2101022101750571357)<br>[Video](https://x.com/ctatedev/status/2101022101750571357)

The main video and author’s source-code reply form one case; quote-posts are not additional applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2101022081810911232/vid/avc1/1080x1080/B52suCKnBqA9pt2e.mp4?tag=29) (metadata duration: 18.5s)

Media source: [original publishing page](https://x.com/ctatedev/status/2101022101750571357). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Turn interface requests into constrained component layouts, including additions, removals and moves.

**Useful aspect (analysis):** Structural constraints are easier to enforce than character-by-character output. Compared with pixel drawing, this produces an interactive component tree that code can validate.

## Inputs, steps and outputs

Project documentation describes one batch for component membership and counts, then another for parent slots and ordering. Code builds and validates JSON using 17 app-owned component types, bindings and actions, rather than full-page templates or another generative model.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares an editable UI video and source links. Documentation rules out freeform generation calls; independent quality comparisons are absent. | Author report | [Post and attached media](https://x.com/ctatedev/status/2101022101750571357) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101022101750571357) | Snapshot at the recorded time, not a live count |

**Documentation review:** Read the [pinned documentation](https://github.com/vercel-labs/json-render/blob/3ad381881194e7011ad3ccd6d668033495a06c29/apps/web/lib/jev/README.md). Implementation descriptions above come from documentation, not installation, execution or independent reproduction.

Updates and deduplicated supporting sources:

- [Supporting post by @ctatedev](https://x.com/ctatedev/status/2101022105647157442): published 2026-09-18T18:54:39+00:00; 390 likes retrieved 2026-09-18T22:51:25+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2101022105647157442).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/vercel-labs/json-render)
- [Project / demo link 2](https://github.com/vercel-labs/json-render/blob/3ad381881194e7011ad3ccd6d668033495a06c29/apps/web/lib/jev/README.md)

## Mechanism and comparison

Documented limits include 14 new elements per batch, 14 evaluator calls per request and depth 4. Structural validity does not guarantee semantic correctness or good design.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
