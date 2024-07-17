from selenium.webdriver.common.by import By
from .base_page import BasePage

class CapProductPage(BasePage):
    URL = "https://woocommerce-850415-2933260.cloudwaysapps.com/product/cap"
    
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'single_add_to_cart_button')

    def navigate(self):
        self.driver.get(self.URL)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
