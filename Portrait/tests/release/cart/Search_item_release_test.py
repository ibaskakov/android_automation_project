from Portrait.pages.cart_page import CartPage
import time


# Поиск товара
def test_search_option(driver):
    page = CartPage(driver)
    a = page.find_element_from_list_cart_menu('Go to Menu') #Go to Menu
    a.click()
    time.sleep(1)
    page.search_option("Item 1")
    time.sleep(1)
    a = page.find_element_from_list_name("Item 1")
    a.click()



