import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

print("LOGIN TEST STARTED")

# -------------------------------
# Chrome setup (local + CI safe)
# -------------------------------
options = Options()

if os.name == "nt":   # Only for Windows (your laptop)
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # -------------------------------
    # App URL (CI + Local)
    # -------------------------------
    APP_URL = os.getenv("APP_URL", "http://136.115.237.98:3000")
    driver.get(APP_URL)

    # -------------------------------
    # Run login flow
    # -------------------------------
    home = HomePage(driver)
    home.click_sign_in()

    login = LoginPage(driver)
    login.enter_email(os.getenv("TEST_EMAIL"))
    login.click_with_password()
    login.enter_password(os.getenv("TEST_PASSWORD"))
    login.click_submit()

    dashboard = DashboardPage(driver)
    dashboard.verify_login_success()

    print("LOGIN SUCCESSFUL ✅")

finally:
    driver.quit()