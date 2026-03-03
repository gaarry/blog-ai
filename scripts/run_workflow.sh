#!/bin/bash
# AI 资讯速览 - 完整工作流执行脚本
# 运行完整的数据处理和文章生成流程

set -e  # 遇到错误立即退出

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 获取脚本所在目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BASE_DIR="$(dirname "$SCRIPT_DIR")"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}AI 资讯速览 - 自动化工作流${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# 检查环境
echo -e "${YELLOW}📋 检查环境...${NC}"

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}❌ 错误: 未找到 python3${NC}"
    exit 1
fi

# 检查 API Key
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo -e "${RED}❌ 错误: 未设置 ANTHROPIC_API_KEY 环境变量${NC}"
    echo -e "${YELLOW}请运行: export ANTHROPIC_API_KEY='your-api-key'${NC}"
    exit 1
fi

echo -e "${GREEN}✅ 环境检查通过${NC}"
echo ""

# 步骤 1: 准备数据
echo -e "${BLUE}步骤 1/7: 准备数据${NC}"
cd "$BASE_DIR"
cp data/examples/sources_raw.example.json data/sources_raw.json
cp data/examples/sources_with_engagement.example.json data/sources_with_engagement.json
echo -e "${GREEN}✅ 数据准备完成${NC}"
echo ""

# 步骤 2: 验证数据
echo -e "${BLUE}步骤 2/7: 验证数据格式${NC}"
python3 scripts/validate_data.py
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ 数据验证失败${NC}"
    exit 1
fi
echo ""

# 步骤 3: 评分处理
echo -e "${BLUE}步骤 3/7: 评分处理${NC}"
python3 scripts/process_sources.py
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ 评分处理失败${NC}"
    exit 1
fi
echo ""

# 步骤 4: 主题选择
echo -e "${BLUE}步骤 4/7: 主题选择${NC}"
python3 scripts/select_topics.py
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ 主题选择失败${NC}"
    exit 1
fi
echo ""

# 步骤 5: 生成文章
echo -e "${BLUE}步骤 5/7: 生成文章${NC}"
python3 scripts/generate_article.py
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ 文章生成失败${NC}"
    exit 1
fi
echo ""

# 步骤 6: 质量检查
echo -e "${BLUE}步骤 6/7: 质量检查${NC}"
python3 scripts/quality_check.py
QUALITY_CHECK_RESULT=$?
if [ $QUALITY_CHECK_RESULT -ne 0 ]; then
    echo -e "${YELLOW}⚠️  质量检查未完全通过，但继续执行...${NC}"
fi
echo ""

# 步骤 7: Git 操作（可选）
if [ "$DRY_RUN" != "true" ]; then
    echo -e "${BLUE}步骤 7/7: Git 提交${NC}"

    # 检查是否有变更
    if git diff --quiet content/posts/; then
        echo -e "${YELLOW}⚠️  没有需要提交的变更${NC}"
    else
        TODAY=$(date +%Y-%m-%d)

        # Git add
        git add content/posts/*.md data/quality_report.json

        # Git commit
        git commit -m "Add: AI资讯简报 ${TODAY}

- 3 篇深度文章
- 5 条快讯
- 质量评分: $(cat data/quality_report.json | grep -o '\"score\": [0-9.]*' | cut -d' ' -f2)

Co-Authored-By: Automation Script <noreply@automation.com>"

        echo -e "${GREEN}✅ Git 提交完成${NC}"

        # Git push (需要用户确认)
        read -p "是否推送到远程仓库? (y/N): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            git push origin main
            echo -e "${GREEN}✅ 推送完成${NC}"
        else
            echo -e "${YELLOW}⚠️  跳过推送${NC}"
        fi
    fi
else
    echo -e "${YELLOW}⚠️  DRY_RUN 模式，跳过 Git 操作${NC}"
fi

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✅ 工作流执行完成！${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# 显示生成的文件
TODAY=$(date +%Y-%m-%d)
ARTICLE_FILE="content/posts/${TODAY}-ai-digest.md"

if [ -f "$ARTICLE_FILE" ]; then
    echo -e "${BLUE}📄 生成的文章:${NC}"
    echo -e "  ${ARTICLE_FILE}"
    echo -e "  大小: $(wc -c < "$ARTICLE_FILE") 字节"
    echo -e "  行数: $(wc -l < "$ARTICLE_FILE") 行"
    echo ""
fi

# 显示质量报告
if [ -f "data/quality_report.json" ]; then
    echo -e "${BLUE}📊 质量报告:${NC}"
    cat data/quality_report.json | python3 -m json.tool | grep -E "(check|status|message|score)" | head -20
    echo ""
fi

echo -e "${BLUE}💡 提示:${NC}"
echo -e "  - 查看文章: hugo server --buildDrafts"
echo -e "  - 访问: http://localhost:1313/"
echo -e "  - 构建: hugo --cleanDestinationDir"
