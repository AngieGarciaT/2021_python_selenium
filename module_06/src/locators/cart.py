"""Locators for inventory items"""
from selenium.webdriver.common.by import By


class CartItemLoc:
    """Cart item locators.
    Locators are relative to parent container div.
    """
    QTY = (By.CLASS_NAME, 'cart_quantity')
    TITLE = (By.CLASS_NAME, 'inventory_item_name')
    DESCRIPTION = (By.CLASS_NAME, 'inventory_item_desc')
    PRICE = (By.CLASS_NAME, 'inventory_item_price')
    BTN = (By.XPATH, "//button[contains(@class,'cart_button')]")
    BTN_SHOP =(By.ID, 'continue-shopping')
    BTN_CHECK = (By.XPATH, "//button[contains(@class,'checkout_button')]")