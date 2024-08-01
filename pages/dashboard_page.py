#Dashboard Page
#import the necessary modules
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

#define class for the dashboard page
class DashboardPage:
    def __init__(self,driver):
        self.driver = driver
        self.banner_button = By.XPATH,"//span[@class='absolute right-0 top-0 flex h-[28px] w-[28px] -translate-y-1/2 translate-x-1/2 cursor-pointer items-center justify-center rounded-full bg-red-400 font-bold text-white md:h-[32px] md:w-[32px] ']"
        self.courses = (By.ID, 'course')
        self.name_field = By.XPATH,"//input[@placeholder='Full Name']"
        self.email_field = By.XPATH,"//input[@placeholder='Email']"
        self.phone_field = By.XPATH,"//input[@placeholder='Phone Number']"
        self.submit_button = By.XPATH,"//button[normalize-space()='Submit']"

    #method for launching the website
    def open_page(self,url):
        self.driver.get(url)

    #method for closing the dashboard banner
    def close_banner(self):
        self.driver.find_element(*self.banner_button).click()

    #method for scrolling down the window
    def scroll_window(self):
        target_y = 8000
        scroll_distance = 2000
        current_y = 0

        while current_y < target_y:
            self.driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
            current_y += scroll_distance
            time.sleep(2)

    def enter_interest(self):
        interested_course = self.driver.find_element(*self.courses)
        select = Select(interested_course)
        select.select_by_index(4)



    def enter_name(self,name):
        self.driver.find_element(*self.name_field).send_keys(name)

    def enter_email(self,email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_phone(self,phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()
