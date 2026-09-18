# Contributing

[简体中文](CONTRIBUTING.md) | **English**

## 1. Check eligibility

The current focus is **TypeSafe Jev** applications on X. A formal entry needs:

- A main post demonstrating the application with **at least 200 likes at retrieval**.
- The original author, post URL, publication time and metric-retrieval time.
- A concrete use case and public implementation details, with unknowns labeled explicitly.
- A corresponding image or video, previewed and linked from the README.

Ideas, unrelated namesakes, news reposts and leads without media go to the [inbox](inbox/README.en.md). Do not add likes across posts. Supporting updates can have fewer than 200 likes but cannot establish eligibility.

## 2. Deduplicate and categorize

Check post ID, author, project name and repository URL. Put updates and reposts in the existing entry's `supplementary_posts`. Independent implementations of the same game or problem can remain separate, but should be grouped and compared.

Assign one main category per case. Do not count multi-purpose projects several times. See the [11 categories](docs/taxonomy.en.md); a category with one entry must acknowledge the lack of a same-category comparison.

## 3. Write for readers, in both languages

Begin with what the application helps someone do. Use a concrete example, then explain which job Jev handles and which jobs belong to other code or models. Define necessary jargon. Analogies should clarify responsibilities without implying capabilities that the sources do not establish.

For each case, maintain both `summary` (what it does) and `plain_explanation` (how it works in everyday language), followed by the more technical `mechanism`. Unknown implementation details must stay unknown in both languages.

`data/catalog.json` contains Chinese editorial text and shared evidence. `data/catalog.en.json` contains English editorial translations keyed by case slug and group ID. Authors, post URLs, likes, dates and media are read from the shared catalog; do not duplicate them into the translation file.

`scripts/build_catalog.py` generates both homepages, case pages, indexes and comparisons. Do not edit generated Markdown alone: regeneration will overwrite it. Add or update the same cases and groups in both data files. Missing translations or extra/missing fields fail validation; this checks completeness, not translation accuracy.

Every case requires timezone-aware ISO 8601 `readme_added_at` and `readme_updated_at` values in the shared catalog. Set both when first adding it to README. For subsequent changes to its introduction, mechanism, evidence or either language, update only `readme_updated_at`. Both languages display Beijing time. Formatting, regeneration and timestamp backfills do not advance content timestamps; post publication, metric retrieval and the catalog-wide review time are separate. [Historical provenance](references/README.en.md#readme-times)

Use the [case template](templates/case.en.md) as a completeness guide. Record the summary, plain-language explanation, inputs/outputs, advantages, limitations, author-reported results, snapshots, media and project links. Group records hold selection advice, common workflows, analysis and proposed experiments.

- `post.likes` must be an observed value; `retrieved_at` must be the actual retrieval time with timezone.
- `post.media_source` identifies the post that owns the media. For quoted media, identify its original source and explain the date and use.
- Do not store complete posts, credentials or private account data in the public catalog.
- Separate author reports from analysis. Do not infer undocumented mechanisms as facts or mark unrun applications as reproduced.

```sh
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
git diff --check
```

The script is offline and checks eligibility, unique main posts, media, timezones, translation completeness and generated-file synchronization. It does not establish external availability or truth of author claims. Review source posts, media, relative links and comparisons separately.

## 4. Analysis and reproduction

Keep shared mechanisms in category analyses. Use the [analysis template](templates/breakdown.en.md) for deeper notes. Add new notes to both language indexes in the generator so regeneration preserves their entries.

Before recording a real reproduction, extend the catalog and renderer with reproduction details, or link a separate experiment note from the case. Do not merely change `verification` while leaving boilerplate saying no experiment was run. Record version, environment, inputs, success criteria, full cost, timing and errors before changing status.

Official documentation, author self-tests, viewing a demo and independent reproduction are different evidence levels. Include preprocessing, fallback, retries and executors in cost comparisons; distinguish per-decision latency from full-task time.

Cross-day publishing: case directories use the Beijing date of `readme_added_at`. Keep `collected_on` as the original collection/category-path date to preserve existing URLs. Add an actual source-review event to `updates` and mirror its last entry in `latest_update`; only cases named in an event advance their source-review date. Translation-only edits advance content time without inventing a source review. Check date/path behavior with `python3 -m unittest discover -s scripts -p 'test_*.py'`.

When a reported result comes from documentation instead of the main post, set the shared `reported_result_source` URL so the evidence table links directly to it.

## 5. Media and maintenance

Prefer links to original posts and media URLs; rights remain with creators. For small files you have permission to publish, follow the [asset policy](assets/README.en.md) and add `SOURCES.md`. Do not commit large videos or private raw material.

Preserve the original snapshot when likes decline, a post disappears or an application stops working. Add actual review findings without inventing new retrieval timestamps. Keep private research in ignored `local/` and inspect staged files before committing.
