#Dashboard Page

#import the necessary modules
from selenium.webdriver.common.by import By
import time

#define class for the dashboard page
class DashboardPage:
    def __init__(self,driver):
        self.driver = driver
        self.banner_button = By.XPATH,"//span[@class='absolute right-0 top-0 flex h-[28px] w-[28px] -translate-y-1/2 translate-x-1/2 cursor-pointer items-center justify-center rounded-full bg-red-400 font-bold text-white md:h-[32px] md:w-[32px] ']"

    #method for launching the website
    def open_page(self,url):
        self.driver.get(url)

    #method for closing the dashboard banner
    def close_banner(self):
        self.driver.find_element(*self.banner_button).click()

    #method for scrolling down the window
    def scroll_window(self):
        target_y = 6000
        scroll_distance = 1000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(5)