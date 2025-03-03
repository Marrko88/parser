import random
import requests

# Указываем URL, к которому будем отправлять запрос для тестирования прокси
url = 'http://httpbin.org/ip'

# Открываем файл с прокси и читаем его
with open('proxi.txt') as file:
    proxy_file = file.read().split('\n')

    random.shuffle(proxy_file)


    for proxy_ in proxy_file:
        try:
            ip = proxy_.strip()
            print(proxy_)

            proxy = {
                'http': f'http://{ip}',
                'https': f'https://{ip}'
            }
            # Выполняем GET-запрос с использованием выбранного прокси
            response = requests.get(url=url, proxies=proxy)

            print(response.json(), 'Success connection')
        except Exception as _ex:

            # В случае неудачи пропускаем текущую итерацию
            continue