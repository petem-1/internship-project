from pages.base_page import Page
from pages.main_page import MainPage
from pages.reely_filter_page import ReellyFilterPage
from pages.reely_login_page import ReellyLoginPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.reely_login_page = ReellyLoginPage(driver)
        # self.reely_filter_page = ReellyFilterPage(driver)