from Portrait.pages.cart_page import CartPage
from appium.webdriver.common.touch_action import TouchAction
import time

def test_open_item_form(driver):
    page = CartPage(driver)
    a = page.find_element_from_list_cart_menu('Go to Menu') #Go to Menu
    a.click()
    time.sleep(1)
    a = page.find_element_from_list_name("test item")
    a.click()
    time.sleep(1)
    page.press_button_create_item()

def test_enter_item_data_1_page(driver):
    page = CartPage(driver)
    a = page.find_element_from_item_input_fields("Name")
    a.set_value("Item_create")
    a = page.find_element_from_item_input_fields("$0.00")
    a.set_value("12.25")
    a = page.find_element_from_item_input_fields("Barcode")
    a.set_value("5484515486")
    page.find_element_from_item_input_actv_fields("test item")

def test_enter_item_data_2_page(driver):
    page = CartPage(driver)
    page.press_button_next()
    time.sleep(1)
    a = page.find_element_from_item_input_fields("0")
    a.set_value("35")
    a = page.find_element_from_item_input_fields("$0.00")
    a.set_value("7.99")
    a = page.find_element_from_item_input_actv_fields("Printer type")
    a.set_value("Bar")
    #page.scroll(100, 100, 400, 860)
    a = page.find_element_from_item_input_actv_fields("Brand")
    a.set_value("default 1")
    #page.press_variable_price()
    #page.press_favorite()

def test_enter_item_data_3_4_5_pages(driver):
    page = CartPage(driver)
    page.press_button_next() #to Taxes tab
    time.sleep(1)
    page.press_button_next() #to Discounts tab
    time.sleep(1)
    a = page.find_element_from_list_name("Discount_item_1")
    a.click() #Enable discount for item
    page.press_button_next() #to Modifiers tab
    time.sleep(1)
    a = page.find_element_from_list_name("Test_Mod_1")
    a.click() #Enable modifier for item
    page.press_button_save_item_in_cart()
