# NPCs, driving and population simulations: how they work and compare

[简体中文](2026-09-18-simulation.md) | **English**

First compiled: 2026-09-18; see each case for its source-review date. Status: **not independently reproduced**.

## Choosing an approach

Needs-driven NPCs explore behavior; the 500-agent demo explores throughput. Unpaused driving exposes latency constraints. The drone project provides code. Towns and fictional personas are storytelling or ideation tools, not evidence of real-world behavior. Traffic signals, dual-arm manipulation and vital signs respectively concern signal direction, layered actions and state labels. Robotics explicitly leaves IK/physics to code; the traffic ratio and practical monitoring claims lack matching validation. Evaluate each task separately from real deployment.

## Individual comparisons

These are analytical strengths and limitations based on public descriptions, not controlled experimental findings.

| Example | Strengths / suitable uses | Limitations / missing evidence |
| --- | --- | --- |
| [Needs-driven NPCs](../cases/2026-09-18-npc-needs/README.en.md) | Semantic descriptions could extend behavior in utility-AI / smart-object scenarios. | Need weighting, conflicts and long-term consistency are unspecified; traditional rules may be simpler and cheaper. |
| [500 agents in a 3D environment](../cases/2026-09-18-npc-500/README.en.md) | Focuses on population scale and throughput under simulation load. | 35 calls/second is not 35 updates per second for every agent; per-agent update frequency is absent. |
| [“FSD” driving simulation](../cases/2026-09-18-driving-toy/README.en.md) | A visual example of fast decisions inside a driving simulation. | Not a reproduction of Tesla FSD or a real-road validation; it establishes no road-safety or autonomous-driving capability. |
| [Unpaused real-time driving](../cases/2026-09-18-realtime-driving/README.en.md) | Explicitly exposes latency and stale-state constraints rather than pausing the simulation. | Still a simulator, without coverage, crash-rate or long-duration stability data. |
| [Jev drone simulation](../cases/2026-09-18-drone-sim/README.en.md) | Publishes perception, tactical decision and flight-control layers, including a baseline and failure boundaries. | MuJoCo simulation, not a real flight. The main successful comparison is a single run; an earlier seed-matched test showed no advantage over the baseline. |
| [Unstable Government town](../cases/2026-09-18-unstable-government/README.en.md) | Separates narrative generation from character choices for interactive storytelling. | Fictional reactions cannot be used as predictions of policy effects in the real world. |
| [150 fictional user personas](../cases/2026-09-18-synthetic-personas/README.en.md) | A quick way to explore persona/product fit and draft interview questions. | Synthetic opinions are not actual user research or market-demand validation. |
| [Jev City: nine-intersection traffic simulation](../cases/2026-09-19-traffic-light-city/README.en.md) | Unlike controlling one simulated car, this coordinates junctions to explore network-level congestion effects. | Matched traffic demand, seeds, repeated trials and fixed/adaptive rule baselines are missing. A virtual network does not establish real-city outcomes. |
| [Vital-sign simulation: judging state changes](../cases/2026-09-19-vital-signs-simulator/README.en.md) | Unlike traffic or robotics control, this explores state assessment and false alarms; scenarios can inform later evaluation questions. | No clinical dataset, independent validation or missed-event statistics was provided. The author’s repeatability-based explanation of calibration does not establish risk-probability validity. |
| [Dual-arm robot simulation: layered action decisions](../cases/2026-09-19-dual-arm-robot-sim/README.en.md) | Like drone simulation, this separates decisions from motion computation, but explores object selection and dual-arm manipulation. | No physical-robot deployment or complete success-rate evaluation. A roughly 500ms response is not a joint-control period or full task duration. |

## Workflow and mechanism

Simulation state and character goals → Jev decisions → simulated actions → updated state; an LLM may supply narrative reaction candidates.

FSD is the driving demo author’s label, not a reproduction of Tesla’s product or real-road capability. Overall API throughput differs from per-character update frequency. Fictional adoption intent is not user research. The drone repository specifies MuJoCo and separates fast control from slower model decisions, while disclosing the limits of its single-run comparison.

Individual input and implementation differences are documented in the linked cases. This is an application-level synthesis, not a claim that every implementation is identical or an account of Jev’s internal training architecture.

## Suggested reproduction experiments

Document environments, update rates, pause policy, network jitter and failure criteria. Track collisions, task success and character consistency over time. Compare synthetic-user findings with real research.

**Not run.** There are no timing, accuracy or cost results produced by this repository.

## Change log

- 2026-09-18: collected the first batch, merged same-project updates and added comparisons.

[Homepage](../README.en.md#simulation) · [Explanation index](README.en.md)
