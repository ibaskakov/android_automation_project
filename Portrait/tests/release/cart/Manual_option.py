from Portrait.locators import CommonLocators, CartPageLocators
from Portrait.pages.cart_page import CartPage
import time


# Проверка наличия элемента "add item"
def test_is_element_present_add_manual_item(driver):
    page = CartPage(driver)
    page.present_element_input_manual()

def test_manual_item(driver):
    page = CartPage(driver)
    page.input_manual_amount()
    time.sleep(1)
    page.is_element_has_special_attribute_value(*CommonLocators.TV_NAME, "text", "Manual Entry")
    page.is_element_has_special_attribute_value(*CartPageLocators.TV_QANTITY, "text", "(x1)")
    page.is_element_has_special_attribute_value(*CartPageLocators.TV_AMOUNT, "text", "$1.23")
    page.is_element_has_special_attribute_value(*CartPageLocators.TV_TOTAL, "text", "$1.41")