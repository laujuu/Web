import re
from tech_news.database import search_news


def search_by_title(title):
    query = {"title": {"$regex": re.compile(title, re.IGNORECASE)}}
    news_list = search_news(query)
    return [(n["title"], n["url"]) for n in news_list]


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
