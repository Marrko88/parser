import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('div', class_='main')

    items = table.find_all('div', class_='item')

    for row in items:
        input_my = row.find('input')
        input_my.



url = 'https://parsinger.ru/table/2/index.html'
scrape(url)



















# headers = [header.text for header in table.find_all('th')]
#
# rows = table.find_all('tr')
#
#
#
# data = []
#
# for row in rows:
#     row_data = dict(zip(headers, (cell.text for cell in row.find_all('td'))))
#     data.append(row_data)
#
# for entry in data:
#     print(entry)





#
# rows = table.find_all('tr')
#
# for row in rows[1:]:
#     columns = row.find_all('td')
#     #print(columns)
#     name = columns[0].text
#     age = columns[1].text
#     print(f'Имя: {name}, Возраст: {age}')


