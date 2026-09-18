# 收录更新记录

**简体中文** | [English](CHANGELOG.en.md)

## 2026-09-18 · 第二轮增量

核对截止：**2026-09-18 10:43:33 北京时间（02:43:33 UTC）**。从 67 个增加到 **72 个案例，仍为 11 类**：新增 5 个独立案例，补充 4 个已有条目。点赞是各原帖的取数快照，不是此刻的实时值；旧条目的主帖点赞没有批量刷新。

### 新收录

| 应用 | 为什么单独收录 | 主帖点赞快照 |
| --- | --- | ---: |
| [意图预测启动器](cases/2026-09-18-predictive-launcher/README.md) | 按意图排序文件候选，与网页点击、OCR 操作不同 | [252](https://x.com/dabit3/status/2100756930054504776) |
| [实时电商导购与头像表情](cases/2026-09-18-live-commerce-assistant/README.md) | 对话中的商品推荐及表达反馈，与离线客服意图分类不同 | [217](https://x.com/rinte0321/status/2100736454850908344) |
| [Minecraft 三层协作](cases/2026-09-18-minecraft-hybrid/README.md) | Jev 反应、Astra 规划、本地策略执行的独立游戏系统 | [354](https://x.com/wuyang_zhou/status/2100727660875808913) |
| [实时表情候选](cases/2026-09-18-emoji-suggestions/README.md) | 从 emoji 集合选择，与逐字聊天或像素绘图任务不同 | [230](https://x.com/riku720720/status/2100705558512963602) |
| [语音与指向控制画布](cases/2026-09-18-voice-gesture-canvas/README.md) | 用指向解决语言指代并操作对象，与 TypeGPU 视听特效不同 | [915](https://x.com/jackcheng/status/2100729670991802386) |

每条均已同步中英文简介、通俗原理、局限和原帖媒体；新条目仍全部未复现。Minecraft 主视频约 2× 加速，已合并作者提供的原速版本与分层说明。

### 合并更新，不增加案例数

| 原有条目 | 合并内容与依据 |
| --- | --- |
| [工具调用上下文压缩](cases/2026-09-18-context-compaction/README.md) | [作者仓库链接](https://x.com/tamarajtran/status/2100694552369897539)、[Alex 使用报告](https://x.com/altryne/status/2100739055923425589)、[Theo 质疑](https://x.com/theo/status/2100762304862384257)都指向同一原帖或 `tamaratran/fast-jev-compaction`。补读固定代码版本，区分对话裁剪、工具输出省略与不调用 API 的录屏动画 |
| [帖子传播分类器](cases/2026-09-18-viral-classifier/README.md) | [作者新视频](https://x.com/robj3d3/status/2100722975645598191)引用原帖；补充 61 个问题、样本规模及成本报告，未将 Jev + SuperX 另算一个项目 |
| [语音控制浏览器](cases/2026-09-18-voice-browser/README.md) | [作者教程](https://x.com/moritzkremb/status/2100715237267660873)的 5:59 章节是同用途演示，合并来源 |
| [记忆系统检索筛选](cases/2026-09-18-memory-retrieval/README.md) | 同一教程的 11:33 章节属于这个已收录用途；允许一个多案例教程作为两条记录的补充来源，不新建“教程应用” |

[Rikuo 的压缩转述](https://x.com/riku720720/status/2100716449568596261)也引用同一压缩原帖，没有新增实现证据，不另建记录。

### 待补证据与非应用动态

- [OpenCode 意图权限插件](https://x.com/OpeOginni/status/2100702649834188855)：作者原帖取数时 **160 赞**。即使[转发](https://x.com/thdxr/status/2100723765718008238)超过千赞，也不替代主帖门槛，放入待整理区。
- 教程 17:27 的 [YouTube predictor](https://x.com/moritzkremb/status/2100715237267660873)：目录提供线索，但尚未核清输入、输出及独立实现，暂不另计。
- [RAG 筛选建议](https://x.com/kushbhuwalka/status/2100731050075050485)：本次取数 405 赞，但没有具体实现媒体；不能据一句建议认定“解决了 RAG 精度”。
- [OpenRouter beta 公告](https://x.com/OpenRouter/status/2100744709589316009)与 [TypeSafe 转发](https://x.com/typesafeai/status/2100747035746193598)是同一接入动态，不算两个应用；[Laravel AI SDK 公告](https://x.com/taylorotwell/status/2100700952923713641)对应的 [PR #1010](https://github.com/laravel/ai/pull/1010)已合并，属于开发支持资料，不新增终端应用计数。未验证这些服务的实际调用。

### 检索与去重范围

使用 X 最新搜索 `Jev min_faves:200 since:2026-09-17`，复查自上次收录后出现的结果，并回看到已收录的上下文压缩原帖附近；按帖 ID、引用链、作者、项目链接与用途判断是否新增。补查 Minecraft、画布和表情演示讨论串；元数据使用 FxTwitter 公共接口，可能有缓存。未把整个搜索时段称为全量覆盖，也未声称每段视频都已逐帧审查。

新增与合并列表保存在 [共享目录](data/catalog.json) 的 `latest_update`；精确取数时间保存在各主帖及补充帖。下一轮先对照这些 ID 和项目，避免重复加入。

[返回全部应用](README.md) · [待整理区](inbox/README.md) · [来源方法](references/README.md)
