import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
result = 0
with  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
    driver.get('https://parsinger.ru/selenium/3/3.html')
    codeks = driver.find_elements(By.TAG_NAME, "p")
    for p in codeks:
        result += int(p.text)
    print(result)
    time.sleep(10)