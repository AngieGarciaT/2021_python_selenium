'''Includes function to control sauce lab login page'''


from selenium.webdriver.common.by import By

from module_05.sauce_func_lib.common import write_to_input, click


def login(wait, user, password):
    """

    :param wait:
    :param user: Username
    :param password: Password
    :return:
    """

    write_to_input(wait, (By.ID, 'user-name'), user)
    write_to_input(wait, (By.ID, 'password'), password)
    click(wait, (By.ID, 'login-button'))
