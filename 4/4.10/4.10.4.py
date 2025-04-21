import requests
from bs4 import BeautifulSoup
import json
import os

base = 'https://parsinger.ru/html/'
result_json = []

def get_soup(url):
    responce = requests.get(url=url)
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')
    return soup

def write_file(result_json):
    with open('res.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)

soup = get_soup("https://parsinger.ru/html/index4_page_1.html")

pag = soup.find('div', class_='pagen')

pagen = [f"{base}{link.attrs['href']}" for link in pag.find_all('a')]

for stran in pagen:
    l = get_soup(stran)
    items = l.find_all('div', class_='item')
    for el in items:
        name = el.select('a.name_item')[0].text.strip()
        descriptions = [value.text.split(':')[1].strip() for value in el.find_all('li')]
        print(descriptions)
        price = [x.text for x in el.find_all('p', class_='price')]
        result_json.append({
            "Наименование": name,
            "Бренд": descriptions[0],
            "Форм-фактор": descriptions[1],
            "Ёмкость": descriptions[2],
            "Объем буферной памяти": descriptions[3],
            "Цена": price[0]
        })
        #Открываем файл для дополнительной записи данных
        write_file(result_json)

print('Файл res.json создан')