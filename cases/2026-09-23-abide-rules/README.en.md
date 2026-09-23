# Abide: check project rules after code changes

[简体中文](README.md) | **English**

> Check changes against project instructions and return suspected violations to the coding agent.

**Content updated:** 2026-09-23 12:45:07 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>A covers code and transparent measurements. Catch-and-fix-everything wording is unsupported; thresholds require project calibration.<br>[Assessment and sources](../../references/2026-09-23-expanded-audit.en.md#abide-rules)

## How it works, in plain English

A reviewer consults team agreements after each edit and points out possible departures.

[Back to catalog](../../README.en.md#review) · [Compare similar examples](../../breakdowns/2026-09-18-review.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Code quality and safety checks |
| Platform / author | X / [@OhansEmmanuel](https://x.com/OhansEmmanuel) |
| Main post | [Source post](https://x.com/OhansEmmanuel/status/2101034822760288452) |
| Published (UTC) | 2026-09-18T19:45:11+00:00 |
| Main-post likes snapshot | **921** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-23T04:32:32+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2101034822760288452); may be cached |
| Last source review | 2026-09-23; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/amplify_video_thumb/2101034808826851328/img/I9qffLGFLpK0-4Tn.jpg" width="640" alt="Abide: check project rules after code changes preview">](https://x.com/OhansEmmanuel/status/2101034822760288452)<br>[Video](https://x.com/OhansEmmanuel/status/2101034822760288452)

Media belongs to the original post; snapshots and supporting evidence are below. Reposts and related updates are not extra applications.

- [Direct video 1](https://video.twimg.com/amplify_video/2101034808826851328/vid/avc1/1080x1080/geHO2dNn7R866i7M.mp4?tag=16) (metadata duration: 12.5s)

Media source: [original publishing page](https://x.com/OhansEmmanuel/status/2101034822760288452). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Check changes against project instructions and return suspected violations to the coding agent.

**Useful aspect (analysis):** Expresses semantic rules such as avoiding premature abstractions and publishes false-positive analysis.

## Inputs, steps and outputs

Compile instructions into rules, then send rules and diffs to Jev after edits or turns. Probability bands control feedback; missing network/key lets edits through with a recorded miss.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| In 93 replayed sessions, 10/39 edit flags and 11/15 turn flags were confirmed. A 300ms model call is not complete hook latency. | Author report | [Results documentation](https://github.com/coldteadotai/abide/blob/f2683828965ced03da07abae811e78af0383040c/benchmarks/replay/README.md) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2101034822760288452) | Snapshot at the recorded time, not a live count |



Updates and deduplicated supporting sources:

None.

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/coldteadotai/abide/blob/f2683828965ced03da07abae811e78af0383040c/README.md)
- [Project / demo link 2](https://github.com/coldteadotai/abide/blob/f2683828965ced03da07abae811e78af0383040c/packages/cli/src/lib/jev.ts)
- [Project / demo link 3](https://github.com/coldteadotai/abide/blob/f2683828965ced03da07abae811e78af0383040c/benchmarks/replay/README.md)

## Mechanism and comparison

Replay does not test successful repair. The second reviewer is Claude, not an independent human study. Edit-level false positives are substantial.

See the [category analysis](../../breakdowns/2026-09-18-review.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-23 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
