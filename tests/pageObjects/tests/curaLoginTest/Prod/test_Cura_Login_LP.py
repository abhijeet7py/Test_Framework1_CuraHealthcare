import allure
import pytest
import time
from selenium import webdriver
from tests.constants.constants import Constants
from tests.pageObjects.pom.landing_page import LandingPage
from tests.pageObjects.pom.login_page import LoginPage

#Assertions and use of page object class
# Webdriver start
# User Interaction + assertion
# close driver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Constants.landing_url())
    return driver

@allure.epic("Cure Login test")
@allure.feature("TC0 - Landing page test case")
@pytest.mark.positive
def test_Landing_page(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    landing_page.get_url_change()
    time.sleep(5)
