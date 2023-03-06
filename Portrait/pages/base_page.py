from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from appium.webdriver.common.touch_action import TouchAction

from Portrait.locators import CommonLocators, CartPageLocators


class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def search_option(self, value):
        ''' self.driver.find_element(*CartPageLocators.BUTTON_SEARCH_ITEMS).click() '''
        self.driver.find_element(*CommonLocators.SEARCH_ELEMENT).click()
        self.driver.find_element(*CommonLocators.OPTION_SEARCH).click()
        self.driver.find_element(*CommonLocators.OPTION_SEARCH).set_value(value)


    """Поиск элемента в списке по значению параметра TV_VALUE"""
    def find_element_from_list_value(self, value):
        elements = self.driver.find_elements(*CommonLocators.TV_VALUE)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра TV_NAME"""
    def find_element_from_list_name(self, value):
        elements = self.driver.find_elements(*CommonLocators.TV_NAME)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра TV_TEXT"""
    def find_element_from_list_text(self, value):
        elements = self.driver.find_elements(*CommonLocators.TV_TEXT)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра TV_TITLE"""
    def find_element_from_list_title(self, value):
        elements = self.driver.find_elements(*CommonLocators.TV_TITLE)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра TV_HINT"""
    def find_element_from_list_hint(self, value):
        elements = self.driver.find_elements(*CommonLocators.TV_HINT)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра TV_PHONE"""
    def find_element_from_list_phone(self, value):
        elements = self.driver.find_elements(*CommonLocators.TV_PHONE)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра TV_ORDER_TYPE"""
    def find_element_from_list_order_type(self, value):
        elements = self.driver.find_elements(*CommonLocators.TV_ORDER_TYPE)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра PAYMENT_TOOL"""
    def find_element_from_list_payment_tool(self, value):
        elements = self.driver.find_elements(*CommonLocators.PAYMENT_TOOL)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра TV_QUICK"""
    def find_element_from_list_cart_menu(self, value):
        elements = self.driver.find_elements(*CommonLocators.TV_QUICK)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра ET_FIELD"""
    def find_element_from_item_input_fields(self, value):
        elements = self.driver.find_elements(*CommonLocators.ET_FIELD)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError

    """Поиск элемента в списке по значению параметра ACTV_TEXT"""
    def find_element_from_item_input_actv_fields(self, value):
        elements = self.driver.find_elements(*CommonLocators.ACTV_TEXT)
        for element in elements:
            if value not in element.text:
                continue

            else:
                return element
        raise ValueError


    def flick(self, start_x: int, start_y: int, end_x: int, end_y: int):
        """Flick from one point to another point.
        Args:
            start_x: x-coordinate at which to start
            start_y: y-coordinate at which to start
            end_x: x-coordinate at which to stop
            end_y: y-coordinate at which to stop
        Usage:
            driver.flick(100, 100, 100, 400)
        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        actions = ActionChains(self)
        actions.w3c_actions = ActionBuilder(self, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        actions.w3c_actions.pointer_action.release()
        actions.perform()
        return self  # type: ignore

    def is_element_has_special_attribute_value(self, how, what, attribute, expected_value, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
            elements = self.driver.find_elements(how, what)
            element = self.driver.find_element(how, what)
            element_attribute = element.get_attribute(attribute)
            for element in elements:
                if expected_value not in element_attribute:
                    continue
                else:
                    return element
            assert element_attribute == expected_value, f"Expected: {expected_value}, Actual: {element_attribute}"
        except NoSuchElementException:
            print(f"Element not found by {how} and {what} after {timeout} seconds.")
            return False
        except TimeoutException:
            print(
                f"Timed out after {timeout} seconds when searching for attribute='{attribute}' and text={expected_value}")
            return False
        return True