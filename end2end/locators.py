from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    LOGIN_FIELD = (By.ID,'username')
    PASSWORD_FIELD = (By.ID,'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR,"button[type=submit]")

class LoginPageCreds(object):
    LOGIN = "ag10chat_1"
    PASSWORD = "1234567"
