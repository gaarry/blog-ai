# AI 资讯速览 - OpenClaw 配置包

> 完整的自动化配置，让 OpenClaw AI Agent 自主生成每日 AI 资讯简报

---

## 📦 这个配置包是什么？

这是一个 **即插即用** 的 OpenClaw 配置包，包含：

- ✅ **完整的方法论和写作规范**
- ✅ **数据结构定义和示例**
- ✅ **质量标准和检查规则**
- ✅ **OpenClaw 任务配置**

你只需要：

```bash
# 1. 部署 OpenClaw
openclaw init


# 3. 运行任务
openclaw run ai-digest

# 完成！AI 会自动完成所有工作
```

---

## 📁 文件结构

```
.openclaw-config/
├── README.md                          # 本文件
├── task.yml                           # OpenClaw 任务配置（核心）
├── METHODOLOGY.md                     # 方法论（AI 必读）
├── WRITING_GUIDE.md                   # 写作规范（AI 必读）
├── QUALITY_STANDARDS.md               # 质量标准（AI 必读）
├── data-schemas/                      # 数据结构定义
│   ├── sources_raw.schema.json
│   ├── scored_sources.schema.json
│   └── selected_topics.schema.json
├── data-examples/                     # 数据示例
│   ├── sources_raw.example.json
│   ├── scored_sources.example.json
│   └── selected_topics.example.json
├── templates/                         # 文章模板
│   └── article-template.md
└── reference/                         # 参考资料
    ├── banned-words.txt               # 禁用词汇
    └── sources-list.txt               # 信源列表
```

---

## 🎯 AI 的工作流程

OpenClaw AI Agent 会自主完成以下步骤：

### 1. 采集信源（30 分钟）
- 读取 `reference/sources-list.txt`
- 使用 `WebFetch` 工具采集 20+ 英文信源
- 提取标题、摘要、链接、发布时间
- 保存到 `data/sources_raw.json`

### 2. 评分和筛选（10 分钟）
- 读取 `METHODOLOGY.md` 了解评分算法
- 对每篇文章进行 4 维度评分：
  - 多源交叉验证 (40%)
  - 社区参与度 (25%)
  - 来源权威性 (20%)
  - 时效性 (15%)
- 保存到 `data/scored_sources.json`

### 3. 主题选择（5 分钟）
- 选择 3 篇深度文章（评分 > 70）
- 选择 5 条快讯（评分 > 50）
- 确保主题多样性（不同类别）
- 保存到 `data/selected_topics.json`

### 4. 生成文章（20 分钟）
- 读取 `WRITING_GUIDE.md` 了解写作规范
- 读取 `templates/article-template.md` 了解格式
- 使用 Claude API 生成文章
- 保存到 `content/posts/YYYY-MM-DD-ai-digest.md`

### 5. 质量检查（5 分钟）
- 读取 `QUALITY_STANDARDS.md` 了解质量标准
- 检查禁用词汇（`reference/banned-words.txt`）
- 检查 HTML 结构完整性
- 检查来源数量和链接有效性
- 保存报告到 `data/quality_report.json`

### 6. 提交和部署（5 分钟）
- Git add + commit
- Git push
- Hugo 自动部署（GitHub Actions）

**总耗时：~75 分钟**

---

## 🚀 快速开始

### 前置要求

1. **OpenClaw 已安装**
   ```bash
   npm install -g openclaw
   # 或参考 OpenClaw 官方文档
   ```

   ```bash
   ```

3. **Hugo 已安装**（用于本地预览）
   ```bash
   brew install hugo
   ```

### 首次运行

```bash
# 1. 进入项目目录
cd /path/to/blog-ai

# 2. 初始化 OpenClaw（如果还没有）
openclaw init

# 3. 运行任务
openclaw run ai-digest

# 4. 查看生成的文章
ls -l content/posts/

# 5. 本地预览
hugo server --buildDrafts
# 访问 http://localhost:1313
```

### 定时执行

**方式 1: Cron（Linux/Mac）**
```bash
crontab -e
# 添加：每天 18:00 执行
0 18 * * * cd /path/to/blog-ai && openclaw run ai-digest
```

**方式 2: GitHub Actions**
```yaml
name: Daily AI Digest
on:
  schedule:
    - cron: '0 10 * * *'  # UTC 10:00 = 北京 18:00
jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run OpenClaw
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          npm install -g openclaw
          openclaw run ai-digest
```

---

## 📊 监控和维护

### 查看执行日志

```bash
# 查看最近的日志
tail -f logs/ai-digest-$(date +%Y-%m-%d).log

# 查看质量报告
cat data/quality_report.json | jq '.'
```

### 检查生成的文章

```bash
# 查看今天的文章
cat content/posts/$(date +%Y-%m-%d)-ai-digest.md

# 统计文章元素
grep -c "article-section" content/posts/$(date +%Y-%m-%d)-ai-digest.md
grep -c "quick-news-item" content/posts/$(date +%Y-%m-%d)-ai-digest.md
```

### 调整配置

如果需要调整：

1. **修改信源列表**：编辑 `reference/sources-list.txt`
2. **调整评分权重**：编辑 `METHODOLOGY.md` 中的权重说明
3. **更新禁用词汇**：编辑 `reference/banned-words.txt`
4. **修改写作风格**：编辑 `WRITING_GUIDE.md`

修改后，OpenClaw 会自动使用新配置。

---

## 🔧 故障排查


```bash
# 检查环境变量
echo $ANTHROPIC_API_KEY

# 重新设置
```

### 问题 2: 采集失败

查看日志：
```bash
tail -100 logs/ai-digest-$(date +%Y-%m-%d).log
```

常见原因：
- 网络问题
- 信源网站变更
- Rate limiting

### 问题 3: 质量检查失败

```bash
# 查看质量报告
cat data/quality_report.json | jq '.checks[] | select(.status == "fail")'
```

常见问题：
- 使用了禁用词汇
- HTML 结构不完整
- 来源数量不足

### 问题 4: Git 提交失败

```bash
# 检查 Git 状态
git status

# 手动提交
git add content/posts/*.md
git commit -m "Add: AI资讯简报 $(date +%Y-%m-%d)"
git push
```

---

## 📈 性能指标

### 预期指标

- **执行时间**: 60-90 分钟
- **采集文章数**: 100-200 篇
- **评分文章数**: 50-100 篇
- **选中深度文章**: 3 篇
- **选中快讯**: 5 条
- **质量评分**: > 85 分

### 监控告警

建议设置告警：
- 执行时间 > 120 分钟
- 质量评分 < 80 分
- 采集失败率 > 20%

---

## 🤝 贡献指南

### 添加新信源

1. 编辑 `reference/sources-list.txt`
2. 添加格式：`名称 | URL | RSS Feed (可选)`
3. 提交 PR

### 改进方法论

1. 编辑 `METHODOLOGY.md`
2. 说明改进原因
3. 提供测试数据
4. 提交 PR

### 报告问题

https://github.com/gaarry/blog-ai/issues

---

## 📄 许可证

MIT License

---

## 🙏 致谢

- 参考网站: https://ai-digest.liziran.com/zh/
- OpenClaw: https://github.com/openclaw/openclaw
- Claude API: https://anthropic.com

---

**最后更新**: 2026-03-03

**状态**: ✅ 生产就绪
