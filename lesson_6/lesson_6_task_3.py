from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
    )

    wait = WebDriverWait(driver, 10)

    wait.until(
        lambda d: all(
            d.execute_script(
                "return arguments[0].complete && "
                "arguments[0].naturalHeight > 0",
                img,
            )
            for img in d.find_elements(By.CSS_SELECTOR, "img")
        )
    )

    imgs = driver.find_elements(By.CSS_SELECTOR, "img")

    if len(imgs) >= 3:
        third_img = imgs[2]
        src_value = third_img.get_attribute("src")
        print(src_value)
    else:
        print(f"Found only {len(imgs)} images, index 2 is out of range")

finally:
    driver.quit()
