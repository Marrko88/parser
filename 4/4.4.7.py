from lib__my import *

url = 'https://parsinger.ru/4.1/1/index2.html'
req = requests.get(url)
req.encoding = 'utf-8'

html = req.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    tag = soup.find(attrs={
        'class': ['description_detail', 'class1', 'class2', 'class3'],
        'data-fdg45': 'value13',
        'data-54dfg60': 'value14',
        'data-d6f50hg': 'value15'
    }) # Допишите поиск тега в супе

    print(tag.text)


get_html(html)