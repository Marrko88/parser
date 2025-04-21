import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/3/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

rows = table.find_all('tr')
data = []

for row in rows[1:]:
    tds = row.find_all('td')
    for el in tds:
        i = el.find('b')
        if i:
            i = float(i.text)
            data.append(i)
print(sum(data))
