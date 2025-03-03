from lib__my import *


req = requests.get('https://parsinger.ru/4.3/3/index.html')
req.encoding = 'utf-8'

if req.status_code == 200:
    # print(req.text)
    soup = BeautifulSoup(req.text, 'html.parser')
    imgs = soup.find_all('img')

    total_sum = sum([int(el.get('alt')) for el in imgs])

    print(total_sum)
