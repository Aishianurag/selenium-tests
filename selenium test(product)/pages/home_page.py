from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
 
 
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)
 
    def click_sign_in(self):
        try:
            # 1️⃣ Wait until ANY DOM content appears (CI-safe)
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//*"))
            )
 
            # 2️⃣ Try to find Sign In / Login button or link
            sign_in = self.wait.until(
                EC.any_of(
                    EC.element_to_be_clickable((
                        By.XPATH,
                        "//button[contains(translate(.,'SIGNLOGIN','signlogin'),'sign')]"
                    )),
                    EC.element_to_be_clickable((
                        By.XPATH,
                        "//button[contains(translate(.,'SIGNLOGIN','signlogin'),'login')]"
                    )),
                    EC.element_to_be_clickable((
                        By.XPATH,
                        "//a[contains(translate(.,'SIGNLOGIN','signlogin'),'sign')]"
                    )),
                    EC.element_to_be_clickable((
                        By.XPATH,
                        "//a[contains(translate(.,'SIGNLOGIN','signlogin'),'login')]"
                    ))
                )
            )
 
            # 3️⃣ Scroll + JS click (headless Chrome fix)
            self.driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});", sign_in
            )
            self.driver.execute_script("arguments[0].click();", sign_in)
 
            # 4️⃣ Confirm login page loaded (email field or form)
            self.wait.until(
                EC.presence_of_element_located((
                    By.XPATH,
                    "//input[@type='email'] | //form"
                ))
            )
 
        except TimeoutException:
            # 🔴 CI debugging (ABSOLUTELY NECESSARY)
            self.driver.save_screenshot("home_page_failure.png")
 
            with open("home_page_source.html", "w", encoding="utf-8") as f:
                f.write(self.driver.page_source)
 
            raise TimeoutException(
                "Home page Sign/Login button not found. "
                "Screenshot + HTML dumped for debugging."
            )
