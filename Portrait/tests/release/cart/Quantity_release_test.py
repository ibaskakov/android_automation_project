from Portrait.pages.cart_page import CartPage
import time


# Проверка наличия элемента "add item"
def test_is_element_present_add_item(driver):
    page = CartPage(driver)
    page.present_element_add_item_button()

# Проверка наличия элемента "search" + поиск товара
def test_search_option(driver):
    page = CartPage(driver)
    page.press_button_add_item()
    page.present_element_search_button()
    page.search_option("Item 1")
    time.sleep(1)
    page.find_element_from_list_name("Item 1")
    page.press_button_return()

def test_quantity_raise(driver):
    page = CartPage(driver)
    page.find_element_from_list_name("Item 1")
    page.press_button_up()
    page.press_button_save_item_in_cart()
    time.sleep(1)
    page.present_correct_quantity("(x2)")
    page.present_correct_item_amount("$20.00")

def test_quantity_manual_enter(driver):
    page = CartPage(driver)
    page.find_element_from_list_name("Item 1")
    page.input_quntity("5")
    page.press_button_save_item_in_cart()
    time.sleep(1)
    page.present_correct_quantity("(x5)")
    page.present_correct_item_amount("$50.00")

def test_quantity_decrease(driver):
    page = CartPage(driver)
    page.find_element_from_list_name("Item 1")
    page.press_button_down()
    page.press_button_save_item_in_cart()
    time.sleep(1)
    page.present_correct_quantity("(x4)")
    page.present_correct_item_amount("$40.00")
