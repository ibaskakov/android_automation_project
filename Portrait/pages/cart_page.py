from Portrait.pages.base_page import BasePage
from Portrait.locators import CartPageLocators, CommonLocators, MoreOptionPageLocators
from appium.webdriver.common.touch_action import TouchAction


class CartPage(BasePage):

    # Проверки элементов
    def present_element_search_line(self):
        assert self.is_element_present(*CommonLocators.OPTION_SEARCH), ("Search line is not present")

    def present_element_add_item_button(self):
        assert self.is_element_present(*CartPageLocators.BUTTON_ADD_ITEM), ("Add item button is not present")

    def present_element_search_button(self):
        assert self.is_element_present(*CartPageLocators.BUTTON_SEARCH_ITEMS), ("Search button is not present")

    def present_element_input_manual(self):
        assert self.is_element_present(*CartPageLocators.INPUT_MANUAL_ITEM), ("Manual item input amount line is not present")

    def present_element_consumer(self):
        assert self.is_element_present(*MoreOptionPageLocators.BUTTON_CONSUMER), ("Consumer button is not present")

    def present_element_clear_consumer(self):
        assert self.is_element_present(*MoreOptionPageLocators.BUTTON_CLEAR_CONSUMER), ("Clear consumer button is not present")

    def not_present_element_clear_consumer(self):
        assert self.is_not_element_present(*MoreOptionPageLocators.BUTTON_CLEAR_CONSUMER), ("Clear consumer is present, but shouldn't")

    def not_present_element_cart_total(self):
        assert self.is_not_element_present(*CartPageLocators.TV_TOTAL), ("Total is present, but shouldn't")



    # Нажатие кнопок
    def long_press(self, driver):
        ta = TouchAction(driver)
        button_add_item = self.driver.find_element(*CommonLocators.TV_NAME)
        ta.press(button_add_item).wait(200).release().perform()

    def press_button_add_item(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_ADD_ITEM)
        button.click()

    def press_button_search(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_SEARCH_ITEMS)
        button.click()

    def press_button_return(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_RETURN)
        button.click()

    def press_button_up(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_UP)
        button.click()

    def press_button_down(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_DOWN)
        button.click()

    def press_button_save_item_in_cart(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_SAVE_ITEM_IN_CART)
        button.click()

    def press_button_save(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_SAVE)
        button.click()

    def press_button_create_cateory(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_CREATE_CATEGORY)
        button.click()

    def press_button_create_item(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_CREATE_ITEM)
        button.click()

    def press_button_add_picture(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_CHOOSE_PICTURE)
        button.click()

    def press_button_open_gallery(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_OPEN_GALLERY)
        button.click()

    def press_button_open_more(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_OPEN_MORE)
        button.click()

    def press_button_consumer(self):
        button = self.driver.find_element(*MoreOptionPageLocators.BUTTON_CONSUMER)
        button.click()

    def press_button_clear_consumer(self):
        button = self.driver.find_element(*MoreOptionPageLocators.BUTTON_CLEAR_CONSUMER)
        button.click()

    def go_checkout(self):
        button = self.driver.find_element(*CartPageLocators.TV_TOTAL)
        button.click()

    def open_color_picker(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_OPEN_COLOR_PICKER)
        button.click()

    def set_new_color(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_COLOR)
        button.click()

    def press_button_next(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_NEXT)
        button.click()

    def press_button_previous(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_PREVIOUS)
        button.click()

    def press_variable_price(self):
        button = self.driver.find_element(*CartPageLocators.SWITCH_VARIABLE_PRICE)
        button.click()

    def press_favorite(self):
        button = self.driver.find_element(*CartPageLocators.SWITCH_FAVORITE)
        button.click()

    def press_void_order(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_VOID_CURRENT_ORDER)
        button.click()

    def press_open_orders(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_OPEN_ORDERS)
        button.click()

    def press_button_positive(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_POSTIVE)
        button.click()

    def press_view_return_to_cart(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_ITEM_ADDED_VIEWER)
        button.click()

    def press_button_open_item_menu(self):
        button = self.driver.find_element(*CartPageLocators.BUTTON_OPEN_ITEM_MENU)
        button.click()

    def press_button_open_checkout(self):
        button = self.driver.find_element(*CartPageLocators.TV_TOTAL)
        button.click()

    # Заполнение строк
    def input_quntity(self, q):
        set_note = self.driver.find_element(*CartPageLocators.INPUT_Quantity)
        set_note.set_value(q)

    def input_manual_amount(self):
        self.driver.find_element(*CartPageLocators.BUTTON_KEY_1).click()
        self.driver.find_element(*CartPageLocators.BUTTON_KEY_2).click()
        self.driver.find_element(*CartPageLocators.BUTTON_KEY_3).click()
        self.driver.find_element(*CartPageLocators.BUTTON_KEY_ENTER).click()



    # Проверки
    def present_correct_quantity(self, value):
        item = self.driver.find_element(*CartPageLocators.TV_QANTITY).get_attribute('text')
        assert item == value, 'Qantity has wrong result'

    def present_correct_item_amount(self, value):
        item = self.driver.find_element(*CartPageLocators.TV_AMOUNT).get_attribute('text')
        assert item == value, 'Item amount has wrong result'

    def present_correct_total_amount(self, value):
        item = self.driver.find_element(*CartPageLocators.TV_TOTAL).get_attribute('text')
        assert item == value, 'Total amount has wrong result'

    def present_correct_cart_item_name(self, value):
        item = self.driver.find_element(*CommonLocators.TV_NAME).get_attribute('text')
        assert item == value, 'Total amount has wrong result'

    #Специальные действия
    def scroll(self, start_x, start_y, end_x, end_y):
        self.driver.flick(start_x, start_y, end_x, end_y)
