import requests
from bs4 import BeautifulSoup
import csv
base = 'https://parsinger.ru/html/'

def get_soup(url):
    responce = requests.get(url=url)
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')
    return soup

def write_file(name, descriptions, price):
    with open('res.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for item, descr, price in zip(name, descriptions, price):
            # Формируем строку для записи
            flatten = name, *[x.split(':')[1].strip() for x in descr if x], price
            writer.writerow(flatten)

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
            descriptions = [x.text.split('\n') for x in el.find_all('div', class_='description')]
            price = [x.text for x in el.find_all('p', class_='price')]

            #Открываем файл для дополнительной записи данных
            write_file(name, descriptions, price)

print('Файл res4.csv создан')

