# Probably: semantic judgments as program control

[简体中文](README.md) | **English**

> Write judgments such as “is this email urgent?” into branches, then ask a text model to draft a reply.

**Added to README:** 2026-09-18 14:17:58<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>The site documents interpreter, Jev and text-model responsibilities and toy-language limits. Hosted examples replay cached results; custom inputs require local live calls. This disclosed replay is not a live speed benchmark.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#probably-language) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Put a judgment inside a program: Jev decides whether a condition holds or which branch fits, an interpreter coordinates the steps, and a separate model writes text.

[Back to catalog](../../README.en.md#interaction) · [Compare similar examples](../../breakdowns/2026-09-18-interaction.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Real-time interaction and composition experiments |
| Platform / author | X / [@southpolesteve](https://x.com/southpolesteve) |
| Main post | [Source post](https://x.com/southpolesteve/status/2100767781868150938) |
| Published (UTC) | 2026-09-18T02:04:04+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 14:17:58 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **894** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T06:08:49+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100767781868150938); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSdr-ILWUAAN29Y.jpg?name=orig" width="640" alt="Probably: semantic judgments as program control preview">](https://x.com/southpolesteve/status/2100767781868150938)<br>[Image](https://x.com/southpolesteve/status/2100767781868150938)

The main post includes a language-example image. The website was read; programs were not executed and cached demonstrations were not treated as live API tests.

- [Original image 1](https://pbs.twimg.com/media/HSdr-ILWUAAN29Y.jpg?name=orig)

Media source: [original publishing page](https://x.com/southpolesteve/status/2100767781868150938). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Write judgments such as “is this email urgent?” into branches, then ask a text model to draft a reply.

**Useful aspect (analysis):** Combines classification, branching and revision loops in a readable small language. Useful alongside vocabulary-chat and RISC-jeV experiments for understanding composition.

## Inputs, steps and outputs

The Probably 0.1 website describes a TypeScript interpreter: feels asks Jev about conditions, match selects a descriptive branch, while repeats judgments, and llm calls a separate text model. Conditions support confidence gates; match has no confidence gate in this version.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author posts a language-example image and playground URL, describing feels, match and while, with Jev making judgments and an LLM writing. | Author report | [Post and attached media](https://x.com/southpolesteve/status/2100767781868150938) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100767781868150938) | Snapshot at the recorded time, not a live count |

**Website review:** [Probably 0.1](https://probably-lang.southpolesteve.workers.dev) states that its hosted Worker replays bundled recordings and rejects uncached custom code or inputs without model calls. The interpreter also limits model calls and loop iterations per run. These are documented behaviors, not results from running the local interpreter.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://probably-lang.southpolesteve.workers.dev)

## Mechanism and comparison

Explicitly a toy language without general-purpose features such as arrays or functions. The hosted playground replays recorded results; custom programs require local execution with live model providers. Playback speed is not an inference benchmark.

See the [category analysis](../../breakdowns/2026-09-18-interaction.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
