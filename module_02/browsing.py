"""Browsing example using Selenium"""
from pathlib import Path
from selenium import webdriver


def get_project_root() -> Path:
    """Get project root path"""
    return Path(__file__).parent.parent


def get_chrome_path() -> Path:
    """Get chrome driver path"""
    root = get_project_root()
    return root.joinpath('drivers', 'chromedriver')


driver = webdriver.Chrome(executable_path=get_chrome_path())


