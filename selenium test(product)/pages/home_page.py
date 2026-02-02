from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)
 
    def click_sign_in(self):
        # 1️⃣ Wait until React app fully loads
        self.wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
 
        # 2️⃣ Ensure body is present
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
 
        # 3️⃣ Locate Sign In / Login button or link (case-insensitive)
        sign_in = self.wait.until(
            EC.any_of(
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[contains(translate(normalize-space(.), "
                    "'SIGNLOGIN', 'signlogin'), 'sign')]"
                )),
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//button[contains(translate(normalize-space(.), "
                    "'SIGNLOGIN', 'signlogin'), 'login')]"
                )),
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//a[contains(translate(normalize-space(.), "
                    "'SIGNLOGIN', 'signlogin'), 'sign')]"
                )),
                EC.element_to_be_clickable((
                    By.XPATH,
                    "//a[contains(translate(normalize-space(.), "
                    "'SIGNLOGIN', 'signlogin'), 'login')]"
                ))
            )
        )
 
        # 4️⃣ Scroll into view (critical for headless Chrome)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", sign_in
        )
 
        # 5️⃣ Click Sign In
        sign_in.click()
 
        # 6️⃣ Wait until login form / email input appears
        self.wait.until(
            EC.presence_of_element_located((
                By.XPATH,
                "//input[@type='email'] "
                "| //input[contains(translate(@name,'EMAIL','email'),'email')] "
                "| //form"
            ))
        )