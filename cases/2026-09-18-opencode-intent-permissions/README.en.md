# OpenCode intent-aware permissions

[简体中文](README.md) | **English**

> Check an agent’s actions across tools using policies such as “only access Google.”

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The every-route wording refers to the demonstrated attempts, so B rather than C. Published docs explicitly expose a Code Mode bypass and preserve native permission controls; the demo is not a universal network boundary.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#opencode-intent-permissions)

## How it works, in plain English

Like a gatekeeper considering both access rules and the purpose of a request: Jev judges tool-input intent, and the plugin allows, asks or denies. Native OpenCode permissions remain the outer layer.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@OpeOginni](https://x.com/OpeOginni) |
| Main post | [Source post](https://x.com/OpeOginni/status/2100702649834188855) |
| Published (UTC) | 2026-09-17T21:45:15+00:00 |
| Main-post likes snapshot | **235** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T06:07:34+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100702649834188855); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2100701224920129536/img/-vzxHYoZxMjXKOKh.jpg" width="640" alt="OpenCode intent-aware permissions preview">](https://x.com/OpeOginni/status/2100702649834188855)<br>[Video](https://x.com/OpeOginni/status/2100702649834188855)

The main post includes a roughly 91-second video and configuration image. Eligibility uses the author’s post, without adding repost likes.

- [Direct video 1](https://video.twimg.com/amplify_video/2100701224920129536/vid/avc1/1112x720/ghw0VjLAOMM6qB14.mp4?tag=14) (metadata duration: 90.6s)
- [Original image 2](https://pbs.twimg.com/media/HScw-Q-XEAA2AMF.jpg?name=orig)

Media source: [original publishing page](https://x.com/OpeOginni/status/2100702649834188855). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Check an agent’s actions across tools using policies such as “only access Google.”

**Useful aspect (analysis):** Expresses a shared semantic restriction across shell, webfetch and other tools without enumerating every command. Goes beyond risk scoring by participating in permission decisions.

## Inputs, steps and outputs

The oc-auto-perms 0.1.0 documentation sends selected tool inputs, policies and recent requests to Jev, using ordered rules for allow/ask/deny. Low confidence or API failure becomes ask. Native deny stays denied and native ask still prompts; Jev further restricts native allow.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author demonstrates a Google-only policy and reports blocking the shown attempts; the main post now has 235 likes at retrieval. | Author report | [Post and attached media](https://x.com/OpeOginni/status/2100702649834188855) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100702649834188855) | Snapshot at the recorded time, not a live count |

**Promoted from the inbox:** The 2026-09-18 02:38:04 UTC snapshot had 160 likes; the 06:07:34 UTC snapshot has 235 and now qualifies. The [author’s reply](https://x.com/OpeOginni/status/2100705405013754312) links the package. Read [npm metadata and README](https://registry.npmjs.org/oc-auto-perms), whose latest version was 0.1.0. The plugin was not installed.

Updates and deduplicated supporting sources:

- [Supporting post by @OpeOginni](https://x.com/OpeOginni/status/2100705405013754312): published 2026-09-17T21:56:12+00:00; 5 likes retrieved 2026-09-18T06:11:15+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100705405013754312).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://www.npmjs.com/package/oc-auto-perms)
- [Project / demo link 2](https://github.com/OpeOginni/oc-plugins/tree/main/packages/oc-auto-perms)

## Mechanism and comparison

The video does not establish bypass resistance; deterministic hard boundaries remain necessary. Version 0.1.0 explicitly excludes Code Mode execute and sends policies, recent user messages and tool inputs to TypeSafe. No adversarial or permission tests were run here.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
