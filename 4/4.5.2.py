from bs4 import BeautifulSoup
import requests

# # Задаем URL-адрес веб-страницы для парсинга
# url = 'http://parsinger.ru/html/headphones/5/5_32.html'
#
# # Отправляем GET-запрос к указанной странице
# response = requests.get(url=url)
#
# # Устанавливаем кодировку ответа сервера в UTF-8 для корректного отображения текста на кириллице
# response.encoding = 'utf-8'
#
# # Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
# soup = BeautifulSoup(response.text, 'lxml')
#
# # Ищем на странице тег <p> с классом 'article' и извлекаем из него текстовое содержимое
# div = soup.find('p', class_='article').get_text()
#
# # Выводим на экран текст, найденный внутри тега <p> с классом 'article'
# print(div)

# Задаем URL-адрес веб-страницы, с которой необходимо извлечь данные
url = 'http://parsinger.ru/html/headphones/5/5_32.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8, чтобы корректно отображать кириллический текст
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup с использованием парсера 'lxml'
soup = BeautifulSoup(response.text, 'lxml')

# Ищем на странице тег <p> с идентификатором 'p_header' и извлекаем из него текстовое содержимое
div = soup.find('p', id='p_header').get_text()

# Выводим на экран текст, найденный внутри тега <p> с идентификатором 'p_header'
print(div)
