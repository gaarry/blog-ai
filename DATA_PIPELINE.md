# AI 资讯速览 - 数据处理流程

> 从原始数据采集到最终文章生成的完整数据流

---

## 数据流概览

```
sources_raw.json
    ↓ [enrichment]
sources_with_engagement.json
    ↓ [scoring]
scored_sources.json
    ↓ [selection]
selected_topics.json
    ↓ [generation]
YYYY-MM-DD-ai-digest.md
    ↓ [validation]
quality_report.json
    ↓ [publish]
Git commit & push
```

---

## 步骤 1: 原始数据采集 (sources_raw.json)

### 数据来源

从 20+ 英文信源采集最新 AI 资讯：

**官方博客：** OpenAI, Anthropic, Google AI, DeepMind, Meta AI, NVIDIA...
**技术媒体：** MIT Technology Review, TechCrunch, The Verge...
**社区平台：** Hacker News, HuggingFace, Reddit...

### 数据结构

```json
{
  "metadata": {
    "collected_at": "2026-03-03T10:00:00+08:00",
    "time_range": "24h",
    "total_sources": 22,
    "total_articles": 156
  },
  "sources": [
    {
      "id": "openai_blog_20260303_001",
      "url": "https://openai.com/blog/...",
      "title": "Article Title",
      "summary": "Brief summary",
      "content": "Full article content...",
      "source": "OpenAI Blog",
      "domain": "openai.com",
      "published": "2026-03-02T15:30:00Z",
      "author": "Sam Altman",
      "tags": ["partnership", "defense"],
      "language": "en"
    }
  ]
}
```

### 关键字段

- `id`: 唯一标识符（URL hash）
- `url`: 文章完整 URL
- `content`: 完整文章内容（用于 LLM 阅读）
- `published`: ISO 8601 时间戳
- `source`: 来源名称（用于权威性评分）

### Schema 文件

`data/schemas/sources_raw.schema.json`

### 示例文件

`data/examples/sources_raw.example.json`

---

## 步骤 2: 社区参与度数据 (sources_with_engagement.json)

### 数据增强

为每篇文章添加社区参与度数据：

- **Hacker News**: 投票数、评论数
- **Reddit**: 点赞数、评论数
- **Twitter**: 点赞数、转发数（可选）

### 数据结构

```json
{
  "metadata": {
    "collected_at": "2026-03-03T10:00:00+08:00",
    "enriched_at": "2026-03-03T10:15:00+08:00",
    "total_articles": 156,
    "matched_articles": 87
  },
  "sources": [
    {
      "id": "openai_blog_20260303_001",
      "url": "...",
      "title": "...",
      "content": "...",
      "engagement": {
        "total_score": 92.5,
        "hacker_news": {
          "item_id": 39582341,
          "score": 847,
          "comments": 523,
          "url": "https://news.ycombinator.com/item?id=39582341"
        },
        "reddit": {
          "post_id": "1b3xyz9",
          "subreddit": "MachineLearning",
          "upvotes": 3421,
          "comments": 892,
          "url": "https://reddit.com/..."
        }
      }
    }
  ]
}
```

### 参与度评分算法

```python
hn_score = min(100, (hn_votes / 10) + (hn_comments / 5))
reddit_score = min(100, (upvotes / 50) + (comments / 10))
total_score = hn_score * 0.6 + reddit_score * 0.4
```

### Schema 文件

`data/schemas/sources_with_engagement.schema.json`

### 示例文件

`data/examples/sources_with_engagement.example.json`

---

## 步骤 3: 算法评分 (scored_sources.json)

### 评分维度

**四个维度，权重分配：**

1. **多源交叉验证 (40%)**
   - 3+ 独立来源报道同一事件：95 分
   - 2 个来源：85 分
   - 1 个来源：70 分
   - 仅单一来源：50 分

2. **社区参与度 (25%)**
   - 基于步骤 2 的参与度数据
   - HN > 200 票或 Reddit > 500 赞：高分

3. **来源权威性 (20%)**
   - 官方博客：100 分
   - 技术媒体：80 分
   - Newsletter：70 分
   - 社区平台：60 分

4. **时效性 (15%)**
   - 0-6 小时：100 分
   - 6-12 小时：90 分
   - 12-18 小时：75 分
   - 18-24 小时：60 分
   - 24+ 小时：30 分

### 数据结构

```json
{
  "metadata": {
    "scored_at": "2026-03-03T10:30:00+08:00",
    "total_articles": 156,
    "scoring_version": "1.0.0",
    "weights": {
      "cross_verification": 0.40,
      "community_engagement": 0.25,
      "source_authority": 0.20,
      "timeliness": 0.15
    }
  },
  "sources": [
    {
      "id": "openai_blog_20260303_001",
      "url": "...",
      "title": "...",
      "score": 95.2,
      "score_breakdown": {
        "cross_verification": {
          "score": 95.0,
          "weight": 0.40,
          "weighted_score": 38.0,
          "related_articles": ["id1", "id2", "id3"],
          "similarity": 0.85
        },
        "community_engagement": {
          "score": 92.5,
          "weight": 0.25,
          "weighted_score": 23.1,
          "hn_score": 84.7,
          "reddit_score": 85.5
        },
        "source_authority": {
          "score": 100.0,
          "weight": 0.20,
          "weighted_score": 20.0,
          "source_type": "official_blog"
        },
        "timeliness": {
          "score": 93.8,
          "weight": 0.15,
          "weighted_score": 14.1,
          "hours_ago": 18.5
        }
      },
      "rank": 1
    }
  ]
}
```

### 最终评分计算

```
final_score =
    cross_verification_score * 0.40 +
    community_engagement_score * 0.25 +
    source_authority_score * 0.20 +
    timeliness_score * 0.15
```

### 处理脚本

`scripts/process_sources.py`

### Schema 文件

`data/schemas/scored_sources.schema.json`

### 示例文件

`data/examples/scored_sources.example.json`

---

## 步骤 4: 主题选择 (selected_topics.json)

### 选择标准

**深度文章（3 篇）：**
- 最低评分：70 分
- 最少来源：2 个
- 主题多样性：每个类别最多 1 篇
- 去重检查：与近 7 天内容对比

**快讯（3-5 条）：**
- 最低评分：50 分
- 最大长度：150 字符
- 不与深度文章重复

### 主题分类

- `model_release`: 模型发布
- `ai_agent`: AI Agent
- `safety_ethics`: 安全与伦理
- `industry_news`: 行业动态
- `tools_apps`: 工具与应用
- `research`: 研究进展
- `policy_regulation`: 政策法规

### 数据结构

```json
{
  "metadata": {
    "selected_at": "2026-03-03T11:00:00+08:00",
    "date": "2026-03-03",
    "total_candidates": 156,
    "selection_criteria": {
      "min_score": 70,
      "diversity_enabled": true,
      "duplicate_check_days": 7
    }
  },
  "deep_articles": [
    {
      "theme": "OpenAI与五角大楼合作争议",
      "category": "policy_regulation",
      "suggested_title": "OpenAI向五角大楼让步，交出的恰是Anthropic的底线",
      "sources": [
        {
          "id": "openai_blog_20260303_001",
          "url": "...",
          "title": "...",
          "summary": "...",
          "content": "Full content for LLM to read...",
          "domain": "openai.com",
          "source": "OpenAI Blog",
          "published": "2026-03-02T15:30:00Z",
          "score": 95.2
        }
      ],
      "key_points": [
        "要点1",
        "要点2",
        "要点3"
      ]
    }
  ],
  "quick_news": [
    {
      "title": "News headline",
      "url": "...",
      "domain": "example.com",
      "summary": "Brief summary (max 150 chars)",
      "published": "2026-03-02T08:30:00Z",
      "score": 71.3
    }
  ]
}
```

### 选择逻辑

1. 按评分排序所有文章
2. 对文章进行分类
3. 从每个类别选择最高分的文章
4. 为每个主题找 2-4 个相关来源
5. 确保总共 3 篇深度文章，5 条快讯

### 处理脚本

`scripts/select_topics.py`

### Schema 文件

`data/schemas/selected_topics.schema.json`

### 示例文件

`data/examples/selected_topics.example.json`

---

## 步骤 5: 文章生成 (YYYY-MM-DD-ai-digest.md)

### 输入

`selected_topics.json` 中的数据 + 系统提示词

### LLM 任务

1. 阅读所有来源文章的完整内容
2. 综合多个来源，形成连贯叙事
3. 提炼关键要点（key-tags）
4. 按照 `BLOG_TEMPLATE.md` 格式生成

### 输出格式

```markdown
---
title: "文章标题"
date: 2026-03-03T20:00:00+08:00
draft: false
description: "要点1；要点2；要点3"
coverImage: "https://images.unsplash.com/..."
tags: ["AI", "OpenAI", "Anthropic"]
categories: ["AI资讯"]
---

<div class="article-section">
<h2><span class="article-num">01</span>第一篇文章标题</h2>

<p>正文第一段...</p>

<p>正文第二段...</p>

<div class="key-tags">
<span class="key-tag">关键要点1</span>
<span class="key-tag">关键要点2</span>
</div>

<div class="sources-list">
<div class="sources-label">来源</div>
<a href="..." class="source-item" target="_blank">
  <span class="source-title">文章标题</span>
  <span class="source-domain">domain.com</span>
</a>
</div>
</div>

<div class="article-section">
<h2><span class="article-num">02</span>第二篇文章标题</h2>
...
</div>

<div class="quick-news-section">
<div class="quick-news-item">
  <span class="paper-num">04</span>
  <div class="quick-news-body">
    <p><strong>快讯标题</strong> 内容...
    <a href="..." class="qn-source" target="_blank">
      <span class="source-domain">domain.com</span>
    </a></p>
  </div>
</div>
</div>
```

### 生成参数

- Model: `claude-3-5-sonnet-20241022`
- Temperature: `0.3` (较低温度保持客观)
- Max Tokens: `8000`
- System Prompt: `AI_DIGEST_SYSTEM_PROMPT.md`

---

## 步骤 6: 质量检查 (quality_report.json)

### 检查项目

1. **禁用词汇检查**
   - 扫描 `data/banned_words.txt`
   - 发现即失败，不发布

2. **链接有效性检查**
   - 验证所有来源链接
   - 失败仅警告

3. **HTML 结构检查**
   - 必须包含：article-section, article-num, key-tags, sources-list
   - 缺少则失败

4. **来源数量检查**
   - 每篇深度文章：2-5 个来源
   - 超出范围则失败

5. **文章数量检查**
   - 深度文章：3 篇
   - 快讯：3-5 条

6. **重复内容检查**
   - 与近 7 天内容对比
   - 相似度 > 80% 则警告

### 数据结构

```json
{
  "date": "2026-03-03",
  "file": "content/posts/2026-03-03-ai-digest.md",
  "checks": [
    {
      "check": "banned_words",
      "status": "pass",
      "message": "No banned words found",
      "details": {}
    },
    {
      "check": "link_validity",
      "status": "pass",
      "message": "All 15 links are valid",
      "details": {
        "total_links": 15,
        "valid_links": 15,
        "invalid_links": 0
      }
    },
    {
      "check": "html_structure",
      "status": "pass",
      "message": "All required elements present",
      "details": {
        "article_sections": 3,
        "key_tags": 9,
        "sources_lists": 3
      }
    },
    {
      "check": "source_count",
      "status": "pass",
      "message": "All articles have 2-5 sources",
      "details": {
        "article_1": 4,
        "article_2": 2,
        "article_3": 3
      }
    },
    {
      "check": "article_count",
      "status": "pass",
      "message": "Correct article counts",
      "details": {
        "deep_articles": 3,
        "quick_news": 5
      }
    },
    {
      "check": "duplicate_content",
      "status": "warn",
      "message": "Some similarity with recent content",
      "details": {
        "similar_articles": [
          {
            "date": "2026-03-02",
            "similarity": 0.65
          }
        ]
      }
    }
  ],
  "all_passed": true,
  "score": 95,
  "timestamp": "2026-03-03T11:45:00+08:00"
}
```

### 验证脚本

`scripts/validate_data.py`

---

## 步骤 7: Git 提交与发布

### 提交信息格式

```
Add: AI资讯简报 2026-03-03

- 3 篇深度文章
- 5 条快讯
- 来源：15 个一手信源

Co-Authored-By: OpenClaw <noreply@openclaw.com>
```

### 发布流程

1. `git add content/posts/2026-03-03-ai-digest.md`
2. `git commit -m "..."`
3. `git push origin main`
4. GitHub Actions 自动构建和部署

---

## 数据文件位置

### 运行时数据

```
data/
├── sources_raw.json                    # 步骤 1 输出
├── sources_with_engagement.json        # 步骤 2 输出
├── scored_sources.json                 # 步骤 3 输出
├── selected_topics.json                # 步骤 4 输出
└── quality_report.json                 # 步骤 6 输出
```

### Schema 定义

```
data/schemas/
├── sources_raw.schema.json
├── sources_with_engagement.schema.json
├── scored_sources.schema.json
└── selected_topics.schema.json
```

### 示例数据

```
data/examples/
├── sources_raw.example.json
├── sources_with_engagement.example.json
├── scored_sources.example.json
└── selected_topics.example.json
```

### 处理脚本

```
scripts/
├── validate_data.py        # 数据验证
├── process_sources.py      # 评分处理
└── select_topics.py        # 主题选择
```

---

## 使用脚本

### 验证数据

```bash
# 验证所有数据文件
python3 scripts/validate_data.py

# 输出示例：
# 🔍 Validating data files...
#
# ✅ sources_raw.json is valid
# ✅ sources_with_engagement.json is valid
# ✅ scored_sources.json is valid
# ✅ selected_topics.json is valid
#
# ✅ All validations passed!
```

### 处理数据

```bash
# 步骤 3: 评分
python3 scripts/process_sources.py

# 步骤 4: 选择主题
python3 scripts/select_topics.py
```

---

## 数据保留策略

| 数据类型 | 保留时间 | 说明 |
|---------|---------|------|
| sources_raw.json | 7 天 | 原始采集数据 |
| sources_with_engagement.json | 7 天 | 参与度数据 |
| scored_sources.json | 30 天 | 评分数据 |
| selected_topics.json | 30 天 | 选择记录 |
| quality_report.json | 90 天 | 质量报告 |
| *.md (已发布文章) | 永久 | 发布内容 |

---

## 监控指标

### 数据质量指标

- 采集文章数：100-200 篇/天
- 匹配参与度：> 50%
- 平均评分：70-90 分
- 选中文章评分：> 85 分

### 处理性能指标

- 采集耗时：< 10 分钟
- 评分耗时：< 3 分钟
- 选择耗时：< 5 分钟
- 总处理时间：< 40 分钟

---

## 故障排查

### 数据文件缺失

```bash
# 检查文件是否存在
ls -la data/*.json

# 如果缺失，从示例复制
cp data/examples/sources_raw.example.json data/sources_raw.json
```

### Schema 验证失败

```bash
# 查看详细错误
python3 scripts/validate_data.py

# 检查 JSON 格式
cat data/sources_raw.json | jq '.'
```

### 评分异常

```bash
# 检查评分逻辑
python3 scripts/process_sources.py

# 查看评分分布
cat data/scored_sources.json | jq '.sources[] | {id, score}'
```

---

## 扩展开发

### 添加新的数据源

1. 在工作流配置中添加信源
2. 更新 schema（如需要）
3. 测试数据采集
4. 验证数据格式

### 调整评分权重

修改 `scripts/process_sources.py` 中的权重：

```python
weights = {
    'cross_verification': 0.40,    # 调整这里
    'community_engagement': 0.25,
    'source_authority': 0.20,
    'timeliness': 0.15
}
```

### 自定义主题分类

修改 `scripts/select_topics.py` 中的 `categorize_article` 函数。

---

## 参考资料

- [JSON Schema 规范](https://json-schema.org/)
- [OpenClaw 文档](https://github.com/openclaw/openclaw)
- [系统提示词](AI_DIGEST_SYSTEM_PROMPT.md)
- [文章模板](BLOG_TEMPLATE.md)

---

**最后更新：** 2026-03-03
