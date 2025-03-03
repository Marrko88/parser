from fake_useragent import UserAgent
import requests
import time
from random import randint

url = ''

count = 0
for i in range(1, 201):
    response = requests.get(f'https://parsinger.ru/3.3/2/{i}.html')
    count += response.status_code
    print(f'{i} - {count} - {response.status_code}')

print(count)