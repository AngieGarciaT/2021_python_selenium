from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://www.amazon.com.mx')
driver.implicitly_wait(10)


element = driver.find_elements_by_xpath("//a[@href]")

for item in element:
    if item.text == "Prime":
        print(item.text)

    if item.text == "AmazonBasics":
        print(item.text)

    if item.text == "Los Más Regalados":
        print(item.text)
