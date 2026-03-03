#!/usr/bin/env python3
"""
Topic Selection Script
Selects 3 deep articles + 5 quick news from scored sources
"""

import json
from datetime import datetime, date
from pathlib import Path
from typing import Dict, List
from collections import defaultdict

def categorize_article(article: Dict) -> str:
    """Categorize article based on tags and content"""
    tags = article.get('tags', [])
    title = article['title'].lower()

    # Simple keyword-based categorization
    if any(word in title for word in ['release', 'launch', 'model', 'gpt', 'claude']):
        return 'model_release'
    elif any(word in title for word in ['agent', 'autonomous', 'tool']):
        return 'ai_agent'
    elif any(word in title for word in ['safety', 'ethics', 'bias', 'harm']):
        return 'safety_ethics'
    elif any(word in title for word in ['company', 'funding', 'acquisition', 'partnership']):
        return 'industry_news'
    elif any(word in title for word in ['app', 'tool', 'product']):
        return 'tools_apps'
    elif any(word in title for word in ['research', 'paper', 'study']):
        return 'research'
    elif any(word in title for word in ['policy', 'regulation', 'law', 'government']):
        return 'policy_regulation'
    else:
        return 'industry_news'

def find_related_articles(article: Dict, all_articles: List[Dict], max_related: int = 5) -> List[Dict]:
    """Find related articles for a theme"""
    related = []
    article_tags = set(article.get('tags', []))

    for other in all_articles:
        if other['id'] == article['id']:
            continue

        other_tags = set(other.get('tags', []))
        overlap = len(article_tags & other_tags)

        if overlap >= 2:  # At least 2 common tags
            related.append(other)

        if len(related) >= max_related:
            break

    return related

def select_deep_articles(scored_sources: Dict, min_score: float = 70) -> List[Dict]:
    """Select 3 deep articles with diversity"""
    articles = [a for a in scored_sources['sources'] if a['score'] >= min_score]

    # Categorize all articles
    by_category = defaultdict(list)
    for article in articles:
        category = categorize_article(article)
        by_category[category].append(article)

    selected = []
    used_categories = set()

    # Select top article from each category (max 1 per category)
    for article in articles:
        if len(selected) >= 3:
            break

        category = categorize_article(article)
        if category not in used_categories:
            # Find related articles
            related = find_related_articles(article, articles, max_related=4)
            all_sources = [article] + related

            # Generate theme
            theme = article['title']

            selected.append({
                'theme': theme,
                'category': category,
                'suggested_title': theme,
                'sources': [
                    {
                        'id': src['id'],
                        'url': src['url'],
                        'title': src['title'],
                        'summary': src.get('summary', ''),
                        'content': src['content'],
                        'domain': src['domain'],
                        'source': src['source'],
                        'published': src['published'],
                        'score': src['score']
                    }
                    for src in all_sources[:5]  # Max 5 sources
                ],
                'key_points': []  # Will be filled by LLM
            })
            used_categories.add(category)

    return selected

def select_quick_news(scored_sources: Dict, deep_articles: List[Dict], min_score: float = 50, count: int = 5) -> List[Dict]:
    """Select quick news items"""
    articles = scored_sources['sources']

    # Exclude articles already used in deep articles
    used_ids = set()
    for deep in deep_articles:
        for src in deep['sources']:
            used_ids.add(src['id'])

    # Filter and select
    candidates = [
        a for a in articles
        if a['id'] not in used_ids and a['score'] >= min_score
    ]

    quick_news = []
    for article in candidates[:count]:
        quick_news.append({
            'title': article['title'],
            'url': article['url'],
            'domain': article['domain'],
            'summary': article.get('summary', article['title']),
            'published': article['published'],
            'score': article['score']
        })

    return quick_news

def main():
    """Main selection function"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'

    # Load scored sources
    with open(data_dir / 'scored_sources.json', 'r') as f:
        scored_sources = json.load(f)

    print("🎯 Selecting topics...")

    # Select deep articles
    deep_articles = select_deep_articles(scored_sources, min_score=70)
    print(f"✅ Selected {len(deep_articles)} deep articles")

    # Select quick news
    quick_news = select_quick_news(scored_sources, deep_articles, min_score=50, count=5)
    print(f"✅ Selected {len(quick_news)} quick news items")

    # Build output
    selected_topics = {
        'metadata': {
            'selected_at': datetime.now().isoformat(),
            'date': date.today().isoformat(),
            'total_candidates': len(scored_sources['sources']),
            'selection_criteria': {
                'min_score': 70,
                'diversity_enabled': True,
                'duplicate_check_days': 7
            }
        },
        'deep_articles': deep_articles,
        'quick_news': quick_news
    }

    # Save
    output_file = data_dir / 'selected_topics.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(selected_topics, f, indent=2, ensure_ascii=False)

    print(f"💾 Saved to {output_file}")

    # Print summary
    print("\n📋 Selected topics:")
    for i, article in enumerate(deep_articles, 1):
        print(f"  {i}. [{article['category']}] {article['theme']}")
        print(f"     Sources: {len(article['sources'])}")

    print("\n📰 Quick news:")
    for i, news in enumerate(quick_news, 1):
        print(f"  {i}. {news['title'][:60]}...")

if __name__ == '__main__':
    main()
