from lib__my import *

url = 'https://parsinger.ru/4.1/1/index4.html'
req = requests.get(url)
req.encoding = 'utf-8'

html = req.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup.find_all('a', {'class':'name_item product_name'}) # Допишите поиск тега в супе

    for tag in tags:
        print(tag.text.strip())  # Извлеките текст и обрежьте лишние пробелы

get_html(html)