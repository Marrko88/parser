from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index3_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
schema = 'https://parsinger.ru/html/'
pagens = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
total_list_names = []
for el in pagens:
    req = requests.get(url=el)
    req.encoding = 'utf-8'
    soup_i = BeautifulSoup(req.text, 'lxml')
    names = [name.text for name in soup_i.find_all('a', class_ = 'name_item')]
    total_list_names.append(names)

print(total_list_names)