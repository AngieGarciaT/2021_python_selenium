from selenium.webdriver.support.wait import WebDriverWait
from module_06.src.elements.base_page_element import BasePageElement
from module_06.src.locators.check_overview import CheckoutOverviewLoc


class CheckoutOver:
    def __init__(self, wait: WebDriverWait):
        self._wait = wait
        self._subtotal = BasePageElement(CheckoutOverviewLoc.ITEM_TOTAL, wait=wait)
        self._total = BasePageElement(CheckoutOverviewLoc.TOTAL, wait=wait)
        self._cancel_btn = BasePageElement(CheckoutOverviewLoc.BTN_CANCEL, wait=wait)
        self._finish_btn = BasePageElement(CheckoutOverviewLoc.BTN_FINISH, wait=wait)
        self._success_msg = BasePageElement(CheckoutOverviewLoc.SUCCESS_MSG, wait=wait)
        self._title = BasePageElement(CheckoutOverviewLoc.TITLE_LABEL, wait=wait)

    def cancel_check(self):
        self._cancel_btn.click()

    def finish(self):
        self._finish_btn.click()

    def get_subtotal(self) -> str:
        return self._subtotal.get_text()

    def get_total(self) -> str:
        return self._total.get_text()

    def get_success_msg(self) -> str:
        return self._success_msg.get_text()

    def get_title(self) -> str:
        return self._title.get_text()