# Codex Model Router: choose a model each turn

[简体中文](README.md) | **English**

> Select a model and reasoning settings for each Codex task.

**Added to README:** 2026-09-19 07:04:48<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>The inspectable routing infrastructure and candid user report support the bounded integration claim. Replay savings do not prove live cost or equal-quality gains for this user.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#codex-model-router) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Like assigning easy tickets to a lighter assistant and difficult ones to a stronger one: Jev classifies and a proxy applies routing policy.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@antonioleivag](https://x.com/antonioleivag) |
| Main post | [Source post](https://x.com/antonioleivag/status/2100962426439000484) |
| Published (UTC) | 2026-09-18T14:57:31+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-19 07:04:48 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **437** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T22:49:18+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100962426439000484); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSgeLlIX0AAjedL.png?name=orig" width="640" alt="Codex Model Router: choose a model each turn preview">](https://x.com/antonioleivag/status/2100962426439000484)<br>[Image](https://x.com/antonioleivag/status/2100962426439000484)

The main screenshot, repository and tuning gist are one case.

- [Original image 1](https://pbs.twimg.com/media/HSgeLlIX0AAjedL.png?name=orig)

Media source: [original publishing page](https://x.com/antonioleivag/status/2100962426439000484). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Select a model and reasoning settings for each Codex task.

**Useful aspect (analysis):** Embeds routing specifically in Codex with documented policies. The user report also exposes excessive routing to a stronger model.

## Inputs, steps and outputs

The linked pinned repository classifies turns through a local proxy and selects Luna, Sol or Astra plus reasoning settings. Low confidence defaults to a middle tier, with error fallback.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author reports initial over-routing to Sol even for easy tasks, then prompt adjustments, without a full personal-workflow quality/cost comparison. | Author report | [Post and attached media](https://x.com/antonioleivag/status/2100962426439000484) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100962426439000484) | Snapshot at the recorded time, not a live count |

**Documentation review:** Read the [pinned documentation](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/README.md). Implementation descriptions above come from documentation, not installation, execution or independent reproduction.

Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/0xNatoshi/jev-codex-router)
- [Project / demo link 2](https://github.com/0xNatoshi/jev-codex-router/blob/8292b519659280884627a962c826ac7721136a64/README.md)
- [Project / demo link 3](https://gist.github.com/antoniolg/62f82f2a5d191fe074e3f5065501993d)

## Mechanism and comparison

Prompt tuning is ongoing; cache benefits and context effects remain uncertain. Repository replay savings are not this user’s measured savings.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
