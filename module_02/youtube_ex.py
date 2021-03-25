from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from common.webdriver_factory import get_driver
from selenium.webdriver.support import  expected_conditions as EC


driver = get_driver('chrome')
driver.get('https://www.youtube.com/')

wait = WebDriverWait(driver, 20)
search_locator = (By.ID, 'search')
search_box = wait.until(EC.element_to_be_clickable(search_locator))
search_box.send_keys("Selenium")

search_btn_locator = (By.ID, 'search-icon-legacy')
search_button = wait.until(EC.element_to_be_clickable(search_btn_locator))
search_button.click()


results_locator = [By.ID, 'video-title']
results = wait.until(EC.visibility_of_all_elements_located(results_locator))


print(f'Titulos: {len(results)}')

for result in results:
    print(result.text)

driver.quit()




