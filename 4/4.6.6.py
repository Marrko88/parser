from bs4 import BeautifulSoup
import requests

from bs4 import BeautifulSoup
import requests

url = 'https://parsinger.ru/html/index1_page_1.html'
response = requests.get(url=url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'lxml')
schema = 'https://parsinger.ru/html/'
total_sum = []

nav_menu = [f"{schema}{menu_el['href']}" for menu_el in soup.find('div', class_='nav_menu').find_all('a')]
print(nav_menu)
for el_nav in nav_menu:
    res_nav = requests.get(url=el_nav)
    res_nav.encoding = 'utf-8'
    soup = BeautifulSoup(res_nav.text, 'lxml')
    pages = [f"{schema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
    for el in pages:
        req = requests.get(url=el)
        req.encoding = 'utf-8'
        soup_i = BeautifulSoup(req.text, 'lxml')
        goods = [f"{schema}{link.find('a')['href']}" for link in soup_i.find('div', class_='item_card').find_all('div', class_='sale_button')]
        print(goods)
        for g in goods:
            req_2 = requests.get(url=g)
            req_2.encoding = 'utf-8'
            soup_ii = BeautifulSoup(req_2.text, 'lxml')
            in_stock = soup_ii.find('span', {'id':'in_stock'})
            price = soup_ii.find('span', {'id':'price'})
            #print(f"in_stock - {in_stock.text[10:]}, price - {price.text[:-3]}")
            total = int(in_stock.text[10:])*int(price.text[:-3])
            total_sum.append(total)
            print(total_sum)





#
#
print(sum(total_sum))