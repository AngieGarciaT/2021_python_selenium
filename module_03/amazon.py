from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://www.amazon.com.mx')
driver.implicitly_wait(10)

one_element = driver.find_elements_by_xpath("//a")
for element in one_element:
    print(element.text)



head_childs = driver.find_elements_by_xpath("//a[@head/*]")  # List: [WebElement, WebElement, WebElement]
print(f'Total of Head childs = {len(head_childs)}')
for child in head_childs:
    print(child.text)
