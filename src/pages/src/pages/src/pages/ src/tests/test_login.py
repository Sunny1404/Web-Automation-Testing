

import pytest
from selenium import webdriver
from src.pages.login_page import LoginPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # You need ChromeDriver installed
    driver.maximize_window()
    yield driver
    driver.quit()

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_success_message()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open("https://the-internet.herokuapp.com/login")
    login_page.login("wrong", "wrong")
    assert "Your username is invalid!" in login_page.get_error_message()

