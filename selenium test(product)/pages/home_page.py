from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def click_sign_in(self):
        # Wait until page is fully loaded
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Find ANY link or button containing Sign / Login / Sign In
        sign_in = self.wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(., 'Sign') or contains(., 'Login') or contains(., 'Sign In')] | "
                    "//button[contains(., 'Sign') or contains(., 'Login') or contains(., 'Sign In')]"
                )
            )
        )

        sign_in.click()

        # Wait until login form appears
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(., 'Email') or contains(., 'Password')]")
            )
    )