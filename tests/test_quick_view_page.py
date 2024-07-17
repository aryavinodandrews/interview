import os
from pages.shop_page import ShopPage
from pages.product_page import ProductPage

def test_product_quickview_fields(driver):
    shop_page = ShopPage(driver)
    product_page = ProductPage(driver)
    
    shop_page.navigate()
    shop_page.click_quick_view()
    
    product_page.select_color('Red')
    product_page.select_orientation('Landscape')
    product_page.add_description('Test description under 100 characters.')
    product_page.check_phone_checkbox()
    product_page.enter_phone_number('9876543210')
    
    logo_file_path = os.path.abspath('image.png')
    product_page.upload_logo(logo_file_path)
    
    product_page.select_border_options(['border_dotted', 'border_dashed'])

    product_page.click_add_to_cart()
    
    if not product_page.is_product_added_to_cart():
        raise AssertionError("The product was not added to the cart.")
