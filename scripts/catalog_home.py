"""Compact bilingual field-guide homepages; detailed evidence stays in case pages."""
import html
import json
from pathlib import Path

from catalog_dates import beijing_day, case_day, latest_review_day

COPY = Path(__file__).resolve().parents[1] / 'data/homepage.json'
LABELS = {
    'A': ('原理较清楚', 'Clearer mechanism'),
    'B': ('效果待验证', 'Effectiveness unverified'),
    'C': ('主张缺依据', 'Claims lack support'),
}


def render_homepage(d, en=None):
    english = en is not None
    lang, suffix = ('en', '.en') if english else ('zh', '')
    copy = json.loads(COPY.read_text())
    cases = [{**c, **(en['cases'][c['slug']] if english else {})} for c in d['cases']]
    by_slug = {c['slug']: c for c in cases}
    featured = copy['featured']
    assert len(featured) == len({f['slug'] for f in featured}) == 6
    assert {f['slug'] for f in featured} <= by_slug.keys()
    assert set(copy['groups']) == {g['id'] for g in d['groups']}
    for entry in featured + list(copy['groups'].values()):
        assert set(entry['zh']) == set(entry['en'])
        assert all(isinstance(v, str) and v.strip() for l in ('zh', 'en') for v in entry[l].values())

    def details(c):
        return f'cases/{case_day(c)}-{c["slug"]}/README{suffix}.md'

    def preview(c, width):
        p = c['post']
        m = p['media'][0]
        url = html.escape(m.get('thumbnail_url') or m['url'], quote=True)
        alt = html.escape(c['title'], quote=True)
        return f'[<img src="{url}" width="{width}" alt="{alt}">]({p["media_source"]})'

    def evidence(c):
        review = c.get('claim_review')
        if not review:
            return 'Not assessed' if english else '尚未审核'
        label = LABELS[review['tier']][english]
        report = review['report'].replace('.md', f'{suffix}.md')
        return f'[{label}]({report}#{c["slug"]})'

    def footer(c):
        p = c['post']
        source = f'X · {p["likes"]:,} ' + ('likes at collection' if english else '赞快照')
        return (f'{evidence(c)} · [{source}]({p["url"]}) · '
                f'[{"How it works & evidence" if english else "原理与依据"}]({details(c)})\n\n'
                f'**{"Content updated:" if english else "内容更新："}** {beijing_day(c["readme_updated_at"])}\n')

    if english:
        out = [f'''# Jev: small decisions, surprising applications

Most AI tools are known for writing answers. **TypeSafe Jev specializes in making judgments.**
Give it the current situation and a question or set of choices; it returns a choice, score or yes/no judgment for code to act on.
This guide explores what people have built with it—and what their demonstrations actually establish.

**{len(cases)} examples · {len(d['groups'])} categories** · Sources checked through {latest_review_day(d)}

[Browse all applications](#all-apps) · [How Jev works](breakdowns/{d['collected_on']}-how-jev-apps-work.en.md) · [Latest additions](CHANGELOG.en.md)

## Six ideas worth understanding

Start with examples that have clear uses and inspectable mechanisms. Click an image to see its original demo.
''']
    else:
        out = [f'''# Jev：小判断，能做什么？

大多数 AI 以写答案见长，**TypeSafe Jev 擅长做判断。**
给它当前情况和问题或选项，它返回选择、评分或是非判断，再由程序执行。
这里介绍人们用它做出的应用，也解释演示究竟能证明什么。

**{len(cases)} 个案例 · {len(d['groups'])} 类用途** · 来源核对至 {latest_review_day(d)}

[浏览全部应用](#all-apps) · [Jev 如何工作](breakdowns/{d['collected_on']}-how-jev-apps-work.md) · [最近收录](CHANGELOG.md)

## 先看这六个点子

从用途直观、原理较清楚的案例开始。点击图片可看原始演示。
''']
    for item in featured:
        c, text = by_slug[item['slug']], item[lang]
        out += [f'\n### {text["title"]}\n\n', f'[{c["title"]}]({details(c)})\n\n',
                preview(c, 480) + '\n\n', text['takeaway'] + '\n\n',
                f'**{"Keep in mind:" if english else "证据边界："}** {text["limit"]}\n\n', footer(c)]
    out += ['\n<a id="all-apps"></a>\n\n', '## All applications\n\n' if english else '## 按用途找应用\n\n',
            ('Expand a category to browse every example, including the six above. Dates are content-update dates in Beijing time.\n\n' if english else '展开分类查看所有案例，包含上面的六项精选。日期均为北京时间的内容更新日期。\n\n'),
            ('Evidence labels link to the assessment: **Clearer mechanism / Effectiveness unverified / Claims lack support**. They describe public evidence; none of these applications has been independently reproduced here.\n\n' if english else '证据标签可点开查看依据：**原理较清楚 / 效果待验证 / 主张缺依据**。它们描述公开证据的充分程度；本库尚未独立复现这些应用。\n\n')]
    for group in d['groups']:
        gid = group['id']
        text = copy['groups'][gid][lang]
        cs = [c for c in cases if c['group'] == gid]
        out += [f'<a id="{gid}"></a>\n\n<details>\n<summary><strong>{html.escape(text["title"])}</strong> · {len(cs)}</summary>\n\n',
                text['intro'] + '\n\n',
                f'[{"Compare approaches" if english else "同类优劣对比"}](breakdowns/{d["collected_on"]}-{gid}{suffix}.md)\n']
        for c in cs:
            out += [f'\n### [{c["title"]}]({details(c)})\n\n', c['summary'] + '\n\n',
                    preview(c, 320) + '\n\n', footer(c)]
        out.append('\n</details>\n\n')
    if english:
        out.append('''## About this collection

Original application posts must have at least **200 likes** and relevant media. Updates to one project are merged; independent implementations are grouped for comparison. Counts are snapshots, not credibility scores, and this is not an exhaustive inventory of X.

Exact metric timestamps, technical details and assessment grades are kept in the linked records. Media remains with its original creators; click through if a preview stops working.

[Case index](cases/README.en.md) · [Sources & method](references/README.en.md) · [Pending evidence](inbox/README.en.md) · [Contribute a case](CONTRIBUTING.en.md)
''')
    else:
        out.append('''## 关于这份收集

收录原始应用主帖达到 **200 赞**、有对应图片或视频的案例。同项目更新合并，独立实现按用途对比。点赞是历史快照，不是可信度评分；本库不承诺穷尽 X。

精确取数时间、技术细节和审核等级保留在详情与报告中。媒体权利归原作者；预览失效时可点击回原帖查看。

[案例索引](cases/README.md) · [来源与收录方法](references/README.md) · [待补证据](inbox/README.md) · [贡献案例](CONTRIBUTING.md)
''')
    return ''.join(out)
