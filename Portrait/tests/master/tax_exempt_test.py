from Android.Landscape.pages.cart_page import CartPage
from Android.Landscape.resources import items_names


# Проверка наличия элемента "tax exempt"
def test_is_element_present_tax_exempt(driver):
    page = CartPage(driver)
    page.is_element_present_tax_exempt()


#
def test_without_tax_exempt_option(driver):
    page = CartPage(driver)
    page.search_option(items_names.without_tax)
    page.add_item_from_search_to_cart()
    page.search_option(items_names.with_tax)
    page.add_item_from_search_to_cart()
    page.check_tax_sign('Taxable', 'Tax Exempt')
    page.total_check('$53.00')
    page.press_button_save()

def test_with_tax_exempt_option(driver):
    page = CartPage(driver)
    page.search_option(items_names.without_tax)
    page.add_item_from_search_to_cart()
    page.search_option(items_names.with_tax)
    page.add_item_from_search_to_cart()
    page.press_button_tax_exempt()
    page.check_tax_sign('Tax Exempt', 'Tax Exempt')
    page.total_check('$50.00')
    page.press_button_save()


