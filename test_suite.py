from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text

    assert "You logged into a secure area!" in message
    print("Valid Login Test Passed")

    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(2)
    message = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in message
    print("Invalid Login Test Passed")

    driver.quit()


test_valid_login()
test_invalid_login()