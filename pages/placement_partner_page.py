# import the necessary modules
from selenium.webdriver.common.by import By
import time

# define the class for post plus 2 courses page
class PlacementPartner:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)


    #method to scroll down the window
    def scroll_window(self):
        target_y = 7000
        scroll_distance = 2000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)
