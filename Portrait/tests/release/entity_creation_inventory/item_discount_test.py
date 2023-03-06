from Android.Landscape.pages.settings_inventory_page import InventoryPage
import time

def test_is_element_present_discounts(driver):
    page = InventoryPage(driver)
    page.is_element_present_discounts()

def test_item_discount_create(driver):
    page = InventoryPage(driver)
    page.press_button_discounts()
    page.press_button_item_discounts()
    page.press_button_create_discount()
    page.name_input('Discount_item_1')
    page.percent_input('3300')
    page.barcode_input('135791')
    page.press_button_save()

def test_item_discount_check(driver):
    page = InventoryPage(driver)
    page.find_element_from_list_name('Discount_item_1')
    time.sleep(1)
    page.name_check('Discount_item_1, Name')
    page.percent_check('33.00%, Percent')
    page.barcode_check('135791, Barcode')
    page.is_element_present_percent_switch()
    page.is_element_present_manual_switch()
