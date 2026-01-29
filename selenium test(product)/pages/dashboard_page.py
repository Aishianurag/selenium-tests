from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 40)

    def verify_login_success(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(),'Dashboard') or contains(text(),'Login Successful')]")
            )
        )