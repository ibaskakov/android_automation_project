from Portrait.pages.cart_page import CartPage
from appium.webdriver.common.touch_action import TouchAction
import time

def test_open_search(driver):
    page = CartPage(driver)
    a = page.find_element_from_list_cart_menu('Go to Menu') #Go to Menu
    a.click()
    time.sleep(1)
    page.search_option("Venus")
