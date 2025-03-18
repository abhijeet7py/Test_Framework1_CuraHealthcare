# Page class
# Page locators
# page Actions

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from tests.utils.common_utils import webdriver_wait_url,webdriver_wait
from selenium.webdriver.support.ui import Select

class Appointment_Page:
    def __init__(self,driver):
        self.driver = driver

    # Page locators
    facility_selectbox = (By.ID,"combo_facility")
    checkbox = (By.XPATH,"//input[@id='chk_hospotal_readmission']")
    medicare_radio_button = (By.ID,"radio_program_medicare")
    medicaid_radio_button = (By.ID,"radio_program_medicaid")
    none_radio_button = (By.ID,"radio_program_none")
    date_control = (By.ID,"txt_visit_date")
    comment = (By.ID,"txt_comment")
    book_appointment = (By.ID,"btn-book-appointment")
    confirmation = (By.XPATH,"//p[@class = 'lead' and contains(text(),'appointment has been booked')]")

    #Page Actions
    # Write functions to access page locators

    def get_facility(self,value):
        select_element = self.driver.find_element(*Appointment_Page.facility_selectbox)
        select = Select(select_element)
        select.select_by_visible_text(value)

    def get_checkbox(self):
        return self.driver.find_element(*Appointment_Page.checkbox)

    def get_medicare(self):
        return self.driver.find_element(*Appointment_Page.medicare_radio_button)

    def get_medicaid(self):
        return self.driver.find_element(*Appointment_Page.medicaid_radio_button)

    def get_none(self):
        return self.driver.find_element(*Appointment_Page.none_radio_button)

    def get_date(self):
        return self.driver.find_element(*Appointment_Page.date_control)

    def get_comment(self):
        return self.driver.find_element(*Appointment_Page.comment)

    def get_appoinment(self):
        return self.driver.find_element(*Appointment_Page.book_appointment)

    def get_confirmation_text(self):
        try:
            return self.driver.find_element(*self.confirmation).text
        except Exception as e:
            print(f"Confirmation text not found: {e}")
            return None