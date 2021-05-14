""""Test cases filling information on Checkout step 1"""
from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.inventory import InventorySortOptions
from module_06.src.pages.login import LoginPage
from module_06.src.pages.cart import CartPage
from module_06.tests.common.test_base import TestBase
from module_06.src.pages.checkout_first import CheckoutFirstStep


_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

class TestCheckoutStep1(TestBase):

    def test_filling_info_checkout(self):
        """Test adding 1 product to cart and continue with checkout"""
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
        print('\n')
        print(f'Label: {inventory_page.get_label()}')
        assert inventory_page.get_label() == 'CHECKOUT: YOUR INFORMATION', 'Checkout page label should be Checkout'

        contact_info_page.checkout()

    def test_go_back(self):
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
        contact_info_page.back_to_cart()

    def test_error(self):
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
        contact_info_page.checkout()
        contact_info_page.get_error_msg()










