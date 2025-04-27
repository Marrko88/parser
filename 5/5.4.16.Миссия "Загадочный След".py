import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from bs4 import BeautifulSoup
from lib__my import *
req = requests.get('https://parsinger.ru/selenium/6/6.html')
req.encoding = 'utf-8'
x = ''
res = 0
if req.status_code == 200:
    html = req.text
    soup = BeautifulSoup(html, "html.parser")
    div_text_box = soup.find('div', id='text_box')
    # Находим тег <span>
    span_tags = div_text_box.find_all('span')

    for el in span_tags:
        x += el.text
        next_element = el.next_sibling
        if next_element is not None:
            x += next_element


    res = x.replace(" ", '').replace("\n", '')

result = eval(res)


with  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
    driver.get('https://parsinger.ru/selenium/6/6.html')
    selects = driver.find_element(By.ID, "selectId").find_elements(By.TAG_NAME, 'option')
    for option in selects:
        if result == int(option.text):
            option.click()
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(10)