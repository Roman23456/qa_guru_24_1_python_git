import time

import pytest
from selenium import webdriver


@pytest.mark.first
def test_selenium_web():
    driver = webdriver.Chrome()
    url = "https://www.google.com/"
    driver.get(url)

    assert driver.title == "Google"
    assert driver.current_url == url
    time.sleep(3)


@pytest.mark.second
def test_selenium_web():
    driver = webdriver.Chrome()
    url = "https://github.com/"
    driver.get(url)
    assert driver.current_url == url
    time.sleep(3)
