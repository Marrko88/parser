import json
import requests
from bs4 import BeautifulSoup
import csv

url = "https://parsinger.ru/html/index4_page_1.html"
responce = requests.get(url=url)
responce.encoding = 'utf-8'
soup = BeautifulSoup(responce.text, 'lxml')
schema = 'https://parsinger.ru/html/index4_page_1.html'
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')]

with open('result.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        "Наименование","Бренд","Форм-фактор","Ёмкость","Объем буферной памяти","Цена"])

for i in pagen:
    url = f"https://parsinger.ru/html/index4_page_{i}.html"
    responce = requests.get(url=url)
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')
    item_card = soup.find('div', class_='item_card')
    name_items = item_card.find_all('a', class_='name_item')
    # Извлекаем имена товаров и убираем лишние пробелы
    name = [el.text.strip() for el in name_items]
    # Извлекаем описание товаров и разбиваем на строки
    description = [x.text.split('\n') for x in soup.find_all('div', class_='description')]

    # Извлекаем цены товаров
    price = [x.text for x in soup.find_all('p', class_='price')]

    # Открываем файл для дополнительной записи данных
    with open('result.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for item, descr, price in zip(name, description, price):

            # Формируем строку для записи
            flatten = item, *[x.split(':')[1].strip() for x in descr if x], price
            writer.writerow(flatten)

print('Файл res.csv создан')