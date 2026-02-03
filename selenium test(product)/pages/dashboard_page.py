from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 90)

    def verify_login_success(self):
        # Wait for React to hydrate
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # Wait until the React root is populated
        self.wait.until(lambda d: d.execute_script(
            "return document.getElementById('root') && document.getElementById('root').children.length > 0"
        ))

        # Now wait until login page is gone
        self.wait.until(lambda d: "/login" not in d.current_url)

        # Finally wait for any dashboard UI
        self.wait.until(
            EC.any_of(
                EC.presence_of_element_located((By.XPATH, "//nav")),
                EC.presence_of_element_located((By.XPATH, "//header")),
                EC.presence_of_element_located((By.XPATH, "//aside")),
                EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Dashboard')]")),
                EC.presence_of_element_located((By.XPATH, "//*[contains(., 'Welcome')]")),
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href,'dashboard')]"))
            )
        )
