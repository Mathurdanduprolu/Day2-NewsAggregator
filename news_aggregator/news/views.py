import requests
from django.shortcuts import render
from django.conf import settings
from datetime import datetime

def news_list(request):
    query = request.GET.get('q', '')
    
    if query:
        url = f"https://newsapi.org/v2/everything?q={query}&apiKey={settings.NEWS_API_KEY}"
    else:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={settings.NEWS_API_KEY}"
    
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    
    for article in articles:
        published_at = article.get('publishedAt')
        if published_at:
            article['formatted_publishedAt'] = datetime.fromisoformat(published_at[:-1]).strftime('%Y-%m-%d %H:%M:%S')
    
    context = {
        'articles': articles,
        'query': query
    }
    return render(request, 'news/news_list.html', context)
