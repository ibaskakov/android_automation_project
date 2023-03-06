from Android.Landscape.pages.cart_page import CartPage


# Проверка наличия элемента "+Manual"
def test_is_element_present_manual(driver):
    page = CartPage(driver)
    page.is_element_present_tax_exempt()

#Ввод значения
def test_enter_amount(driver):
    page = CartPage(driver)
    page.press_button_add_manual()
    page.input_manual_amount()
    page.manual_amount_check('$12.00')
    page.press_button_close()

#Удаление одного символа
def test_delete_simbol(driver):
    page = CartPage(driver)
    page.press_button_add_manual()
    page.input_manual_amount()
    page.press_button_delete()
    page.manual_amount_check('$1.20')
    page.press_button_close()

#Очистка поля
def test_clear_input(driver):
    page = CartPage(driver)
    page.press_button_add_manual()
    page.input_manual_amount()
    page.press_button_key_clear()
    page.manual_amount_check('Enter Amount')
    page.press_button_close()

#Добавить в корзину с налогом
def test_add_to_cart_with_tax(driver):
    page = CartPage(driver)
    page.press_button_add_manual()
    page.input_manual_amount()
    page.press_button_key_enter()
    page.total_check('$13.20')
    page.press_button_close()
    page.press_button_save()

#Добавить в корзину с tax exempt
def test_add_to_cart_without_tax(driver):
    page = CartPage(driver)
    page.press_button_add_manual()
    page.input_manual_amount()
    page.press_button_tax_exempt()
    page.press_button_key_enter()
    page.total_check('$12.00')
    page.press_button_close()
    page.press_button_save()
