from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")  # Раскомментировать, если нужно без GUI


service = Service(ChromeDriverManager().install())


driver = webdriver.Chrome(service=service, options=chrome_options)

try:

    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()
    time.sleep(3)

    driver.save_screenshot("screenshot.png")
    print("Скриншот'")

finally:

    driver.quit()
