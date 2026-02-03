from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 120)

    def wait_for_react(self):
        self.wait.until(lambda d: d.execute_script(
            "return document.getElementById('root') && document.getElementById('root').children.length > 0"
        ))

    def enter_email(self, email):
        self.wait_for_react()

        email_field = self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//input[contains(@type,'email') or contains(@placeholder,'Email') or contains(@name,'email')]"
            ))
        )
        email_field.clear()
        email_field.send_keys(email)

        # Click the Next / Continue / Arrow button
        next_btn = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button | //div[@role='button'] | //span[@role='button']"
            ))
        )
        next_btn.click()

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        password_field.clear()
        password_field.send_keys(password)

    def click_submit(self):
        submit = self.wait.until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[contains(.,'Sign') or contains(.,'Login') or contains(.,'Submit')]"
            ))
        )
        submit.click()
