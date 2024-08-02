#import all the necessary modules
from selenium.webdriver.common.by import By
import time

#define class for the blog page
class ContactUs:
    def __init__(self,driver):
        self.driver = driver
        self.name_field = By.XPATH,"//input[@placeholder='Name']"
        self.email_field = By.XPATH,"//input[@placeholder='Email']"
        self.phone_field = By.XPATH,"//input[@placeholder='Phone']"
        self.subject_field = By.XPATH,"//input[@placeholder='Subject']"
        self.queries_field = By.XPATH,"//textarea[@placeholder='Queries']"

    def open_page(self,url):
        self.driver.get(url)

    def scroll_window(self):
        target_y = 7000
        scroll_distance = 2000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)


    def enter_name(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def enter_subject(self, subject):
        self.driver.find_element(*self.subject_field).send_keys(subject)

    def enter_queries(self,queries):
        self.driver.find_element(*self.queries_field).send_keys(queries)

