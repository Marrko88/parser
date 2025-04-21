import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.8/7/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
tables= soup.find_all('table')

ar = []

for table in tables:
    rows = table.find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        for el in tds:
            el = int(el.text)
            if el % 3 == 0:
                ar.append(el)

print(sum(ar))