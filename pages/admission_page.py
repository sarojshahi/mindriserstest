#import all the necessary modules
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#define class for the admission page
class Admission:
    def __init__(self,driver):
        self.driver = driver
        self.fullname_textbox = By.XPATH,"//input[@id='full_name']"
        self.email_textbox = By.XPATH,"//input[@id='email']"
        self.phone_textbox = By.XPATH,"//input[@id='mobile_no']"
        self.college_textbox = By.XPATH,"//input[@id='college']"
        self.academic_status_dropdown = (By.ID, 'qualification')
        self.interest= (By.ID,'course')
        self.preferred_schedule = (By.ID,'shedule')
        self.queries_textbox = By.XPATH,"//textarea[@id='question']"
    def open_page(self,url):
        self.driver.get(url)

    def enter_fullname(self,fullname):
        self.driver.find_element(*self.fullname_textbox).send_keys(fullname)

    def enter_email(self,email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*self.phone_textbox).send_keys(phone)

    def enter_college(self,college):
        self.driver.find_element(*self.college_textbox).send_keys(college)

    def enter_academic_qualification(self):
        academics = self.driver.find_element(*self.academic_status_dropdown)
        select1 = Select(academics)
        select1.select_by_index(1)

    def enter_interest(self):
        interested_course = self.driver.find_element(*self.interest)
        select2 = Select(interested_course)
        select2.select_by_index(4)

    def enter_schedule(self):
        schedule = self.driver.find_element(*self.preferred_schedule)
        select3 = Select(schedule)
        select3.select_by_index(2)

    def enter_queries(self, queries):
        self.driver.find_element(*self.queries_textbox).send_keys(queries)



