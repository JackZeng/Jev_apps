# RISC-jeV logic-gate experiment

[简体中文](README.md) | **English**

> Use Jev for simple logic decisions and compose them into small computer instructions.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author explicitly describes logic-gate judgments composed through SERV, not a native Jev CPU. Integration correctness, stability and any advantage over deterministic computation remain unverified.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#riscv) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Like building a machine from blocks, Jev supplies AND/OR-style decisions that SERV combines into instructions. This illustrates composition rather than efficient computation.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@i2cjak](https://x.com/i2cjak) |
| Main post | [Source post](https://x.com/i2cjak/status/2100454307405365673) |
| Published (UTC) | 2026-09-17T05:18:26+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **208** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:30.049692+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100454307405365673); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100454137695469568/img/pGRTotN_ZQaAuc4V.jpg" width="640" alt="RISC-jeV logic-gate experiment preview">](https://x.com/i2cjak/status/2100454307405365673)<br>[Video](https://x.com/i2cjak/status/2100454307405365673)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100454137695469568/vid/avc1/2560x1440/b4YhzEsIMYgQ5A-V.mp4?tag=29) (metadata duration: 40.2s)

Media source: [original publishing page](https://x.com/i2cjak/status/2100454307405365673). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Use Jev for simple logic decisions and compose them into small computer instructions.

**Useful aspect (analysis):** An explicit hierarchy illustrates how decisions can compose into computation.

## Inputs, steps and outputs

Jev judges AND/OR-style operations → SERV instruction execution → arithmetic, bit operations and printing.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author publishes a live demo and names the SERV implementation. | Author report | [Post and attached media](https://x.com/i2cjak/status/2100454307405365673) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100454307405365673) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://jev-riscv-production.up.railway.app)

## Mechanism and comparison

A concept experiment, not a computational-efficiency advantage; deterministic code is more appropriate for logic gates.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
