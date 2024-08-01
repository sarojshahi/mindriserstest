from selenium.webdriver.common.by import By
import time

class SuccessfulStories:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,url):
        self.driver.get(url)

    # method for scrolling down the window
    def scroll_window(self):
        target_y = 14000
        scroll_distance = 4000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)
    