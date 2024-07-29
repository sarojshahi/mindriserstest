#import all the necessary modules
from selenium.webdriver.common.by import By

#define class for the admission page
class Admission:
    def __init__(self,driver):
        self.driver = driver
        self.fullname_textbox = By.XPATH,"//input[@id='full_name']"
        self.email_textbox = By.XPATH,"//input[@id='email']"
        self.phone_textbox = By.XPATH,"//input[@id='mobile_no']"
        self.college_textbox = By.XPATH,"//input[@id='college']"
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

    def enter_queries(self, queries):
        self.driver.find_element(*self.queries_textbox).send_keys(queries)



