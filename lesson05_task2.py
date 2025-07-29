from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

import time

service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    button = driver.find_element(By.CLASS_NAME, "btn-primary")
    button.click()
    print("Кнопка успешно нажата")
finally:
    time.sleep(2)  # чтобы визуально увидеть результат
    driver.quit()
