'''Includes function to control sauce lab inventory page'''
from collections import namedtuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

InventoryItem = namedtuple('InventoryItem', ['title', 'description', 'price'])


def get_inventory(wait: WebDriverWait):
    """

    :param wait: Instance of web driver wait
    :return: List with product information
    """

    item_locator = (By.XPATH, '//div[@class= "inventory_item"]')
    elements: WebElement
    elements = wait.until(EC.visibility_of_all_elements_located(item_locator))
    items_inv = []
    for index, element in enumerate(elements):
        element: WebElement
        title = element.find_element_by_class_name('inventory_item_name').text
        description = element.find_element_by_class_name('inventory_item_desc').text
        price = element.find_element_by_class_name('inventory_item_price').text
        tmp = InventoryItem(title, description, price)
        items_inv.append(tmp)
    return items_inv
