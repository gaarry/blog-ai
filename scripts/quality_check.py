#!/usr/bin/env python3
"""
Quality Check Script
Validates generated article against quality standards
"""

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path
from typing import Dict, List
import requests

def load_banned_words() -> List[str]:
    """Load banned words from file"""
    base_dir = Path(__file__).parent.parent
    banned_file = base_dir / 'data' / 'banned_words.txt'

    words = []
    with open(banned_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                words.append(line)

    return words

def check_banned_words(content: str, banned_words: List[str]) -> Dict:
    """Check for banned words"""
    found_words = []

    for word in banned_words:
        if word in content:
            # Find all occurrences
            count = content.count(word)
            found_words.append({'word': word, 'count': count})

    if found_words:
        return {
            'status': 'fail',
            'message': f'发现 {len(found_words)} 个禁用词汇',
            'details': {'banned_words': found_words}
        }
    else:
        return {
            'status': 'pass',
            'message': '未发现禁用词汇',
            'details': {}
        }

def check_html_structure(content: str) -> Dict:
    """Check required HTML elements"""
    required_elements = {
        'article-section': r'<div class="article-section">',
        'article-num': r'<span class="article-num">',
        'key-tags': r'<div class="key-tags">',
        'sources-list': r'<div class="sources-list">'
    }

    missing = []
    counts = {}

    for element, pattern in required_elements.items():
        count = len(re.findall(pattern, content))
        counts[element] = count
        if count == 0:
            missing.append(element)

    if missing:
        return {
            'status': 'fail',
            'message': f'缺少必需元素: {", ".join(missing)}',
            'details': {'counts': counts, 'missing': missing}
        }
    else:
        return {
            'status': 'pass',
            'message': '所有必需元素存在',
            'details': {'counts': counts}
        }

def check_link_validity(content: str) -> Dict:
    """Check if links are valid (basic check)"""
    # Extract all URLs
    url_pattern = r'href="(https?://[^"]+)"'
    urls = re.findall(url_pattern, content)

    if not urls:
        return {
            'status': 'warn',
            'message': '未找到任何链接',
            'details': {'total_links': 0}
        }

    # For now, just count links (actual validation would require HTTP requests)
    # In production, you'd want to check each URL with requests.head()

    return {
        'status': 'pass',
        'message': f'找到 {len(urls)} 个链接',
        'details': {
            'total_links': len(urls),
            'sample_links': urls[:5]
        }
    }

def check_source_count(content: str) -> Dict:
    """Check number of sources per article"""
    # Count article sections
    article_sections = re.findall(r'<div class="article-section">', content)
    num_articles = len(article_sections)

    # Count sources-list divs
    sources_lists = re.findall(r'<div class="sources-list">', content)
    num_sources_lists = len(sources_lists)

    # Extract individual source links
    source_items = re.findall(r'<a[^>]*class="source-item"', content)
    total_sources = len(source_items)

    if num_articles == 0:
        return {
            'status': 'fail',
            'message': '未找到文章区块',
            'details': {}
        }

    avg_sources = total_sources / num_articles if num_articles > 0 else 0

    if avg_sources < 2:
        return {
            'status': 'fail',
            'message': f'平均每篇文章来源不足 ({avg_sources:.1f} < 2)',
            'details': {
                'articles': num_articles,
                'total_sources': total_sources,
                'avg_sources': avg_sources
            }
        }
    elif avg_sources > 5:
        return {
            'status': 'warn',
            'message': f'平均每篇文章来源过多 ({avg_sources:.1f} > 5)',
            'details': {
                'articles': num_articles,
                'total_sources': total_sources,
                'avg_sources': avg_sources
            }
        }
    else:
        return {
            'status': 'pass',
            'message': f'来源数量合适 (平均 {avg_sources:.1f} 个/篇)',
            'details': {
                'articles': num_articles,
                'total_sources': total_sources,
                'avg_sources': avg_sources
            }
        }

def check_article_count(content: str) -> Dict:
    """Check number of articles and quick news"""
    deep_articles = len(re.findall(r'<div class="article-section">', content))
    quick_news = len(re.findall(r'<div class="quick-news-item">', content))

    issues = []

    if deep_articles != 3:
        issues.append(f'深度文章数量不正确 (期望 3, 实际 {deep_articles})')

    if quick_news < 3 or quick_news > 5:
        issues.append(f'快讯数量不正确 (期望 3-5, 实际 {quick_news})')

    if issues:
        return {
            'status': 'fail',
            'message': '; '.join(issues),
            'details': {
                'deep_articles': deep_articles,
                'quick_news': quick_news
            }
        }
    else:
        return {
            'status': 'pass',
            'message': f'文章数量正确 ({deep_articles} 深度, {quick_news} 快讯)',
            'details': {
                'deep_articles': deep_articles,
                'quick_news': quick_news
            }
        }

def main():
    """Main quality check function"""
    base_dir = Path(__file__).parent.parent
    content_dir = base_dir / 'content' / 'posts'
    data_dir = base_dir / 'data'

    # Find today's article
    today = date.today().isoformat()
    article_file = content_dir / f'{today}-ai-digest.md'

    if not article_file.exists():
        print(f"❌ 错误: {article_file} 不存在")
        sys.exit(1)

    print(f"🔍 检查文章: {article_file}")

    # Load article
    with open(article_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Run checks
    checks = []

    print("\n运行质量检查...")

    # 1. Banned words check
    print("  1. 检查禁用词汇...")
    banned_words = load_banned_words()
    checks.append({
        'check': 'banned_words',
        **check_banned_words(content, banned_words)
    })

    # 2. HTML structure check
    print("  2. 检查 HTML 结构...")
    checks.append({
        'check': 'html_structure',
        **check_html_structure(content)
    })

    # 3. Link validity check
    print("  3. 检查链接...")
    checks.append({
        'check': 'link_validity',
        **check_link_validity(content)
    })

    # 4. Source count check
    print("  4. 检查来源数量...")
    checks.append({
        'check': 'source_count',
        **check_source_count(content)
    })

    # 5. Article count check
    print("  5. 检查文章数量...")
    checks.append({
        'check': 'article_count',
        **check_article_count(content)
    })

    # Calculate overall status
    all_passed = all(c['status'] == 'pass' for c in checks)
    has_failures = any(c['status'] == 'fail' for c in checks)

    # Calculate score
    pass_count = sum(1 for c in checks if c['status'] == 'pass')
    score = (pass_count / len(checks)) * 100

    # Build report
    report = {
        'date': today,
        'file': str(article_file),
        'timestamp': datetime.now().isoformat(),
        'checks': checks,
        'all_passed': all_passed,
        'has_failures': has_failures,
        'score': round(score, 1)
    }

    # Save report
    report_file = data_dir / 'quality_report.json'
    with open(report_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    # Print results
    print(f"\n📊 质量检查结果:")
    for check in checks:
        status_icon = {'pass': '✅', 'warn': '⚠️', 'fail': '❌'}[check['status']]
        print(f"  {status_icon} {check['check']}: {check['message']}")

    print(f"\n总体评分: {score}/100")
    print(f"💾 报告已保存: {report_file}")

    if has_failures:
        print("\n❌ 质量检查失败")
        sys.exit(1)
    else:
        print("\n✅ 质量检查通过")
        sys.exit(0)

if __name__ == '__main__':
    main()
