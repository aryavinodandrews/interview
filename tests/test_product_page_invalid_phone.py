import os
from pages.product_page import ProductPage

def test_product_page_fields(driver):
    product_page = ProductPage(driver)
    product_page.navigate()
    product_page.select_color('Red')
    product_page.select_orientation('Landscape')
    product_page.add_description('Test description under 100 characters.')
    product_page.check_phone_checkbox()
    product_page.enter_phone_number('asdddd')
    
    logo_file_path = os.path.abspath('image.png')
    product_page.upload_logo(logo_file_path)
    
    product_page.select_border_options(['border_dotted', 'border_dashed'])

    product_page.click_add_to_cart()
    
    assert product_page.is_phone_validation_displayed()
