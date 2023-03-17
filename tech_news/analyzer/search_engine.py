import re
from datetime import datetime
from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    news_list = search_news(query)
    return [(n["title"], n["url"]) for n in news_list]


# Requisito 8
def search_by_date(date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        formatted_date = date_obj.strftime('%d/%m/%Y')
        news = search_news({'timestamp': {'$regex': f'^{formatted_date}.*'}})
        return [(n['title'], n['url']) for n in news]
    except ValueError:
        raise ValueError('Data inválida')


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
