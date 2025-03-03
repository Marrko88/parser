from lib import *

# import requests
#
# # Отправляем GET-запрос
# r = requests.get('https://api.github.com/events')
# print("Текущая кодировка:", r.encoding)
# # Получаем текст ответа
# print("Содержимое ответа:")
#
# print(r.text)


# response = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
# print(response.json())
# print(response.text)

response = requests.get(url='http://httpbin.org/image/jpeg')
with open('image.jpeg', 'wb') as file:
    file.write(response.content)