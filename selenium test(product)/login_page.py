from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click_sign_in(self):
        # Click the top-right "Sign In" button on landing page
        sign_in_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Sign In')]")
            )
        )
        sign_in_btn.click()

    def enter_username(self, username):
        email_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='email']")
            )
        )
        email_field.clear()
        email_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@type='password']")
            )
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Sign In') or contains(text(),'Login')]")
            )
        )
        login_button.click()
