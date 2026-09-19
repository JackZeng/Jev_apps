"""English presentation; source metrics and media are shared with catalog.json."""
from catalog_reviews import review_line
import html
from catalog_home import render_homepage
from catalog_dates import readme_dates, case_day, case_review_day

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
    files = {}
    update = d.get('latest_update')
    index = ['# Case index\n\nAll examples are not independently reproduced. Likes are snapshots of individual main posts. Content-update times use Beijing time (UTC+08:00). See the [homepage](../README.en.md) for previews and plain-language explanations.\n']
    breakdowns = [f'# Explanations and comparisons\n\nAnalysis of public sources; no reproduction experiments have been run here.\n\n- [How Jev apps work: judgments and software composition]({date}-how-jev-apps-work.en.md)\n']
    for g in groups:
        gid = g['id']
        cs = [c for c in cases if c['group'] == gid]
        bp = f'breakdowns/{date}-{gid}.en.md'
        index.append(f'\n## {g["title"]}\n\n| Application | What it does | Main-post likes |\n| --- | --- | ---: |\n')
        breakdowns.append(f'- [{g["title"]}]({date}-{gid}.en.md): {len(cs)} examples.\n')
        b = [f'# {g["title"]}: how they work and compare\n\nFirst compiled: {date}; see each case for its source-review date. Status: **not independently reproduced**.\n\n## Choosing an approach\n\n{g["comparison"]}\n\n## Individual comparisons\n\nThese are analytical strengths and limitations based on public descriptions, not controlled experimental findings.\n\n| Example | Strengths / suitable uses | Limitations / missing evidence |\n| --- | --- | --- |\n']
        for c in cs:
            p = c['post']
            path = f'cases/{case_day(c)}-{c["slug"]}'
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
    files['README.en.md'] = render_homepage(d, en)
    files['cases/README.en.md'] = ''.join(index)
    files['breakdowns/README.en.md'] = ''.join(breakdowns)
    return files
