#import the necessary module
from selenium.webdriver.common.by import By
import time

#define class with methods for our courses page
class OurCourses:
    def __init__(self,driver):
        self.driver = driver
        self.search_field = (By.XPATH,"//input[@name='searchTerm']")
        self.search_button = (By.XPATH,"//button[@class='btn-simple']")
        self.searched_link = By.XPATH,"//a[contains(@href,'/courses/quality-assurance-training-in-nepal')]//div[contains(@class,'z-10 inline-block transition group-hover:bg-green-50 group-hover:text-primary')]//span[@class='transition-all group-hover:mr-2'][normalize-space()='Learn More']"


    def open_page(self,url):
        self.driver.get(url)

        # method for scrolling down the window

    def scroll_window(self):
        target_y = 4000
        scroll_distance = 2000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)

    def enter_searchbar(self, course):
        self.driver.find_element(*self.search_field).send_keys(course)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def click_searched_course(self):
        self.driver.find_element(*self.searched_link).click()
