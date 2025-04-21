import requests
from bs4 import BeautifulSoup
import csv
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
    with open('res5.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)

soup = get_soup("https://parsinger.ru/html/index1_page_1.html")


nav_menu = [f"{base}{nav.attrs['href']}" for nav in soup.find('div', class_='nav_menu').find_all('a')]



for link in nav_menu:
    pag = get_soup(link)
    pagen = [f"{base}{link.attrs['href']}" for link in pag.find('div', class_='pagen').find_all('a')]
    for stran in pagen:
        l = get_soup(stran)
        items = l.find_all('div', class_='item')
        for el in items:
            name = el.select('a.name_item')[0].text.strip()
            descriptions = [value.text.split(':') for value in el.find_all('li')]
            price = [x.text for x in el.find_all('p', class_='price')]
            result_json.append({
                "Наименование": name,            #
                f"{descriptions[0][0]}": f"{descriptions[0][1].strip()}",
                f"{descriptions[1][0]}": f"{descriptions[1][1].strip()}",
                f"{descriptions[2][0]}": f"{descriptions[2][1].strip()}",
                f"{descriptions[3][0]}": f"{descriptions[3][1].strip()}",
                "Цена": price[0]
            })
            # Открываем файл для дополнительной записи данных
            write_file(result_json)
print('Файл res5.csv создан')
