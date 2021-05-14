"""Contact Information"""
from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.checkout import CheckoutItemLoc


class ContactCheckout:
    """Represent Contact Info section"""

    def __init__(self, wait: WebDriverWait):
        self._wait = wait
        self._firstname = BasePageElement(CheckoutItemLoc.F_NAME, wait=wait)
        self._lastname = BasePageElement(CheckoutItemLoc.L_NAME, wait=wait)
        self._postal_code = BasePageElement(CheckoutItemLoc.ZIPCODE, wait=wait)
        self._error_msg = BasePageElement(CheckoutItemLoc.ERROR_MSG, wait=wait)
        self._cancel_btn = BasePageElement(CheckoutItemLoc.BTN_BACK, wait=wait)
        self._continue_btn = BasePageElement(CheckoutItemLoc.BTN_CONT, wait=wait)

    def fill_info(self, firstname="", lastname="", postal_code=""):
        self._firstname.write(firstname)
        self._lastname.write(lastname)
        self._postal_code.write(postal_code)

    def checkout(self):
        self._continue_btn.click()

    def back_to_cart(self):
        self._cancel_btn.click()

    def get_error_msg(self):
        return self._error_msg.get_text()



