#import the necessary module
from selenium.webdriver.common.by import By

#define class with methods for our courses page
class OurCourses:
    def __init__(self,driver):
        self.driver = driver
        self.search_field = By.XPATH,"//input[@name='searchTerm']"
        self.search_button = By.XPATH,"//button[@class='btn-simple']"

    def open_page(self,url):
        self.driver.get(url)

    def enter_searchbar(self,course):
        self.driver.find_element(*self.search_field).send_keys(course)
    def search_courses(self):
        self.driver.find_element(*self.search_button).click()