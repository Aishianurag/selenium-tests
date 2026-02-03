from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def verify_login_success(self):
        # Wait until URL changes away from /login
        self.wait.until(lambda d: "/login" not in d.current_url)

        # Wait until something that only exists after login appears
        self.wait.until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//nav")),
                EC.presence_of_element_located((By.XPATH, "//header")),
                EC.presence_of_element_located((By.XPATH, "//aside")),
                EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Dashboard')]")),
                EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Welcome')]"))
            )
        )
