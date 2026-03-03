# OpenClaw 部署检查清单

> 确保所有配置正确，可以顺利运行

---

## ✅ 部署前检查

### 1. 环境准备

- [ ] OpenClaw 已安装
  ```bash
  openclaw --version
  ```

  ```bash
  echo $ANTHROPIC_API_KEY
  # 应该输出: sk-ant-...
  ```

- [ ] Hugo 已安装（用于本地预览）
  ```bash
  hugo version
  # 应该输出: hugo v0.145.0 或更高
  ```

- [ ] Git 已配置
  ```bash
  git config user.name
  git config user.email
  ```

### 2. 配置文件检查

- [ ] 主配置文件存在
  ```bash
  ls -l .openclaw-config/task.yml
  ```

- [ ] 必读文档存在
  ```bash
  ls -l .openclaw-config/METHODOLOGY.md
  ls -l .openclaw-config/WRITING_GUIDE.md
  ls -l .openclaw-config/QUALITY_STANDARDS.md
  ```

- [ ] 模板文件存在
  ```bash
  ls -l .openclaw-config/templates/article-template.md
  ```

- [ ] 参考文件存在
  ```bash
  ls -l .openclaw-config/reference/sources-list.txt
  ls -l .openclaw-config/reference/banned-words.txt
  ```

- [ ] 数据结构定义存在
  ```bash
  ls -l .openclaw-config/data-schemas/*.json
  ```

- [ ] 数据示例存在
  ```bash
  ls -l .openclaw-config/data-examples/*.json
  ```

### 3. 目录结构检查

- [ ] 输出目录存在
  ```bash
  mkdir -p content/posts data logs
  ```

- [ ] 目录权限正确
  ```bash
  ls -ld content/posts data logs
  # 应该都是可写的
  ```

---

## 🧪 测试运行

### 步骤 1: 测试模式运行

```bash
# 使用 --dry-run 模式测试
openclaw run ai-digest --dry-run
```

**预期结果**：
- ✅ 配置文件加载成功
- ✅ 必读文档加载成功
- ✅ 任务目标理解正确
- ✅ 工具可用性检查通过

### 步骤 2: 单步测试

```bash
# 仅测试信源采集
openclaw run ai-digest --step collect_sources

# 检查输出
ls -lh data/sources_raw.json
cat data/sources_raw.json | jq '.metadata'
```

**预期结果**：
- ✅ 生成 `data/sources_raw.json`
- ✅ 文件大小 > 10KB
- ✅ 包含至少 50 篇文章

### 步骤 3: 完整测试

```bash
# 完整运行一次
openclaw run ai-digest
```

**预期结果**：
- ✅ 所有步骤成功执行
- ✅ 生成文章文件
- ✅ 质量检查通过（评分 >= 85）
- ✅ Git 提交成功

### 步骤 4: 验证输出

```bash
# 检查生成的文章
TODAY=$(date +%Y-%m-%d)
cat content/posts/${TODAY}-ai-digest.md | head -50

# 检查文章结构
grep -c "article-section" content/posts/${TODAY}-ai-digest.md
# 应该输出: 3

grep -c "quick-news-item" content/posts/${TODAY}-ai-digest.md
# 应该输出: 5

# 检查质量报告
cat data/quality_report.json | jq '.score'
# 应该输出: >= 85
```

### 步骤 5: 本地预览

```bash
# 启动 Hugo 服务器
hugo server --buildDrafts

# 在浏览器打开
open http://localhost:1313
```

**检查项**：
- ✅ 首页显示文章卡片
- ✅ 点击卡片可以进入详情页
- ✅ 文章详情页布局正确
- ✅ "来源" 部分显示正常
- ✅ "简讯" 部分显示正常
- ✅ 所有样式正常

---

## 🚀 生产部署

### 方式 1: 手动执行

```bash
# 每天 18:00 手动运行
openclaw run ai-digest
```

### 方式 2: Cron 定时任务

```bash
# 编辑 crontab
crontab -e

# 添加定时任务
0 18 * * * cd /Users/gary/git/blog-ai && /usr/local/bin/openclaw run ai-digest >> /var/log/ai-digest.log 2>&1

# 验证 crontab
crontab -l
```

### 方式 3: GitHub Actions

1. **添加 Secret**
   - 进入 GitHub 仓库设置
   - Settings → Secrets and variables → Actions
   - 添加 `ANTHROPIC_API_KEY`

2. **创建 Workflow**
   ```bash
   # 文件已存在
   ls -l .github/workflows/daily-digest.yml
   ```

3. **测试 Workflow**
   - 进入 GitHub Actions 页面
   - 点击 "Daily AI Digest"
   - 点击 "Run workflow"
   - 等待执行完成

4. **验证结果**
   ```bash
   git pull
   ls -l content/posts/
   ```

---

## 📊 监控设置

### 1. 日志监控

```bash
# 创建日志查看脚本
cat > scripts/check-logs.sh << 'EOF'
#!/bin/bash
TODAY=$(date +%Y-%m-%d)
LOG_FILE="logs/ai-digest-${TODAY}.log"

if [ -f "$LOG_FILE" ]; then
    echo "=== 今天的日志 ==="
    tail -100 "$LOG_FILE"

    echo ""
    echo "=== 错误统计 ==="
    grep -i "error" "$LOG_FILE" | wc -l
else
    echo "今天还没有日志"
fi
EOF

chmod +x scripts/check-logs.sh
```

### 2. 质量监控

```bash
# 创建质量检查脚本
cat > scripts/check-quality.sh << 'EOF'
#!/bin/bash
echo "=== 最近 7 天的质量评分 ==="
for i in {0..6}; do
    date=$(date -v-${i}d +%Y-%m-%d 2>/dev/null || date -d "-${i} days" +%Y-%m-%d)
    report="data/quality_report_${date}.json"
    if [ -f "$report" ]; then
        score=$(cat "$report" | jq '.score')
        status=$(cat "$report" | jq -r '.grade')
        echo "${date}: ${score} (${status})"
    fi
done
EOF

chmod +x scripts/check-quality.sh
```

### 3. 告警设置

```bash
# 创建告警脚本
cat > scripts/alert.sh << 'EOF'
#!/bin/bash
TODAY=$(date +%Y-%m-%d)
REPORT="data/quality_report.json"

if [ -f "$REPORT" ]; then
    score=$(cat "$REPORT" | jq '.score')

    if [ "$score" -lt 80 ]; then
        echo "⚠️ 警告: 质量评分过低 ($score)"
        # 发送邮件或通知
        # mail -s "AI资讯质量告警" admin@example.com < "$REPORT"
    fi
fi
EOF

chmod +x scripts/alert.sh
```

---

## 🔧 故障排查

### 常见问题

#### 问题 1: OpenClaw 未找到

```bash
# 检查安装
which openclaw

# 重新安装
npm install -g openclaw
```


```bash
# 检查环境变量
echo $ANTHROPIC_API_KEY

# 重新设置

# 或添加到配置文件
source ~/.zshrc
```

#### 问题 3: 权限错误

```bash
# 检查目录权限
ls -ld content/posts data logs

# 修复权限
chmod 755 content/posts data logs
```

#### 问题 4: Git 错误

```bash
# 检查 Git 状态
git status

# 检查远程仓库
git remote -v

# 重新配置
git config user.name "Your Name"
git config user.email "your@email.com"
```

### 调试模式

```bash
# 启用详细日志
openclaw run ai-digest --verbose

# 启用调试模式
openclaw run ai-digest --debug

# 仅运行特定步骤
openclaw run ai-digest --step collect_sources
```

---

## 📈 性能优化

### 1. 加速采集

```yaml
# 修改 task.yml
concurrency:
  max_parallel_fetches: 20  # 增加并发数（原 10）
```

### 2. 使用更快的模型

```yaml
# 修改 task.yml
model: claude-sonnet-4-6  # 更快更便宜（原 opus）
```

### 3. 启用缓存

```yaml
# 修改 task.yml
cache:
  enabled: true
  ttl: 3600
```

### 4. 减少重试次数

```yaml
# 修改 task.yml
quality_requirements:
  max_retries: 1  # 减少重试（原 2）
```

---

## 📝 维护计划

### 每天

- [ ] 检查执行日志
  ```bash
  ./scripts/check-logs.sh
  ```

- [ ] 检查质量报告
  ```bash
  ./scripts/check-quality.sh
  ```

### 每周

- [ ] 审查生成的文章质量
- [ ] 更新禁用词汇列表
- [ ] 检查信源可用性

### 每月

- [ ] 评估评分算法效果
- [ ] 调整权重配置
- [ ] 更新系统提示词
- [ ] 添加新信源

### 每季度

- [ ] 全面审查系统性能
- [ ] 优化工作流配置
- [ ] 升级依赖版本
- [ ] 评估 AI 模型效果

---

## ✅ 部署完成检查

### 最终验证

- [ ] 测试运行成功
- [ ] 生成的文章质量 >= 85 分
- [ ] 网站预览正常
- [ ] Git 提交成功
- [ ] 定时任务配置完成
- [ ] 监控脚本就绪
- [ ] 告警机制配置完成

### 文档归档

- [ ] 保存部署日期和版本
  ```bash
  echo "部署日期: $(date)" >> DEPLOYMENT_LOG.md
  echo "OpenClaw 版本: $(openclaw --version)" >> DEPLOYMENT_LOG.md
  echo "配置版本: 2.0.0" >> DEPLOYMENT_LOG.md
  ```

- [ ] 备份配置文件
  ```bash
  tar -czf openclaw-config-backup-$(date +%Y%m%d).tar.gz .openclaw-config/
  ```

---

## 🎉 部署成功！

现在系统已经完全配置好，可以自动运行了。

**下一步**：
1. 等待第一次自动执行（每天 18:00）
2. 或者手动触发一次：`openclaw run ai-digest`
3. 查看生成的文章并分享

**获取帮助**：
- 文档：`.openclaw-config/README.md`
- 快速开始：`.openclaw-config/QUICKSTART.md`
- Issues：https://github.com/gaarry/blog-ai/issues

---

**最后更新**：2026-03-03

**维护者**：Gary Yao
