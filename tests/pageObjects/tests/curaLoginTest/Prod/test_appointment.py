import allure
import time
from selenium import webdriver
import pytest
from tests.constants.constants import Constants
from tests.pageObjects.pom.login_page import LoginPage
from tests.pageObjects.pom.landing_page import LandingPage
from tests.pageObjects.pom.appointment_page import Appointment_Page
from selenium.webdriver.support.ui import Select

#Assertions and use of page object class
# Webdriver start
# User Interaction + assertion
# close driver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get(Constants.appointment_url())
    return driver

@allure.epic("Cure Login test")
@allure.feature("TC3 - get appointment with Tokyo")
@pytest.mark.positive

def test_appoinment_with_tokyo(setup):
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Tokyo CURA Healthcare Center")
    time.sleep(5)