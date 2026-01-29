from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 40)
        self.driver = driver

    def enter_email(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input"))
        )
        email_field.clear()
        email_field.send_keys(email)

    def click_with_password(self):
        password_btn = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='With Password']")
            )
        )
        password_btn.click()

        # Wait until password field appears
        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )

    def enter_password(self, password):
        pwd = self.driver.find_element(By.XPATH, "//input[@type='password']")
        pwd.clear()
        pwd.send_keys(password)

    def click_submit(self):
        submit = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[normalize-space()='Submit']")
            )
        )
        submit.click()
