from lib__my import *

url = 'https://parsinger.ru/4.1/1/index.html'
req = requests.get(url)
req.encoding = 'utf-8'

html = req.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    img =soup.find(attrs={'class': 'description detailz'}) # Допишите поиск тега в супе

    print(img)


get_html(html)