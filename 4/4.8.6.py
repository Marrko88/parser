import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

rows = table.find_all('tr')
data = []

for row in rows[1:]:
    tdo = row.find('td', class_ = 'orange').text
    tdl = row.select('td:last-child')[0].text
    res = float(tdo) * int(tdl)
    data.append(res)
print(sum(data))
