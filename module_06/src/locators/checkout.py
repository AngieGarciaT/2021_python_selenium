"""Locators for checkout items"""
from selenium.webdriver.common.by import By


class CheckoutItemLoc:
    """Checkout item locators.
    Locators are relative to parent container div.
    """
    F_NAME = (By.ID, 'first-name')
    L_NAME = (By.ID, 'last-name')
    ZIPCODE = (By.ID, 'postal-code')
    BTN_BACK = (By.XPATH, "//button[contains(@class,'cart_cancel_link')]")
    BTN_CONT = (By.ID, "continue")

