from Portrait.pages.cart_page import CartPage
import time

# Проверка наличия элемента "consumer"
def test_is_element_present_consumer(driver):
    page = CartPage(driver)
    page.press_button_open_more()
    page.present_element_consumer()

def test_add_consumer(driver):
    page = CartPage(driver)
    page.press_button_consumer()
    time.sleep(1)
    page.find_element_from_list_phone("(777) 777-7777").click()
    time.sleep(1)
    page.present_element_clear_consumer()
    page.press_button_save()
    time.sleep(1)
    page.find_element_from_list_text("Just For Fan").click()

def test_clear_consumer(driver):
    page = CartPage(driver)
    page.present_element_clear_consumer()
    page.press_button_clear_consumer()

def test_consumer_removed_from_order(driver):
    page = CartPage(driver)
    page.press_button_open_more()
    page.press_button_consumer()
    time.sleep(1)
    page.find_element_from_list_phone("(777) 777-7777").click()
    time.sleep(1)
    page.present_element_clear_consumer()
    page.press_button_save()
