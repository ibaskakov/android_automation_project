from Android.Landscape.pages.cart_page import CartPage


#Проверка наличия элемента "комментарий корзины"
def test_is_element_present_note(driver):
    page = CartPage(driver)
    page.is_element_present_note()

#Опция "Skip"
def test_skip(driver):
    page = CartPage(driver)
    page.fill_cart_notes()
    page.press_button_skip()
    page.is_not_element_present_note()

#Опция "Close"
def test_сlose(driver):
    page = CartPage(driver)
    page.fill_cart_notes()
    page.press_button_close()
    page.is_not_element_present_note()

#Опция "Clear"
def test_сlear(driver):
    page = CartPage(driver)
    page.fill_cart_notes()
    page.press_button_clear()
    page.press_button_save()
    page.is_not_element_present_note()

#Опция "Save"
def test_Save(driver):
    page = CartPage(driver)
    page.fill_cart_notes()
    page.press_button_save()
    page.check_cart_comment_filled()