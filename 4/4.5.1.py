from bs4 import BeautifulSoup
import requests

# # Задаем URL-адрес веб-страницы, с которой будем извлекать данные
# url = 'https://parsinger.ru/html/index1_page_1.html'
#
# # Выполняем HTTP-запрос к указанному URL-адресу
# response = requests.get(url=url)
#
# # Устанавливаем кодировку ответа в 'utf-8', чтобы корректно отображать кириллицу
# response.encoding = 'utf-8'
#
# # Создаем объект BeautifulSoup для анализа HTML-кода страницы
# # Второй аргумент 'lxml' указывает на используемый парсер
# soup = BeautifulSoup(response.text, 'lxml')
#
# # Ищем на странице первый элемент 'div' с классом 'item'
# div = soup.find('div', 'item')
#
# # Выводим найденный элемент на экран
# print(div)

# Задаем URL-адрес веб-страницы, которую хотим проанализировать
url = 'http://parsinger.ru/html/index1_page_1.html'

# Отправляем GET-запрос к указанной странице
response = requests.get(url=url)

# Устанавливаем кодировку ответа сервера в UTF-8, чтобы корректно отображать кириллицу
response.encoding = 'utf-8'

# Преобразуем текст ответа сервера в объект BeautifulSoup для дальнейшего анализа
soup = BeautifulSoup(response.text, 'lxml')

# Ищем на странице первый элемент <div> с классом 'item' и извлекаем из него все вложенные элементы <li>
div = soup.find('div', 'item').find_all('li')

# Проходимся по списку найденных элементов <li> и выводим их текстовое содержимое
for txt in div:
    print(txt.text)

# # Выводим на экран список найденных элементов <li>
# print(div)