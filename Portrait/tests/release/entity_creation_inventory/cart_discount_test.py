from Android.Landscape.pages.settings_inventory_page import InventoryPage
import time

def test_is_element_present_discounts(driver):
    page = InventoryPage(driver)
    page.is_element_present_discounts()

def test_cart_discount_create(driver):
    page = InventoryPage(driver)
    page.press_button_discounts()
    page.press_button_cart_discounts()
    page.press_button_create_discount()
    page.name_input('Discount_cart_1')
    page.percent_input('6600')
    page.barcode_input('246802')
    page.select_mode_automatic()
    #page.switch_activate_discount()
    page.press_button_save()

def test_cart_discount_check(driver):
    page = InventoryPage(driver)
    page.press_button_discounts()
    time.sleep(1)
    page.press_button_cart_discounts()
    time.sleep(1)
    page.find_element_from_list_value("66.00%")
    time.sleep(1)
    page.name_check('Discount_cart_1, Name')
    page.percent_check('66.00%, Percent')
    page.barcode_check('246802, Barcode')
    page.is_element_present_percent_switch()
    page.scroll(406, 620, 406, 336)
    page.start_time_check("00:00")
    page.end_time_check("23:59")
    page.week_days_check("Mon, Tue, Wed, Thu, Fri, Sat, Sun")
    page.is_element_present_start_date()
    page.is_element_present_end_date()
    page.switch_activate_check('true')
    page.press_button_inventory()
    time.sleep(1)
    page.find_element_from_list_value("66.00%")
