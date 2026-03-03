# 🚀 从这里开始

> OpenClaw AI 资讯自动生成系统 - 即插即用配置包

---

## ✨ 这是什么？

一个完整的配置包，让 **OpenClaw AI Agent** 自动生成每日 AI 资讯简报。

**你只需要**：
1. 部署 OpenClaw
3. 运行 `openclaw run ai-digest`

**AI 会自动**：
- 采集 20+ 英文信源
- 评分和筛选
- 生成 3 篇深度文章 + 5 条快讯
- 质量检查
- Git 提交和发布

---

## 📦 配置包包含

```
.openclaw-config/
├── task.yml                    ⭐ OpenClaw 任务配置
├── METHODOLOGY.md              ⭐ 方法论（评分算法）
├── WRITING_GUIDE.md            ⭐ 写作规范
├── QUALITY_STANDARDS.md        ⭐ 质量标准
├── templates/                  📝 文章模板
├── reference/                  📚 信源和禁用词汇
├── data-schemas/               📐 数据结构定义
├── data-examples/              📊 数据示例
└── 文档（5 个）
```

**总计**: 19 个文件，全部准备就绪！

---

## ⚡ 2 步开始

### 1️⃣ 运行任务

```bash
openclaw run ai-digest
```

### 2️⃣ 查看结果

```bash
# 查看生成的文章
cat content/posts/$(date +%Y-%m-%d)-ai-digest.md

# 本地预览
hugo server --buildDrafts
```

---

## 📚 文档导航

### 🏃 快速开始
- **[QUICKSTART.md](QUICKSTART.md)** - 5 分钟快速开始指南

### 📋 部署指南
- **[DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)** - 完整部署检查清单

### 📖 详细说明
- **[README.md](README.md)** - 配置包完整说明
- **[PACKAGE_SUMMARY.md](PACKAGE_SUMMARY.md)** - 配置包总结

### 🔧 配置文件
- **[task.yml](task.yml)** - OpenClaw 任务配置（核心）
- **[METHODOLOGY.md](METHODOLOGY.md)** - 方法论和评分算法
- **[WRITING_GUIDE.md](WRITING_GUIDE.md)** - 写作规范和格式
- **[QUALITY_STANDARDS.md](QUALITY_STANDARDS.md)** - 质量标准和检查规则

---

## 🎯 工作流程

```
OpenClaw AI Agent 自主完成：

1. 读取配置文档（5 分钟）
   ↓
2. 采集英文信源（30 分钟）
   ↓
3. 评分和排序（10 分钟）
   ↓
4. 选择主题（5 分钟）
   ↓
5. 生成文章（20 分钟）
   ↓
6. 质量检查（5 分钟）
   ↓
7. Git 提交（5 分钟）

总计：~80 分钟
```

---

## ✅ 预期结果

### 生成的文章

- ✅ 3 篇深度文章（每篇 3-5 段，2-5 个来源）
- ✅ 5 条快讯（每条 1 句话 + 1 个来源）
- ✅ 完整的 HTML 结构
- ✅ 质量评分 >= 85

### 生成的数据

```
content/posts/YYYY-MM-DD-ai-digest.md    # 文章
data/sources_raw.json                     # 原始数据
data/scored_sources.json                  # 评分数据
data/selected_topics.json                 # 选中主题
data/quality_report.json                  # 质量报告
logs/ai-digest-YYYY-MM-DD.log            # 执行日志
```

---

## 🔧 常见调整

### 更换 AI 模型

编辑 `task.yml`:
```yaml
model: claude-sonnet-4-6  # 更快更便宜
```

### 调整文章数量

编辑 `task.yml`:
```yaml
objective: |
  - 5 篇深度文章（修改这里）
  - 10 条快讯（修改这里）
```

### 添加新信源

编辑 `reference/sources-list.txt`:
```
新信源 | https://example.com | https://example.com/feed
```

### 更新禁用词汇

编辑 `reference/banned-words.txt`:
```
新禁用词汇
```

---

## 🤖 定时执行

### Cron（推荐）

```bash
crontab -e
# 添加: 每天 18:00 执行
0 18 * * * cd /path/to/blog-ai && openclaw run ai-digest
```

### GitHub Actions

配置文件已准备好：`.github/workflows/daily-digest.yml`

只需添加 Secret: `ANTHROPIC_API_KEY`

---

## 💡 核心理念

### 为什么这样设计？

1. **AI 自主决策** - 不是执行脚本，而是理解任务后自主完成
2. **文档驱动** - 所有规则在文档中，修改文档即可调整行为
3. **质量优先** - 6 项自动检查，确保输出质量
4. **即插即用** - 一个配置包，立即可用

### 与传统脚本的区别

| 传统脚本 | OpenClaw AI |
|---------|-------------|
| 固定流程 | 灵活决策 |
| 硬编码规则 | 文档驱动 |
| 难以调整 | 修改文档即可 |
| 需要维护代码 | 只需维护文档 |

---

## 📞 获取帮助

### 文档

- 📖 [完整说明](README.md)
- 🏃 [快速开始](QUICKSTART.md)
- ✅ [部署清单](DEPLOYMENT_CHECKLIST.md)
- 📊 [配置总结](PACKAGE_SUMMARY.md)

### 社区

- 💬 [GitHub Issues](https://github.com/gaarry/blog-ai/issues)
- 📧 Email: gary@example.com

---

## 🎉 准备好了！

**现在就开始**：

```bash
# 1. 运行
openclaw run ai-digest

# 2. 查看结果
hugo server --buildDrafts
```

**或者先阅读**：

- 新手 → [QUICKSTART.md](QUICKSTART.md)
- 运维 → [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
- 开发 → [README.md](README.md)

---

**版本**: 2.0.0
**更新**: 2026-03-03
**状态**: ✅ 生产就绪

**祝你使用愉快！** 🚀
