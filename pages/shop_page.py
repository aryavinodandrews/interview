import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from .base_page import BasePage

class ShopPage(BasePage):
    URL = "https://woocommerce-850415-2933260.cloudwaysapps.com/shop"
    PRODUCT_CONTAINER = (By.CSS_SELECTOR, "li.post-145")
    QUICK_VIEW_BUTTON = (By.CSS_SELECTOR, "a[data-product_id='145']")

    def navigate(self):
        self.driver.get(self.URL)

    def hover_over_product(self):
        product = self.find_element(self.PRODUCT_CONTAINER)
        action = ActionChains(self.driver)
        action.move_to_element(product).perform()

    def click_quick_view(self):
        self.hover_over_product()
        quick_view_button = self.driver.find_elements(*self.QUICK_VIEW_BUTTON)[1]
        time.sleep(1)
        quick_view_button.click()
        time.sleep(2)