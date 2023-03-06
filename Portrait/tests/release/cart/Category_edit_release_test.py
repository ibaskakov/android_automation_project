from Portrait.pages.cart_page import CartPage
from appium.webdriver.common.touch_action import TouchAction
import time

def test_edit_category(driver):
    page = CartPage(driver)
    ta = TouchAction(driver)
    a = page.find_element_from_list_cart_menu('Go to Menu') #Go to Menu
    a.click()
    time.sleep(1)
    a = page.find_element_from_list_name("Portrait_category_creation")
    ta.press(a).wait(200).release().perform()

def test_change_values(driver):
    page = CartPage(driver)
    a = page.find_element_from_item_input_fields("Portrait_category_creation")
    a.set_value("Portrait_category_creation 1")
    page.open_color_picker()
    page.set_new_color()
    page.press_button_save_item_in_cart()
    time.sleep(2)
    page.find_element_from_list_name("Portrait_category_creation 1")

