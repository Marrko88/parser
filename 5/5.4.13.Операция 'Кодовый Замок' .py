import time
from selenium.webdriver.common.by import By
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
result = 0
with  webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver:
    driver.get('https://parsinger.ru/selenium/4/4.html')
    checks = driver.find_elements(By.CLASS_NAME, "check")
    for check in checks:
        check.click()
    time.sleep(10)