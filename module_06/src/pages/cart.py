"""Implements sauce lab login cart."""
from enum import Enum
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.elements.header import Header
from module_06.src.elements.inventory_items import InventoryItems
from module_06.src.elements.select_element import SelectElement
from module_06.src.locators.inventory import InventoryPageLoc
from module_06.src.locators.cart import CartItemLoc
from module_06.src.pages.base_page import BasePage
from module_06.src.mixin.InventoryItemMixin import InventoryItemMixin
from module_06.src.locators.inventory_details import InventoryDetailsLoc


_URL = 'https://www.saucedemo.com/cart.html'

class CartPage(InventoryItemMixin, BasePage):
    """Implements inventory item details"""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self._quantity = BasePageElement(CartItemLoc.QTY, wait=self._wait)
        self._title = BasePageElement(CartItemLoc.TITLE, wait=self._wait)
        self._description = BasePageElement(CartItemLoc.DESCRIPTION, wait=self._wait)
        self._price = BasePageElement(CartItemLoc.PRICE, wait=self._wait)
        self._inv_btn = BasePageElement(CartItemLoc.BTN, wait=self._wait)
        self._back_shop = BasePageElement(CartItemLoc.BTN_SHOP, wait=self._wait)
        self._check_btn = BasePageElement(CartItemLoc.BTN_CHECK, wait=self._wait)
        self.header = Header(self._wait)

    def get_quantity(self):
        """Get product quantity"""
        return self._quantity.get_text()

    def back(self):
        """Go back to inventory page"""
        self._back_shop.click()

    def checkout(self):
        """Continue with checkout"""
        self._check_btn.click()
