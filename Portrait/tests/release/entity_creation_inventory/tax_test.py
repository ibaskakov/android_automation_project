from Android.Landscape.pages.settings_inventory_page import InventoryPage
import time

def test_is_element_present_inventory(driver):
    page = InventoryPage(driver)
    page.is_element_present_inventory()

def test_tax_create(driver):
    page = InventoryPage(driver)
    page.press_button_inventory()
    time.sleep(1)
    page.press_button_add_tax()
    page.name_input('Tax_test_1')
    page.percent_input('1500')
    page.press_keyboard_done()
    page.switch_default_tax()
    page.press_button_save()
    page.press_button_save()

def test_tax_check(driver):
    page = InventoryPage(driver)
    page.press_button_inventory()
    time.sleep(1)
    page.find_element_from_list_title('Tax_test_1')
    time.sleep(1)
    page.name_check('Tax_test_1, Name')
    page.switch_default_tax_check('true')