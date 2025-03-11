# Login page class

# Page locators
# Page Actions

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from tests.constants.constants import Constants
from tests.utils.common_utils import webdriver_wait_url,webdriver_wait


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    # Page locators

    username = (By.ID,"txt-username")
    password = (By.ID,"txt-password")
    login_button = (By.ID,"btn-login")
    error_msg = (By.XPATH,"//p[contains(@class, 'text-danger')]")

    #Page Actions
    # Write functions to access page locators

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_login_button(self):
        return self.driver.find_element(*LoginPage.login_button)

    def get_error_msg(self):
        webdriver_wait(self.driver,element_tuple= self.error_msg,timeout=5)
        return self.driver.find_element(*LoginPage.error_msg)


    def login_to_Cura(self,usr,pwd):
        try:
            self.get_username().send_keys(usr)
            self.get_password().send_keys(pwd)
            self.get_login_button().click()
        except Exception as e:
            print(e)

    def get_error_msg_text(self):
        return self.get_error_msg().text

    def get_change_url(self):
        expected_url = Constants.appointment_url()
        webdriver_wait_url(self.driver,timeout=5)
        assert self.driver.current_url == expected_url, f"Expected {expected_url} but got {self.driver.current_url}"