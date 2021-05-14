"""Test cases completing Checkout step 2"""
from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.inventory import InventorySortOptions
from module_06.src.pages.login import LoginPage
from module_06.src.pages.cart import CartPage
from module_06.tests.common.test_base import TestBase
from module_06.src.pages.checkout_first import CheckoutFirstStep
from module_06.src.pages.checkout_overview import CheckoutPage


_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

class TestCheckoutStep2(TestBase):

    def test_completing_checkout(self):
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        cart_page = inventory_page.open_cart()
        cart_page.checkout()
        contact_info_page = CheckoutFirstStep(self.driver)
        contact_info_page.fill_info("Angie", "Garcia", "44540")
        contact_info_page.checkout()
        checkout_page = CheckoutPage(self.driver)
        print('\n')
        print(f'Label: {checkout_page.get_title_text()}')
        assert checkout_page.get_title_text() == 'CHECKOUT: OVERVIEW', 'Checkout page title should be CHECKOUT: OVERVIEW'
        checkout_page.finish_buy()
        assert checkout_page.get_thanks_text() == 'THANK YOU FOR YOUR ORDER', 'Success page label should be THANK YOU FOR YOUR ORDER'
        assert checkout_page.get_img() != 'False', 'Image Pony OK'

    def test_validation_prices(self):
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        cart_page = inventory_page.open_cart()
        cart_page.checkout()
        contact_info_page = CheckoutFirstStep(self.driver)
        contact_info_page.fill_info("Angie", "Garcia", "44540")
        contact_info_page.checkout()
        checkout_page = CheckoutPage(self.driver)
        assert checkout_page.get_subtotal_text() == "Item total: $29.99"
        assert checkout_page.get_tax_text() == "Tax: $2.40"
        assert checkout_page.get_total_text() == "Total: $32.39"


    def test_cancel_checkout(self):
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        cart_page = inventory_page.open_cart()
        cart_page.checkout()
        contact_info_page = CheckoutFirstStep(self.driver)
        contact_info_page.fill_info("Angie", "Garcia", "44540")
        contact_info_page.checkout()
        checkout_page = CheckoutPage(self.driver)
        checkout_page.cancel_checkout()
        assert inventory_page.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

