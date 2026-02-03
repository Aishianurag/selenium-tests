from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def verify_login_success(self):
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        self.wait.until(
            EC.any_of(
                EC.url_contains("dashboard"),
                EC.presence_of_element_located((By.TAG_NAME, "nav")),
                EC.presence_of_element_located((By.TAG_NAME, "aside")),
                EC.presence_of_element_located((By.XPATH, "//*[contains(.,'Dashboard')]")),
            )
        )
