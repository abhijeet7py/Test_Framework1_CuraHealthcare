#Landing page class

#Page locators
# Page Actions


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from tests.constants.constants import Constants
from tests.utils.common_utils import webdriver_wait_url

class LandingPage:
    def __init__(self,driver):
        self.driver = driver

    # Page Locators
    # --> in the form of store the locators/ objects

    make_appointment_button = (By.XPATH,"//a[@id='btn-make-appointment']")

    # Page actions
    # write functions to access the page locators

    def get_appointment_button(self):
        return self.driver.find_element(*LandingPage.make_appointment_button) #Syntax to get the locators
    #(*) --> means from current class give me tuple/ variable


    def get_url_change(self):
        expected_url = Constants.login_url()
        webdriver_wait_url(self.driver, timeout= 5)
        assert self.driver.current_url == expected_url, f"Expected {expected_url} but got {self.driver.current_url}"


