import requests
from requests.auth import HTTPBasicAuth

re = requests.get('https://bitrix.traktorodetal.ru', auth=HTTPBasicAuth('mmk@tmwk.ru', '25408-Freia'))
print(re.text)