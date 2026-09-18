# Real-time interaction and composition experiments: how they work and compare

[简体中文](2026-09-18-interaction.md) | **English**

First compiled: 2026-09-18; see each case for its source-review date. Status: **not independently reproduced**.

## Choosing an approach

TypeGPU combines local perception with remote semantic decisions. Ask Jev exposes simple judgments. Word/character chat demonstrates selection loops; pixel drawing and RISC-jeV combine small judgments into outputs. These are conceptual examples, not established replacements for specialized models or programs. Other entries cover file selection, emoji suggestions, live shopping and voice-and-pointing canvas control. Their distinct tasks warrant separate cases. Both the canvas and TypeGPU combine perception with decisions, but one manipulates objects while the other changes audiovisual effects. Probably organizes judgments, branches and text generation into a small language. Its hosted site uses recorded playback, which must be distinguished from live local model calls when discussing responsiveness. Shell-history suggestions and the launcher both select a next step from candidates. The former documents thresholds in a pinned version but uses fabricated demo history; the latter selects files. Compare hit rates, acceptance and execution risks separately. json-render assembles interactive component trees, the color experiment visualizes 16-color judgments, and CNVS gates whether to respond to speech. They require structural/semantic checks, subjective matching and false-activation tests respectively, not just latency comparisons.

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
| [Intent-aware predictive launcher](../cases/2026-09-18-predictive-launcher/README.en.md) | Explores contextual requests such as “just downloaded” beyond filename or alias matching; useful for selecting among file candidates. | The roughly 100ms figure is author-reported. No evaluation covers large file collections, duplicate names or ambiguous references. High model confidence does not guarantee a correct match. |
| [Live shopping assistant and avatar expressions](../cases/2026-09-18-live-commerce-assistant/README.en.md) | Places recommendations inside a live conversation; closer to a customer-facing shopping experience than offline intent labeling. | A simple demo without recommendation-relevance, inventory-consistency or end-to-end latency evaluation. Expression mapping does not establish a capability exclusive to Jev. |
| [Live emoji suggestions](../cases/2026-09-18-emoji-suggestions/README.en.md) | A bounded output space with immediately visible feedback; simpler than the repeated selection loop in character-by-character chat. | The 100–200ms and candidate-count claims describe this demo, not arbitrary scales. No language, ambiguity or emoji-relevance evaluation is available. |
| [Voice-and-pointing canvas control](../cases/2026-09-18-voice-gesture-canvas/README.en.md) | Combines language and pointing to resolve references missing from text alone. Compared with TypeGPU’s semantic effects, this example focuses on manipulating canvas objects. | The author explicitly describes an imperfect feasibility experiment. No pointing-error, speech-error or action-success evaluation is available, and separate decisions still require consistency checks. |
| [Probably: semantic judgments as program control](../cases/2026-09-18-probably-language/README.en.md) | Combines classification, branching and revision loops in a readable small language. Useful alongside vocabulary-chat and RISC-jeV experiments for understanding composition. | Explicitly a toy language without general-purpose features such as arrays or functions. The hosted playground replays recorded results; custom programs require local execution with live model providers. Playback speed is not an inference benchmark. |
| [Shell history: semantic command suggestions](../cases/2026-09-18-shell-history-suggestions/README.en.md) | Supports intent descriptions beyond literal prefixes while restricting outputs to historical candidates. Like the predictive launcher it selects candidates, but operates on commands rather than files. | History can be stale or sensitive and is sent to the service as candidate data. A suitable suggestion does not establish safe execution; user review remains necessary. The README reports roughly 0.7–0.9 seconds per request, not the millisecond claims from other demos. The author presents an experiment, not evidence of daily use. |
| [json-render: assemble interfaces from component choices](../cases/2026-09-19-json-render-ui/README.en.md) | Structural constraints are easier to enforce than character-by-character output. Compared with pixel drawing, this produces an interactive component tree that code can validate. | Documented limits include 14 new elements per batch, 14 evaluator calls per request and depth 4. Structural validity does not guarantee semantic correctness or good design. |
| [CNVS: gate voice commands without a wake word](../cases/2026-09-19-cnvs-voice-gate/README.en.md) | Unlike the voice-and-gesture canvas, this focuses on deciding whether to respond, without a fixed activation phrase. | False activations, missed commands, recording handling and end-to-end latency lack evaluation. A text decision model should not be described as directly understanding raw audio. |
| [Words and colors: visualize 16-color judgments](../cases/2026-09-19-color-judgments/README.en.md) | A smaller candidate set than pixel drawing offers direct semantic feedback for exploring word-to-visual interaction. | Constrained by palette and prompts, subjective associations have no single correct answer. This is not an image-recognition or color-science evaluation. |

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
