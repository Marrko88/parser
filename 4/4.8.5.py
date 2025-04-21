import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/4/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

rows = table.find_all('tr')
data = []

for row in rows[1:]:
    tds = row.find_all('td', class_ = 'green')
    for el in tds:
        el = float(el.text)
        data.append(el)
print(sum(data))
