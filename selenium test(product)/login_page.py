from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='email' or contains(@placeholder,'Email')]")
            )
        )
        email_field.clear()
        email_field.send_keys(email)

    def click_with_password(self):
        # Volt UI uses the same screen – no button needed
        pass

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@type='password' or contains(@placeholder,'Password')]")
            )
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_submit(self):
        submit = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Sign') or contains(., 'Login')]")
            )
        )
        submit.click()
