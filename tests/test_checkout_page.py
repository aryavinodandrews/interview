from pages.cap_product_page import CapProductPage
from pages.checkout_page import CheckoutPage

def test_product_page_fields(driver):
    product_page = CapProductPage(driver)
    product_page.navigate()
    product_page.click_add_to_cart()

    checkout_page = CheckoutPage(driver)
    checkout_page.navigate()

    checkout_page.enter_first_name('Fname')
    checkout_page.enter_last_name('Lname')
    checkout_page.select_country('India')
    checkout_page.enter_street_address('123 abc')
    checkout_page.enter_city('Calicut')
    checkout_page.choose_state('Kerala')
    checkout_page.enter_postcode('673016')
    checkout_page.enter_phone('123456789')
    checkout_page.enter_email('test@example.com')
    checkout_page.choose_delivery_option()
    checkout_page.choose_delivery_date('2024-07-18')
    checkout_page.choose_delivery_time('10:00 AM')
    checkout_page.choose_add_ons()
    checkout_page.choose_payment_method()
    checkout_page.place_order()

    if "Order received" in driver.title:
        raise AssertionError("Order not received")