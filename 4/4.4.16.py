import re

from lib__my import *

url = 'https://parsinger.ru/4.1/1/index5.html'
req = requests.get(url)
req.encoding = 'utf-8'

html = req.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    email_my = []
    emails = soup.find_all('strong', text='Электронная почта:')

    for el in emails:
        email = el.next_sibling
        email_my.append(email.text.strip())


    return email_my

print(get_html(html))