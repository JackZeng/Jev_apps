# Compact Adviser: choose when to compact

[简体中文](README.md) | **English**

> Suggest when a coding conversation has reached a suitable point for context compaction.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The two-question policy, usage-dependent thresholds and 96-checkpoint evaluation are documented. The author tuned prompts on a private evaluation set; an independent held-out set and unseen-session safety are not established.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#compact-adviser)

## How it works, in plain English

Like a secretary choosing a pause between topics for meeting notes: Jev judges timing and the host performs compaction. It does not select passages for deletion.

[Back to catalog](../../README.en.md#memory) · [Compare similar examples](../../breakdowns/2026-09-18-memory.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Context and memory filtering |
| Platform / author | X / [@kunchenguid](https://x.com/kunchenguid) |
| Main post | [Source post](https://x.com/kunchenguid/status/2101032677940117875) |
| Published (UTC) | 2026-09-18T19:36:40+00:00 |
| Main-post likes snapshot | **242** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T22:48:32+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101032677940117875); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HShbIHcbcAAJvsR.jpg?name=orig" width="640" alt="Compact Adviser: choose when to compact preview">](https://x.com/kunchenguid/status/2101032677940117875)<br>[Image](https://x.com/kunchenguid/status/2101032677940117875)

The main post includes an image; pinned documentation explains the process and evaluation scope.

- [Original image 1](https://pbs.twimg.com/media/HShbIHcbcAAJvsR.jpg?name=orig)

Media source: [original publishing page](https://x.com/kunchenguid/status/2101032677940117875). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Suggest when a coding conversation has reached a suitable point for context compaction.

**Useful aspect (analysis):** Complements tool-output compaction by deciding when it should happen. Documented gates and fallbacks make the policy inspectable.

## Inputs, steps and outputs

Pinned documentation uses two yes/no judgments about work-unit completion and hands-on versus coordination work. Code combines them with context usage, token floors and cooldowns. Pi and Claude support optional automatic mode; Codex CLI is advisory only.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports 96 checkpoints from 40 sessions, examining precision at low context usage and recall at high usage, not a public benchmark. | Author report | [Results documentation](https://github.com/kunchenguid/compact-adviser/blob/17e441a81e9dbacfef15756b7d0cca66461a9b98/README.md) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101032677940117875) | Snapshot at the recorded time, not a live count |

**Documentation review:** Read the [pinned documentation](https://github.com/kunchenguid/compact-adviser/blob/17e441a81e9dbacfef15756b7d0cca66461a9b98/README.md). Implementation descriptions above come from documentation, not installation, execution or independent reproduction.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/kunchenguid/compact-adviser)
- [Project / demo link 2](https://github.com/kunchenguid/compact-adviser/blob/17e441a81e9dbacfef15756b7d0cca66461a9b98/README.md)

## Mechanism and comparison

The private labeled evaluation is unavailable for independent validation. Conversation excerpts reach the service; best-effort redaction is not a complete guarantee.

See the [category analysis](../../breakdowns/2026-09-18-memory.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
