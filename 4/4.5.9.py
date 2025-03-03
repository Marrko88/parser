from lib__my import *


url = 'https://parsinger.ru/html/index1_page_1.html'

req = requests.get(url=url)
req.encoding = 'utf-8'

soup = BeautifulSoup(req.text, 'html.parser')

prices = soup.find_all('p', {'class':'price'})
all_price = 0
for el in prices:
    all_price += int(el.text[:-3])

print(all_price)