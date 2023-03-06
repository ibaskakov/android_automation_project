import pytest
from appium import webdriver

@pytest.fixture(scope="function")
def driver():
    desired_cap = {
        "platformName": "Android",
        "deviceName": "9950b2b3",
    }
    print("\nstart driver for android device for test..")
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    yield driver
    print("\nquit driver..")
    driver.quit()
    