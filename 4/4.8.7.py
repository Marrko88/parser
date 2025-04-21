import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')

rows = table.find_all('tr')
ob ={}
ths = rows[0].find_all('th')

for i, th in enumerate(ths):
    print(th.text)
    sum = 0
    for tr in rows[1:]:
        tds = tr.find_all('td')
        for td in tds[i]:
            sum+=float(td)
        ob[th.text] = round(sum, 3)

print(ob)