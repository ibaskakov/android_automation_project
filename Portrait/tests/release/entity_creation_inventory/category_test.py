from Android.Landscape.pages.settings_inventory_page import InventoryPage
import time

#Проверка наличия элемента "Categories"
def test_is_element_present_categories(driver):
    page = InventoryPage(driver)
    page.is_element_present_categories()

def test_category_create(driver):
    page = InventoryPage(driver)
    page.press_button_categories()
    page.press_button_create()
    time.sleep(1)
    page.name_input("Test_category_1")
    page.press_button_image()
    time.sleep(1)
    page.press_button_gallery()
    time.sleep(1)
    page.press_button_pictures()
    time.sleep(1)
    page.select_picture()
    time.sleep(1)
    page.press_button_save()

def test_category_find(driver):
    page = InventoryPage(driver)
    page.press_button_categories()
    page.search_option("Test_category_1")
    time.sleep(1)
    page.find_element_from_list_name("Test_category_1")
    time.sleep(1)
    page.is_element_present_picture()
