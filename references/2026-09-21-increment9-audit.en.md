# 2026-09-21 · Ninth incremental intake and evidence review

[简体中文](2026-09-21-increment9-audit.md) | **English**

Reviewed through **2026-09-21 11:02:26 Beijing time**. **10 new cases**, **2 merged updates**, **137 cases in 11 groups**. A 25 / B 96 / C 16. All remain **not independently reproduced**.

X Latest search used `Jev min_faves:200 since:2026-09-20`, overlapping the previous cutoff of September 20, 11:01:10 Beijing time. Original threads, pinned repositories and public resource pages were checked. AnimeAct is an older original discovered through a newer quote. X indexing is incomplete; this is not an exhaustive census.

Original-post likes and media come from per-post FxTwitter snapshots, which can be cached. Reply and quote likes are not added. The exact retrieval timestamps and channels are preserved. No third-party projects or paid model calls were run. A means clear implementation evidence, B a concrete prototype with unverified outcomes, and C central claims exceeding the evidence; none means independent reproduction.

## Deduplication decisions

| Lead | Treatment |
| --- | --- |
| DuckDB rewrite | Same extension; merge the new speed claim, whose baseline is the author’s old implementation. |
| Third Hand / arc-cua | Separate Swift/Python repositories by one author. arc-cua explicitly reuses the text-entry approach; group related work on one card without claiming identical code. |
| Minecraft | Separate author/repository from the existing hybrid controller; compare fixed-route priors and runtime roles. |
| Mario teacher data | Different author and architecture: Jev prepares training data and LightGBM runs gameplay. Reposted footage is not another case. |
| Toothless / CNVS | Similar activation task, independent authors and media: group for comparison. |
| Token / word / character loops | Independent experiments; compare candidate granularity rather than count reposts. |
| Jev Field Notes | Count its curation workflow once, not all demos embedded in the collection. |
| AnimeAct | Use the original author’s post; newer quotations do not create new apps. |

## Per-case evidence

<a id="docjev"></a>

### DocJev: classify documents and split bundles · A

Implementation and timing scope are clear. Equal accuracy and roughly sixfold speed claims need qualification: splitting differs and OCR is excluded.

Full mechanism, outcome boundaries and comparison: [DocJev: classify documents and split bundles](../cases/2026-09-21-docjev/README.en.md)。

Sources: [X @jerryjliu0](https://x.com/jerryjliu0/status/2101738281046294552)

Implementation / method: [README.md](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/README.md) · [jev.py](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/src/jev_docs/engines/jev.py) · [report.md](https://github.com/jerryjliu/docjev/blob/9ed0fe05984ce1906af9272b8b400c8d46520f98/benchmarks/results/real-small-v1-run01/report.md)

Main-post snapshot: **695 likes**, 2026-09-21T02:44:57+00:00; [snapshot source](https://api.fxtwitter.com/status/2101738281046294552).

<a id="dasheng-reading"></a>

### ReadAloud: check missing words and changed meaning · C

Inspectable implementation, but full-product replacement and fully offline wording exceed the implemented assessment and network behavior.

Full mechanism, outcome boundaries and comparison: [ReadAloud: check missing words and changed meaning](../cases/2026-09-21-dasheng-reading/README.en.md)。

Sources: [X @wquguru](https://x.com/wquguru/status/2101711235628810669)

Implementation / method: [README.md](https://github.com/wquguru/dasheng/blob/1bacff4a075527e6c02da242a72d117e7cb3286b/README.md) · [jev.js](https://github.com/wquguru/dasheng/blob/1bacff4a075527e6c02da242a72d117e7cb3286b/lib/jev.js) · [score.js](https://github.com/wquguru/dasheng/blob/1bacff4a075527e6c02da242a72d117e7cb3286b/lib/score.js)

Main-post snapshot: **351 likes**, 2026-09-21T02:45:24+00:00; [snapshot source](https://api.fxtwitter.com/status/2101711235628810669).

<a id="needle-semantic-find"></a>

### Needle: find webpage passages by meaning · A

Pinned code establishes extraction, relevance and sentence selection. A reflects clear implementation, not verified search completeness.

Full mechanism, outcome boundaries and comparison: [Needle: find webpage passages by meaning](../cases/2026-09-21-needle-semantic-find/README.en.md)。

Sources: [X @Saboo_Shubham_](https://x.com/Saboo_Shubham_/status/2101576462042366114) · [X @Saboo_Shubham_](https://x.com/Saboo_Shubham_/status/2101577105809240488)

Implementation / method: [README.md](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/9e860951aaf5c82801779e43e748dcf92042879a/advanced_llm_apps/needle/README.md) · [search.mjs](https://github.com/Shubhamsaboo/awesome-llm-apps/blob/9e860951aaf5c82801779e43e748dcf92042879a/advanced_llm_apps/needle/server/search.mjs)

Main-post snapshot: **1658 likes**, 2026-09-21T02:50:32+00:00; [snapshot source](https://api.fxtwitter.com/status/2101576462042366114).

<a id="reddit-radar-mcp"></a>

### Reddit Radar MCP: filter discussions by your criteria · B

A clear task and demo, with scale and business outcomes remaining author claims.

Full mechanism, outcome boundaries and comparison: [Reddit Radar MCP: filter discussions by your criteria](../cases/2026-09-21-reddit-radar-mcp/README.en.md)。

Sources: [X @oguzhankayancom](https://x.com/oguzhankayancom/status/2101667801274478707)

Main-post snapshot: **295 likes**, 2026-09-21T02:47:23+00:00; [snapshot source](https://api.fxtwitter.com/status/2101667801274478707).

<a id="toothless-voice-gate"></a>

### Toothless: decide whether speech addresses the assistant · B

Supports an activation-gate prototype; natural turn-taking and persistent reliability remain unverified.

Full mechanism, outcome boundaries and comparison: [Toothless: decide whether speech addresses the assistant](../cases/2026-09-21-toothless-voice-gate/README.en.md)。

Sources: [X @ashutoshpuro97](https://x.com/ashutoshpuro97/status/2101660362882085299)

Main-post snapshot: **266 likes**, 2026-09-21T02:48:14+00:00; [snapshot source](https://api.fxtwitter.com/status/2101660362882085299).

<a id="mario-lightgbm-teacher"></a>

### Mario teacher data: Jev demonstrates, LightGBM takes over · B

Teacher and runtime models are clearly distinguished, while generalization and reliable completion remain unverified.

Full mechanism, outcome boundaries and comparison: [Mario teacher data: Jev demonstrates, LightGBM takes over](../cases/2026-09-21-mario-lightgbm-teacher/README.en.md)。

Sources: [X @nwnwnyo](https://x.com/nwnwnyo/status/2101605150242849140)

Main-post snapshot: **945 likes**, 2026-09-21T02:49:26+00:00; [snapshot source](https://api.fxtwitter.com/status/2101605150242849140).

<a id="minecraft-fixed-route"></a>

### Minecraft fixed route: planning plus bounded actions · C

The WASD/mouse claim conflicts with documented structured-state, higher-level actions. Treat this as a bounded route experiment, not general autonomous completion.

Full mechanism, outcome boundaries and comparison: [Minecraft fixed route: planning plus bounded actions](../cases/2026-09-21-minecraft-fixed-route/README.en.md)。

Sources: [X @rronak_](https://x.com/rronak_/status/2101544156757950697) · [X @rronak_](https://x.com/rronak_/status/2101544158502728002)

Implementation / method: [README.md](https://github.com/rmalde/minecraft-agent/blob/78b40ed59514e5e2abde33a05ce398ecb2c39e05/README.md) · [config.json](https://github.com/rmalde/minecraft-agent/blob/78b40ed59514e5e2abde33a05ce398ecb2c39e05/optimization/nether/config.json)

Main-post snapshot: **6861 likes**, 2026-09-21T02:51:31+00:00; [snapshot source](https://api.fxtwitter.com/status/2101544156757950697).

<a id="token-choice-loop"></a>

### Token-choice loop: assemble text through repeated decisions · B

A sourced loop and prototype, with text quality and efficiency still unverified.

Full mechanism, outcome boundaries and comparison: [Token-choice loop: assemble text through repeated decisions](../cases/2026-09-21-token-choice-loop/README.en.md)。

Sources: [X @erikdunteman](https://x.com/erikdunteman/status/2101533797527454109)

Main-post snapshot: **211 likes**, 2026-09-21T02:50:32+00:00; [snapshot source](https://api.fxtwitter.com/status/2101533797527454109).

<a id="jev-field-notes-curation"></a>

### Jev Field Notes: curate Jev examples with Jev · B

Supports an author-described curation prototype, not established completeness, deduplication or fact-checking capability.

Full mechanism, outcome boundaries and comparison: [Jev Field Notes: curate Jev examples with Jev](../cases/2026-09-21-jev-field-notes-curation/README.en.md)。

Sources: [X @omarsar0](https://x.com/omarsar0/status/2101696753749655863)

Implementation / method: [jev-field-notes](https://academy.dair.ai/resources/jev-field-notes)

Main-post snapshot: **298 likes**, 2026-09-21T02:45:54+00:00; [snapshot source](https://api.fxtwitter.com/status/2101696753749655863).

<a id="animeact-jev-demo"></a>

### AnimeAct: connect dialogue to character acting · B

A sourced integration demo, with exact interface and release availability unresolved. Future-dated product-page text is not evidence of a completed launch.

Full mechanism, outcome boundaries and comparison: [AnimeAct: connect dialogue to character acting](../cases/2026-09-21-animeact-jev-demo/README.en.md)。

Sources: [X @frombit_jp](https://x.com/frombit_jp/status/2101298040741253195)

Implementation / method: [8507737](https://frombit.booth.pm/items/8507737)

Main-post snapshot: **2014 likes**, 2026-09-21T02:50:32+00:00; [snapshot source](https://api.fxtwitter.com/status/2101298040741253195).

<a id="duckdb"></a>

### DuckDB semantic classification · B

The new figures describe software optimization of the same DuckDB integration. The author acknowledges the earlier inefficiency; no public matched benchmark, so B is retained and the update merged.

Full mechanism, outcome boundaries and comparison: [DuckDB semantic classification](../cases/2026-09-18-duckdb/README.en.md)。

Sources: [X @hamiltonulmer](https://x.com/hamiltonulmer/status/2100370557405667768) · [X @hamiltonulmer](https://x.com/hamiltonulmer/status/2101700765656264896)

Main-post snapshot: **1310 likes**, 2026-09-17T22:42:25.668728+00:00; [snapshot source](https://api.fxtwitter.com/status/2100370557405667768).

<a id="third-hand"></a>

### Third Hand / arc-cua: choose actions on a Mac · A

A concerns inspectable implementation roles. arc-cua explicitly reuses Third Hand’s text-entry approach and is grouped as related work. Solved computer use and universal speed gains lack benchmarks.

Full mechanism, outcome boundaries and comparison: [Third Hand / arc-cua: choose actions on a Mac](../cases/2026-09-20-third-hand/README.en.md)。

Sources: [X @sxhivs](https://x.com/sxhivs/status/2101367048223982065) · [X @sxhivs](https://x.com/sxhivs/status/2101367050207981608) · [X @sxhivs](https://x.com/sxhivs/status/2101729362194432184) · [X @sxhivs](https://x.com/sxhivs/status/2101729364203475072)

Implementation / method: [README.md](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/README.md) · [TextEntryPlan.swift](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/TextEntryPlan.swift) · [JevClient.swift](https://github.com/shhivv/third-hand/blob/430394b35dbb44ff8b303bf19da29b0828d92bd2/Sources/ThirdHand/JevClient.swift) · [README.md](https://github.com/shhivv/arc-cua/blob/85fc321715e23f51c222d59d31461b75804ba4ac/README.md) · [typesafe.py](https://github.com/shhivv/arc-cua/blob/85fc321715e23f51c222d59d31461b75804ba4ac/src/arc_cua/policies/typesafe.py)

Main-post snapshot: **549 likes**, 2026-09-20T02:46:29+00:00; [snapshot source](https://api.fxtwitter.com/status/2101367048223982065).

## Status and scope

The [official September 21 announcement](https://x.com/typesafeai/status/2101786156572823624) says Jev no longer has a waitlist. This is access status, not a new application or proof that every listed tool works.

Ambiguous leads remain in the [inbox](../inbox/README.en.md), outside the formal count. Existing main-post snapshots and first-added times are preserved; only these 12 cases get new content-update times. Both languages retain the six highlights and 11 folded, two-column categories.
