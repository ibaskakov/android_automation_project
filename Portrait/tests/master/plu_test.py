from Android.Landscape.pages.cart_page import CartPage
import time

# Проверка наличия элемента "PLU"
def test_is_element_present_plu(driver):
    page = CartPage(driver)
    page.is_element_present_plu()

def test_no_match(driver):
    page = CartPage(driver)
    page.press_button_plu()
    time.sleep(1)
    page.plu_input('12345678')
    page.press_keyboard_enter()
    page.plu_result_check('Can\'t find anything with code 12345678')
    page.press_keyboard_return()
    page.press_keyboard_return()

def test_match_found_item(driver):
    page = CartPage(driver)
    page.press_button_plu()
    time.sleep(1)
    page.plu_input('123456789')
    page.press_keyboard_enter()
    page.plu_result_check('Added to order: Item 2')
    page.press_keyboard_return()
    page.press_keyboard_return()
    page.item_in_cart_check('Item 2')

def test_match_foun_discount(driver):
    page = CartPage(driver)
    page.press_button_plu()
    time.sleep(1)
    page.plu_input('987654321')
    page.press_keyboard_enter()
    page.plu_result_check('Discount 100.00% for order')
    page.press_keyboard_return()
    page.press_keyboard_return()
    page.total_check('$0.00')

def test_order_save(driver):
    page = CartPage(driver)
    page.press_button_save()