from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(
    service=Service(GeckoDriverManager().install())
)

try:
    driver.get("http://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    time.sleep(2)

    message = driver.find_element(
        By.CSS_SELECTOR,
        "div.flash.success"
        ).text.strip()

    print(message)

finally:
    driver.quit()
