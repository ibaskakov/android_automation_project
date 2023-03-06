from Portrait.pages.base_page import BasePage
from Portrait.pages.cart_page import CartPage
import time

def open_browser(driver):
    browser_name = driver.config.getoption("browser_name")

'''
def test_create_order_for_partial(driver):
    page = CartPage(driver)
    page.press_button_open_item_menu()
    time.sleep(1)
    page.search_option("Partial item")
    time.sleep(1)
    a = page.find_element_from_list_name("Partial item")
    a.click()
    page.press_button_return()
    page.press_button_return()
    time.sleep(1)
    page.press_button_open_checkout()
'''

def test_1(driver):
    page = CartPage(driver)
    page.press_button_open_item_menu()
    time.sleep(1)
    page.search_option("Partial item")
    time.sleep(1)
    a = page.find_element_from_list_name("Partial item")
    a.click()
    page.press_button_return()
    page.press_button_return()
    time.sleep(1)
    page.press_button_open_checkout()