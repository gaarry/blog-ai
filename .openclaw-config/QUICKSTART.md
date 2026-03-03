# OpenClaw 快速开始指南

> 5 分钟部署 AI 资讯自动生成系统

---

## 🚀 快速开始

### 步骤 1: 安装 OpenClaw

```bash
# 使用 npm 安装（推荐）
npm install -g openclaw

# 或使用 yarn
yarn global add openclaw

# 验证安装
openclaw --version
```

### 步骤 2: 进入项目目录

```bash
cd /Users/gary/git/blog-ai
```

### 步骤 3: 运行任务

```bash
# 方式 1: 直接运行（推荐）
openclaw run ai-digest

# 方式 2: 指定配置文件
openclaw run --config .openclaw-config/task.yml

# 方式 3: 测试模式（不实际发布）
openclaw run ai-digest --dry-run
```

### 步骤 4: 查看结果

```bash
# 查看生成的文章
ls -l content/posts/

# 查看今天的文章
cat content/posts/$(date +%Y-%m-%d)-ai-digest.md

# 查看质量报告
cat data/quality_report.json | jq '.'

# 本地预览网站
hugo server --buildDrafts
# 访问 http://localhost:1313
```

---

## 📋 预期输出

### 执行过程

```
[OpenClaw] Starting task: ai-digest
[OpenClaw] Reading configuration...
[OpenClaw] Loading required documents...
  ✓ METHODOLOGY.md
  ✓ WRITING_GUIDE.md
  ✓ QUALITY_STANDARDS.md
  ✓ article-template.md

[Step 1/6] Collecting sources...
  ✓ Fetched 20 sources
  ✓ Extracted 156 articles
  ✓ Saved to data/sources_raw.json

[Step 2/6] Scoring articles...
  ✓ Scored 87 articles
  ✓ Top score: 95.3
  ✓ Saved to data/scored_sources.json

[Step 3/6] Selecting topics...
  ✓ Selected 3 deep articles
  ✓ Selected 5 quick news
  ✓ Saved to data/selected_topics.json

[Step 4/6] Generating article...
  ✓ Generated 18,543 bytes
  ✓ Saved to content/posts/2026-03-03-ai-digest.md

[Step 5/6] Quality check...
  ✓ banned_words: PASS
  ✓ html_structure: PASS
  ✓ link_validity: PASS
  ✓ source_count: PASS
  ✓ article_count: PASS
  ✓ duplicate_content: PASS
  Score: 100/100
  ✓ Saved to data/quality_report.json

[Step 6/6] Git commit...
  ✓ Added content/posts/2026-03-03-ai-digest.md
  ✓ Committed: Add: AI资讯简报 2026-03-03
  ✓ Pushed to origin/main

[OpenClaw] Task completed successfully!
Time: 75 minutes
```

### 生成的文件

```
blog-ai/
├── content/posts/
│   └── 2026-03-03-ai-digest.md      # 生成的文章（18KB）
├── data/
│   ├── sources_raw.json              # 原始采集（50KB）
│   ├── scored_sources.json           # 评分结果（70KB）
│   ├── selected_topics.json          # 选中主题（30KB）
│   └── quality_report.json           # 质量报告（2KB）
└── logs/
    └── ai-digest-2026-03-03.log      # 执行日志（10KB）
```

---

## ⚙️ 配置说明

### 任务配置文件

主配置文件：`.openclaw-config/task.yml`

**关键配置项**：

```yaml
name: ai-digest                    # 任务名称
model: claude-opus-4-6            # AI 模型
objective: |                      # 任务目标
  生成今天的 AI 资讯简报...

required_reading:                 # 必读文档
  - METHODOLOGY.md
  - WRITING_GUIDE.md
  - QUALITY_STANDARDS.md

quality_requirements:             # 质量要求
  min_score: 85                   # 最低评分
  max_retries: 2                  # 最大重试次数

timeout: 7200                     # 超时时间（秒）
```

### 修改配置

#### 1. 更换 AI 模型

```yaml
# 使用更快更便宜的 Sonnet
model: claude-sonnet-4-6

# 使用 GPT-4
model: gpt-4-turbo
```

#### 2. 调整文章数量

编辑 `task.yml` 中的 `objective`：

```yaml
objective: |
  生成今天的 AI 资讯简报，包括：
  - 5 篇深度文章（修改这里）
  - 10 条快讯（修改这里）
```

#### 3. 添加新信源

编辑 `.openclaw-config/reference/sources-list.txt`：

```
新信源名称 | https://example.com | https://example.com/feed.xml
```

#### 4. 更新禁用词汇

编辑 `.openclaw-config/reference/banned-words.txt`：

```
新禁用词汇1
新禁用词汇2
```

---

## 🔧 常见问题


**错误**：
```
Error: ANTHROPIC_API_KEY not found
```

**解决**：
```bash
```

### Q2: OpenClaw 命令未找到

**错误**：
```
command not found: openclaw
```

**解决**：
```bash
npm install -g openclaw
# 或检查 PATH
echo $PATH
```

### Q3: 任务超时

**错误**：
```
Error: Task timeout after 7200 seconds
```

**解决**：
修改 `task.yml` 中的 `timeout`：
```yaml
timeout: 10800  # 3 小时
```

### Q4: 质量检查失败

**错误**：
```
Quality check failed: score 75 < 85
```

**解决**：
```bash
# 查看质量报告
cat data/quality_report.json | jq '.checks[] | select(.status == "fail")'

# 重新运行
openclaw run ai-digest --retry
```

### Q5: Git 提交失败

**错误**：
```
Error: Git push failed
```

**解决**：
```bash
# 检查 Git 状态
git status

# 手动提交
git add content/posts/*.md
git commit -m "Add: AI资讯简报 $(date +%Y-%m-%d)"
git push
```

---

## 🤖 自动化部署

### 方式 1: Cron（Linux/Mac）

```bash
# 编辑 crontab
crontab -e

# 添加定时任务（每天 18:00）
0 18 * * * cd /Users/gary/git/blog-ai && /usr/local/bin/openclaw run ai-digest >> /var/log/ai-digest.log 2>&1
```

### 方式 2: Systemd Timer（Linux）

创建 `/etc/systemd/system/ai-digest.service`：

```ini
[Unit]
Description=AI Digest Generator
After=network.target

[Service]
Type=oneshot
User=gary
WorkingDirectory=/Users/gary/git/blog-ai
Environment="ANTHROPIC_API_KEY=sk-ant-..."
ExecStart=/usr/local/bin/openclaw run ai-digest

[Install]
WantedBy=multi-user.target
```

创建 `/etc/systemd/system/ai-digest.timer`：

```ini
[Unit]
Description=Run AI Digest daily at 18:00
Requires=ai-digest.service

[Timer]
OnCalendar=daily
OnCalendar=18:00
Persistent=true

[Install]
WantedBy=timers.target
```

启用：

```bash
sudo systemctl enable ai-digest.timer
sudo systemctl start ai-digest.timer
```

### 方式 3: GitHub Actions

创建 `.github/workflows/daily-digest.yml`：

```yaml
name: Daily AI Digest

on:
  schedule:
    - cron: '0 10 * * *'  # UTC 10:00 = 北京 18:00
  workflow_dispatch:      # 允许手动触发

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install OpenClaw
        run: npm install -g openclaw

      - name: Run Task
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: openclaw run ai-digest

      - name: Commit and Push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add content/posts/ data/
          git commit -m "Add: AI资讯简报 $(date +%Y-%m-%d)" || exit 0
          git push
```

---

## 📊 监控和日志

### 查看实时日志

```bash
# 实时查看日志
tail -f logs/ai-digest-$(date +%Y-%m-%d).log

# 查看最近 100 行
tail -100 logs/ai-digest-$(date +%Y-%m-%d).log

# 搜索错误
grep -i "error" logs/ai-digest-*.log
```

### 监控质量趋势

```bash
# 查看最近 7 天的质量评分
for i in {0..6}; do
  date=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "-${i} days" +%Y-%m-%d)
  if [ -f "data/quality_report_${date}.json" ]; then
    score=$(cat data/quality_report_${date}.json | jq '.score')
    echo "${date}: ${score}"
  fi
done
```

### 统计执行时间

```bash
# 提取执行时间
grep "Time:" logs/ai-digest-*.log | awk '{print $2}'
```

---

## 🎓 进阶使用

### 1. 自定义评分权重

编辑 `METHODOLOGY.md`，修改权重说明：

```markdown
## 评分算法

- 多源交叉验证: 50%（原 40%）
- 社区参与度: 20%（原 25%）
- 来源权威性: 20%（不变）
- 时效性: 10%（原 15%）
```

### 2. 添加新的质量检查

编辑 `QUALITY_STANDARDS.md`，添加新的检查项：

```markdown
### 7. 图片质量检查（WARN 级别）

**检查内容**：文章中的图片必须清晰可访问

...
```

### 3. 使用不同的模板

创建新模板 `.openclaw-config/templates/custom-template.md`

修改 `task.yml`：

```yaml
references:
  - path: .openclaw-config/templates/custom-template.md
    description: 自定义文章模板
```

---

## 📞 获取帮助

### 文档

- **本项目**: `/Users/gary/git/blog-ai/.openclaw-config/README.md`
- **OpenClaw 官方**: https://openclaw.dev/docs
- **Claude API**: https://docs.anthropic.com/

### 社区

- **GitHub Issues**: https://github.com/gaarry/blog-ai/issues
- **OpenClaw Discord**: https://discord.gg/openclaw

### 联系方式

- **Email**: gary@example.com
- **Twitter**: @gary_yao

---

**祝你使用愉快！** 🎉

如有问题，请查看 [README.md](.openclaw-config/README.md) 或提交 Issue。
