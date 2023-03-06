from Android.Landscape.locators import CartPageLocators
from appium import webdriver

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    pass


desired_cap = {
        "platformName": "Android",
        "deviceName": "9950b2b3",
    }
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)

def test_press_button_cart_discount():
    test = driver.find_element(*CartPageLocators.INPUT_NOTES)
    test.click()

