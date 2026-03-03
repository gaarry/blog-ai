#!/usr/bin/env python3
"""
Article Generation Script
Uses Claude API to generate articles from selected topics
"""

import json
import os
import sys
from datetime import date
from pathlib import Path

# Only import anthropic if not in DRY_RUN mode
if os.getenv('DRY_RUN') != 'true':
    from anthropic import Anthropic

def load_system_prompt():
    """Load system prompt from file"""
    base_dir = Path(__file__).parent.parent
    prompt_file = base_dir / 'AI_DIGEST_SYSTEM_PROMPT.md'

    with open(prompt_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract the system prompt section
    start = content.find('```\n你是一个专业的 AI 资讯编辑助手')
    end = content.find('```', start + 3)

    if start != -1 and end != -1:
        return content[start+4:end].strip()
    else:
        # Fallback to a basic prompt
        return """你是一个专业的 AI 资讯编辑助手，负责生成每日 AI 行业资讯简报。

核心原则：
1. 仅使用英文一手信源，不使用任何中文媒体或翻译内容
2. 事实陈述，不添加主观评论或情绪化表达
3. 所有信息必须有可追溯的来源链接
4. 禁止使用营销词汇：震撼、颠覆、革命性、划时代等
5. 平等对待所有公司和产品，不接受商业推广

写作要求：
- 标题：陈述句，15-35 字，直接说明事件
- 正文：3-5 段，每段 2-4 句，逻辑清晰
- 关键要点：2-4 条，15-30 字，提炼核心洞察
- 来源：2-5 个一手信源，标题和域名清晰

你将收到今天筛选的主题和来源，请生成完整的 Markdown 文章。"""

def load_template():
    """Load article template"""
    base_dir = Path(__file__).parent.parent
    template_file = base_dir / 'BLOG_TEMPLATE.md'

    with open(template_file, 'r', encoding='utf-8') as f:
        return f.read()

def generate_article(selected_topics: dict, api_key: str) -> str:
    """Generate article using Claude API"""

    # Initialize Claude client
    client = Anthropic(api_key=api_key)

    # Load system prompt
    system_prompt = load_system_prompt()

    # Prepare input for Claude
    topics_json = json.dumps(selected_topics, indent=2, ensure_ascii=False)

    user_prompt = f"""请根据以下筛选的主题和来源，生成今日的 AI 资讯简报。

输入数据：
{topics_json}

要求：
1. 严格遵循 BLOG_TEMPLATE.md 中的格式
2. 每个深度文章包含：
   - <div class="article-section">
   - <h2><span class="article-num">编号</span>标题</h2>
   - 正文段落
   - <div class="key-tags">关键要点</div>
   - <div class="sources-list">来源链接</div>
3. 快讯使用 <div class="quick-news-section">
4. 所有事实必须有来源支撑
5. 禁止使用营销和夸张词汇

请生成完整的 Markdown 文件内容（包含 Front Matter）。"""

    print("🤖 调用 Claude API 生成文章...")

    try:
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=8000,
            temperature=0.3,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        article_content = message.content[0].text
        print("✅ 文章生成成功")
        return article_content

    except Exception as e:
        print(f"❌ API 调用失败: {e}")
        raise

def main():
    """Main generation function"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'
    content_dir = base_dir / 'content' / 'posts'

    # Check API key (skip in DRY_RUN mode)
    api_key = os.getenv('ANTHROPIC_API_KEY')
    dry_run = os.getenv('DRY_RUN') == 'true'

    if not api_key and not dry_run:
        print("❌ 错误: 未设置 ANTHROPIC_API_KEY 环境变量")
        print("请运行: export ANTHROPIC_API_KEY='your-api-key'")
        sys.exit(1)

    if dry_run:
        print("⚠️  DRY_RUN 模式: 跳过文章生成")
        print("✅ 如需生成文章，请设置 ANTHROPIC_API_KEY 并移除 DRY_RUN")
        sys.exit(0)

    # Load selected topics
    topics_file = data_dir / 'selected_topics.json'
    if not topics_file.exists():
        print(f"❌ 错误: {topics_file} 不存在")
        print("请先运行 select_topics.py")
        sys.exit(1)

    with open(topics_file, 'r', encoding='utf-8') as f:
        selected_topics = json.load(f)

    print(f"📖 读取主题: {len(selected_topics['deep_articles'])} 篇深度文章, {len(selected_topics['quick_news'])} 条快讯")

    # Generate article
    article_content = generate_article(selected_topics, api_key)

    # Save to file
    today = date.today().isoformat()
    output_file = content_dir / f'{today}-ai-digest.md'

    content_dir.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(article_content)

    print(f"💾 文章已保存: {output_file}")
    print(f"📄 文件大小: {output_file.stat().st_size} 字节")

    # Print summary
    lines = article_content.split('\n')
    article_sections = article_content.count('<div class="article-section">')
    quick_news = article_content.count('<div class="quick-news-item">')

    print(f"\n📊 生成统计:")
    print(f"  - 总行数: {len(lines)}")
    print(f"  - 深度文章: {article_sections} 篇")
    print(f"  - 快讯: {quick_news} 条")

if __name__ == '__main__':
    main()
