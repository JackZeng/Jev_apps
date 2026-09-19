"""Render editorial claim assessments without equating them with reproduction."""
from collections import Counter
from datetime import datetime
from catalog_dates import format_readme_time

LABELS = {
    'A': ('🟢 A · 功能/原理证据较清楚', '🟢 A · Clearer evidence for function/mechanism'),
    'B': ('🟡 B · 效果待验证', '🟡 B · Effectiveness unverified'),
    'C': ('🟠 C · 宣传超出证据', '🟠 C · Claims exceed evidence'),
}


def validate_review(c):
    review = c.get('claim_review')
    if not review:
        assert 'review_summary' not in c, f'{c["slug"]}: review text without assessment'
        return
    assert review['tier'] in LABELS, f'{c["slug"]}: unknown assessment'
    assert datetime.fromisoformat(review['reviewed_at']).tzinfo, 'Review time needs timezone'
    report = review['report']
    assert report.startswith('references/') and report.endswith('.md') and '..' not in report
    assert c.get('review_summary') and '|' not in c['review_summary']


def review_line(c, prefix='', english=False):
    review = c.get('claim_review')
    if not review:
        return '**⚪ Not assessed**' if english else '**⚪ 尚未审核**'
    report = review['report'].replace('.md', '.en.md') if english else review['report']
    label = LABELS[review['tier']][english]
    source_label = 'Assessment and sources' if english else '判断依据与来源'
    return (f'**{label}**<br>{c["review_summary"]}<br>'
            f'[{source_label}]({prefix}{report}#{c["slug"]})')


def review_legend(cases, english=False):
    counts = Counter(c['claim_review']['tier'] for c in cases if c.get('claim_review'))
    if not counts:
        return ''
    reviewed = max((c['claim_review']['reviewed_at'] for c in cases if c.get('claim_review')),
                   key=datetime.fromisoformat)
    pending = len(cases) - sum(counts.values())
    if english:
        return (f'## Claim assessments\n\n'
                f'**A: {counts["A"]} · B: {counts["B"]} · C: {counts["C"]} · Not assessed: {pending}.** '
                f'Latest assessment: {format_readme_time(reviewed)} Beijing time. '
                'Each application below includes a label, a short reason and a link to its evidence.\n\n'
                '- **🟢 A:** clearer support for a bounded function or mechanism; not certification of all performance claims.\n'
                '- **🟡 B:** a plausible demo or author test, with effectiveness still unverified.\n'
                '- **🟠 C:** a specific promotional claim exceeds its evidence; this does not mean the whole project is fake.\n\n'
                'These are editorial assessments of public claims, separate from reproduction status. All cases remain unreproduced.\n\n')
    return (f'## 项目证据审核\n\n'
            f'**A：{counts["A"]} 项 · B：{counts["B"]} 项 · C：{counts["C"]} 项 · 尚未审核：{pending} 项。** '
            f'最近审核：{format_readme_time(reviewed)} 北京时间。下方每个项目均标注等级、简短理由和具体依据。\n\n'
            '- **🟢 A：功能/原理证据较清楚**，只支持限定范围，不认证所有性能宣传。\n'
            '- **🟡 B：效果待验证**，有合理演示或作者自测，但缺完整效果证据。\n'
            '- **🟠 C：宣传超出证据**，针对具体主张，不等于整个项目造假。\n\n'
            '审核等级与复现状态分开：本库全部案例仍未独立复现，点赞数不作为可信度评分。\n\n')
