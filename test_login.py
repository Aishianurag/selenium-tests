from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("tomsmith", "SuperSecretPassword!")

    assert "You logged into a secure area!" in page.get_message()


def test_invalid_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login("wrong", "wrong")

    assert "Your username is invalid!" in page.get_message()