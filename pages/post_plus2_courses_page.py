#import the necessary modules
from selenium.webdriver.common.by import By
import time
#define the class for post plus 2 courses page
class PostPlusTwo:
    def __init__(self,driver):
        self.driver = driver

    # method to launch the webpage
    def open_page(self,url):
        self.driver.get(url)

     # method for scrolling down the window
    def scroll_window(self):
        target_y = 1500
        scroll_distance = 750
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)