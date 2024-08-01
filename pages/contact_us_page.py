#import all the necessary modules
from selenium.webdriver.common.by import By
import time

#define class for the blog page
class ContactUs:
    def __init__(self,driver):
        self.driver = driver

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


