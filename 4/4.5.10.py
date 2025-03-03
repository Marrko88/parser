from lib__my import *

url = 'https://parsinger.ru/html/hdd/4/4_1.html'

req = requests.get(url=url)
req.encoding = 'utf-8'

soup = BeautifulSoup(req.text, 'html.parser')

price = soup.find('span', {'id' : 'price'}).text
old_price = soup.find('span', {'id' : 'old_price'}).text

price = float(price[:-3])
old_price = float(old_price[:-3])


percent = (old_price - price) * 100 / old_price

print(round(percent, 1))

