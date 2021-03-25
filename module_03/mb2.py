from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common.webdriver_factory import get_driver

def select_Option(wait: WebDriverWait, datavalue):
    locator = (By.XPATH, f"//*[@data-value='{datavalue}']")
    element = wait.until(EC.element_to_be_clickable(locator))
    element.click()

def select_listDropdown(wait: WebDriverWait, option: str):
    locator = (By.XPATH, "//*[contains(@class, 'p-dropdown__standings')]")
    element = wait.until(EC.element_to_be_clickable(locator))
    div_dropdown = Select(element)
    div_dropdown.select_by_value(option)


driver = get_driver('chrome')
wait = WebDriverWait(driver, 10)

driver.get('https://www.mlb.com/es/standings')
select_listDropdown(wait, 'league')
select_Option(wait, "standard")



