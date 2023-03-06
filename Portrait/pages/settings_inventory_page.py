from Portrait.pages.base_page import BasePage
from Portrait.locators import InventoryPageLocators

class InventoryPage(BasePage):

    # Проверки элементов

    def is_element_present_categories(self):
        assert self.is_element_present(*InventoryPageLocators.BUTTON_CATEGORIES), ("Categories button is not present")

    def is_element_present_picture(self):
        assert self.is_element_present(*InventoryPageLocators.FILE_PIC_SAVED), ("Picture is not saved")

    def is_element_present_modifiers(self):
        assert self.is_element_present(*InventoryPageLocators.BUTTON_MODIFIERS), ("Modifiers tab is not present")

    def is_element_present_inventory(self):
        assert self.is_element_present(*InventoryPageLocators.BUTTON_INVENTORY), ("Inventory tab is not present")

    def is_element_present_discounts(self):
        assert self.is_element_present(*InventoryPageLocators.BUTTON_DISCOUNTS), ("Discounts tab is not present")

    def is_element_present_percent_switch(self):
        assert self.is_element_present(*InventoryPageLocators.SWITCH_PERCENT_VALUE), ("Percent switch is not present")

    def is_element_present_manual_switch(self):
        assert self.is_element_present(*InventoryPageLocators.SWITCH_MANUAL_VALUE), ("Manual switch is not present")

    def is_element_present_items(self):
        assert self.is_element_present(*InventoryPageLocators.BUTTON_ITEMS), ("Items tab is not present")

    def is_element_present_start_date(self):
        assert self.is_element_present(*InventoryPageLocators.OUTPUT_START_DATE), ("Start date field is not present")

    def is_element_present_end_date(self):
        assert self.is_element_present(*InventoryPageLocators.OUTPUT_END_DATE), ("End date field is not present")


    # Нажатие кнопок

    def press_button_categories(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CATEGORIES)
        button.click()

    def press_button_create(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CREATE)
        button.click()

    def press_button_save(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_SAVE)
        button.click()

    def press_button_image(self):
        button = self.driver.find_element(*InventoryPageLocators.FILE_CATEGORY_IMAGE)
        button.click()

    def press_button_gallery(self):
        button = self.driver.find_element(*InventoryPageLocators.FILE_GALLERY)
        button.click()

    def press_button_pictures(self):
        button = self.driver.find_element(*InventoryPageLocators.FILE_PICTURES)
        button.click()

    def select_picture(self):
        button = self.driver.find_element(*InventoryPageLocators.FILE_PIC_1)
        button.click()

    def press_found_category(self):
        button = self.driver.find_element(*InventoryPageLocators.CATEGORY_FIND_RESULT)
        button.click()

    def switch_forced(self):
        button = self.driver.find_element(*InventoryPageLocators.SWITCH_FORCED)
        button.click()

    def press_button_modifiers(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_MODIFIERS)
        button.click()

    def press_button_items(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_ITEMS)
        button.click()

    def press_button_create_modifier(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CREATE_MODIFIER)
        button.click()

    def press_button_add_option(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_ADD_OPTION)
        button.click()

    def switch_default_option(self):
        button = self.driver.find_element(*InventoryPageLocators.SWITCH_DEFAULT_OPTION)
        button.click()

    def press_button_inventory(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_INVENTORY)
        button.click()

    def press_button_add_tax(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_ADD_TAX)
        button.click()

    def switch_default_tax(self):
        button = self.driver.find_element(*InventoryPageLocators.SWITCH_DEFAULT_TAX)
        button.click()

    def press_button_discounts(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_DISCOUNTS)
        button.click()

    def press_button_item_discounts(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_ITEM_DISCOUNTS)
        button.click()

    def press_button_cart_discounts(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CART_DISCOUNTS)
        button.click()

    def press_button_create_discount(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CREATE_DISCOUNT)
        button.click()

    def switch_activate_discount(self):
        button = self.driver.find_element(*InventoryPageLocators.SWITCH_ACTIVATE_DISCOUNT)
        button.click()

    def switch_use_weighing(self):
        button = self.driver.find_element(*InventoryPageLocators.SWITCH_USE_WEIGHING)
        button.click()

    def press_keyboard_done(self):
        self.driver.press_keycode(16)

    def press_button_create_item(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CREATE_ITEM)
        button.click()

    def press_button_choose_category(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CHOOSE_CATEGORY)
        button.click()

    def press_button_printer_type(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_PRINTER_TYPE_SELECT)
        button.click()

    def press_button_confirm(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CONFIRM)
        button.click()

    def press_button_modifiers_item(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CHOOSE_MODIFIER)
        button.click()

    def press_button_discounts_item(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_CHOOSE_DISCOUNTS)
        button.click()

    def select_mode_automatic(self):
        button = self.driver.find_element(*InventoryPageLocators.BUTTON_AUTOMATIC)
        button.click()


    # Заполнение строк

    def name_input(self, value):
        self.driver.find_element(*InventoryPageLocators.INPUT_NAME).set_value(value)

    def price_input(self, value):
        self.driver.find_element(*InventoryPageLocators.INPUT_PRICE).set_value(value)

    def percent_input(self, value):
        self.driver.find_element(*InventoryPageLocators.INPUT_PERCENT).set_value(value)

    def barcode_input(self, value):
        self.driver.find_element(*InventoryPageLocators.INPUT_BARCODE).set_value(value)

    def cost_input(self, value):
        self.driver.find_element(*InventoryPageLocators.INPUT_COST).set_value(value)

    # Проверки

    def switch_forced_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.SWITCH_FORCED).get_attribute('checked')
        assert attribute == value, 'Wrong switch state'

    def switch_multisellect_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.SWITCH_MULTISELECT).get_attribute('checked')
        assert attribute == value, 'Wrong switch state'

    def switch_default_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.SWITCH_DEFAULT_OPTION).get_attribute('checked')
        assert attribute == value, 'Wrong switch state'

    def price_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.INPUT_PRICE).get_attribute('text')
        assert attribute == value

    def name_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.INPUT_NAME).get_attribute('text')
        assert attribute == value

    def percent_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.INPUT_PERCENT).get_attribute('text')
        assert attribute == value

    def barcode_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.INPUT_BARCODE).get_attribute('text')
        assert attribute == value

    def modifier_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.OUTPUT_MODIFIER_NAME).get_attribute('text')
        assert attribute == value

    def discount_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.OUTPUT_DISCOUNT_NAME).get_attribute('text')
        assert attribute == value

    def switch_default_tax_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.SWITCH_DEFAULT_TAX).get_attribute('checked')
        assert attribute == value, 'Wrong switch state'

    def switch_activate_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.SWITCH_ACTIVATE_DISCOUNT).get_attribute('checked')
        assert attribute == value, 'Wrong switch state'

    def start_time_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.OUTPUT_START_TIME).get_attribute('text')
        assert attribute == value

    def end_time_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.OUTPUT_END_TIME).get_attribute('text')
        assert attribute == value

    def week_days_check(self, value):
        attribute = self.driver.find_element(*InventoryPageLocators.OUTPUT_WEEK_DAYS).get_attribute('text')
        assert attribute == value

    #Специальные действия
    def scroll(self, start_x, start_y, end_x, end_y):
        self.driver.flick(start_x, start_y, end_x, end_y)