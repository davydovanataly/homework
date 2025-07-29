from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

import time

service = Service()

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get('http://uitestingplayground.com/classattr')
    blue_button = driver.find_element(By.CLASS_NAME, 'btn-primary')
    blue_button.click()

    time.sleep(2)

finally:
    driver.quit()
