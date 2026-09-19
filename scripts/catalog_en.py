"""English presentation; source metrics and media are shared with catalog.json."""
from collections import Counter
from catalog_reviews import review_line, review_legend
import html
from catalog_dates import readme_dates, format_readme_time, case_day, case_review_day, latest_review_day

CASE_FIELDS = {'title', 'summary', 'plain_explanation', 'mechanism', 'advantage', 'limitation', 'reported_result', 'media_note'}
GROUP_FIELDS = {'title', 'comparison', 'flow', 'analysis', 'evaluation'}


def validate_translations(d, en):
    assert set(en) == {'cases', 'groups'}, 'English catalog must contain only cases and groups'
    assert set(en['cases']) == {c['slug'] for c in d['cases']}, 'Missing or extra English cases'
    assert set(en['groups']) == {g['id'] for g in d['groups']}, 'Missing or extra English groups'
    for c in d['cases']:
        required = CASE_FIELDS | {k for k in ('source_notes', 'jev_version', 'review_summary') if k in c}
        t = en['cases'][c['slug']]
        assert set(t) == required, f'Translation fields differ: {c["slug"]}'
        assert all(isinstance(v, str) and v.strip() and '|' not in v for v in t.values()), c['slug']
    for g in d['groups']:
        t = en['groups'][g['id']]
        assert set(t) == GROUP_FIELDS, f'Translation fields differ: {g["id"]}'
        assert all(isinstance(v, str) and v.strip() and '|' not in v for v in t.values()), g['id']


def preview(c, width=160):
    p = c['post']
    m = p['media'][0]
    url = m.get('thumbnail_url') or m['url']
    label = 'Video' if m['type'] in ('video', 'gif') else 'Image'
    return f'[<img src="{html.escape(url, quote=True)}" width="{width}" alt="{html.escape(c["title"], quote=True)} preview">]({p["media_source"]})<br>[{label}]({p["media_source"]})'


def generate_en(d, en):
    date = d['collected_on']
    cases = [{**c, **en['cases'][c['slug']]} for c in d['cases']]
    groups = [{**g, **en['groups'][g['id']]} for g in d['groups']]
    counts = Counter(c['group'] for c in cases)
    files = {}
    update = d.get('latest_update')
    update_notice = (f"Latest incremental source review: **{update['reviewed_at']} (UTC)**; **{len(update['new_cases'])} new cases**, **{len(update['updated_cases'])} existing entries updated**. [Additions, merges and exclusions](CHANGELOG.en.md). Existing main-post metric snapshots retain their original retrieval times.\n\n" if update else '')
    readme = [f'''# Jev Apps: Examples and How They Work

A bilingual field guide to **TypeSafe Jev** applications found on X: what they do, how they work, and the strengths and limits of similar approaches. **{len(cases)} examples · {len(groups)} categories · each main post had ≥ {d['minimum_likes']} likes when collected · every entry includes an image or video.**

{update_notice}## What is Jev, in plain English?

Think of Jev as a fast sorting assistant inside software. The application prepares the current situation and a set of questions or choices. Jev makes judgments, and code turns them into actions: label an email, choose an AI worker, or pick the next browser button. Larger applications combine many such small decisions.

For example, a flight-search agent reads the webpage and lists available controls. Jev selects a next action, a browser tool executes it, and the loop repeats. Other components still handle observation, text generation when needed, and checking whether the task actually succeeded. [Official introduction](https://docs.typesafe.ai/introduction) · [Illustrated explanation](breakdowns/{date}-how-jev-apps-work.en.md)

**Collection updated: {latest_review_day(d)} (Asia/Shanghai).** This is a collection from that search, not an exhaustive inventory of X. All examples are **not independently reproduced**. Performance and cost figures are attributed to their authors; comparisons are analysis of public designs, not our own benchmarks.

## How to read this catalog

- **One qualifying main post:** at least 200 likes, an explicit TypeSafe Jev use case and concrete media. Updates and reposts are merged; likes are not added together.
- **Counts are snapshots:** discovery used X; exact metrics and media metadata were cross-checked through the public FxTwitter API, which may cache or lag. Each detail page records timestamps and sources. [Evidence method](references/README.en.md) · [Shared source data](data/catalog.json)
- **Clickable previews:** images come from source photos or video covers. Details retain original media URLs; links and CDN content can change. Skillbox explicitly uses an older quoted product image.
- **Similar examples stay together:** each group has guidance and a detailed strengths/limitations table. Entries are organized by use, not ranked by likes. Demonstration footage does not establish long-term reliability.
- **Dates beside each introduction:** first addition to README and the latest content update, both in **Beijing time (UTC+08:00)**. Post publication and metric retrieval times are recorded separately. [Timestamp provenance](references/README.en.md#readme-times)

{review_legend(cases, english=True)}## Categories

| Category | Examples | Comparison |
| --- | ---: | --- |
''']
    for g in groups:
        readme.append(f'| [{g["title"]}](#{g["id"]}) | {counts[g["id"]]} | [Read analysis](breakdowns/{date}-{g["id"]}.en.md) |\n')
    readme.append('\n[Case index](cases/README.en.md) · [All explanations](breakdowns/README.en.md) · [Pending evidence](inbox/README.en.md) · [Contributing](CONTRIBUTING.en.md)\n\n## All applications\n')
    index = ['# Case index\n\nAll examples are not independently reproduced. Likes are snapshots of individual main posts. Addition and content-update times use Beijing time (UTC+08:00). See the [homepage](../README.en.md) for previews and plain-language explanations.\n']
    breakdowns = [f'# Explanations and comparisons\n\nAnalysis of public sources; no reproduction experiments have been run here.\n\n- [How Jev apps work: judgments and software composition]({date}-how-jev-apps-work.en.md)\n']
    for g in groups:
        gid = g['id']
        cs = [c for c in cases if c['group'] == gid]
        bp = f'breakdowns/{date}-{gid}.en.md'
        readme.append(f'\n<a id="{gid}"></a>\n\n### {g["title"]} ({len(cs)})\n\n{g["comparison"]}\n\n[Detailed strengths, limitations and mechanisms]({bp})\n\n| Application and explanation | Main-post likes | Image / video |\n| --- | ---: | --- |\n')
        index.append(f'\n## {g["title"]}\n\n| Application | What it does | Main-post likes |\n| --- | --- | ---: |\n')
        breakdowns.append(f'- [{g["title"]}]({date}-{gid}.en.md): {len(cs)} examples.\n')
        b = [f'# {g["title"]}: how they work and compare\n\nFirst compiled: {date}; see each case for its source-review date. Status: **not independently reproduced**.\n\n## Choosing an approach\n\n{g["comparison"]}\n\n## Individual comparisons\n\nThese are analytical strengths and limitations based on public descriptions, not controlled experimental findings.\n\n| Example | Strengths / suitable uses | Limitations / missing evidence |\n| --- | --- | --- |\n']
        for c in cs:
            p = c['post']
            path = f'cases/{case_day(c)}-{c["slug"]}'
            readme.append(f'| [**{c["title"]}**]({path}/README.en.md)<br>{c["summary"]}<br>**How it works:** {c["plain_explanation"]}<br>{review_line(c, english=True)}<br>{readme_dates(c, english=True)} | [{p["likes"]:,}]({p["url"]}) | {preview(c)} |\n')
            index.append(f'| [{c["title"]}]({case_day(c)}-{c["slug"]}/README.en.md) | {c["summary"]}<br>{review_line(c, prefix="../", english=True)}<br>{readme_dates(c, english=True)} | [{p["likes"]:,}]({p["url"]}) |\n')
            b.append(f'| [{c["title"]}](../{path}/README.en.md) | {c["advantage"]} | {c["limitation"]} |\n')
            supplement = '\n'.join(f'- [Supporting post by @{s["author"]}]({s["url"]}): published {s["published_at"]}; {s["likes"]:,} likes retrieved {s["retrieved_at"]}. Supporting source only; not counted toward the threshold. [Metadata source]({s["metrics_source"]}).' + ''.join(f' [Supplementary media {i}]({m["url"]})' for i, m in enumerate(s.get('media', []), 1)) for s in c['supplementary_posts']) or 'None.'
            update_entry = ''.join(f"| {u['reviewed_at']} | Merged supporting sources and refined mechanism, evidence or tutorial notes; [deduplication record](../../CHANGELOG.en.md) |\n" for u in d.get('updates', [update] if update else []) if c['slug'] in u['updated_cases'])
            links = '\n'.join(f'- [Project / demo link {i}]({url})' for i, url in enumerate(c['links'], 1)) or 'No separately verified project entry point recorded from the post; the thread may provide further leads.'
            media = []
            for i, m in enumerate(p['media'], 1):
                label = 'Direct video' if m['type'] in ('video', 'gif') else 'Original image'
                media.append(f'- [{label} {i}]({m["url"]})' + (f' (metadata duration: {m["duration"]:.1f}s)' if m.get('duration') else ''))
            files[f'{path}/README.en.md'] = f'''# {c['title']}

> {c['summary']}

{readme_dates(c, english=True)} (Beijing time, UTC+08:00)

{review_line(c, prefix="../../", english=True)}

## How it works, in plain English

{c['plain_explanation']}

[Back to catalog](../../README.en.md#{gid}) · [Compare similar examples](../../{bp})

## Record

| Field | Value |
| --- | --- |
| Category | {g['title']} |
| Platform / author | X / [@{p['author']}](https://x.com/{p['author']}) |
| Main post | [Source post]({p['url']}) |
| Published (UTC) | {p['published_at']} |
| Added to README / content updated (Beijing time) | {format_readme_time(c['readme_added_at'])} / {format_readme_time(c['readme_updated_at'])} |
| Main-post likes snapshot | **{p['likes']:,}** (threshold ≥ {d['minimum_likes']}) |
| Metrics/media retrieved (UTC) | {p['retrieved_at']} |
| Metadata source | [Public FxTwitter API]({p['metrics_source']}); may be cached |
| Last source review | {case_review_day(c, d)}; public descriptions and metadata reviewed, application not run |
| Jev version | {c.get('jev_version', 'Unspecified in the post; unknown')} |
| Reproduction / availability | Not independently reproduced / unknown (not tested) |

## Images and video

{preview(c, 640)}

{c['media_note']}

{chr(10).join(media)}

Media source: [original publishing page]({p['media_source']}). Externally linked; rights remain with the original creators. Original third-party media is not copied into this repository.

## Use and value

{c['summary']}

**Useful aspect (analysis):** {c['advantage']}

## Inputs, steps and outputs

{c['mechanism']}

Undisclosed prompts, state formats, thresholds and recovery logic remain unknown. Inclusion of a demo does not establish a stable release.

## Evidence and sources

| Claim | Evidence type | Source | Scope |
| --- | --- | --- | --- |
| {c['reported_result']} | Author report | [{"Results documentation" if c.get('reported_result_source') else "Post and attached media"}]({c.get('reported_result_source', p['url'])}) | Not reproduced here; a demo does not establish general performance |
| Main post meets the threshold and has media | Metadata check | [Retrieval endpoint]({p['metrics_source']}) | Snapshot at the recorded time, not a live count |

{c.get('source_notes', '')}

Updates and deduplicated supporting sources:

{supplement}

Public project / demo links (a link does not mean availability has been tested here):

{links}

## Mechanism and comparison

{c['limitation']}

See the [category analysis](../../{bp}) for comparisons, common patterns and suggested experiments. Implementation statements come from public sources; the strengths and missing-evidence assessment are our analysis, not verification of model internals.

## Reproduction record

**Not independently reproduced.** No application installation, paid Jev API calls or performance validation were performed for this record. Future reproduction should record environment, version, inputs, success criteria, total time and full cost before changing its status.

## Change log

| Date | Change |
| --- | --- |
| {case_day(c)} | First collection; checked the main post, metric snapshot and media; added to category comparisons |
{update_entry}'''
        b.append(f'\n## Workflow and mechanism\n\n{g["flow"]}\n\n{g["analysis"]}\n\nIndividual input and implementation differences are documented in the linked cases. This is an application-level synthesis, not a claim that every implementation is identical or an account of Jev’s internal training architecture.\n\n## Suggested reproduction experiments\n\n{g["evaluation"]}\n\n**Not run.** There are no timing, accuracy or cost results produced by this repository.\n\n## Change log\n\n- {date}: collected the first batch, merged same-project updates and added comparisons.\n\n[Homepage](../README.en.md#{gid}) · [Explanation index](README.en.md)\n')
        files[bp] = ''.join(b)
    readme.append('''
## Keeping both languages in sync

Add new leads to the [inbox](inbox/README.en.md). Shared sources, likes and media live in [data/catalog.json](data/catalog.json); English editorial text lives in [data/catalog.en.json](data/catalog.en.json). Then run:

```sh
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

The dependency-free script generates both languages locally. It does not use the network or refresh likes. Missing English entries or fields fail validation. Update retrieval timestamps only after actually checking a new snapshot. See [Contributing](CONTRIBUTING.en.md) and [Taxonomy](docs/taxonomy.en.md).

Third-party images, videos and code remain the property of their creators. Inclusion is not endorsement; this catalog primarily provides original summaries and source links.
''')
    files['README.en.md'] = ''.join(readme)
    files['cases/README.en.md'] = ''.join(index)
    files['breakdowns/README.en.md'] = ''.join(breakdowns)
    return files
