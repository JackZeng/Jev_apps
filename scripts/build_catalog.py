#!/usr/bin/env python3
"""从公开元数据和原创笔记生成 Markdown；仅使用 Python 标准库，不访问网络。"""
import argparse
from collections import Counter
from datetime import datetime
import html
import json
from pathlib import Path
import sys

from catalog_en import generate_en, validate_translations
from catalog_dates import readme_dates, format_readme_time

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/catalog.json'

def case_dir(c, date):
    return f'cases/{date}-{c["slug"]}'

def thumb(c, width=160):
    p = c['post']
    m = p['media'][0]
    url = m.get('thumbnail_url') or m['url']
    label = '视频' if m['type'] in ('video', 'gif') else '图片'
    source = p['media_source']
    return f'[<img src="{html.escape(url, quote=True)}" width="{width}" alt="{html.escape(c["title"], quote=True)}预览">]({source})<br>[{label}]({source})'

def validate(d):
    cases = d['cases']
    assert len({c['slug'] for c in cases}) == len(cases), '案例 slug 重复'
    assert len({c['post']['id'] for c in cases}) == len(cases), '主帖重复，请合并'
    groups = {g['id'] for g in d['groups']}
    assert len(groups) == len(d['groups']), '分组重复'
    assert d['minimum_likes'] >= 200
    update = d.get('latest_update')
    updates = d.get('updates', [update] if update else [])
    if updates:
        assert updates[-1] == update, '最近增量与历史末项不一致'
        timestamps = [datetime.fromisoformat(u['reviewed_at']) for u in updates]
        assert all(t.tzinfo for t in timestamps), '增量时间缺时区'
        assert timestamps == sorted(set(timestamps)), '增量时间重复或未排序'
    for entry in updates:
        changed = entry['new_cases'] + entry['updated_cases']
        assert len(changed) == len(set(changed)), '增量记录重复'
        assert set(changed) <= {c['slug'] for c in cases}, '增量记录引用未知案例'
    for c in cases:
        p = c['post']
        added = datetime.fromisoformat(c['readme_added_at'])
        updated = datetime.fromisoformat(c['readme_updated_at'])
        assert added.tzinfo and updated.tzinfo, f'{c["slug"]} README 时间缺时区'
        assert added <= updated, f'{c["slug"]} README 更新时间早于收录时间'
        source_ids = [p['id']] + [s['id'] for s in c['supplementary_posts']]
        assert len(source_ids) == len(set(source_ids)), f'{c["slug"]} 来源重复，请合并'
        assert c['group'] in groups
        assert p['likes'] >= d['minimum_likes'], c['slug']
        assert p['media'], f'{c["slug"]} 缺媒体'
        assert p['url'].endswith('/' + p['id'])
        assert p['metrics_source'] == 'https://api.fxtwitter.com/status/' + p['id']
        for key in ('retrieved_at', 'published_at'):
            assert datetime.fromisoformat(p[key]).tzinfo, f'{c["slug"]} 缺时区'
        for m in p['media']:
            assert m['type'] in ('photo', 'video', 'gif')
            assert m['url'].startswith('https://')
        for k in ('title', 'summary', 'plain_explanation', 'mechanism', 'advantage', 'limitation', 'reported_result'):
            assert c[k] and '|' not in c[k], (c['slug'], k)

def generate(d):
    date, cases = d['collected_on'], d['cases']
    groups = {g['id']: g for g in d['groups']}
    counts = Counter(c['group'] for c in cases)
    files = {}
    update = d.get('latest_update')
    update_notice = (f"最近增量核对：**{update['reviewed_at']}（UTC）**；新增 **{len(update['new_cases'])}** 个独立案例，补充 **{len(update['updated_cases'])}** 个已有条目。[本轮新增、合并与未收录原因](CHANGELOG.md)。已有主帖的点赞快照保持原取数时间。\n\n" if update else '')
    readme = [f'''# Jev 应用案例与原理拆解

从 X 收集 **TypeSafe Jev** 的应用演示，整理用途、实现思路和同类优劣。**当前 {len(cases)} 个案例 · {len(groups)} 类 · 每条主帖收录时均 ≥ {d['minimum_likes']} 赞 · 每条附图或视频**。

{update_notice}## Jev 是什么？先用一句人话理解

可以把 Jev 想成软件里的快速分拣员：程序先把当前情况和问题准备好，Jev 负责判断，程序再把判断变成动作。例如给邮件贴标签、为任务挑一个 AI 助手，或决定网页上下一步点哪个按钮。许多个小判断组合起来，就能构成下面这些应用。

以查航班为例：程序先读网页、列出可操作的按钮，Jev 选下一步，浏览器工具负责点击，然后再看页面有什么变化。读取页面、需要时生成输入文字、检查结果是否正确，都由整套程序配合完成。

更新日期：**{date}（北京时间）**。这是本次检索覆盖到的案例集，不承诺穷尽 X；目前全部**未复现**。正文中的性能、成本与效果均标明为作者报告，优劣是根据公开设计作出的分析，不是本仓库跑分。

Jev 接收状态与类型化问题，输出可供代码使用的选择、评分或是非判断。它在下面许多应用中充当决策组件，周围仍需要观测、执行器，有时也需要 LLM。[官方介绍](https://docs.typesafe.ai/introduction) · [基本原理与阅读方法](breakdowns/2026-09-18-how-jev-apps-work.md)

## 收录与阅读规则

- **门槛按单条主帖判断**：点赞 ≥ 200，明确使用 TypeSafe Jev，有具体演示或实现截图；同项目更新与转载合并，点赞不相加。
- **数字是快照**：检索来自 X；精确点赞与媒体元数据通过 FxTwitter 公共接口复核，可能有缓存或延迟。每篇保留原帖时间、取数时间和来源。[检索与证据说明](references/README.md) · [结构化目录与点赞快照](data/catalog.json)
- **预览可点击**：表中的图来自原帖图片或视频封面，点击打开对应来源。详情保留视频直链/原图；X 图片 CDN、视频直链或帖子可能失效，优先回原帖查看。Skillbox 的图来自它被引用的旧版介绍，已单独说明。
- **同类放一起**：每组下面给选择建议，详细对比逐项列出优势与限制。类别内按用途排列，不按点赞排名。视频只是演示证据，不证明长期可靠性。
- **简介旁的时间**：每条标注收录到 README 和最近内容更新的时间，统一为**北京时间（UTC+08:00）**；与原帖发布时间、点赞取数时间分别记录。[时间依据](references/README.md#readme-times)

## 分类导航

| 类别 | 案例数 | 对比与原理 |
| --- | ---: | --- |
''']
    for g in groups.values():
        readme.append(f'| [{g["title"]}](#{g["id"]}) | {counts[g["id"]]} | [阅读分析](breakdowns/{date}-{g["id"]}.md) |\n')
    readme.append('\n[案例索引](cases/README.md) · [全部拆解](breakdowns/README.md) · [待补证据](inbox/README.md) · [收录流程](CONTRIBUTING.md)\n\n## 全部应用列表\n')
    index = ['# 案例索引\n\n全部条目未复现；点赞为各自主帖的取数快照。收录与内容更新时间统一为北京时间（UTC+08:00）。图文总览见 [首页](../README.md)。\n']
    breakdowns = ['# 原理拆解与同类对比\n\n这些是公开资料分析，尚未执行复现实验。\n\n- [Jev 应用如何工作：三种原语与应用组合](2026-09-18-how-jev-apps-work.md)\n']
    for group_id, g in groups.items():
        group_cases = [c for c in cases if c['group'] == group_id]
        bp = f'breakdowns/{date}-{group_id}.md'
        readme.append(f'\n<a id="{group_id}"></a>\n\n### {g["title"]}（{len(group_cases)}）\n\n{g["comparison"]}\n\n[逐项优劣与原理对比]({bp})\n\n| 应用与简介 | 主帖点赞 | 图片 / 视频 |\n| --- | ---: | --- |\n')
        index.append(f'\n## {g["title"]}\n\n| 应用 | 简介 | 主帖点赞 |\n| --- | --- | ---: |\n')
        breakdowns.append(f'- [{g["title"]}]({date}-{group_id}.md)：{len(group_cases)} 个案例。\n')
        b = [f'# {g["title"]}：原理与对比\n\n收录 / 更新 / 来源复查：{date}。验证状态：**未复现**。\n\n## 选择建议\n\n{g["comparison"]}\n\n## 同类逐项对比\n\n以下优势和限制是基于作者公开说明的技术分析；不构成同条件实验结论。\n\n| 案例 | 相对优势 / 适用场景 | 限制 / 尚缺证据 |\n| --- | --- | --- |\n']
        for c in group_cases:
            path = case_dir(c, date)
            p = c['post']
            readme.append(f'| [**{c["title"]}**]({path}/README.md)<br>{c["summary"]}<br>**原理：** {c["plain_explanation"]}<br>{readme_dates(c)} | [{p["likes"]:,}]({p["url"]}) | {thumb(c)} |\n')
            index.append(f'| [{c["title"]}]({date}-{c["slug"]}/README.md) | {c["summary"]}<br>{readme_dates(c)} | [{p["likes"]:,}]({p["url"]}) |\n')
            b.append(f'| [{c["title"]}](../{path}/README.md) | {c["advantage"]} | {c["limitation"]} |\n')
            supplement = '\n'.join(f'- [@{s["author"]} 的补充帖]({s["url"]})：发布于 {s["published_at"]}；{s["retrieved_at"]} 取数时 {s["likes"]:,} 赞，仅作补充、不计入门槛。[取数来源]({s["metrics_source"]})。' + ''.join(f' [补充媒体 {i}]({m["url"]})' for i, m in enumerate(s.get('media', []), 1)) for s in c['supplementary_posts']) or '无。'
            update_entry = ''.join(f"| {u['reviewed_at']} | 合并补充来源，完善原理、证据或教程说明；[去重记录](../../CHANGELOG.md) |\n" for u in d.get('updates', [update] if update else []) if c['slug'] in u['updated_cases'])
            links = '\n'.join(f'- [项目入口 {i}]({url})' for i, url in enumerate(c['links'], 1)) or '原帖未提供已核对的独立入口；后续可继续从讨论串补充。'
            media = []
            for i, m in enumerate(p['media'], 1):
                label = '视频直链' if m['type'] in ('video', 'gif') else '原图'
                media.append(f'- [{label} {i}]({m["url"]})' + (f'（元数据时长 {m["duration"]:.1f} 秒）' if m.get('duration') else ''))
            files[f'{path}/README.md'] = f'''# {c['title']}

> {c['summary']}

{readme_dates(c)}（北京时间，UTC+08:00）

## 用人话解释原理

{c['plain_explanation']}

[返回总表](../../README.md#{group_id}) · [同类优劣与原理](../../{bp})

## 基本信息

| 字段 | 内容 |
| --- | --- |
| 应用分类 | {g['title']} |
| 来源平台 / 原作者 | X / [@{p['author']}](https://x.com/{p['author']}) |
| 原帖 | [查看原帖]({p['url']}) |
| 原帖发布时间（UTC） | {p['published_at']} |
| README 收录 / 内容更新（北京时间） | {format_readme_time(c['readme_added_at'])} / {format_readme_time(c['readme_updated_at'])} |
| 主帖点赞快照 | **{p['likes']:,}**（门槛 ≥ {d['minimum_likes']}） |
| 点赞与媒体取数时间（UTC） | {p['retrieved_at']} |
| 元数据核验渠道 | [FxTwitter 公共接口]({p['metrics_source']})；可能有缓存 |
| 最后来源复查 | {date}，核对公开说明与元数据；未运行应用 |
| Jev 版本 | {c.get('jev_version', '原帖未明确固定版本，未知')} |
| 验证状态 / 可用性 | {c['verification']} / {c['availability']} |

## 图片与视频

{thumb(c, 640)}

{c['media_note']}

{chr(10).join(media)}

媒体来源：[原始发布页]({p['media_source']})。仅外链，权利归原作者；未把第三方原始素材复制到仓库。

## 应用场景与价值

{c['summary']}

**可借鉴点（分析）**：{c['advantage']}

## 输入、操作与输出

{c['mechanism']}

没有披露的提示词、状态格式、阈值或失败恢复逻辑保持未知。应用按作者演示收录，不认定已稳定上线。

## 证据与来源

| 主张 | 依据类型 | 来源 | 适用范围 |
| --- | --- | --- | --- |
| {c['reported_result']} | 作者陈述 | [主帖正文及附带媒体]({p['url']}) | 本仓库未复测，演示不证明普遍性能 |
| 主帖达到收录门槛、附带媒体 | 元数据核对 | [取数接口]({p['metrics_source']}) | 仅上述时间快照，非实时数值 |

{c.get('source_notes', '')}

补充更新与去重来源：

{supplement}

公开项目 / 体验入口（存在入口不等于本仓库已验证可用）：

{links}

## 原理拆解与同类比较

{c['limitation']}

同类逐项对比、公共流程和建议实验见 [专题分析](../../{bp})。实现说明来自作者公开材料；优势及尚缺证据属于本仓库分析，不能视为模型内部架构已被证实。

## 复现记录

**未复现**。未安装应用、调用付费 Jev API 或验证性能；该条没有实际测试结果。复现应记录环境、版本、输入、成功标准、完整耗时及费用，再更新验证状态。

## 更新记录

| 日期 | 更新内容 |
| --- | --- |
| {date} | 首次收录；核对主帖、点赞与媒体，加入同类对比 |
{update_entry}'''
        b.append(f'\n## 可观察流程与机制\n\n{g["flow"]}\n\n{g["analysis"]}\n\n各案例的输入和实现差异见上表链接的来源记录。该流程是应用层归纳，不代表每个项目都采用完全相同的实现，也不是对 Jev 内部训练架构的推断。\n\n## 复现实验建议\n\n{g["evaluation"]}\n\n**尚未执行实验。** 当前没有本仓库产生的耗时、准确率或成本结果。\n\n## 更新记录\n\n- {date}：整理首批案例，合并同项目更新，建立对比。\n\n[返回首页](../README.md#{group_id}) · [拆解索引](README.md)\n')
        files[bp] = ''.join(b)
    readme.append('''
## 继续维护

新增线索先放 [待整理区](inbox/README.md)。中文内容与共享来源保存在 [data/catalog.json](data/catalog.json)，英文介绍保存在 [data/catalog.en.json](data/catalog.en.json)。点赞、作者和媒体只维护一份，再执行：

```sh
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

脚本同时生成中英文 Markdown，缺英文条目或字段会报错；不联网、不需要第三方依赖，不会自动刷新点赞。人工核对新快照后再更新取数时间。详见 [贡献流程](CONTRIBUTING.md) 与 [分类约定](docs/taxonomy.md)。

所有第三方图片、视频和代码权利归各自作者；收录不表示背书。本库以原创摘要和来源链接为主。
''')
    files['README.md'] = ''.join(readme)
    files['cases/README.md'] = ''.join(index)
    files['breakdowns/README.md'] = ''.join(breakdowns)
    return files

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='验证元数据与生成文件同步，不写入')
    args = parser.parse_args()
    d = json.loads(DATA.read_text())
    validate(d)
    en = json.loads((ROOT / 'data/catalog.en.json').read_text())
    validate_translations(d, en)
    files = {**generate(d), **generate_en(d, en)}
    for name, content in files.items():
        filename = Path(name).name
        if name.endswith('.en.md'):
            nav = f'[简体中文]({filename.replace(".en.md", ".md")}) | **English**'
        else:
            nav = f'**简体中文** | [English]({filename.replace(".md", ".en.md")})'
        heading, rest = content.split('\n', 1)
        files[name] = heading + '\n\n' + nav + '\n' + rest
    mismatches = []
    for name, content in files.items():
        p = ROOT / name
        if args.check:
            if not p.exists() or p.read_text() != content:
                mismatches.append(name)
        else:
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content)
    if mismatches:
        print('文件不同步：\n' + '\n'.join(mismatches), file=sys.stderr)
        return 1
    print(f'{"Verified" if args.check else "Generated"}: {len(d["cases"])} cases, {len(d["groups"])} groups, 2 languages, {len(files)} Markdown files.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
