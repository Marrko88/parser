import requests
from bs4 import BeautifulSoup
import csv
import json
import os

from reportlab.lib.randomtext import PRINTING

base = 'https://parsinger.ru/html/'
result_json = []

def get_soup(url):
    responce = requests.get(url=url)
    responce.encoding = 'utf-8'
    soup = BeautifulSoup(responce.text, 'lxml')
    return soup

def write_file(result_json):
    with open('res_6.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)

def all_link_carts(paginations, tag, class_name):
    arr = []
    for st in paginations:
        st = get_soup(st)
        items = st.find_all(tag, class_=class_name)
        for cart in items:
            arr.append(f"{base}{cart.find('a').attrs['href']}")
    return arr


soup = get_soup('https://parsinger.ru/html/index2_page_1.html')

paginations = [f"{base}{pag.attrs['href']}" for pag in soup.find('div', class_="pagen").find_all("a")]
all_carts = all_link_carts(paginations, "div", "item")

for cart in all_carts:
    soup_cart = get_soup(cart)
    name = soup_cart.find("p", id="p_header").text
    article = soup_cart.find("p", class_="article").text.split(':')[1].strip()
    descriptions = {}
    for value in soup_cart.find('ul', id="description").find_all("li"):
        descriptions[value.attrs['id']] = value.text.split(':')[1].strip()
    in_stock = soup_cart.find('span', id='in_stock').text.split(':')[1].strip()
    price = soup_cart.find('span', id='price').text
    old_price = soup_cart.find('span', id='old_price').text

    result_json.append({
        "categories": "mobile",
        "name": name,
        "article": article,
        "description": descriptions,
        "count": in_stock,
        "price": price,
        "old_price": old_price,
        "link": cart
    })
    write_file(result_json)
print('Файл res6.json создан')













