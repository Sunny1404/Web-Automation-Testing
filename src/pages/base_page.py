

from selenium.webdriver.common.by import By

class BasePage:
    """Base class for all pages"""

    def _init_(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find(self, by, value):
        return self.driver.find_element(by, value)

    def click(self, by, value):
        self.find(by, value).click()

    def type(self, by, value, text):
        self.find(by, value).send_keys(text)

