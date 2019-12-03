from locators import LoginPageLocators
from element import BasePageElement

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def write_login(self,keys):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_FIELD)
        element.send_keys(keys)

    def write_password(self,keys):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD)
        element.send_keys(keys)

    def click_login(self):
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()
