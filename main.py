from bs4 import BeautifulSoup
import requests

response = requests.get('https://parsinger.ru/2.1/DOM/sostav_selector.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')


#a = soup.select('a[name="4_1"]')
# paragraphs = soup.select('p.my_class[data-example]')
p=soup.select('.author .text')


for i in p:
    print(f'Найденный элемент: {i.text}')