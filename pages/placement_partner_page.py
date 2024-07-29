# import the necessary modules
from selenium.webdriver.common.by import By


# define the class for post plus 2 courses page
class PlacementPartner:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

