import allure
import time
import pytest
from selenium import webdriver
from tests.constants.constants import Constants
from tests.pageObjects.pom.login_page import LoginPage
from tests.pageObjects.pom.landing_page import LandingPage


#Assertions and use of page object class
# Webdriver start
# User Interaction + assertion
# close driver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get(Constants.login_url())
    return driver

@allure.epic("Cure Login test")
@allure.feature("TC1 - Negative Login page test case")
@pytest.mark.negative

def test_cura_login_negative(setup):
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr= "john",pwd="123")
    time.sleep(5)
    error = login.get_error_msg_text()
    assert error == "Login failed! Please ensure the username and password are valid."

@allure.epic("Cure Login test")
@allure.feature("TC2 - positive Login page test case")
@pytest.mark.positive

def test_cura_login_positive(setup):
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe",pwd="ThisIsNotAPassword")
    login.get_change_url()
    time.sleep(5)
