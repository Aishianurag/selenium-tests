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
# Validate required env variables
# -------------------------------
APP_URL = os.getenv("APP_URL", "http://136.115.237.98:3000")
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")

if not TEST_EMAIL or not TEST_PASSWORD:
    raise Exception("❌ TEST_EMAIL or TEST_PASSWORD not found in environment variables")

print(f"Testing URL: {APP_URL}")
print("Credentials loaded successfully")

# -------------------------------
# Chrome setup (Local + CI safe)
# -------------------------------
options = Options()

if os.name == "nt":   # Only for Windows (local laptop)
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    # -------------------------------
    # Open application
    # -------------------------------    
    driver.get(APP_URL)

    # -------------------------------
    # Run login flow
    # -------------------------------
    home = HomePage(driver)
    home.click_sign_in()

    login = LoginPage(driver)
    login.enter_email(TEST_EMAIL)
    login.click_with_password()
    login.enter_password(TEST_PASSWORD)
    login.click_submit()

    # -------------------------------
    # Verify dashboard
    # -------------------------------
    dashboard = DashboardPage(driver)
    dashboard.verify_login_success()

    print("LOGIN SUCCESSFUL ✅")

finally:
    driver.quit()
