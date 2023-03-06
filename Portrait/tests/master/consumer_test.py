from Android.Landscape.pages.cart_page import CartPage
import time


# Проверка наличия элемента "consumer"
def test_is_element_present_consumer(driver):
    page = CartPage(driver)
    page.present_element_consumer()

def test_clear_option(driver):
    page = CartPage(driver)
    page.press_button_consumer()
    page.is_element_present_new_consumer()
    page.press_button_new_consumer()
    time.sleep(1)
    page.cell_phone_input('9999999999')
    page.press_button_clear_consumer()
    time.sleep(1)
    page.press_button_consumer()
    time.sleep(1)
    page.search_option('9999999999')
    page.is_not_element_present_phone()
    page.press_button_close()

def test_restictions_to_save_and_save(driver):
    page = CartPage(driver)
    page.press_button_consumer()
    page.is_element_present_new_consumer()
    page.press_button_new_consumer()
    page.press_button_save_consumer()
    page.is_element_present_text_error()
    page.cell_phone_input('9999999999')
    page.press_button_save_consumer()
    time.sleep(1)
    #page.search_option('9999999999')
    #page.consumer_phone_search('(999) 999-9999')
    #page.press_button_close()

def test_fill_all_fields(driver):
    page = CartPage(driver)
    page.cell_phone_input('7777777777')
    page.first_name_input('Just')
    page.last_name_input('For Fan')
    page.email_input('aaaaa@gmail.com')
    page.address_1_input('Planet')
    page.address_2_input('Mars')
    page.city_input('Dune')
    page.scroll(406, 620, 406, 336)
    page.state_input('AR')
    page.zip_input('123456')
    page.notes_input('Let the galaxy burn!')
    page.press_button_save_consumer()
    time.sleep(1)
    page.search_option('7777777777')
    #Дописать проверку на содержимое полей

#Дописать тесты на:
#- проверку поиска