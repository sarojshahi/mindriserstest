#import all the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pages.dashboard_page import DashboardPage
from pages.our_courses_page import OurCourses
from pages.post_plus2_courses_page import PostPlusTwo
from pages.placement_partner_page import PlacementPartner
from pages.successful_stories_page import SuccessfulStories
from pages.blogs_page import Blogs
from pages.contact_us_page import ContactUs
from pages.admission_page import Admission

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
    time.sleep(2)
    # dashboard_page.close_banner()
    # time.sleep(2)
    dashboard_page.scroll_window()
    time.sleep(1)
    dashboard_page.enter_interest()
    time.sleep(2)
    dashboard_page.enter_name("John Doe")
    time.sleep(2)
    dashboard_page.enter_email("John@gmail.com")
    time.sleep(1)
    dashboard_page.enter_phone("9898998989")
    time.sleep(1)
    dashboard_page.click_submit() #click_submit() method to submit the form
    time.sleep(2)

    print("The Dashboard has been tested successfully!!")


def test_ourcourses(driver):
    our_courses = OurCourses(driver)
    our_courses.open_page("https://www.mindrisers.com.np/courses")
    driver.maximize_window()
    time.sleep(1)
    our_courses.scroll_window()
    time.sleep(1)
    our_courses.enter_searchbar("QA")
    time.sleep(1)
    our_courses.search()
    time.sleep(3)
    # our_courses.search_course()

    print("Our Courses Page has been tested successfully!!")


def test_postplus2(driver):
    post_plus = PostPlusTwo(driver)
    post_plus.open_page("https://www.mindrisers.com.np/after+2-courses")
    driver.maximize_window()
    time.sleep(1)
    post_plus.scroll_window()
    time.sleep(1)


def test_placement_partner(driver):
    placement = PlacementPartner(driver)
    placement.open_page("https://www.mindrisers.com.np/placement-partner")
    driver.maximize_window()
    time.sleep(1)
    placement.scroll_window()
    time.sleep(2)

    print("Placement Partner Page has been tested successfully!!")

def test_successful_stories(driver):
    stories = SuccessfulStories(driver)
    stories.open_page("https://www.mindrisers.com.np/success-gallery")
    driver.maximize_window()
    time.sleep(1)
    stories.scroll_window()
    time.sleep(2)

    print("Successful Stories Page has been tested successfully!!")

def test_blogs(driver):
    blogs = Blogs(driver)
    blogs.open_page("https://www.mindrisers.com.np/blogs")
    driver.maximize_window()
    blogs.scroll_window()
    time.sleep(2)

    print("Blogs Page has been tested successfully!!")


def test_contactus(driver):
    contact_us = ContactUs(driver)
    contact_us.open_page("https://www.mindrisers.com.np/contact-us")
    driver.maximize_window()
    time.sleep(1)
    contact_us.scroll_window()
    time.sleep(1)

    print("Contact Us Page has been tested successfully!!")

def test_admission(driver):
    admission = Admission(driver)
    admission.open_page("https://www.mindrisers.com.np/online-admission")
    driver.maximize_window()
    time.sleep(1)
    admission.enter_fullname("ram nepali")
    time.sleep(1)
    admission.enter_email("ram@gmail.com")
    time.sleep(1)
    admission.enter_phone("9818839688")
    time.sleep(1)
    admission.enter_college("New Horizon College")
    time.sleep(1)
    admission.enter_academic_qualification()
    time.sleep(1)
    admission.enter_interest()
    time.sleep(1)
    admission.enter_schedule()
    time.sleep(1)
    admission.enter_queries("This is a test for admission")
    time.sleep(1)

    print("Admission Page has been tested successfully!!")