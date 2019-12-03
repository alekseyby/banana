#run: py.test -v tests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.browser = driver
        self.browser.maximize_window()

class DuckDuckGoSearchPage(BasePage):
    URL = 'https://www.duckduckgo.com'
    #need create file for locators
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
#Moved to BasePage
    #def __init__(self, browser):
        #self.browser = browser

    def load(self):
        self.browser.get(self.URL)
        #self.browser.maximize_window()

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
