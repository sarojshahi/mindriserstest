#import all the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pages.dashboard_page import DashboardPage

#set the driver as Chrome Driver Manager
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(2)
    #yield the driver
    yield driver
    #close the driver instance
    driver.quit()

#define function for dashboard
def test_dashboard(driver):
    dashboard_page = DashboardPage(driver)
    dashboard_page.open_page("https://www.mindrisers.com.np/")
    driver.maximize_window()
    dashboard_page.close_banner()
    time.sleep(3)
    dashboard_page.scroll_window()
    time.sleep(1)
    print("The Dashboard has been tested succesfully!!")
