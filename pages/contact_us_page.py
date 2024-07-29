#import all the necessary modules
from selenium.webdriver.common.by import By

#define class for the blog page
class ContactUs:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,url):
        self.driver.get(url)


