import requests
from bs4 import BeautifulSoup




def scrape_table(url):
    response = requests.get(url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    # Поиск первой таблицы на веб-странице с атрибутом 'border' равным '3'
    table = soup.find('table')
    # Поиск всех строк (tr) в таблице и сохранение их в переменной rows
    rows = table.find_all('tr')
    data = []
    # Проход по всем строкам таблицы, начиная со второй
    for row in rows[1:]:
        columns = row.find_all('td')
        print(columns)
    # return data


url = 'https://parsinger.ru/table/1/index.html'
scrape_table(url)



















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


