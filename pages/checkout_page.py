import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class CheckoutPage(BasePage):
    URL = "https://woocommerce-850415-2933260.cloudwaysapps.com/checkout"

    FIRST_NAME_FIELD = (By.ID, 'billing_first_name')
    LAST_NAME_FIELD = (By.ID, 'billing_last_name')
    COUNTRY_DROPDOWN = (By.ID, 'billing_country')
    STREET_ADDRESS_FIELD = (By.ID, 'billing_address_1')
    CITY_FIELD = (By.ID, 'billing_city')
    STATE_DROPDOWN = (By.ID, 'billing_state')
    POSTCODE_FIELD = (By.ID, 'billing_postcode')
    PHONE_FIELD = (By.ID, 'billing_phone')
    EMAIL_FIELD = (By.ID, 'billing_email')
    DELIVERY_CHECKBOX = (By.ID, 'product_delivery_yes')
    PACKING_CHECKBOX = (By.ID, 'packaging_plastic')
    WOODEN_BOX_CHECKBOX = (By.ID, 'packaging_wooden')
    PAYMENT_METHOD_RADIO = (By.ID, 'payment_method_cod')
    PLACE_ORDER_BUTTON = (By.ID, 'place_order')

    def navigate(self):
        self.driver.get(self.URL)

    def enter_first_name(self, first_name):
        self.send_keys(self.FIRST_NAME_FIELD, first_name)

    def enter_last_name(self, last_name):
        self.send_keys(self.LAST_NAME_FIELD, last_name)

    def select_country(self, country):
        self.select_dropdown_by_visible_text(self.COUNTRY_DROPDOWN, country)

    def enter_street_address(self, address):
        self.send_keys(self.STREET_ADDRESS_FIELD, address)

    def enter_city(self, city):
        self.send_keys(self.CITY_FIELD, city)

    def choose_state(self, state):
        self.select_dropdown_by_visible_text(self.STATE_DROPDOWN, state)

    def enter_postcode(self, postcode):
        self.send_keys(self.POSTCODE_FIELD, postcode)

    def enter_phone(self, phone):
        self.send_keys(self.PHONE_FIELD, phone)

    def enter_email(self, email):
        self.send_keys(self.EMAIL_FIELD, email)

    def choose_delivery_option(self):
        self.click(self.DELIVERY_CHECKBOX)
        time.sleep(2)

    def choose_delivery_date(self, date):
        self.driver.execute_script(f"document.getElementById('date_delivery').value = '{date}';")

    def choose_delivery_time(self, time):
        self.driver.execute_script(f"document.getElementById('time_delivery').value = '{time}';")

    def choose_add_ons(self):
        self.click(self.PACKING_CHECKBOX)
        self.click(self.WOODEN_BOX_CHECKBOX)

    def choose_payment_method(self):
        radio = self.find_element(self.PAYMENT_METHOD_RADIO)
        self.scroll_to_element(radio)
        time.sleep(2)
        product = self.find_element(self.PAYMENT_METHOD_RADIO)
        action = ActionChains(self.driver)
        action.move_to_element(product).click().perform()

    def place_order(self):
        self.click(self.PLACE_ORDER_BUTTON)
        time.sleep(5)
