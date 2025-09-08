

from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Login Page Object"""

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".flash.success")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".flash.error")

    def login(self, username, password):
        self.type(*self.USERNAME, text=username)
        self.type(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BUTTON)

    def get_success_message(self):
        return self.find(*self.SUCCESS_MESSAGE).text

    def get_error_message(self):
        return self.find(*self.ERROR_MESSAGE).text

