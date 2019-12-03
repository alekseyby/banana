Learn more or give us feedback
import unittest
from selenium import webdriver
import page
import time
from locators import LoginPageCreds

class open_ai_and_enter_creds(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://agent-west.digital.nuance.com/")

    def test_enter_credentials(self):
        LoginPage = page.LoginPage(self.driver)
        LoginPage.write_login(LoginPageCreds.LOGIN)
        LoginPage.write_password(LoginPageCreds.PASSWORD)
        time.sleep(1)
        LoginPage.click_login()

if __name__ == "__main__":
    unittest.main()


    def tearDown(self):
        self.driver.close()
