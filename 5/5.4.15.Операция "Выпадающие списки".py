import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

result = 0
with  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
    driver.get('https://parsinger.ru/selenium/7/7.html')
    selects = driver.find_element(By.ID, "opt").find_elements(By.TAG_NAME, 'option')
    for option in selects:
            result += int(option.text)

    driver.find_element(By.ID, "input_result").send_keys(result)
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(10)