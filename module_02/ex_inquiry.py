from selenium.webdriver.support.select import Select

from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.get('https://formsmarts.com/html-form-example')
driver.switch_to.frame(driver.find_element_by_class_name('fs_embed'))

print(driver.current_url)
print(driver.title)

f_Name = driver.find_element_by_name("u_jSx_4607")
f_Name.send_keys("Angie")

l_Name = driver.find_element_by_name("u_jSx_338354")
l_Name.send_keys("Garcia")


email = driver.find_element_by_name("u_jSx_4608")
email.send_keys("angelica.garcia.tapia@gmai.com")

dropdown = Select(driver.find_element_by_name("u_jSx_338367"))
dropdown.select_by_value("Sales Inquiry")


text_Area = driver.find_element_by_name("u_jSx_4609")
text_Area.send_keys("This is a new account")

continue_Button = driver.find_element_by_xpath("//*[@value= 'Continue →']")
continue_Button.click()









