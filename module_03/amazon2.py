from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://www.amazon.com.mx')
driver.implicitly_wait(10)


prime_element = driver.find_element_by_xpath("//a[@href='/prime?ref_=nav_cs_primelink_nonmember_542c13292a364e9b90e220b1580ec24c']")
print(prime_element.text)

prime_element2 = driver.find_element_by_xpath("//a[@href='/stores/node/12273534011/?field-lbr_brands_browse-bin=Amazon+Basics&ref_=nav_cs_amazonbasics_d64e1c4aa88849d9b6bc6ae7c06f5118']")
print(prime_element2.text)

prime_element3 = driver.find_element_by_xpath("//a[@href='/gcx/-/gfhz/?ref_=nav_cs_giftfinder_84c9e1115de24ed3be6d8360d1340d66']")
print(prime_element3.text)






