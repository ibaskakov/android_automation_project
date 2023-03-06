from Portrait.pages.cart_page import CartPage
import time


# Поиск товара и добавление товара
def test_search_option(driver):
    page = CartPage(driver)
    a = page.find_element_from_list_cart_menu('Go to Menu') #Go to Menu
    a.click()
    time.sleep(1)
    page.search_option("Item 1")
    time.sleep(1)
    a = page.find_element_from_list_name("Item 1")
    a.click()
    page.press_button_return()
    page.press_button_return()

# Void order
def test_void_tab(driver):
    page = CartPage(driver)
    page.press_button_open_more()
    page.press_void_order()
    time.sleep(1)
    page.press_button_positive()

# Check result
def test_check_order(driver):
    page = CartPage(driver)
    page.not_present_element_cart_total()


