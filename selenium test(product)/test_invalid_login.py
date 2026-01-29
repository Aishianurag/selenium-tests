from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import time

print("=== INVALID LOGIN TEST FILE LOADED ===")

def run_invalid_login_test():
    print("=== INVALID LOGIN TEST STARTED ===")

    options = Options()
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options.add_argument("--start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    wait = WebDriverWait(driver, 40)

    print("Opening HOME page...")
    driver.get("http://136.115.237.98:3000/")

    login = LoginPage(driver)

    print("Opening login modal...")
    login.open_login_modal()

    login.enter_username("mohit12@gmail.com")
    login.enter_password("wrongpassword")
    login.click_login()

    print("Submitted invalid credentials")

    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'invalid') or contains(text(),'error')]")
        )
    )

    print("INVALID LOGIN BLOCKED ✅")

    time.sleep(5)
    driver.quit()
    print("=== INVALID LOGIN TEST COMPLETED ===")


if __name__ == "__main__":
    run_invalid_login_test()
