
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()

timeout = 25

WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(
            (By.ID, "content"),
            "Data loaded with AJAX get request."
        )
    )

result = driver.find_element(By.ID, "content").text
print(result)


driver.quit()
