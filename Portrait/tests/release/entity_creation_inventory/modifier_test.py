from Android.Landscape.pages.settings_inventory_page import InventoryPage
import time

def test_is_element_present_modifiers(driver):
    page = InventoryPage(driver)
    page.is_element_present_modifiers()

def test_create_modifier(driver):
    page = InventoryPage(driver)
    page.press_button_modifiers()
    page.press_button_create_modifier()
    page.name_input('Test_Mod_1')
    page.switch_forced()
    page.press_button_save()

def test_create_option(driver):
    page = InventoryPage(driver)
    page.press_button_modifiers()
    page.find_element_from_list_name('Test_Mod_1')
    page.press_button_add_option()
    page.name_input('Test_Opt_1')
    page.price_input('1000')
    page.switch_default_option()
    page.press_button_save()
    page.press_button_save()

def test_creation_check(driver):
    page = InventoryPage(driver)
    page.press_button_modifiers()
    page.find_element_from_list_name('Test_Mod_1')
    time.sleep(1)
    page.switch_forced_check('true')
    page.switch_multisellect_check('true')
    page.find_element_from_list_title('Test_Opt_1')
    time.sleep(1)
    page.switch_default_check('true')
    page.price_check('$10.00, Price')