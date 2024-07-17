from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://woocommerce-850415-2933260.cloudwaysapps.com/my-account"
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.NAME, "login")
    
    LOGGED_IN_INDICATOR = (By.CSS_SELECTOR, ".woocommerce-MyAccount-content")

    def navigate(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.LOGGED_IN_INDICATOR)
            )
            return True
        except:
            return False