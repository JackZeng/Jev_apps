# Claude Code Mod: model and effort routing

[简体中文](README.md) | **English**

> Choose subagent models and adjust reasoning effort in the main conversation.

**Content updated:** 2026-09-19 17:48:49 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>Pinned source exposes hooks, defaults and fallback. Main-model behavior differs from the post’s description; savings remain unverified.<br>[Assessment and sources](../../references/2026-09-19-increment7-audit.en.md#claude-code-jev-router)

## How it works, in plain English

Like ticket triage: Jev judges task difficulty and the plugin assigns an assistant; the selected model still writes the code.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@dani_avila7](https://x.com/dani_avila7) |
| Main post | [Source post](https://x.com/dani_avila7/status/2101176629745561686) |
| Published (UTC) | 2026-09-19T05:08:41+00:00 |
| Main-post likes snapshot | **417** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-19T09:41:40+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101176629745561686); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101176234411425792/img/UgEWGdQPunczzXcv.jpg" width="640" alt="Claude Code Mod: model and effort routing preview">](https://x.com/dani_avila7/status/2101176629745561686)<br>[Video](https://x.com/dani_avila7/status/2101176629745561686)

Same purpose as the Codex router but a distinct repository, host, author and video; grouped as an independent implementation.

- [Direct video 1](https://video.twimg.com/amplify_video/2101176234411425792/vid/avc1/2278x1632/cdyZyiAMhglYXq-s.mp4?tag=29) (metadata duration: 25.1s)

Media source: [original publishing page](https://x.com/dani_avila7/status/2101176629745561686). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Choose subagent models and adjust reasoning effort in the main conversation.

**Useful aspect (analysis):** Unlike the Codex router, this uses Claude Code hooks and separates main-session and subagent decisions, making cache and fallback policies inspectable.

## Inputs, steps and outputs

Pinned code classifies at prompt submission and applies decisions at model requests and subagent creation. Subagent-model and main-effort routing default on; main-model switching defaults off. This differs from the post’s session-start-only description; the pinned implementation takes precedence.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The post includes a roughly 25-second video; source supports TypeSafe or Vercel Gateway. It establishes a routing mechanism, not cheaper equivalent-quality completion. | Author report | [Post and attached media](https://x.com/dani_avila7/status/2101176629745561686) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101176629745561686) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/README.md)
- [Project / demo link 2](https://github.com/davila7/claude-code-templates/blob/61bfcd1586bf1076f6d3cfa0436317c912811e6c/cli-tool/components/mods/productivity/jev-model-router/hooks/jev-model-router.ts)

## Mechanism and comparison

No complete quality, cache-cost or savings comparison. Without a Jev key, the host classifier is used, so that path is not evidence of Jev performance.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-19 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
