from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
schema = 'https://parsinger.ru/html/'
pages = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
print(pages)
article_list = []
for el in pages:
    req = requests.get(url=el)
    req.encoding = 'utf-8'
    soup_i = BeautifulSoup(req.text, 'lxml')
    goods = [f"{schema}{link.find('a')['href']}" for link in soup_i.find('div', class_='item_card').find_all('div', class_='sale_button')]
    for g in goods:
        req_2 = requests.get(url=g)
        req_2.encoding = 'utf-8'
        soup_ii = BeautifulSoup(req_2.text, 'lxml')
        article = soup_ii.find('p', class_ = 'article')
        print(article.text)
        article_list.append(int(article.text[8:]))

print(sum(article_list))