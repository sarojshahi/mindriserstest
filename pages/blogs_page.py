#import all the necessary modules

#define class for the blog page
class Blogs:
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,url):
        self.driver.get(url)

