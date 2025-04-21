import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.8/8/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
tables= soup.find_all('table')

ar = []
d = 0

cells = [x.text for x in soup.select('[colspan]')]

for el in cells[1:]:
    d+=int(el)

print(d)