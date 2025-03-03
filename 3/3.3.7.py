from lib import *

l =[]
for i in range(1, 101):
    response = requests.get(f'https://parsinger.ru/3.3/4/{i}.html')
    if response.status_code == 200:
        print(i)
        l.append(i)


i_max = max(l)
i_min = min(l)

first_available_page = f'{i_min}.html'
last_available_page = f'{i_max}.html'
print(f"Первая доступная страница: {first_available_page}")
print(f"Последняя доступная страница: {last_available_page}")