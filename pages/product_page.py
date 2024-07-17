import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    URL = "https://woocommerce-850415-2933260.cloudwaysapps.com/product/rf-id-card"
    
    COLOR_DROPDOWN = (By.ID, 'color')
    ORIENTATION_DROPDOWN = (By.ID, 'orientation')
    DESCRIPTION_FIELD = (By.ID, 'profile_desc')
    PHONE_CHECKBOX = (By.ID, 'phone_number_checkbox')
    PHONE_FIELD = (By.ID, 'phone_number_field')
    UPLOAD_LOGO = (By.ID, 'logo')

    ADD_TO_CART_BUTTON = (By.CLASS_NAME, 'single_add_to_cart_button')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.woocommerce-message')
    ERROR_MESSAGE = (By.CSS_SELECTOR, '.woocommerce-error')

    def navigate(self):
        self.driver.get(self.URL)

    def select_color(self, color):
        dropdown = self.find_element(self.COLOR_DROPDOWN)
        dropdown.send_keys(color)

    def select_orientation(self, orientation):
        dropdown = self.find_element(self.ORIENTATION_DROPDOWN)
        dropdown.send_keys(orientation)

    def add_description(self, description):
        self.send_keys(self.DESCRIPTION_FIELD, description)

    def check_phone_checkbox(self):
        self.click(self.PHONE_CHECKBOX)

    def enter_phone_number(self, phone_number):
        self.send_keys(self.PHONE_FIELD, phone_number)

    def upload_logo(self, file_path):
        self.send_keys(self.UPLOAD_LOGO, file_path)

    def select_border_options(self, options):
        for option in options:
            checkbox = self.find_element((By.ID, option))
            self.scroll_to_element(checkbox)
            time.sleep(1)
            self.click((By.ID, option))

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def is_product_added_to_cart(self):
        try:
            success_message_element = self.find_element(self.SUCCESS_MESSAGE)
            success_message_text = success_message_element.text
            return "“RF ID Card” has been added to your cart." in success_message_text
        except:
            return False

    def is_phone_validation_displayed(self):
        try:
            error_message_element = self.find_element(self.ERROR_MESSAGE)
            error_message_text = error_message_element.text
            return "not a valid number" in error_message_text
        except:
            return False
        
    def is_min_border_validation_displayed(self):
        try:
            error_message_element = self.find_element(self.ERROR_MESSAGE)
            error_message_text = error_message_element.text
            return "Make at least 2 selections" in error_message_text
        except:
            return False