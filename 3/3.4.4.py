from lib import *


resp = requests.get('https://parsinger.ru/3.4/2/index.html')
resp.encoding = 'utf-8'
print(resp.text)