import re

from lib__my import *

url = 'https://parsinger.ru/4.1/1/index4.html'
req = requests.get(url)
req.encoding = 'utf-8'

html = req.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags_li = soup.select("li")# Допишите поиск тегов li
    for tag in tags_li:
        print(tag['id'])
        # Допишите обработку тегов и извлечение идентификаторов

get_html(html)