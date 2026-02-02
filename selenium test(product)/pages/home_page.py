from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def click_sign_in(self):
        # 1. Wait for the page shell to load
        self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # 2. Wait until ANY clickable element that looks like Sign / Login appears
        sign_in = self.wait.until(
            EC.any_of(
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(translate(., 'SIGNLOGIN', 'signlogin'), 'sign')]")
                ),
                EC.element_to_be_clickable(
                    (By.XPATH, "//a[contains(translate(., 'SIGNLOGIN', 'signlogin'), 'login')]")
                ),
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(translate(., 'SIGNLOGIN', 'signlogin'), 'sign')]")
                ),
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(translate(., 'SIGNLOGIN', 'signlogin'), 'login')]")
                )
            )
        )

        sign_in.click()

        # 3. Wait until the login form or input fields appear
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input | //form")
            )
        )