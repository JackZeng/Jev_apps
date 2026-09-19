# Jailbreak prompt prescreen

[简体中文](README.md) | **English**

> Prescreen prompts for attempts to bypass an AI system's rules.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟡 B · Effectiveness unverified**<br>The author distinguishes an initial comparison from a future near-perfect target. Current evidence is limited and does not establish robustness to unseen attacks.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#jailbreak-screen) · 2026-09-19 11:30:00 Beijing time

## How it works, in plain English

Jev checks whether a prompt resembles known bypass patterns. It is an initial screen and may miss unfamiliar forms.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@mayfer](https://x.com/mayfer) |
| Main post | [Source post](https://x.com/mayfer/status/2100343452865265747) |
| Published (UTC) | 2026-09-16T21:57:56+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-19 16:55:36 |
| Main-post likes snapshot | **264** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:25.158271+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100343452865265747); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSXq9mqbsAAtHoT.jpg?name=orig" width="640" alt="Jailbreak prompt prescreen preview">](https://x.com/mayfer/status/2100343452865265747)<br>[Image](https://x.com/mayfer/status/2100343452865265747)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Original image 1](https://pbs.twimg.com/media/HSXq9mqbsAAtHoT.jpg?name=orig)

Media source: [original publishing page](https://x.com/mayfer/status/2100343452865265747). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Prescreen prompts for attempts to bypass an AI system's rules.

**Useful aspect (analysis):** A low-cost classifier could be a first stage in a broader security workflow.

## Inputs, steps and outputs

Prompt → jailbreak-pattern judgment → upstream prescreening; full rules are not published.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shows an initial comparison and claims an advantage over Luna, without a reusable test set. | Author report | [Post and attached media](https://x.com/mayfer/status/2100343452865265747) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100343452865265747) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

No separately verified project entry point recorded from the post; the thread may provide further leads.

## Mechanism and comparison

Explicitly an early attempt. Approaching 100% is an aspiration, not an achieved result.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
