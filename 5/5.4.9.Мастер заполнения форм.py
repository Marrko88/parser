import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

with  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
    driver.get('https://parsinger.ru/selenium/1/1.html')
    input_name = driver.find_element(By.NAME, "first_name").send_keys('Mark')
    input_last_name = driver.find_element(By.NAME, "last_name").send_keys('Mark')
    input_second_name = driver.find_element(By.NAME, "patronymic").send_keys('Mark')
    input_age = driver.find_element(By.NAME, "age").send_keys(30)
    input_city = driver.find_element(By.NAME, "city").send_keys('Mark')
    input_email = driver.find_element(By.NAME, "email").send_keys('Mark')
    btn = driver.find_element(By.ID, "btn").click()
    time.sleep(10)
