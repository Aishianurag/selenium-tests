import pytest
from selenium import webdriver
import os
import datetime

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs["driver"]

        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png"
        screenshot_path = os.path.join("screenshots", file_name)

        driver.save_screenshot(screenshot_path)
        print(f"\nScreenshot saved: {screenshot_path}")