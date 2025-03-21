import allure
import time
from selenium import webdriver
import pytest
from tests.constants.constants import Constants
from tests.pageObjects.pom.login_page import LoginPage
from tests.pageObjects.pom.landing_page import LandingPage
from tests.pageObjects.pom.appointment_page import Appointment_Page
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe",pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Tokyo CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_medicare().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Tokyo test")
    appointment1.get_appoinment().click()
    WebDriverWait(setup, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'appointment has been booked')]"))
    )
    confirmation_text = appointment1.get_confirmation_text()
    assert confirmation_text is not None, "Confirmation text not found"
    assert "Please be informed that your appointment has been booked as following:" in confirmation_text, f"Expected text not found! Got: {confirmation_text}"
    time.sleep(5)

@allure.epic("Cure Login test")
@allure.feature("TC4 - get appointment with Hongkong")
@pytest.mark.positive
def test_appoinment_with_hongkong(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe",pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Hongkong CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_medicare().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Hongkong test")
    appointment1.get_appoinment().click()
    time.sleep(5)

@allure.epic("Cure Login test")
@allure.feature("TC5 - get appointment with Seoul")
@pytest.mark.positive
def test_appoinment_with_Seoul(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe",pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Seoul CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_medicare().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Seoul test")
    appointment1.get_appoinment().click()
    time.sleep(5)

@allure.epic("Cure Login test")
@allure.feature("TC6 - get appointment with medicaid_Tokyo")
@pytest.mark.positive
def test_appointment_with_medicaid_Tokyo(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe", pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Tokyo CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_medicaid().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Tokyo test")
    appointment1.get_appoinment().click()
    time.sleep(5)

@allure.epic("Cure Login test")
@allure.feature("TC7 - get appointment with medicaid_Hongkong")
@pytest.mark.positive
def test_appoinment_with_medicaid_hongkong(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe",pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Hongkong CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_medicaid().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Hongkong test")
    appointment1.get_appoinment().click()
    time.sleep(5)

@allure.epic("Cure Login test")
@allure.feature("TC8 - get appointment with Medicaid_Seoul")
@pytest.mark.positive
def test_appoinment_with_medicaid_Seoul(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe",pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Seoul CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_medicaid().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Seoul test")
    appointment1.get_appoinment().click()
    time.sleep(5)

@allure.epic("Cure Login test")
@allure.feature("TC9 - get appointment with none_Tokyo")
@pytest.mark.positive
def test_appointment_with_none_Tokyo(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe", pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Tokyo CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_none().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Tokyo test")
    appointment1.get_appoinment().click()
    time.sleep(5)

@allure.epic("Cure Login test")
@allure.feature("TC10 - get appointment with none_Hongkong")
@pytest.mark.positive
def test_appoinment_with_none_hongkong(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe",pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Hongkong CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_none().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Hongkong test")
    appointment1.get_appoinment().click()
    time.sleep(5)

@allure.epic("Cure Login test")
@allure.feature("TC11 - get appointment with none_Seoul")
@pytest.mark.positive
def test_appoinment_with_medicaid_Seoul(setup):
    landing_page = LandingPage(driver=setup)
    landing_page.get_appointment_button().click()
    login = LoginPage(driver=setup)
    login.login_to_Cura(usr="John Doe",pwd="ThisIsNotAPassword")
    appointment1 = Appointment_Page(driver=setup)
    appointment1.get_facility("Seoul CURA Healthcare Center")
    appointment1.get_checkbox().click()
    appointment1.get_none().click()
    appointment1.get_date().send_keys("19/03/2025")
    appointment1.get_comment().send_keys("Seoul test")
    appointment1.get_appoinment().click()
    time.sleep(5)

