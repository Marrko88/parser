import re

from lib__my import *

url = 'https://parsinger.ru/4.1/1/index6.html'
req = requests.get(url)
req.encoding = 'utf-8'

html = req.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')

    sibling = soup.find('p', text='Текст раздела 3').next_sibling

    print(sibling.text.strip())


    #return sibling

print(get_html(html))