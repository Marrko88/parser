from fake_useragent import UserAgent
import requests
import time
from random import randint
from bs4 import BeautifulSoup as bs




for i in range(1, 201):
    response = requests.get(f'https://parsinger.ru/3.3/1/{i}.html')
    print(f'{i} - {response.status_code}')
    if response.status_code == 200:
        soup = bs(response.text, 'html.parser')


        print(soup.text)
