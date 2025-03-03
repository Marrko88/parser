import re

from lib__my import *

url = 'https://parsinger.ru/4.1/1/index4.html'
req = requests.get(url)
req.encoding = 'utf-8'

html = req.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    prices = soup.find_all('p', {'class':'price product_price'})# Допишите поиск тегов с ценой

    count = 0
    for price in prices:
        str =  ''.join(price.text.split())
        if price.text == '20 280 руб':
            count += int(str[:-3])
            break
        else:
            count+=int(str[:-3])
        # Допишите обработку тегов и суммирование цен

    return count

print(get_html(html))