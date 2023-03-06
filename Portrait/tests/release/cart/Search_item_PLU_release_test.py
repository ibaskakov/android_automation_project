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
    page.search_option("123456789")
    time.sleep(1)
    page.find_element_from_list_name("Item 2")