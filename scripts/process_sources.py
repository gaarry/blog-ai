#!/usr/bin/env python3
"""
Source Processing Script
Transforms raw sources through the data pipeline
"""

import json
import hashlib
from datetime import datetime
from pathlib import Path
from typing import Dict, List

def hash_url(url: str) -> str:
    """Generate unique ID from URL"""
    return hashlib.md5(url.encode()).hexdigest()[:16]

def calculate_engagement_score(engagement: Dict) -> float:
    """Calculate total engagement score"""
    score = 0.0

    # Hacker News scoring
    if 'hacker_news' in engagement:
        hn = engagement['hacker_news']
        hn_score = min(100, (hn.get('score', 0) / 10) + (hn.get('comments', 0) / 5))
        score += hn_score * 0.6  # 60% weight

    # Reddit scoring
    if 'reddit' in engagement:
        reddit = engagement['reddit']
        reddit_score = min(100, (reddit.get('upvotes', 0) / 50) + (reddit.get('comments', 0) / 10))
        score += reddit_score * 0.4  # 40% weight

    return min(100, score)

def calculate_cross_verification_score(article: Dict, all_articles: List[Dict]) -> Dict:
    """Calculate cross-verification score based on related articles"""
    # Simplified: in real implementation, use NLP similarity
    related = []
    for other in all_articles:
        if other['id'] != article['id']:
            # Simple keyword matching (replace with semantic similarity)
            if any(tag in other.get('tags', []) for tag in article.get('tags', [])):
                related.append(other['id'])

    count = len(related)
    if count >= 3:
        score = 95.0
    elif count == 2:
        score = 85.0
    elif count == 1:
        score = 70.0
    else:
        score = 50.0

    return {
        'score': score,
        'weight': 0.40,
        'weighted_score': score * 0.40,
        'related_articles': related[:5],
        'similarity': 0.85 if count >= 2 else 0.60
    }

def calculate_source_authority_score(source: str) -> Dict:
    """Calculate source authority score"""
    official_blogs = ['OpenAI Blog', 'Anthropic News', 'Google AI Blog', 'DeepMind Blog']
    tech_media = ['TechCrunch', 'The Verge', 'MIT Technology Review', 'Wired']
    newsletters = ['Import AI', "Ben's Bites", 'Latent Space']

    if source in official_blogs:
        return {'score': 100.0, 'weight': 0.20, 'weighted_score': 20.0, 'source_type': 'official_blog'}
    elif source in tech_media:
        return {'score': 80.0, 'weight': 0.20, 'weighted_score': 16.0, 'source_type': 'tech_media'}
    elif source in newsletters:
        return {'score': 70.0, 'weight': 0.20, 'weighted_score': 14.0, 'source_type': 'newsletter'}
    else:
        return {'score': 60.0, 'weight': 0.20, 'weighted_score': 12.0, 'source_type': 'community'}

def calculate_timeliness_score(published: str) -> Dict:
    """Calculate timeliness score based on publication time"""
    pub_time = datetime.fromisoformat(published.replace('Z', '+00:00'))
    now = datetime.now(pub_time.tzinfo)
    hours_ago = (now - pub_time).total_seconds() / 3600

    if hours_ago <= 6:
        score = 100.0
    elif hours_ago <= 12:
        score = 90.0
    elif hours_ago <= 18:
        score = 75.0
    elif hours_ago <= 24:
        score = 60.0
    else:
        score = 30.0

    return {
        'score': score,
        'weight': 0.15,
        'weighted_score': score * 0.15,
        'hours_ago': hours_ago
    }

def score_articles(sources_with_engagement: Dict) -> Dict:
    """Score all articles"""
    articles = sources_with_engagement['sources']

    scored_articles = []
    for article in articles:
        # Calculate individual scores
        cross_verification = calculate_cross_verification_score(article, articles)

        engagement_score = article.get('engagement', {}).get('total_score', 0)
        community_engagement = {
            'score': engagement_score,
            'weight': 0.25,
            'weighted_score': engagement_score * 0.25,
            'hn_score': engagement_score * 0.6,
            'reddit_score': engagement_score * 0.4
        }

        source_authority = calculate_source_authority_score(article['source'])
        timeliness = calculate_timeliness_score(article['published'])

        # Calculate final score
        final_score = (
            cross_verification['weighted_score'] +
            community_engagement['weighted_score'] +
            source_authority['weighted_score'] +
            timeliness['weighted_score']
        )

        scored_article = {
            **article,
            'score': round(final_score, 1),
            'score_breakdown': {
                'cross_verification': cross_verification,
                'community_engagement': community_engagement,
                'source_authority': source_authority,
                'timeliness': timeliness
            }
        }
        scored_articles.append(scored_article)

    # Sort by score and add rank
    scored_articles.sort(key=lambda x: x['score'], reverse=True)
    for i, article in enumerate(scored_articles, 1):
        article['rank'] = i

    return {
        'metadata': {
            'scored_at': datetime.now().isoformat(),
            'total_articles': len(scored_articles),
            'scoring_version': '1.0.0',
            'weights': {
                'cross_verification': 0.40,
                'community_engagement': 0.25,
                'source_authority': 0.20,
                'timeliness': 0.15
            }
        },
        'sources': scored_articles
    }

def main():
    """Main processing function"""
    base_dir = Path(__file__).parent.parent
    data_dir = base_dir / 'data'

    # Load sources with engagement
    with open(data_dir / 'sources_with_engagement.json', 'r') as f:
        sources_with_engagement = json.load(f)

    print("📊 Scoring articles...")
    scored_sources = score_articles(sources_with_engagement)

    # Save scored sources
    output_file = data_dir / 'scored_sources.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(scored_sources, f, indent=2, ensure_ascii=False)

    print(f"✅ Scored {len(scored_sources['sources'])} articles")
    print(f"💾 Saved to {output_file}")

    # Print top 10
    print("\n🏆 Top 10 articles:")
    for article in scored_sources['sources'][:10]:
        print(f"  {article['rank']}. [{article['score']}] {article['title']}")

if __name__ == '__main__':
    main()
