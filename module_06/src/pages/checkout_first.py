"""Implements sauce lab login checkout first step."""
from enum import Enum
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.elements.header import Header
from module_06.src.elements.inventory_items import InventoryItems
from module_06.src.elements.select_element import SelectElement
from module_06.src.locators.inventory import InventoryPageLoc
from module_06.src.locators.cart import CartItemLoc
from module_06.src.locators.checkout import CheckoutItemLoc
from module_06.src.pages.base_page import BasePage
from module_06.src.mixin.InventoryItemMixin import InventoryItemMixin
from module_06.src.locators.inventory_details import InventoryDetailsLoc
from module_06.src.elements.checkout_info import ContactCheckout
from module_06.src.pages.cart import CartPage

_URL = 'https://www.saucedemo.com/checkout-step-one.html'


class CheckoutFirstStep(InventoryItemMixin, BasePage):

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self._info_checkout = ContactCheckout(self._wait)
        self.header = Header(self._wait)

    def fill_info(self, firstname="", lastname="", postal_code=""):
        self._info_checkout.fill_info(firstname, lastname, postal_code)

    def checkout(self):
        self._info_checkout.checkout()
        return CartPage(self._wait._driver, self._wait._timeout)

    def back_to_cart(self):
        self._info_checkout.back_to_cart()


