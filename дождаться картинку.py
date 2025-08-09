
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

award = WebDriverWait(driver, 45).until(
    EC.presence_of_element_located((By.ID, "award"))
)
WebDriverWait(driver, 45).until(
        lambda d: d.execute_script(
            "return Array.from(document.images)."
            \
            "every(i => i.complete && i.naturalWidth > 0);"
        )
    )

award = driver.find_element(By.ID, "award")
src_value = award.get_dom_attribute("src")
print(src_value)

driver.quit()
