from lib import *


response = requests.get('https://parsinger.ru/img_download/index.html')

if response.status_code == 200:
    soup = bs(response.text, 'html.parser')

    div_main = soup.select('.main img[src]')

    src = [el.get('src') for el in div_main]
    print(src)
    for g, i in enumerate(src):
        url = f'https://parsinger.ru/img_download/{i}'
        print(f'{g} - {url}')
        response = requests.get(url=url)
        with open(f'im/img_{g}.png', 'wb') as file:
            file.write(response.content)