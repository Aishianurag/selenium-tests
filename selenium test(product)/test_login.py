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
# Load environment variables
# -------------------------------
APP_URL = os.getenv("APP_URL", "http://136.115.237.98:3000")
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")
 
if not TEST_EMAIL or not TEST_PASSWORD:
    raise Exception("❌ TEST_EMAIL or TEST_PASSWORD not found in environment variables")
 
print(f"Testing URL: {APP_URL}")
print("Credentials loaded successfully")
 
# -------------------------------
# Chrome setup (CI safe)
# -------------------------------
options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--start-maximized")
 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
 
driver.set_page_load_timeout(60)
 
try:
    # -------------------------------
    # Open application
    # -------------------------------
    driver.get(APP_URL)
 
    # -------------------------------
    # Home → Login
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
 
except Exception as e:
    # 📸 Save screenshot for CI debugging
    driver.save_screenshot("login_failure.png")
    print("❌ LOGIN FAILED — Screenshot saved as login_failure.png")
    raise e
 
finally:
    driver.quit()