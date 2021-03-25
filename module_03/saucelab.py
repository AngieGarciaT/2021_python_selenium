'''Sauce lab login example'''
from selenium.webdriver.remote.webelement import WebElement

from common.webdriver_factory import get_driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def login(wait: WebDriverWait, userN: str, secret: str):
    '''Login to sauce lab.'''
    #user_id: user-name
    #password_id: password
    #login_id: login_button
    user_locator = (By.ID, 'user-name')
    #Presence - Existe en DOM, No garantiza visibilidad
    #Visibility - Existe en DOM, garantiza estar visible
    #clickable - Visible y se puede dar click
    #condition = EC.element_to_be_clickable(user_locator)
    user_element = wait.until(EC.element_to_be_clickable(user_locator))
    user_element: WebElement
    user_element.clear()
    user_element.send_keys(userN)

    password_locator = (By.ID, 'password')
    password = wait.until(EC.element_to_be_clickable(password_locator))
    password.clear()
    password.send_keys(secret)

    login_locator = (By.ID, 'login-button')
    login_element = wait.until(EC.element_to_be_clickable(login_locator))
    login_element.click()

def get_catalog_info(wait):
    '''Get catalog information'''
    result = []
    products_locator = (By.CLASS_NAME, 'inventory_item')
    products = wait.until(EC.visibility_of_all_elements_located(products_locator))

    for product in products:
        product: WebElement
        name = product.find_element_by_class_name('inventory_item_name')
        price = product.find_element_by_class_name('inventory_item_price')
        result.append(f'Name {name.text}, Price: {price.text}')

    return result


if __name__ == '__main__':
    driver = get_driver('chrome')

    wait = WebDriverWait(driver, 5)

    driver.get('https://www.saucedemo.com/')

    login(wait, 'standard_user', 'secret_sauce')

    print(get_catalog_info(wait))

    driver.quit()