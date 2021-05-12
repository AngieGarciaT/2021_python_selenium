from module_06.src.elements.checkout_info import ContactCheckout
from module_06.src.elements.checkout_overview import CheckoutOver
from module_06.src.pages.base_page import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from module_06.src.elements.header import Header

_URL = "https://www.saucedemo.com/checkout-step-two.html"


class CheckoutPage(BasePage):
    def __init__(self, driver: WebDriver, timeout: int = 5):
        super().__init__(driver, _URL, timeout)
        self.header = Header(self._wait)
        self.checkout = CheckoutOver(self._wait)
        # self.items = CartItems(self._wait)

    def cancel_buy(self):
        self.checkout.cancel_check()

    def finish_buy(self):
        self.checkout.finish()

    def get_subtotal_text(self)-> str:
        return self.checkout.get_subtotal()

    def get_total_text(self)-> str:
        return self.checkout.get_total()

    def get_title_text(self)-> str:
        return self.checkout.get_title()

    def get_success_msg(self)-> str:
        return self.checkout.get_success_msg()
