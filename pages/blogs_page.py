#import all the necessary modules
import time
from selenium.webdriver.common.by import By

#define class for the blog page
class Blogs:
    def __init__(self,driver):
        self.driver = driver
        self.search_field = By.XPATH,"//input[@name='searchTerm']"
        self.search_button = By.XPATH,"//button[@class='btn-simple']//*[name()='svg']"
        self.searched_result = By.XPATH,"//a[@href='/blogs/career-in-quality-assurance-qa-in-nepal-mindrisers-exploring-opportunities-in-kathmandu-lalitpur-and-bhaktapur']//img[contains(@class,'h-[176px] w-full rounded-tl-xl rounded-tr-xl')]"

    def open_page(self,url):
        self.driver.get(url)


    def scroll_window(self):
        target_y = 4000
        scroll_distance = 2000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)


    def enter_searchbar(self,searchblogs):
        self.driver.find_element(*self.search_field).send_keys(searchblogs)

    def click_search(self):
        self.driver.find_element(*self.search_button).click()

    def click_search_result(self):
        self.driver.find_element(*self.searched_result).click()