from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    def click_sign_in(self):
        sign_in = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[normalize-space()='Sign In']"))
        )
        sign_in.click()

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[text()='Sign in']"))
        )
