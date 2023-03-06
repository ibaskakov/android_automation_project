from Portrait.locators import MoreOptionPageLocators, InventoryPageLocators
from Portrait.pages.base_page import BasePage


class MoreOptionPage(BasePage):
    """Проверки элементов"""

    def is_element_present_note(self):
        assert self.is_element_present(*MoreOptionPageLocators.INPUT_NOTE), ("")

    def is_not_element_present_refund(self):
        assert self.is_not_element_present(*MoreOptionPageLocators.BUTTON_REFUND), (
            "Refund button is present, but shouldn't")

    def is_element_present_refund_receipt(self):
        assert self.is_element_present(*MoreOptionPageLocators.OUTPUT_REFUND_RECEIPT), ("Receipt is not shown")


    """Нажатие кнопок"""

    def manual_amount_enter(self):
        self.driver.find_element(*MoreOptionPageLocators.KEY_BUTTON_01).click()
        self.driver.find_element(*MoreOptionPageLocators.KEY_BUTTON_02).click()
        self.driver.find_element(*MoreOptionPageLocators.KEY_BUTTON_00).click()

    def press_button_key_enter(self):
        self.driver.find_element(*MoreOptionPageLocators.BUTTON_KEY_ENTER).click()

    def input_comment(self, value):
        self.driver.find_element(*MoreOptionPageLocators.INPUT_NOTE).set_value(value)

    def press_button_confirm(self):
        self.driver.find_element(*InventoryPageLocators.BUTTON_SAVE).click()

    def press_button_refund(self):
        self.driver.find_element(*MoreOptionPageLocators.BUTTON_REFUND).click()

    def press_button_finish(self):
        self.driver.find_element(*MoreOptionPageLocators.BUTTON_FINISH).click()


    """Проверки"""

    def refund_amount_check(self, value):
        item = self.driver.find_element(*MoreOptionPageLocators.OUTPUT_AMOUNT).get_attribute('text')
        assert item == value, 'Refund amount has wrong result'

    def refund_reason_check(self, value):
        item = self.driver.find_element(*MoreOptionPageLocators.OUTPUT_REASON).get_attribute('text')
        assert item == value, 'Refund reason has wrong result'

    def scroll(self, start_x, start_y, end_x, end_y):
        self.driver.flick(start_x, start_y, end_x, end_y)






