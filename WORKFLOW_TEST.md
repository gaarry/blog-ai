# 工作流测试指南

> 测试和验证 AI 资讯速览自动化工作流

---

## 快速测试

### 方法 1: 使用 Bash 脚本（推荐）

```bash
# 1. 设置 API Key
export ANTHROPIC_API_KEY="your-api-key"

# 2. 运行完整工作流
./scripts/run_workflow.sh

# 3. 预览生成的文章
hugo server --buildDrafts
```

### 方法 2: 逐步执行

```bash
# 1. 准备示例数据
cp data/examples/sources_raw.example.json data/sources_raw.json
cp data/examples/sources_with_engagement.example.json data/sources_with_engagement.json

# 2. 验证数据
python3 scripts/validate_data.py

# 3. 评分处理
python3 scripts/process_sources.py

# 4. 主题选择
python3 scripts/select_topics.py

# 5. 生成文章（需要 API Key）
export ANTHROPIC_API_KEY="your-api-key"
python3 scripts/generate_article.py

# 6. 质量检查
python3 scripts/quality_check.py

# 7. 查看结果
ls -lh content/posts/
cat data/quality_report.json
```

---

## 测试清单

### 环境准备

- [ ] Python 3.8+ 已安装
- [ ] Hugo 0.145.0+ 已安装
- [ ] Git 已配置
- [ ] ANTHROPIC_API_KEY 已设置

### 数据流测试

- [ ] **步骤 1**: sources_raw.json 生成成功
- [ ] **步骤 2**: sources_with_engagement.json 生成成功
- [ ] **步骤 3**: scored_sources.json 生成成功，评分合理
- [ ] **步骤 4**: selected_topics.json 生成成功，包含 3+5
- [ ] **步骤 5**: YYYY-MM-DD-ai-digest.md 生成成功
- [ ] **步骤 6**: quality_report.json 生成成功

### 内容质量测试

- [ ] 文章标题为陈述句，不含疑问或感叹
- [ ] 无禁用词汇（震撼、颠覆等）
- [ ] 每篇文章有 2-5 个来源
- [ ] 所有链接格式正确
- [ ] HTML 结构完整（article-section, key-tags, sources-list）
- [ ] 3 篇深度文章 + 3-5 条快讯

### 网站测试

- [ ] Hugo 构建无错误
- [ ] 本地预览正常显示
- [ ] 文章页面布局正确
- [ ] 所有链接可点击
- [ ] 分享按钮功能正常
- [ ] 响应式设计正常

---

## 预期输出

### 数据文件

```
data/
├── sources_raw.json              # ~50KB, 5 篇文章
├── sources_with_engagement.json  # ~60KB, 添加参与度数据
├── scored_sources.json           # ~70KB, 添加评分
├── selected_topics.json          # ~30KB, 3+5 选择
└── quality_report.json           # ~2KB, 质量报告
```

### 生成的文章

```
content/posts/
└── 2026-03-03-ai-digest.md      # ~15-20KB
```

**文章结构：**
- Front Matter（标题、日期、描述、标签）
- 3 个 article-section
- 每个 section 包含：
  - 编号标题
  - 3-5 段正文
  - 2-4 个 key-tags
  - 2-5 个来源链接
- 1 个 quick-news-section（3-5 条快讯）

### 质量报告

```json
{
  "date": "2026-03-03",
  "checks": [
    {"check": "banned_words", "status": "pass"},
    {"check": "html_structure", "status": "pass"},
    {"check": "link_validity", "status": "pass"},
    {"check": "source_count", "status": "pass"},
    {"check": "article_count", "status": "pass"}
  ],
  "all_passed": true,
  "score": 100
}
```

---

## 常见问题

### 1. API Key 错误

**症状：**
```
❌ 错误: 未设置 ANTHROPIC_API_KEY 环境变量
```

**解决：**
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

### 2. 数据文件不存在

**症状：**
```
❌ 错误: data/sources_raw.json 不存在
```

**解决：**
```bash
cp data/examples/sources_raw.example.json data/sources_raw.json
```

### 3. Schema 验证失败

**症状：**
```
❌ Validation failed for sources_raw.json
```

**解决：**
- 检查 JSON 格式是否正确
- 参考 data/examples/ 中的示例
- 使用 `cat data/sources_raw.json | jq '.'` 检查格式

### 4. 质量检查失败

**症状：**
```
❌ banned_words: 发现 3 个禁用词汇
```

**解决：**
- 查看 data/quality_report.json 了解详情
- 调整系统提示词
- 重新生成文章

### 5. Hugo 构建错误

**症状：**
```
Error: failed to unmarshal YAML
```

**解决：**
- 检查 Front Matter 格式
- 确保日期格式正确：`2026-03-03T20:00:00+08:00`
- 检查 YAML 缩进

---

## 性能基准

### 执行时间

| 步骤 | 预期时间 | 说明 |
|------|---------|------|
| 数据准备 | < 1 秒 | 复制示例文件 |
| 数据验证 | < 2 秒 | JSON Schema 验证 |
| 评分处理 | < 5 秒 | Python 脚本 |
| 主题选择 | < 3 秒 | Python 脚本 |
| 文章生成 | 30-60 秒 | Claude API 调用 |
| 质量检查 | < 5 秒 | Python 脚本 |
| **总计** | **~1-2 分钟** | 使用示例数据 |

### 资源使用

- 内存：< 500MB
- 磁盘：< 1MB（数据文件）
- 网络：~100KB（API 请求）

---

## 调试技巧

### 1. 查看中间数据

```bash
# 查看评分结果
cat data/scored_sources.json | jq '.sources[] | {id, score, title}' | head -20

# 查看选择的主题
cat data/selected_topics.json | jq '.deep_articles[] | {theme, category}'

# 查看质量报告
cat data/quality_report.json | jq '.checks'
```

### 2. 测试单个脚本

```bash
# 测试验证脚本
python3 scripts/validate_data.py

# 测试评分脚本
python3 scripts/process_sources.py

# 测试选择脚本
python3 scripts/select_topics.py
```

### 3. 查看日志

```bash
# 如果使用 OpenClaw
cat logs/ai-digest-$(date +%Y-%m-%d).log

# 如果使用 Bash 脚本
./scripts/run_workflow.sh 2>&1 | tee workflow.log
```

### 4. 验证生成的文章

```bash
# 检查文章结构
TODAY=$(date +%Y-%m-%d)
cat content/posts/${TODAY}-ai-digest.md | grep -E "article-section|article-num|key-tags|sources-list"

# 统计元素数量
cat content/posts/${TODAY}-ai-digest.md | grep -c "article-section"
cat content/posts/${TODAY}-ai-digest.md | grep -c "quick-news-item"
```

---

## 自动化测试

### 创建测试脚本

```bash
#!/bin/bash
# test_workflow.sh

set -e

echo "🧪 运行自动化测试..."

# 1. 准备测试环境
export DRY_RUN=true
export ANTHROPIC_API_KEY="test-key"

# 2. 运行工作流（跳过 API 调用）
./scripts/run_workflow.sh

# 3. 验证输出
if [ ! -f "data/scored_sources.json" ]; then
    echo "❌ scored_sources.json 未生成"
    exit 1
fi

if [ ! -f "data/selected_topics.json" ]; then
    echo "❌ selected_topics.json 未生成"
    exit 1
fi

echo "✅ 所有测试通过"
```

---

## 生产部署检查

### 部署前检查清单

- [ ] 所有脚本有执行权限（chmod +x）
- [ ] API Key 已安全存储（环境变量或密钥管理）
- [ ] Git 配置正确（用户名、邮箱）
- [ ] GitHub Actions 已配置
- [ ] 域名已正确设置
- [ ] 禁用词汇列表已更新

### 首次部署

```bash
# 1. 克隆仓库
git clone https://github.com/gaarry/blog-ai.git
cd blog-ai

# 2. 设置环境
export ANTHROPIC_API_KEY="your-api-key"

# 3. 测试运行
./scripts/run_workflow.sh

# 4. 验证结果
hugo server --buildDrafts

# 5. 部署
hugo --cleanDestinationDir
# 上传 public/ 目录到服务器
```

### 定时任务设置

**Cron (Linux/Mac):**
```bash
# 编辑 crontab
crontab -e

# 添加定时任务（每天 18:00）
0 18 * * * cd /path/to/blog-ai && /path/to/blog-ai/scripts/run_workflow.sh >> /var/log/ai-digest.log 2>&1
```

**GitHub Actions:**
```yaml
# .github/workflows/daily-digest.yml
name: Daily AI Digest

on:
  schedule:
    - cron: '0 10 * * *'  # UTC 10:00 = UTC+8 18:00
  workflow_dispatch:  # 允许手动触发

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install anthropic jsonschema requests

      - name: Run workflow
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          ./scripts/run_workflow.sh

      - name: Commit and push
        run: |
          git config user.name "GitHub Actions"
          git config user.email "actions@github.com"
          git add content/posts/ data/quality_report.json
          git commit -m "Add: AI资讯简报 $(date +%Y-%m-%d)" || exit 0
          git push
```

---

## 监控和维护

### 日常监控

```bash
# 检查最近生成的文章
ls -lt content/posts/ | head -5

# 查看最近的质量报告
cat data/quality_report.json | jq '.score'

# 检查 Git 提交历史
git log --oneline --grep="AI资讯简报" | head -10
```

### 定期维护

**每周：**
- 检查质量报告，查看是否有异常
- 更新禁用词汇列表
- 检查链接有效性

**每月：**
- 审查生成文章的质量
- 调整评分权重
- 更新系统提示词

**每季度：**
- 添加新的信源
- 评估 LLM 模型性能
- 优化工作流配置

---

## 故障恢复

### 回滚到上一个版本

```bash
# 查看最近的提交
git log --oneline | head -5

# 回滚到上一个版本
git revert HEAD

# 或者硬重置（谨慎使用）
git reset --hard HEAD~1
```

### 重新生成文章

```bash
# 删除今天的文章
rm content/posts/$(date +%Y-%m-%d)-ai-digest.md

# 重新运行工作流
./scripts/run_workflow.sh
```

---

## 参考资料

- [系统提示词](AI_DIGEST_SYSTEM_PROMPT.md)
- [数据流程](DATA_PIPELINE.md)
- [文章模板](BLOG_TEMPLATE.md)
- [自动化指南](AI_DIGEST_AUTOMATION_README.md)

---

**最后更新：** 2026-03-03
