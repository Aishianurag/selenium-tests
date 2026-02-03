import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

print("LOGIN TEST STARTED")

BASE_URL = "http://136.115.237.98:3000"
LOGIN_URL = BASE_URL.rstrip("/") + "/#/Signin"

TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

if not TEST_EMAIL or not TEST_PASSWORD:
    raise Exception("❌ TEST_EMAIL or TEST_PASSWORD not found")

print("Opening:", LOGIN_URL)

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_page_load_timeout(90)

try:
    driver.get(LOGIN_URL)

    print("Current URL:", driver.current_url)

    login = LoginPage(driver)
    login.enter_email(TEST_EMAIL)
    login.enter_password(TEST_PASSWORD)
    login.click_submit()

    dashboard = DashboardPage(driver)
    dashboard.verify_login_success()

    print("LOGIN SUCCESSFUL ✅")

except Exception as e:
    driver.save_screenshot("login_failure.png")
    print("❌ LOGIN FAILED")
    raise e

finally:
    driver.quit()
