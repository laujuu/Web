import requests
import time

from parsel import Selector


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Requisito 2
def scrape_updates(html_content):
    sel = Selector(text=html_content)
    news_urls = sel.css('.cs-overlay > a::attr(href)').getall()
    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    sel = Selector(text=html_content)
    next_link = sel.css("a.next").get()
    if next_link:
        return sel.css("a.next::attr(href)").get()
    else:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
