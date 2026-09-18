# Sources, search method and snapshots

[简体中文](README.md) | **English**

Collection date: **2026-09-18, Asia/Shanghai**. The scope is concrete applications, prototypes, implementation demos and task-specific experiments using **TypeSafe Jev** on X.

## Official references

| Reference | Purpose |
| --- | --- |
| [TypeSafe](https://typesafe.ai) | Product identity and official entry point |
| [Introduction](https://docs.typesafe.ai/introduction) | Decision-model positioning |
| [Primitives](https://docs.typesafe.ai/primitives) | Choice, Score, Noul and batched questions |
| [Confidence](https://docs.typesafe.ai/confidence) | Probability, confidence and application thresholds |
| [Patterns](https://docs.typesafe.ai/patterns) | Composition and routing patterns |

Namesake accounts, unrelated products and local models imitating Jev's interface are not counted as TypeSafe Jev cases.

## Search method and coverage

1. Public web search provided leads; logged-in X search used `Jev min_faves:200 since:2026-09-14` and recent results.
2. Author searches and quote chains helped locate originals and exclude opinions, news reposts, ideas and unrelated names.
3. For concrete applications, the main post, author, publication time, media and likes were reviewed. Same-project updates and reposts were merged.
4. Public metadata from `https://api.fxtwitter.com/status/<post-id>` provided exact counts and media addresses. This is a third-party mirror, not the official X API, and may cache, lag or omit data.
5. The initial 67 cases each have a main-post snapshot of at least 200 likes and corresponding media. Leads needing further evidence remain in the [inbox](../inbox/README.en.md).

This covers a batch from the launch period through collection, not a full export of X. Ranking, indexing, visibility, wording and language affect coverage. Exhaustiveness is not claimed, and no automatic monitoring has been set up.

## Inspecting the evidence

[data/catalog.json](../data/catalog.json) is the shared source catalog and minimum evidence snapshot:

- `post.id`, `post.url`, `post.author`: main post and original author.
- `post.published_at`: publication time in UTC.
- `post.likes`, `post.retrieved_at`: API-reported count and retrieval time in UTC.
- `post.metrics_source`: retrieval endpoint.
- `post.media_source`, `post.media`: owning post, image/video URLs, thumbnail and duration where available.
- `supplementary_posts`: supporting posts; likes are not added and these posts need not meet the main-post threshold.
- `reported_result`: an original paraphrase of the author's report; `advantage` and `limitation`: analysis based on public information.

[data/catalog.en.json](../data/catalog.en.json) translates editorial text only. Both languages use the same underlying evidence, counts and media. Translation does not constitute a new source review or metric refresh.

Each source is linked in the [full catalog](../README.en.md) and [case records](../cases/README.en.md). Full social posts and personal account profiles are not republished; the repository retains necessary public metadata and original summaries.

## Media and verification boundaries

Previews are source photos or video covers. A photo may show code or an author's results rather than a running application. Skillbox uses a quoted earlier product-introduction image because the newer Jev integration post has no new image; the record makes that distinction explicit.

Media remains externally hosted. Clicking a preview opens its X source; detail pages also preserve direct URLs. CDN and video addresses can change, and GitHub's image proxy can cache content. Original-post links provide a recovery path. Rights remain with the creators.

Public descriptions and media metadata have been reviewed; the applications have not been individually run. Reading a post is not reproduction. README numbers are not independent benchmarks, and application availability still requires a runtime check.

## Latest incremental review

The second pass on 2026-09-18 adds 5 cases and supplements 4 existing entries, for 72 total at the end of that pass. See the [update log](../CHANGELOG.en.md) for search scope, main-post eligibility, merge decisions and exclusions. Original main-post retrieval times are unchanged; an incremental review does not imply every source was checked again.

## Third pass and tutorial reference

2026-09-18 06:12 UTC: 5 new cases and 1 existing entry supplemented, for 77 current cases. The permissions plugin moved from the inbox after its main post qualified. See the [third-pass update](../CHANGELOG.en.md).

[Sydney Runkle: Building a Harness with Jev](https://x.com/sydneyrunkle/status/2100754364545761643) explains LangChain classification calls, model routing and tool-risk gating. The main-post snapshot was 855 likes (2026-09-18T06:09:05+00:00 (UTC), FxTwitter). The article and its quotes are one tutorial reference, not multiple applications or an independent performance benchmark.

<a id="readme-times"></a>

## README entry timestamps

Each project has `readme_added_at` for its first addition to this repository’s README and `readme_updated_at` for its latest introduction, mechanism, evidence or bilingual-text edit. Both languages share the project timeline and display Beijing time (UTC+08:00), to the second. These values are separate from post publication and metric retrieval.

The existing 77 entries were backfilled from Git content commits:

| Commit time (Beijing) | Content |
| --- | --- |
| [2026-09-18 06:58:16 · 7bb2c99](https://github.com/JackZeng/Jev_apps/commit/7bb2c9996dd412a98fff99229c2f3e2403c439be) | First 67 projects added to README |
| [2026-09-18 07:24:03 · 9f5db32](https://github.com/JackZeng/Jev_apps/commit/9f5db320122e196c38fe2e84f578e47baeab7fc5) | Bilingual introductions and plain-language mechanisms updated |
| [2026-09-18 10:50:59 · f5eb3ab](https://github.com/JackZeng/Jev_apps/commit/f5eb3ab775f853ac3e0f1e8bc44258fcd57f3805) | Five additions and four supplemented cases |
| [2026-09-18 14:17:58 · e2f80f9](https://github.com/JackZeng/Jev_apps/commit/e2f80f933bc7f74701af518440b720ec0b4ed70a) | Five additions and a Cua update |

Backfills use the timestamps of commits containing the content, comparing each case’s shared and English editorial data. Category-only edits and generic formatting do not make every project in the group “newly updated.” Adding these timestamp fields also preserves existing content times. Future edits should record actual times under the [contribution workflow](../CONTRIBUTING.en.md); generation only renders the values and never replaces them with the current clock.
