from Portrait.pages.cart_page import CartPage
import time

def test_create_category(driver):
    page = CartPage(driver)
    page.find_element_from_list_cart_menu('Go to Menu') #Go to Menu
    time.sleep(2)
    page.press_button_create_cateory()
    time.sleep(2)
    a = page.find_element_from_item_input_fields("Name")
    a.set_value("Portrait_category_creation")
    page.press_button_save_item_in_cart()
    '''page.press_button_add_picture()
    page.press_button_open_gallery()'''
    '''Нельзя выбрать картинку из-за layout'''


def test_check_category(driver):
    page = CartPage(driver)
    page.find_element_from_list_title("Portrait_category_creation")
    page.press_button_return()
