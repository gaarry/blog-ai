# AI 资讯速览 - 质量标准

> 自动质量检查规则和评分标准

---

## 📋 质量检查清单

### 1. 禁用词汇检查（FAIL 级别）

**检查内容**：文章中不得包含以下类型的词汇

**禁用词汇类型**：
- 营销词汇：震撼、颠覆、革命性、划时代、史无前例、前所未有
- 夸张表述：暴涨、狂飙、爆炸式、疯狂、秒杀、碾压
- 情绪化词汇：惊人、惊艳、令人震惊、不可思议、太强了
- 绝对化表述：最好、最强、第一、唯一、完美、必须
- 商业推广：限时、抢购、福利、优惠、免费、赚钱

**检查方法**：
1. 读取 `reference/banned-words.txt`
2. 在文章中搜索每个禁用词汇
3. 如果发现任何禁用词汇，标记为 **FAIL**

**示例**：
```
❌ 错误：OpenAI 发布了震撼性的新模型
✅ 正确：OpenAI 发布了新模型 GPT-5
```

---

### 2. HTML 结构检查（FAIL 级别）

**检查内容**：文章必须包含完整的 HTML 结构

**必需元素**：

#### Front Matter（YAML）
```yaml
---
title: "AI资讯简报 2026年3月3日"
date: 2026-03-03T20:00:00+08:00
description: "OpenAI签署五角大楼合同 | Anthropic推出记忆导入 | AI Agent框架持续进化"
tags: ["AI资讯", "每日简报"]
---
```

#### 深度文章（3 个）
```html
<div class="article-section">
  <h2><span class="article-num">01</span>文章标题</h2>

  <div class="key-tags">
    <span class="key-tag">关键要点1</span>
    <span class="key-tag">关键要点2</span>
  </div>

  <p>正文段落...</p>

  <div class="sources-list">
    <div class="sources-label">来源</div>
    <a href="URL" class="source-item" target="_blank">
      <span class="source-title">标题</span>
      <span class="source-domain">domain.com</span>
    </a>
  </div>
</div>
```

#### 快讯部分（1 个，包含 5 条）
```html
<div class="quick-news-section">
  <h2>简讯</h2>

  <div class="quick-news-item">
    <span class="paper-num">04</span>
    <div class="quick-news-body">
      <p><strong>标题</strong> 内容...
      <a href="URL" class="qn-source" target="_blank">
        <span class="source-domain">domain.com</span>
      </a></p>
    </div>
  </div>
</div>
```

**检查方法**：
1. 检查 `<div class="article-section">` 数量 = 3
2. 检查 `<div class="quick-news-item">` 数量 = 5
3. 检查每个 article-section 包含：
   - `<h2>` + `<span class="article-num">`
   - `<div class="key-tags">`（至少 2 个 key-tag）
   - `<div class="sources-list">`（至少 2 个 source-item）
4. 检查 Front Matter 完整性

**如果任何元素缺失或数量不对，标记为 FAIL**

---

### 3. 链接有效性检查（WARN 级别）

**检查内容**：所有链接格式正确且可访问

**检查项**：
- URL 格式正确（http:// 或 https://）
- 域名有效（不包含中文媒体域名）
- 链接可访问（可选，避免过多请求）

**合格的域名**：
- 官方博客：openai.com, anthropic.com, google.com/blog
- 技术媒体：techcrunch.com, theverge.com, arstechnica.com
- 学术机构：arxiv.org, papers.nips.cc
- 开发者社区：github.com, news.ycombinator.com, reddit.com

**不合格的域名**：
- 中文媒体：36kr.com, sspai.com, ifanr.com
- 营销网站：*.ad.com, *.promo.com
- 聚合网站：*.aggregator.com

**检查方法**：
1. 提取所有 `<a href="...">` 链接
2. 验证 URL 格式
3. 检查域名是否在允许列表中
4. （可选）使用 WebFetch 检查链接可访问性

**如果发现问题链接，标记为 WARN（不影响发布）**

---

### 4. 来源数量检查（FAIL 级别）

**检查内容**：每篇文章必须有足够的来源

**标准**：
- 深度文章：至少 2 个来源，最多 5 个来源
- 快讯：至少 1 个来源

**检查方法**：
1. 统计每个 article-section 中的 source-item 数量
2. 统计每个 quick-news-item 中的 qn-source 数量
3. 如果不符合标准，标记为 FAIL

**示例**：
```
✅ 正确：深度文章有 3 个来源
❌ 错误：深度文章只有 1 个来源
```

---

### 5. 文章数量检查（FAIL 级别）

**检查内容**：文章数量必须符合要求

**标准**：
- 深度文章：恰好 3 篇
- 快讯：恰好 5 条

**检查方法**：
1. 统计 `<div class="article-section">` 数量
2. 统计 `<div class="quick-news-item">` 数量
3. 如果不等于要求数量，标记为 FAIL

---

### 6. 重复内容检查（WARN 级别）

**检查内容**：避免重复的标题和内容

**检查项**：
- 标题不重复（包括深度文章和快讯）
- 内容相似度 < 80%（使用简单的词汇重叠计算）

**检查方法**：
1. 提取所有标题
2. 检查是否有重复
3. 计算内容相似度（可选）
4. 如果发现重复，标记为 WARN

---

## 📊 评分算法

### 总分计算

**总分 = 100 - 扣分**

### 扣分规则

| 检查项 | 级别 | 扣分 |
|--------|------|------|
| 发现禁用词汇 | FAIL | -100（直接失败） |
| HTML 结构错误 | FAIL | -100（直接失败） |
| 来源数量不足 | FAIL | -100（直接失败） |
| 文章数量错误 | FAIL | -100（直接失败） |
| 链接格式错误 | WARN | -5 每个 |
| 链接不可访问 | WARN | -3 每个 |
| 重复内容 | WARN | -10 每处 |

### 评分等级

- **95-100 分**：优秀，可直接发布
- **85-94 分**：良好，建议人工审核
- **80-84 分**：合格，需要人工审核
- **< 80 分**：不合格，需要重新生成

---

## 🔍 检查流程

### 自动检查流程

```
1. 读取文章文件
   ↓
2. 执行 6 项检查
   ↓
3. 记录每项检查结果
   ↓
4. 计算总分
   ↓
5. 生成质量报告
   ↓
6. 保存到 data/quality_report.json
```

### 质量报告格式

```json
{
  "date": "2026-03-03",
  "article_file": "content/posts/2026-03-03-ai-digest.md",
  "checks": [
    {
      "check": "banned_words",
      "status": "pass",
      "message": "未发现禁用词汇",
      "details": []
    },
    {
      "check": "html_structure",
      "status": "pass",
      "message": "HTML 结构完整",
      "details": {
        "article_sections": 3,
        "quick_news_items": 5,
        "key_tags": 9,
        "sources": 11
      }
    },
    {
      "check": "link_validity",
      "status": "pass",
      "message": "所有链接格式正确",
      "details": {
        "total_links": 11,
        "valid_links": 11,
        "invalid_links": 0
      }
    },
    {
      "check": "source_count",
      "status": "pass",
      "message": "来源数量符合要求",
      "details": {
        "deep_articles": [3, 2, 3],
        "quick_news": [1, 1, 1, 1, 1]
      }
    },
    {
      "check": "article_count",
      "status": "pass",
      "message": "文章数量正确",
      "details": {
        "deep_articles": 3,
        "quick_news": 5
      }
    },
    {
      "check": "duplicate_content",
      "status": "pass",
      "message": "未发现重复内容",
      "details": []
    }
  ],
  "score": 100,
  "grade": "优秀",
  "all_passed": true,
  "recommendations": [
    "质量检查全部通过，可以发布"
  ],
  "checked_at": "2026-03-03T20:30:00+08:00"
}
```

---

## ✅ 通过标准

### 必须满足（FAIL 级别）

- ✅ 无禁用词汇
- ✅ HTML 结构完整
- ✅ 来源数量符合要求
- ✅ 文章数量正确

### 建议满足（WARN 级别）

- ✅ 链接格式正确
- ✅ 链接可访问
- ✅ 无重复内容

### 最低发布标准

- **评分 >= 85 分**
- **所有 FAIL 级别检查通过**
- **WARN 级别检查 <= 1 个**

---

## 🔧 故障处理

### 如果质量检查失败

1. **查看质量报告**
   ```bash
   cat data/quality_report.json | jq '.'
   ```

2. **定位问题**
   ```bash
   # 查看失败的检查项
   cat data/quality_report.json | jq '.checks[] | select(.status == "fail")'
   ```

3. **修复或重新生成**
   - 如果是禁用词汇：重新生成文章
   - 如果是 HTML 结构：检查模板是否正确
   - 如果是来源不足：重新选择主题

4. **重新检查**
   ```bash
   # 重新运行质量检查
   openclaw run ai-digest --step quality_check
   ```

---

## 📈 质量趋势监控

### 建议监控指标

- **平均质量评分**：过去 7 天的平均分
- **失败率**：质量检查失败的比例
- **常见问题**：最常出现的检查失败项

### 监控脚本示例

```bash
#!/bin/bash
# 统计过去 7 天的质量评分

for i in {0..6}; do
  date=$(date -v-${i}d +%Y-%m-%d)
  score=$(cat data/quality_report_${date}.json | jq '.score')
  echo "${date}: ${score}"
done | awk '{sum+=$2; count++} END {print "平均分:", sum/count}'
```

---

## 🎯 质量改进建议

### 持续改进

1. **每周审查**：检查过去一周的质量报告
2. **更新禁用词汇**：发现新的营销词汇及时添加
3. **优化评分算法**：根据实际情况调整权重
4. **改进提示词**：让 AI 更好地理解质量标准

### 质量提升路径

```
85 分 → 90 分：减少 WARN 级别问题
90 分 → 95 分：优化内容质量和多样性
95 分 → 100 分：完美的结构和内容
```

---

**最后更新**：2026-03-03

**维护者**：Gary Yao
