# AI 资讯速览自动化系统

> 基于 OpenClaw 的每日 AI 资讯自动生成系统

---

## 📋 目录

- [系统概述](#系统概述)
- [文件说明](#文件说明)
- [快速开始](#快速开始)
- [配置说明](#配置说明)
- [工作流程](#工作流程)
- [质量控制](#质量控制)
- [故障排查](#故障排查)
- [最佳实践](#最佳实践)

---

## 系统概述

这是一个完全自动化的 AI 资讯生成系统，每天自动完成以下工作：

1. ✅ 从 20+ 英文一手信源采集最新 AI 资讯
2. ✅ 基于多维度算法对信息进行评分和筛选
3. ✅ 使用 LLM 生成高质量的资讯简报
4. ✅ 自动质量检查，确保内容符合标准
5. ✅ 自动提交到 Git 并部署到网站

**核心特性：**
- 🤖 完全自动化，无需人工干预
- 📰 仅使用英文一手信源，避免二次失真
- 🎯 多层过滤机制，确保内容质量
- 🔍 严格质量检查，杜绝营销和夸张表述
- 📊 中立客观，事实为基础

---

## 文件说明

### 核心文件

| 文件 | 说明 |
|------|------|
| `AI_DIGEST_SYSTEM_PROMPT.md` | **系统提示词和生成规范**（最重要） |
| `.openclaw/ai-digest-workflow.yml` | OpenClaw 工作流配置文件 |
| `BLOG_TEMPLATE.md` | 文章模板 |
| `data/banned_words.txt` | 禁用词汇列表 |

### 目录结构

```
blog-ai/
├── .openclaw/
│   └── ai-digest-workflow.yml      # OpenClaw 工作流配置
├── content/posts/                   # 生成的文章
│   └── YYYY-MM-DD-ai-digest.md
├── data/
│   ├── banned_words.txt             # 禁用词汇
│   ├── sources_raw.json             # 原始采集数据
│   ├── scored_sources.json          # 评分后数据
│   ├── selected_topics.json         # 选中的主题
│   └── quality_report.json          # 质量报告
├── logs/
│   └── ai-digest-YYYY-MM-DD.log     # 执行日志
├── AI_DIGEST_SYSTEM_PROMPT.md       # 系统提示词
└── BLOG_TEMPLATE.md                 # 文章模板
```

---

## 快速开始

### 前置要求

1. **安装 OpenClaw**
   ```bash
   # 参考 OpenClaw 官方文档安装
   npm install -g openclaw
   ```

2. **配置 API Keys**
   ```bash
   # Claude API Key (推荐)
   export ANTHROPIC_API_KEY="your-api-key"

   # 或 OpenAI API Key (备用)
   export OPENAI_API_KEY="your-api-key"
   ```

3. **克隆仓库**
   ```bash
   git clone https://github.com/gaarry/blog-ai.git
   cd blog-ai
   ```

### 手动执行一次

```bash
# 执行工作流
openclaw run .openclaw/ai-digest-workflow.yml

# 查看生成的文章
ls -la content/posts/

# 预览网站
hugo server
```

### 设置定时任务

#### 方法 1: OpenClaw 内置调度

```bash
# 启动 OpenClaw 守护进程
openclaw daemon start

# 注册工作流（每天 18:00 执行）
openclaw schedule add .openclaw/ai-digest-workflow.yml

# 查看调度状态
openclaw schedule list
```

#### 方法 2: GitHub Actions

已配置自动部署，每次 push 到 main 分支时自动构建和部署。

如需定时生成，可以添加：

```yaml
# .github/workflows/daily-digest.yml
name: Daily AI Digest

on:
  schedule:
    - cron: '0 10 * * *'  # UTC 10:00 = UTC+8 18:00

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup OpenClaw
        run: npm install -g openclaw
      - name: Generate digest
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: openclaw run .openclaw/ai-digest-workflow.yml
      - name: Commit and push
        run: |
          git config user.name "OpenClaw Bot"
          git config user.email "bot@openclaw.com"
          git add content/posts/
          git commit -m "Add: AI资讯简报 $(date +%Y-%m-%d)"
          git push
```

#### 方法 3: Cron (Linux/Mac)

```bash
# 编辑 crontab
crontab -e

# 添加定时任务（每天 18:00）
0 18 * * * cd /path/to/blog-ai && openclaw run .openclaw/ai-digest-workflow.yml
```

---

## 配置说明

### 系统提示词配置

编辑 `AI_DIGEST_SYSTEM_PROMPT.md` 中的关键参数：

```markdown
## 核心原则

### 1. 信息来源原则
- 添加或删除信源
- 调整来源优先级

### 2. 信息筛选标准
- 调整评分权重
- 修改阈值

### 3. 写作原则
- 更新禁用词汇
- 调整语言风格
```

### 工作流配置

编辑 `.openclaw/ai-digest-workflow.yml`：

#### 修改执行时间

```yaml
schedule:
  cron: "0 10 * * *"  # 修改为你需要的时间
  timezone: "Asia/Shanghai"
```

#### 修改文章数量

```yaml
- name: select_topics
  config:
    selection_criteria:
      deep_articles:
        count: 3  # 修改深度文章数量
      quick_news:
        count: 5  # 修改快讯数量
```

#### 修改 LLM 模型

```yaml
- name: generate_article
  model: claude-3-5-sonnet-20241022  # 修改为其他模型
```

可选模型：
- `claude-3-5-sonnet-20241022` (推荐，质量最高)
- `claude-3-opus-20240229` (最强，但较慢)
- `gpt-4-turbo-preview` (OpenAI 备用)
- `gpt-4o` (OpenAI 最新)

#### 添加新的信源

```yaml
- name: collect_sources
  config:
    sources:
      - name: New Source
        url: https://example.com/blog
        type: rss
        feed: https://example.com/feed.xml
        priority: high
```

### 禁用词汇配置

编辑 `data/banned_words.txt`：

```
# 添加新的禁用词汇
新词汇1
新词汇2

# 删除不需要的词汇（注释掉）
# 某个词汇
```

---

## 工作流程

### 完整流程图

```
┌─────────────────────────────────────────────────────────────┐
│ 步骤 1: 信息采集 (10 分钟)                                    │
│ - 从 20+ 信源采集最新内容                                      │
│ - 提取标题、摘要、正文、发布时间                                │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 步骤 2: 社区参与度采集 (5 分钟)                                │
│ - 获取 HN 投票数、Reddit 讨论数                                │
│ - 匹配到步骤 1 的文章                                          │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 步骤 3: 算法评分 (3 分钟)                                      │
│ - 多源交叉验证评分 (40%)                                       │
│ - 社区参与度评分 (25%)                                         │
│ - 来源权威性评分 (20%)                                         │
│ - 时效性评分 (15%)                                            │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 步骤 4: 主题选择 (5 分钟)                                      │
│ - 选择 3 个深度主题 + 5 个快讯                                  │
│ - 确保主题多样性                                               │
│ - 检查近 7 天重复                                              │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 步骤 5: 内容生成 (10 分钟)                                     │
│ - LLM 阅读所有来源文章                                          │
│ - 综合信息，生成文章                                            │
│ - 遵循模板格式                                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 步骤 6: 质量检查 (2 分钟)                                      │
│ - 禁用词汇检查                                                 │
│ - 链接有效性检查                                               │
│ - HTML 结构检查                                                │
│ - 来源数量检查                                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 步骤 7: 发布 (3 分钟)                                          │
│ - Git commit                                                 │
│ - Git push                                                   │
│ - 触发 GitHub Actions 部署                                     │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│ 步骤 8: 通知 (1 分钟)                                          │
│ - 发送邮件/Slack 通知                                           │
│ - 包含文章链接和质量报告                                         │
└─────────────────────────────────────────────────────────────┘

总耗时: ~40 分钟
```

### 数据流

```
sources_raw.json
    ↓
sources_with_engagement.json
    ↓
scored_sources.json
    ↓
selected_topics.json
    ↓
YYYY-MM-DD-ai-digest.md
    ↓
quality_report.json
    ↓
Git commit & push
```

---

## 质量控制

### 自动检查项

1. **禁用词汇检查**
   - 扫描 `data/banned_words.txt` 中的词汇
   - 发现即失败，不会发布

2. **链接有效性检查**
   - 验证所有来源链接可访问
   - 失败仅警告，不阻止发布

3. **HTML 结构检查**
   - 必须包含：article-section, article-num, key-tags, sources-list
   - 缺少任一元素则失败

4. **来源数量检查**
   - 每篇深度文章：2-5 个来源
   - 少于 2 个或多于 5 个则失败

5. **文章数量检查**
   - 深度文章：必须 3 篇
   - 快讯：3-5 条

6. **重复内容检查**
   - 与近 7 天内容对比
   - 相似度 > 80% 则警告

### 质量报告

每次生成后会产生 `data/quality_report.json`：

```json
{
  "date": "2026-03-03",
  "checks": [
    {
      "check": "banned_words",
      "status": "pass",
      "message": "No banned words found"
    },
    {
      "check": "link_validity",
      "status": "pass",
      "message": "All 15 links are valid"
    },
    {
      "check": "html_structure",
      "status": "pass",
      "message": "All required elements present"
    }
  ],
  "all_passed": true,
  "score": 95
}
```

### 手动审核

虽然系统是自动化的，但建议定期抽查：

```bash
# 查看最近生成的文章
ls -lt content/posts/ | head -5

# 查看质量报告
cat data/quality_report.json | jq '.'

# 查看执行日志
tail -100 logs/ai-digest-$(date +%Y-%m-%d).log
```

---

## 故障排查

### 常见问题

#### 1. 工作流执行失败

**症状：** OpenClaw 报错退出

**排查：**
```bash
# 查看日志
cat logs/ai-digest-$(date +%Y-%m-%d).log

# 检查 API Key
echo $ANTHROPIC_API_KEY

# 手动测试某个步骤
openclaw run .openclaw/ai-digest-workflow.yml --step collect_sources
```

#### 2. 生成内容质量不佳

**症状：** 文章包含主观评论或夸张表述

**解决：**
1. 检查是否触发了禁用词汇检查
2. 更新 `data/banned_words.txt`
3. 调整系统提示词中的写作原则
4. 降低 LLM temperature 参数

#### 3. 采集不到内容

**症状：** `sources_raw.json` 为空或内容很少

**排查：**
```bash
# 检查网络连接
curl -I https://openai.com/blog

# 检查 RSS 订阅
curl https://openai.com/blog/rss.xml

# 检查 API 限流
# HN API: 每秒 10 次请求
```

#### 4. 链接失效

**症状：** 质量检查报告链接无效

**解决：**
- 链接失效仅警告，不阻止发布
- 可以手动修复生成的文章
- 或调整来源列表，移除失效的信源

#### 5. 重复内容

**症状：** 与近期文章内容重复

**解决：**
1. 检查 `data/history/` 目录
2. 调整重复检查阈值
3. 增加主题多样性权重

### 日志分析

```bash
# 查看今天的日志
cat logs/ai-digest-$(date +%Y-%m-%d).log

# 搜索错误
grep ERROR logs/ai-digest-$(date +%Y-%m-%d).log

# 搜索警告
grep WARN logs/ai-digest-$(date +%Y-%m-%d).log

# 查看执行时间
grep "execution_time" logs/ai-digest-$(date +%Y-%m-%d).log
```

---

## 最佳实践

### 1. 定期维护

**每周：**
- 检查质量报告，查看是否有异常
- 更新禁用词汇列表
- 检查来源列表，移除失效的信源

**每月：**
- 审查生成文章的质量
- 调整评分权重
- 更新系统提示词

**每季度：**
- 添加新的信源
- 评估 LLM 模型性能
- 优化工作流配置

### 2. 规则调整

**原则：只调整规则，不修改内容**

当发现问题时：
1. ❌ 不要：手动修改生成的文章
2. ✅ 应该：调整规则，重新生成

**示例：**

问题：标题过于夸张
```yaml
# 错误做法
# 手动修改文章标题

# 正确做法
# 1. 在 data/banned_words.txt 添加夸张词汇
# 2. 在系统提示词中强调标题规范
# 3. 重新生成
openclaw run .openclaw/ai-digest-workflow.yml
```

### 3. 监控指标

建议监控以下指标：

| 指标 | 正常范围 | 异常阈值 |
|------|---------|---------|
| 执行时间 | 30-45 分钟 | > 60 分钟 |
| 采集文章数 | 100-200 | < 50 |
| 质量评分 | 85-100 | < 80 |
| 链接有效率 | > 95% | < 90% |
| 发布成功率 | 100% | < 100% |

### 4. 备份策略

```bash
# 每周备份数据
tar -czf backup-$(date +%Y-%m-%d).tar.gz data/ content/posts/

# 保留最近 30 天的备份
find backup-*.tar.gz -mtime +30 -delete
```

### 5. 安全建议

- ✅ 使用环境变量存储 API Key
- ✅ 不要在代码中硬编码敏感信息
- ✅ 定期轮换 API Key
- ✅ 限制 Git 仓库访问权限
- ✅ 启用 GitHub Actions secrets

---

## 进阶配置

### 多语言支持

如需生成英文版本：

1. 复制工作流配置
   ```bash
   cp .openclaw/ai-digest-workflow.yml .openclaw/ai-digest-en-workflow.yml
   ```

2. 修改系统提示词
   ```yaml
   system_prompt: |
     You are a professional AI news editor...
     Write in English...
   ```

3. 修改输出路径
   ```yaml
   output:
     file: ${CONTENT_DIR}/{date}-ai-digest-en.md
   ```

### 自定义主题分类

编辑工作流配置：

```yaml
- name: select_topics
  config:
    selection_criteria:
      deep_articles:
        diversity:
          categories:
            - your_custom_category_1
            - your_custom_category_2
```

### 集成其他工具

#### Slack 通知

```yaml
- name: notify
  config:
    channels:
      - type: slack
        webhook: ${SLACK_WEBHOOK_URL}
```

#### Email 通知

```yaml
- name: notify
  config:
    channels:
      - type: email
        smtp_server: smtp.gmail.com
        smtp_port: 587
        username: ${EMAIL_USERNAME}
        password: ${EMAIL_PASSWORD}
```

---

## 参考资料

- [OpenClaw 官方文档](https://github.com/openclaw/openclaw)
- [Claude API 文档](https://docs.anthropic.com/)
- [Hugo 文档](https://gohugo.io/documentation/)
- [原始方法论](https://ai-digest.liziran.com/zh/methodology)

---

## 支持与反馈

- 提交 Issue: https://github.com/gaarry/blog-ai/issues
- 邮件: your@email.com

---

## 许可证

MIT License

---

**最后更新：** 2026-03-03
