from selenium.webdriver.common.by import By

class SuccessfulStories:
    def __init__(self,driver):
        self.driver = driver


    def open_page(self,url):
        self.driver.get(url)

    