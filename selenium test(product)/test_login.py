from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

print("LOGIN TEST STARTED")

options = Options()
import os

if os.name == "nt":   # Only for Windows (your laptop)
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

import os
from selenium import webdriver
try:
    APP_URL = os.getenv("APP_URL", "http://136.115.237.98:3000")
    driver.get(APP_URL)
    driver.get(your url)

    home = HomePage(driver)
    home.click_sign_in()

    login = LoginPage(driver)
    login.enter_email(email)
    login.click_with_password()
    login.enter_password(password)
    login.click_submit()

    dashboard = DashboardPage(driver)
    dashboard.verify_login_success()

    print("LOGIN SUCCESSFUL ✅")

finally:
    driver.quit()