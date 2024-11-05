from pages.cart_page import Cart
from pages.base_page import Page
from pages.header import Header
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from features.steps.target_app_page_steps import TargetAppPage

class Application:

    def __init__(self, driver):
        self.page = Page(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = Cart(driver)
        self.target_app_page = TargetAppPage(driver)