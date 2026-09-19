# Needs-driven NPCs

[简体中文](README.md) | **English**

> Let game characters choose objects or activities that meet their needs.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The needs-to-tool selection mechanism is plausible and the author acknowledges existing rule-based alternatives. Improved behavior or long-term coherence has not been measured.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#npc-needs)

## How it works, in plain English

Give Jev a character's needs and available options, then execute its choice in the game. The model decides what to do; movement, animation and rules remain in game code.

[Back to catalog](../../README.en.md#simulation) · [Compare similar examples](../../breakdowns/2026-09-18-simulation.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | NPCs, driving and population simulations |
| Platform / author | X / [@m_iraji](https://x.com/m_iraji) |
| Main post | [Source post](https://x.com/m_iraji/status/2100394212743159944) |
| Published (UTC) | 2026-09-17T01:19:38+00:00 |
| Main-post likes snapshot | **201** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:28.761907+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100394212743159944); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100394190643355648/img/52O-mJZSxj4IGHos.jpg" width="640" alt="Needs-driven NPCs preview">](https://x.com/m_iraji/status/2100394212743159944)<br>[Video](https://x.com/m_iraji/status/2100394212743159944)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Direct video 1](https://video.twimg.com/amplify_video/2100394190643355648/vid/avc1/720x772/1by7xrrorWfBV9Gr.mp4?tag=29) (metadata duration: 16.6s)

Media source: [original publishing page](https://x.com/m_iraji/status/2100394212743159944). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Let game characters choose objects or activities that meet their needs.

**Useful aspect (analysis):** Semantic descriptions could extend behavior in utility-AI / smart-object scenarios.

## Inputs, steps and outputs

NPC needs and available objects → Jev choice → character action.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shows a game prototype built with Claude and driven by Jev decisions. | Author report | [Post and attached media](https://x.com/m_iraji/status/2100394212743159944) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100394212743159944) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Need weighting, conflicts and long-term consistency are unspecified; traditional rules may be simpler and cheaper.

See the [category analysis](../../breakdowns/2026-09-18-simulation.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
