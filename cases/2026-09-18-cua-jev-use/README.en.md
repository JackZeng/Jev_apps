# Cua · jev-use

[简体中文](README.md) | **English**

> Give Jev a list of allowed browser actions, execute its choice, then check the result.

**Added to README:** 2026-09-18 06:58:16<br>**Content updated:** 2026-09-18 14:17:58 (Beijing time, UTC+08:00)

## How it works, in plain English

Like ordering from a menu, Jev selects only an action ID prepared by the application. Code checks it, executes it and independently verifies the form. The current preview does not operate arbitrary software from screenshots.

[Back to catalog](../../README.en.md#browser) · [Compare similar examples](../../breakdowns/2026-09-18-browser.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Browser and computer control |
| Platform / author | X / [@trycua](https://x.com/trycua) |
| Main post | [Source post](https://x.com/trycua/status/2100649543079502213) |
| Published (UTC) | 2026-09-17T18:14:13+00:00 |
| Added to README / content updated (Beijing time) | 2026-09-18 06:58:16 / 2026-09-18 14:17:58 |
| Main-post likes snapshot | **1,162** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-17T22:42:22.751882+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100649543079502213); may be cached |
| Last source review | 2026-09-18; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSb_nmIWYAAkGKa.jpg?name=orig" width="640" alt="Cua · jev-use preview">](https://x.com/trycua/status/2100649543079502213)<br>[Image](https://x.com/trycua/status/2100649543079502213)

Image or video attached to the source post; the preview does not verify all implementation or performance claims.

- [Original image 1](https://pbs.twimg.com/media/HSb_nmIWYAAkGKa.jpg?name=orig)

Media source: [original publishing page](https://x.com/trycua/status/2100649543079502213). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Give Jev a list of allowed browser actions, execute its choice, then check the result.

**Useful aspect (analysis):** Local code owns and validates actions; the preview includes Python/TypeScript examples and independent outcome checks.

## Inputs, steps and outputs

PR #3916 describes DOM/semantic observations, locally constructed complete action candidates, Jev selecting a candidate ID, local validation, Driver execution and an independent state endpoint checking the result.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The post advertises a macOS/Windows/Linux development preview and mentions #3943. Repository review identified #3916 as the semantic jev-use preview, still unmerged at collection. | Author report | [Post and attached media](https://x.com/trycua/status/2100649543079502213) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100649543079502213) | Snapshot at the recorded time, not a live count |

**Repository cross-check (2026-09-18)**: [PR #3916](https://github.com/trycua/cua/pull/3916) describes DOM/semantic evidence and Jev selecting actions outside Driver. Mock E2E CI is not live Jev certification across platforms. [PR #3943, mentioned in the post](https://github.com/trycua/cua/pull/3943), has been narrowed to an unwired perception-foundations draft and should not be treated as an available screenshot-perception feature. These are repository statements, not tests run here.

**Third-pass review (2026-09-18 06:12 UTC):** [Teknium’s quote](https://x.com/Teknium/status/2100783833419505941) announces testing planned for the next few weeks, not results; it is merged into the existing Cua case. GitHub API checks show #3916 still open and unmerged, and #3943 still an open, unmerged draft. This pass refreshes PR status only; planned testing is not treated as a shipped integration.

Updates and deduplicated supporting sources:

- [Supporting post by @Teknium](https://x.com/Teknium/status/2100783833419505941): published 2026-09-18T03:07:51+00:00; 652 likes retrieved 2026-09-18T06:08:49+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100783833419505941).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/trycua/cua/pull/3916)
- [Project / demo link 2](https://github.com/trycua/cua/pull/3943)

## Mechanism and comparison

Not a released visual desktop-control feature. The current preview has no screenshot perception and does not certify native Windows/Linux desktop capability.

See the [category analysis](../../breakdowns/2026-09-18-browser.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
| 2026-09-18T06:12:09+00:00 | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |
