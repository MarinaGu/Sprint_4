import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='function')
def browser():
    options = Options()
    options.binary_location = r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'
    options.add_argument("--window-size=1200,800")

    driver = webdriver.Firefox()
    yield driver
    driver.quit()