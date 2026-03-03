# AI 资讯速览 - 自动化系统

> 基于 OpenClaw 的每日 AI 资讯自动生成与发布系统

[![Hugo](https://img.shields.io/badge/Hugo-0.145.0-blue.svg)](https://gohugo.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 项目简介

这是一个完全自动化的 AI 资讯生成系统，每天自动从 20+ 英文一手信源采集、筛选、生成高质量的 AI 行业资讯简报。

**核心特性：**
- 🤖 完全自动化，无需人工干预
- 📰 仅使用英文一手信源，避免二次失真
- 🎯 多层过滤机制，确保内容质量
- 🔍 严格质量检查，杜绝营销和夸张表述
- 📊 中立客观，事实为基础
- ⚡ 每天 18:00 自动生成并发布

---

## 📁 核心文档

| 文档 | 说明 |
|------|------|
| [AI_DIGEST_SYSTEM_PROMPT.md](AI_DIGEST_SYSTEM_PROMPT.md) | **系统提示词和生成规范**（最重要） |
| [DATA_PIPELINE.md](DATA_PIPELINE.md) | 完整数据处理流程 |
| [BLOG_TEMPLATE.md](BLOG_TEMPLATE.md) | 文章模板和写作规范 |
| [AI_DIGEST_AUTOMATION_README.md](AI_DIGEST_AUTOMATION_README.md) | 自动化系统使用指南 |

---

## 🔄 数据流程

```
sources_raw.json (20+ 信源, 150+ 文章)
    ↓
sources_with_engagement.json (HN + Reddit 数据)
    ↓
scored_sources.json (4 维度评分: 40% + 25% + 20% + 15%)
    ↓
selected_topics.json (3 深度 + 5 快讯)
    ↓
YYYY-MM-DD-ai-digest.md (LLM 生成)
    ↓
quality_report.json (6 项检查)
    ↓
Git commit & push (自动部署)
```

---

## 🚀 快速开始

```bash
# 1. 克隆仓库
git clone https://github.com/gaarry/blog-ai.git
cd blog-ai

# 2. 启动 Hugo 服务器
hugo server --buildDrafts

# 3. 访问 http://localhost:1313
```

---

## 📊 完整文档

请查看各个文档文件获取详细信息。
