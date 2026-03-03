# 快速开始指南

> 5 分钟快速测试 AI 资讯速览自动化系统

---

## 🚀 最快速的测试方式

```bash
# 1. 设置 API Key
export ANTHROPIC_API_KEY="sk-ant-your-api-key-here"

# 2. 运行工作流
./scripts/run_workflow.sh

# 3. 预览结果
hugo server --buildDrafts
# 访问 http://localhost:1313
```

**就这么简单！** 🎉

---

## 📋 详细步骤

### 步骤 1: 获取 Claude API Key

1. 访问 https://console.anthropic.com/
2. 登录或注册账号
3. 进入 API Keys 页面
4. 创建新的 API Key
5. 复制 API Key（格式：`sk-ant-...`）

### 步骤 2: 设置环境变量

```bash
# 临时设置（仅当前终端有效）
export ANTHROPIC_API_KEY="sk-ant-your-api-key-here"

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export ANTHROPIC_API_KEY="sk-ant-your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

### 步骤 3: 运行工作流

```bash
cd /path/to/blog-ai
./scripts/run_workflow.sh
```

**预期输出：**
```
========================================
AI 资讯速览 - 自动化工作流
========================================

📋 检查环境...
✅ 环境检查通过

步骤 1/7: 准备数据
✅ 数据准备完成

步骤 2/7: 验证数据格式
✅ sources_raw.json is valid
✅ sources_with_engagement.json is valid

步骤 3/7: 评分处理
📊 Scoring articles...
✅ Scored 5 articles
🏆 Top 10 articles:
  1. [95.2] Our agreement with the Department of Defense
  ...

步骤 4/7: 主题选择
🎯 Selecting topics...
✅ Selected 3 deep articles
✅ Selected 5 quick news items

步骤 5/7: 生成文章
🤖 调用 Claude API 生成文章...
✅ 文章生成成功
💾 文章已保存: content/posts/2026-03-03-ai-digest.md

步骤 6/7: 质量检查
🔍 检查文章: content/posts/2026-03-03-ai-digest.md
  ✅ banned_words: 未发现禁用词汇
  ✅ html_structure: 所有必需元素存在
  ✅ link_validity: 找到 15 个链接
  ✅ source_count: 来源数量合适 (平均 3.0 个/篇)
  ✅ article_count: 文章数量正确 (3 深度, 5 快讯)
总体评分: 100/100
✅ 质量检查通过

步骤 7/7: Git 提交
✅ Git 提交完成
是否推送到远程仓库? (y/N):

========================================
✅ 工作流执行完成！
========================================
```

### 步骤 4: 预览网站

```bash
# 启动 Hugo 服务器
hugo server --buildDrafts

# 在浏览器打开
open http://localhost:1313
```

---

## 🎯 验证清单

运行完成后，检查以下内容：

### ✅ 数据文件已生成

```bash
ls -lh data/*.json
```

应该看到：
- `data/sources_raw.json` (~50KB)
- `data/sources_with_engagement.json` (~60KB)
- `data/scored_sources.json` (~70KB)
- `data/selected_topics.json` (~30KB)
- `data/quality_report.json` (~2KB)

### ✅ 文章已生成

```bash
TODAY=$(date +%Y-%m-%d)
cat content/posts/${TODAY}-ai-digest.md | head -50
```

应该看到：
- Front Matter（标题、日期、描述）
- 3 个 `<div class="article-section">`
- 多个 `<div class="key-tags">`
- 多个 `<div class="sources-list">`
- 1 个 `<div class="quick-news-section">`

### ✅ 质量检查通过

```bash
cat data/quality_report.json | jq '.score'
```

应该看到：`95` 或更高

### ✅ 网站可以访问

访问 http://localhost:1313 应该看到：
- 首页显示文章卡片
- 点击卡片可以进入文章详情页
- 文章详情页布局正确
- 所有样式正常显示

---

## 🐛 常见问题

### 问题 1: API Key 错误

**错误信息：**
```
❌ 错误: 未设置 ANTHROPIC_API_KEY 环境变量
```

**解决方法：**
```bash
export ANTHROPIC_API_KEY="sk-ant-your-api-key"
```

### 问题 2: Python 模块缺失

**错误信息：**
```
ModuleNotFoundError: No module named 'anthropic'
```

**解决方法：**
```bash
pip install anthropic jsonschema requests
```

### 问题 3: 权限错误

**错误信息：**
```
Permission denied: ./scripts/run_workflow.sh
```

**解决方法：**
```bash
chmod +x scripts/*.sh scripts/*.py
```

### 问题 4: Git 错误

**错误信息：**
```
fatal: not a git repository
```

**解决方法：**
```bash
# 确保在正确的目录
cd /path/to/blog-ai

# 或者跳过 Git 操作
export DRY_RUN=true
./scripts/run_workflow.sh
```

---

## 📖 下一步

### 了解更多

- [完整测试指南](WORKFLOW_TEST.md) - 详细的测试和调试指南
- [数据流程](DATA_PIPELINE.md) - 了解数据处理流程
- [系统提示词](AI_DIGEST_SYSTEM_PROMPT.md) - 了解生成规则
- [自动化指南](AI_DIGEST_AUTOMATION_README.md) - 生产部署指南

### 自定义配置

#### 调整评分权重

编辑 `scripts/process_sources.py`：
```python
weights = {
    'cross_verification': 0.40,    # 多源交叉验证
    'community_engagement': 0.25,  # 社区参与度
    'source_authority': 0.20,      # 来源权威性
    'timeliness': 0.15             # 时效性
}
```

#### 修改文章数量

编辑 `scripts/select_topics.py`：
```python
deep_articles = select_deep_articles(scored_sources, min_score=70)  # 3 篇
quick_news = select_quick_news(scored_sources, deep_articles, count=5)  # 5 条
```

#### 更新禁用词汇

编辑 `data/banned_words.txt`：
```
# 添加新的禁用词汇
新词汇1
新词汇2
```

### 定时执行

#### 使用 Cron（Linux/Mac）

```bash
# 编辑 crontab
crontab -e

# 添加定时任务（每天 18:00）
0 18 * * * cd /path/to/blog-ai && /path/to/blog-ai/scripts/run_workflow.sh >> /var/log/ai-digest.log 2>&1
```

#### 使用 GitHub Actions

参考 `.github/workflows/deploy.yml` 创建自动化工作流。

---

## 💡 使用技巧

### 1. 测试模式（不提交 Git）

```bash
export DRY_RUN=true
./scripts/run_workflow.sh
```

### 2. 仅生成不推送

运行脚本时，在提示推送时选择 `N`。

### 3. 查看详细日志

```bash
./scripts/run_workflow.sh 2>&1 | tee workflow.log
```

### 4. 单独运行某个步骤

```bash
# 仅评分
python3 scripts/process_sources.py

# 仅选择主题
python3 scripts/select_topics.py

# 仅生成文章
python3 scripts/generate_article.py
```

### 5. 使用不同的 LLM

编辑 `scripts/generate_article.py`：
```python
# 使用 GPT-4
from openai import OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
```

---

## 🎓 学习资源

### 视频教程

（如果有的话，添加链接）

### 示例文章

- [示例 1](content/posts/2026-03-02-ai-digest.md) - 完整的文章示例
- [数据示例](data/examples/) - 各阶段数据示例

### API 文档

- [Claude API](https://docs.anthropic.com/)
- [Hugo 文档](https://gohugo.io/documentation/)

---

## 📞 获取帮助

### 问题反馈

- GitHub Issues: https://github.com/gaarry/blog-ai/issues
- 邮件: your@email.com

### 社区

- 参考网站: https://ai-digest.liziran.com/zh/
- 方法论: https://ai-digest.liziran.com/zh/methodology

---

## ⚡ 快速命令参考

```bash
# 完整工作流
./scripts/run_workflow.sh

# 测试模式（不提交）
DRY_RUN=true ./scripts/run_workflow.sh

# 验证数据
python3 scripts/validate_data.py

# 质量检查
python3 scripts/quality_check.py

# 预览网站
hugo server --buildDrafts

# 构建网站
hugo --cleanDestinationDir

# 查看日志
cat logs/*.log

# 查看质量报告
cat data/quality_report.json | jq '.'
```

---

**祝你使用愉快！** 🎉

如有问题，请参考 [WORKFLOW_TEST.md](WORKFLOW_TEST.md) 获取详细的故障排查指南。
