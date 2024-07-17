from pages.login_page import LoginPage

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.navigate()
    login_page.login("test_customer", "password")
    assert login_page.is_logged_in()