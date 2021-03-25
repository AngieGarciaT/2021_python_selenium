from common.webdriver_factory import get_driver


driver = get_driver('chrome')
driver.get('https://www.selenium.dev/')

print(driver.current_url)
print(driver.title)

download_link = driver.find_element_by_link_text('Downloads')

if download_link.is_enabled() and download_link.is_displayed():
    print('The text link is: ', download_link.text)
    download_link.click()

driver.quit()







