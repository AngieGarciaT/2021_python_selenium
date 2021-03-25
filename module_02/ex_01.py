from selenium import webdriver
from module_02.browsing import get_chrome_path


driver = webdriver.Chrome(executable_path=get_chrome_path())
driver.get('https://google.com')

print(driver.current_url)
print(driver.title)

driver.get("https://www.mlb.com/es")
print(driver.current_url)
print(driver.title)
print(driver.page_source)

driver.get("https://www.nytimes.com/es/")
driver.refresh()
print(driver.current_url)
print(driver.title)
driver.back()
driver.back()
print(driver.current_url)
print(driver.title)

print(driver.get_cookies())
print(driver.application_cache)

print(driver.find_elements_by_partial_link_text("SOCzOAOac8uhByk5ZGU2Zg=="))


driver.quit()