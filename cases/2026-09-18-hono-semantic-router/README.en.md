# Hono JevRouter: route requests by meaning

[简体中文](README.md) | **English**

> Choose responses such as HTML or Markdown based on whether a request appears to come from a person or an AI.

**Content updated:** 2026-09-19 16:55:36 (Beijing time, UTC+08:00)

**🟢 A · Clearer evidence for function/mechanism**<br>The source directly supports first-matching semantic routing and explicitly states its limits. It is an inspectable routing experiment, not an authentication guarantee.<br>[Assessment and sources](../../references/2026-09-19-claims-audit.en.md#hono-semantic-router)

## How it works, in plain English

Ordinary routing sorts letters by address; this experiment also considers their meaning. Developers describe handlers in words, Jev judges each description, and code selects the first qualifying handler in registration order.

[Back to catalog](../../README.en.md#routing) · [Compare similar examples](../../breakdowns/2026-09-18-routing.en.md)

## Record

| Field | Value |
| --- | --- |
| Category | Model, skill and tool routing |
| Platform / author | X / [@yusukebe](https://x.com/yusukebe) |
| Main post | [Source post](https://x.com/yusukebe/status/2100871075743859182) |
| Published (UTC) | 2026-09-18T08:54:31+00:00 |
| Main-post likes snapshot | **405** (threshold ≥ 200) |
| Metrics/media retrieved (UTC) | 2026-09-18T11:39:03+00:00 |
| Metadata source | [Public FxTwitter API](https://api.fxtwitter.com/status/2100871075743859182); may be cached |
| Last source review | 2026-09-19; public descriptions and metadata reviewed, application not run |
| Jev version | Unspecified in the post; unknown |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

[<img src="https://pbs.twimg.com/media/HSfKgItbcAAwVIl.jpg?name=orig" width="640" alt="Hono JevRouter: route requests by meaning preview">](https://x.com/yusukebe/status/2100871075743859182)<br>[Image](https://x.com/yusukebe/status/2100871075743859182)

The source image shows usage code, not a performance benchmark. An author reply directly links the repository.

- [Original image 1](https://pbs.twimg.com/media/HSfKgItbcAAwVIl.jpg?name=orig)

Media source: [original publishing page](https://x.com/yusukebe/status/2100871075743859182). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

Choose responses such as HTML or Markdown based on whether a request appears to come from a person or an AI.

**Useful aspect (analysis):** Explores intent-sensitive responses alongside ordinary Hono routing. Unlike model routing, it chooses HTTP handlers, making the resulting behavior easier to inspect.

## Inputs, steps and outputs

Pinned code builds state from the method, URL, headers and a truncated textual body, then asks one Noul question per route in a single call. The first registered route reaching the threshold wins (default 0.5), not the highest-scoring route. Ordinary path handlers can respond first; no semantic match falls through to not-found handling.

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| The author shares a usage-code image, playground and open-source package. The example serves Markdown to AI requests and HTML to human browsers. The latest npm version during this review was 0.2.0; it was not installed or tested. | Author report | [Post and attached media](https://x.com/yusukebe/status/2100871075743859182) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint](https://api.fxtwitter.com/status/2100871075743859182) | Snapshot at the recorded time, not a live count |

**Source review:** Read the [README at 04f6e10](https://github.com/yusukebe/hono-jev-router/blob/04f6e103e1397bca659ab85c042011a1f14b679d/README.md) and [src/index.ts](https://github.com/yusukebe/hono-jev-router/blob/04f6e103e1397bca659ab85c042011a1f14b679d/src/index.ts). Route probabilities are independent and need not sum to one; these are multiple yes/no judgments, not mutually exclusive classification. No playground request was submitted.

Updates and deduplicated supporting sources:

- [Supporting post by @yusukebe](https://x.com/yusukebe/status/2100874801850319016): published 2026-09-18T09:09:19+00:00; 7 likes retrieved 2026-09-18T11:41:51+00:00. Supporting source only; not counted toward the threshold. [Metadata source](https://api.fxtwitter.com/status/2100874801850319016).

Public project / demo links (a link does not mean availability has been tested here):

- [Project / demo link 1](https://github.com/yusukebe/hono-jev-router)
- [Project / demo link 2](https://hono-jev-router.yusuke.run)

## Mechanism and comparison

Explicitly experimental and unsuitable as an authentication or authorization boundary. Semantic routing adds model latency and cost. Request content is sent to Jev; only specified sensitive headers are redacted by default. Route order and adversarial input can affect outcomes.

See the [category analysis](../../breakdowns/2026-09-18-routing.en.md) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| 2026-09-18 | First collection; checked the main post, metric snapshot and media; added to category comparisons |
