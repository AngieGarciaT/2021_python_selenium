"""Test cases for login"""
import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver
from module_05.sauce_func_lib.inventory import get_inventory, namedtuple
from module_05.sauce_func_lib.login import login

LOGIN_DATA = [('standard_user', 'secret_sauce'), ('standard_user', 'secret_sauce')]

''' def test_valid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'secret_sauce')
    items = get_inventory(wait)
    assert len(items) > 0, 'Inventory should be loaded'

'''




def test_invalid_user():
    driver = get_driver('chrome')
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.saucedemo.com/')
    login(wait, 'standard_user', 'invalid secret ')
    with pytest.raises(TimeoutException):
        get_inventory()
    driver.close()




