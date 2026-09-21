# Reddit Radar MCP: filter discussions by your criteria

[简体中文](README.md) | **English**

> Find Reddit discussions matching custom criteria from Claude Code or Codex.

**Content updated:** 2026-09-21 11:02:26 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>A clear task and demo, with scale and business outcomes remaining author claims.<br>[Assessment and sources](../../references/2026-09-21-increment9-audit.en.md#reddit-radar-mcp)

## How it works, in plain English

A sorter collects posts, applies your criteria and returns matching discussions.

[Back to catalog](../../README.en.md#data) · [Compare similar examples](../../breakdowns/2026-09-18-data.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Data classification and organization |
| Platform / author | X / [@oguzhankayancom](https://x.com/oguzhankayancom) |
| Main post | [Source post](https://x.com/oguzhankayancom/status/2101667801274478707) |
| Published (UTC) | 2026-09-20T13:40:25+00:00 |
| Main-post likes snapshot | **295** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-21T02:47:23+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101667801274478707); may be cached |
| Last source review | 2026-09-21; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101667558847856640/img/ueDe_Ess6ATvRcz8.jpg" width="640" alt="Reddit Radar MCP: filter discussions by your criteria preview">](https://x.com/oguzhankayancom/status/2101667801274478707)<br>[Video](https://x.com/oguzhankayancom/status/2101667801274478707)

One original MCP product demo, not separate apps for each client.

- [Direct video 1](https://video.twimg.com/amplify_video/2101667558847856640/vid/avc1/1084x720/K4aOnA4wrNlmS5Lx.mp4?tag=29) (metadata duration: 13.0s)

Media source: [original publishing page](https://x.com/oguzhankayancom/status/2101667801274478707). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Find Reddit discussions matching custom criteria from Claude Code or Codex.

**Useful aspect (analysis):** Brings bulk filtering into existing assistants for exploring discussion topics.

## Inputs, steps and outputs

The author describes an MCP tool combining Reddit scanning with Jev classification. Coverage, deduplication, label definitions and source remain unestablished.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author claims tens of thousands of posts in minutes and shows a roughly 12-second clip; throughput and idea validation are unverified. | Author report | [Post and attached media](https://x.com/oguzhankayancom/status/2101667801274478707) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101667801274478707) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Public discussion alone does not validate demand. Precision, recall and full collection/inference costs are missing.

See the [category analysis](../../breakdowns/2026-09-18-data.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-21 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
