# Categories and verification status

[简体中文](taxonomy.md) | **English**

The current focus is TypeSafe Jev applications on X. Give each case one main category; count a project once and group independent implementations by shared purpose.

## Categories

| ID | Category | Scope |
| --- | --- | --- |
| browser | Browser and computer control | DOM, accessibility trees, OCR, desktop execution, voice control and app QA |
| routing | Model, skill and tool routing | Models, agent harnesses, skills, tools and common interfaces |
| review | Code quality and safety checks | PRs, code quality, command risks, prompt screening and upload checks |
| data | Data classification and organization | Email, papers, tables, bank descriptions and support intent |
| content | Content and advertising analysis | Writing feedback, historical analysis, reach experiments, ads and speech analysis |
| filter | Webpage and feed filtering | Semantic content filters and webpage cleanup |
| memory | Context and memory filtering | Conversation compaction and external-memory relevance |
| games | Game decisions and solving | Mario, chess, cards, action games, Rubik's Cube and others |
| simulation | NPCs, driving and population simulations | Characters, vehicles, drones, synthetic personas and narratives |
| interaction | Real-time interaction and composition experiments | Perception, judgment interfaces, text/pixel composition and computing experiments |
| finance | Trading and historical backtests | Market decisions, order submission and historical strategy experiments; no inference of profitability |

Place close substitutes together within categories, such as the Mario implementations and model routers. The generator computes counts. If there is only one example, state that there is no same-category comparison.

## Inclusion threshold

The main post must have at least 200 likes at retrieval, an original source, a concrete application and corresponding media. Preserve the count as a timestamped snapshot. Do not add repost or update likes. Qualifying leads with missing evidence remain pending. Likes indicate attention, not technical validity.

## Verification states

| Chinese source value | English meaning |
| --- | --- |
| 未复现 | Not independently reproduced: collected or read, but not run |
| 复现中 | Reproduction in progress: attempted, no final outcome yet |
| 部分复现 | Partially reproduced: identify what remains unverified |
| 已复现 | Reproduced: explicit expectations met in the recorded environment |
| 复现失败 | Reproduction failed: record environment, steps and errors |

Availability is separate: unknown, available, limited or unavailable. A broken link is different from a failed reproduction.

## Dates and evidence

Use `YYYY-MM-DD` and include a timezone for exact timestamps.

- **Publication date:** when the original post was published; unknown if unconfirmed.
- **Collection date:** when it entered the repository; also used in the case path.
- **Last updated:** when the record was edited.
- **Last reviewed:** when sources, functionality or reproduction were actually checked; do not refresh it merely for translation.
- **Official statements / author reports:** cite the source and relevant location; statements are not automatically verified facts.
- **Observation / reproduction:** state the observation scope, environment and evidence.
- **Technical inference:** identify the basis and what still needs verification.
