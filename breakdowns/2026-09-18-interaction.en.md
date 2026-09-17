# Real-time interaction and composition experiments: how they work and compare

[简体中文](2026-09-18-interaction.md) | **English**

Collected / source-reviewed: 2026-09-18. Status: **not independently reproduced**.

## Choosing an approach

TypeGPU combines local perception with remote semantic decisions. Ask Jev exposes simple judgments. Word/character chat demonstrates selection loops; pixel drawing and RISC-jeV combine small judgments into outputs. These are conceptual examples, not established replacements for specialized models or programs.

## Individual comparisons

These are analytical strengths and limitations based on public descriptions, not controlled experimental findings.

| Example | Strengths / suitable uses | Limitations / missing evidence |
| --- | --- | --- |
| [TypeGPU real-time semantic effects](../cases/2026-09-18-typegpu-realtime/README.en.md) | Separates local perception from semantic decisions for interactive media. | Jev is only one part of the pipeline; end-to-end latency and component ablations are absent. |
| [Ask Jev](../cases/2026-09-18-ask-jev/README.en.md) | A public entry point that makes judgment-style output tangible. | An interaction/entertainment example; arbitrary judgments should not be treated as reliable factual answers. |
| [Finite-vocabulary chat](../cases/2026-09-18-word-chat/README.en.md) | Shows how choice outputs can be composed into a generative interaction. | The vocabulary limits expression; per-word decision costs and latency are not directly comparable with a text model. |
| [29-option character generation](../cases/2026-09-18-character-chat/README.en.md) | An explicit control loop with more freedom than a fixed word list. | Character-level loops require many calls and do not establish a native text-generation API. |
| [Parallel pixel drawing](../cases/2026-09-18-pixel-drawing/README.en.md) | An exploratory way to combine classification outputs into a visual artifact. | Not a validated general image generator; quality, resolution and total cost are unknown. |
| [RISC-jeV logic-gate experiment](../cases/2026-09-18-riscv/README.en.md) | An explicit hierarchy illustrates how decisions can compose into computation. | A concept experiment, not a computational-efficiency advantage; deterministic code is more appropriate for logic gates. |

## Workflow and mechanism

Prepare finite candidates or atomic questions → Jev judges → code composes results → update interaction state or output.

Code assembles word and character choices into text; the API still returns judgments. RISC-jeV stacks logic-gate decisions and instruction interpretation to illustrate composition, not efficiency.

Individual input and implementation differences are documented in the linked cases. This is an application-level synthesis, not a claim that every implementation is identical or an account of Jev’s internal training architecture.

## Suggested reproduction experiments

Record vocabulary size, resolution or character count, loop count and full cost. Compare quality with deterministic code or specialized generators. Measure local perception, remote decisions and rendering separately.

**Not run.** There are no timing, accuracy or cost results produced by this repository.

## Change log

- 2026-09-18: collected the first batch, merged same-project updates and added comparisons.

[Homepage](../README.en.md#interaction) · [Explanation index](README.en.md)
