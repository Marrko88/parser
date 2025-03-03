import requests
from bs4 import BeautifulSoup

from main import response

base_url = 'https://traktorodetal.ru/blog/'

# Номер страницы, с которой мы хотим собрать данные
page_number = 2


params = {'PAGEN_3': page_number}

response = requests.get(base_url, params=params)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    news_articles = soup.select('.item')

    for el in news_articles:
        article_title = el.select_one('.title').text
        print(f'Заголовок статьи: {article_title}')
else:
    print(f'Не удалось выполнить запрос. Код ошибки: {response.status_code}')