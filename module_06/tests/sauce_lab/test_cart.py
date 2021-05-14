"""Test cases for adding items to cart"""
from module_06.src.elements.inventory_item import InventoryItem
from module_06.src.pages.inventory import InventorySortOptions
from module_06.src.pages.login import LoginPage
from module_06.src.pages.cart import CartPage
from module_06.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'


class TestCart(TestBase):

    def test_adding_products_and_back(self):
        """Test adding 2 products to cart and going back to shopping"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        details_page.back()
        inventory_page.products.reload()

        second_item = inventory_page.products[1]
        second_item: InventoryItem
        details_page = second_item.open_details()
        details_page.add_to_cart()
        details_page.back()
        inventory_page.products.reload()

        details_page.header.goto_cart()
        print('\n')
        print(f'Label: {inventory_page.get_label()}')
        assert inventory_page.get_label() == 'YOUR CART', 'Cart page label should be Your Cart'

        cart = inventory_page.open_cart()
        cart.back()

    def test_adding_products_and_checking(self):
        """Test adding 1 product and checking the quantity"""
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        # Adding 1 product to cart
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        details_page.back()
        inventory_page.products.reload()
        cart = inventory_page.open_cart()
        print('\n')
        print(f'Quantity of Products:{cart.get_quantity()}')
        print('\n')
        print(f'Product Name:{cart.get_title()}')
        print('\n')
        print(f'Product description:{cart.get_description()}')
        print('\n')
        print(f'Product Price:{cart.get_price()}')

        cart.checkout()

    def test_remove_product(self):
        login = LoginPage(self.driver)
        login.open()
        inventory_page = login.login(_DEF_USER, _DEF_PASSWORD)
        # Adding 1 product to cart
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.open_details()
        details_page.add_to_cart()
        details_page.back()
        inventory_page.products.reload()
        cart = inventory_page.open_cart()
        cart.remove_from_cart()



















