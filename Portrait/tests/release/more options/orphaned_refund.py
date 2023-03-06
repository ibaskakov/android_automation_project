from Android.Landscape.pages.more_options_page import MoreOptionPage
import time

def test_fill_refund_data(driver):
    page = MoreOptionPage(driver)
    page.find_element_from_list_name("Return")
    time.sleep(1)
    page.input_manual_amount()
    page.press_button_key_enter()
    time.sleep(1)
    page.input_comment("Broken goods")
    time.sleep(1)
    page.press_button_confirm()

def test_check_refund_data(driver):
    page = MoreOptionPage(driver)
    page.refund_amount_check("$12.00")
    page.refund_reason_check("Broken goods")

def test_receipt(driver):
    page = MoreOptionPage(driver)
    page.is_not_element_present_refund()
    page.find_element_from_list_payment_tool("Cash")
    page.press_button_refund()
    time.sleep(2)
    page.is_element_present_refund_receipt()
    page.press_button_finish()
