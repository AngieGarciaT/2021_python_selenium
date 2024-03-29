"""Implements sauce lab login inventory."""
from enum import Enum
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.elements.header import Header
from module_06.src.elements.inventory_items import InventoryItems
from module_06.src.elements.select_element import SelectElement
from module_06.src.locators.inventory import InventoryPageLoc
from module_06.src.pages.base_page import BasePage
from module_06.src.pages.cart import CartPage



_URL = 'https://www.saucedemo.com/inventory.html'


class InventorySortOptions(Enum):
    """Possible options for sort dropdown."""
    A_TO_Z = 'az'
    Z_TO_A = 'za'
    PRICE_LOW_TO_HIGH = 'lohi'
    PRICE_HIGH_TO_LOW = 'hilo'


class InventoryPage(BasePage):
    """Sauce lab login."""

    def __init__(self, driver: WebDriver, timeout: int = 8):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self.products = InventoryItems(InventoryPageLoc.ITEMS, self._wait)
        self.__label = BasePageElement(InventoryPageLoc.LABEL, self._wait)
        self.__sort_dropdown = SelectElement(InventoryPageLoc.SORT_DROPDOWN, self._wait)

    def get_label(self) -> str:
        """Get page label."""
        return self.__label.get_text()

    def sort_by(self, option: InventorySortOptions):
        """Sort by specified value"""
        self.__sort_dropdown.select_by_value(option.value)

    def get_sort_value(self) -> str:
        """Get select sort value."""
        print(self.__sort_dropdown)
        return self.__sort_dropdown.get_selected_value()

    def open_cart(self):
        self.header.goto_cart()
        return CartPage(self._wait._driver, self._wait._timeout)

    def click_cart(self):
        return self.header.goto_cart()

    def display_menu(self):
        self.header.open_menu()

    def click_logout(self):
        return self.header.logout()


