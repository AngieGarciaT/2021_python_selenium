"""Checkout Overview Locators"""
from selenium.webdriver.common.by import By


class CheckoutOverviewLoc:
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")
    BTN_CANCEL = (By.XPATH, "//button[contains(@class,'cart_cancel_link')]")
    BTN_FINISH = (By.ID, 'finish')
    TITLE_LABEL = (By.CLASS_NAME, 'title')

    SUCCESS_MSG = (By.CLASS_NAME, 'complete-header')
    SUCCESS_MSG_TWO = (By.CLASS_NAME, 'complete-text')
