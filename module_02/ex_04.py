from selenium.webdriver.support.select import Select
from common.webdriver_factory import get_driver

driver = get_driver('chrome')
driver.get('https://formsmarts.com/form/axi?mode=h5')

first_name = driver.find_element_by_id('u_LY9_60857')
first_name.clear()
first_name.send_keys('Angie')
last_name = driver.find_element_by_id('u_LY9_60858')
last_name.clear()
last_name.send_keys('Garcia')

email = driver.find_element_by_id('u_LY9_60859')
email.clear()
email.send_keys('glovica@hotmail.com')
address = driver.find_element_by_id('u_LY9_60860')
address.clear()

address.send_keys('Test Address Angie')
country = Select(driver.find_element_by_id('u_LY9_60871'))
country.select_by_value("MX")
'''country.select_by_index(2)'''

check_in_date = driver.find_element_by_id('u_LY9_60861')
check_in_date.clear()
check_in_date.send_keys('12/12/2021')

double_room_btn = driver.find_element_by_id('u_LY9_60866_0')
double_room_btn.click()

address = driver.find_element_by_id('u_LY9_60870')
address.clear()
address.send_keys('4')

continue_btn = driver.find_element_by_name('submit')
continue_btn.click()
