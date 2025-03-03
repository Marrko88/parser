from lib__my import *

url = 'https://parsinger.ru/4.1/1/index.html'
req = requests.get(url)
req.encoding = 'utf-8'

html = req.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find('li', {'data-key': 'cooling_system'})# Допишите поиск тега в супе и извлеките текст

    print(tag.text)


get_html(html)