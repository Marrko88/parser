import requests
from itertools import cycle

# Список прокси
proxies_list = [
    {'http': 'http://194.124.51.52:8000', 'https': 'https://194.124.51.52:8000'},
    {'http': 'http://194.124.48.136:8000', 'https': 'https://194.124.48.136:8000'}
]

proxy_pool = cycle(proxies_list)

url = "http://example.org"

# Создание сессии
session = requests.Session()

for i in range(1, 6):  # Попробуем сделать 5 запросов
    proxy = next(proxy_pool)
    session.proxies.update(proxy)  # Обновление прокси для сессии
    try:
        response = session.get(url, timeout=5)  # Используем сессию для выполнения запроса
        print(f"Request {i}: Success!")
    except requests.exceptions.RequestException as e:
        print(f"Request {i}: Failed, switching proxy. {proxy}")