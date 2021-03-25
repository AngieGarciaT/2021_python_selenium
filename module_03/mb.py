from selenium.webdriver.support.wait import WebDriverWait
from common.webdriver_factory import get_driver

if __name__ == '__main__':
    my_driver = get_driver('chrome')
    my_wait = WebDriverWait(my_driver, 10)

    # Go to page
    my_driver.get('https://www.mlb.com/es/standings')

    # Select league option
    select_dropdown(my_wait, 'league')

    # Select standard
    select_standard(my_wait)

    # Select advance
    select_advance(my_wait)

