import json
import requests
from bs4 import BeautifulSoup
import csv

url = "https://parsinger.ru/html/index1_page_1.html"
responce = requests.get(url=url)
responce.encoding = 'utf-8'
soup = BeautifulSoup(responce.text, 'lxml')
# schema = 'https://parsinger.ru/html/index4_page_1.html'
shema_detail = 'https://parsinger.ru/html/'
pagen = [link.text for link in soup.find('div', class_='pagen').find_all('a')]
link =[]

with open('result1.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow([
        "Наименование","Артикул","Бренд","Модель","Тип","Технология экрана","Материал корпуса","Материал браслета",
        "Размер","Сайт производителя","Наличие","Цена","Старая цена","Ссылка на карточку с товаром"
    ])

for i in pagen:
    url = f"https://parsinger.ru/html/index1_page_{i}.html"
    responce = requests.get(url=url)
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')


    item_card = soup.find('div', class_='item_card')
    name_items = item_card.find_all('a', class_='name_item')



    # Извлекаем имена товаров и убираем лишние пробелы
    for el in name_items:
        link.append(el.attrs['href'])

for url_s in link:
    one = []
    two =[]
    url = f"{shema_detail}{url_s}"
    responce = requests.get(url=url)
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')

    #Извлекаем описание товаров и разбиваем на строки
    name = soup.find('p', id='p_header').text #name
    article = soup.find('p', class_='article') #article
    article = article.text.split(':')[1].strip() #article
    description = [x.text.split(':')[1].strip()  for x in soup.find_all('li')]
    availability = soup.find('span', id="in_stock")#наличие
    availability  = availability.text.split(':')[1].strip()
    new_price = soup.find('span', id='price').text #новая цена
    old_price = soup.find('span', id='old_price').text #старая цена


    # Открываем файл для дополнительной записи данных
    with open('result1.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        # for one, descr, price in zip(one, description, two):
        # Формируем строку для записи
        flatten = name, article, *[x for x in description], availability, new_price, old_price, url
        writer.writerow(flatten)

print('Файл result1.csv создан')