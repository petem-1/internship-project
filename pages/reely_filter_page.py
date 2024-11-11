from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By

class ReellyFilterPage(Page):
    SECONDARY_OPTION = (By.CLASS_NAME, "menu-button-block new w-inline-block")
    SECONDARY_VERIFY = (By.CLASS_NAME, "menu-text-link-leaderboard w--current")
    FILTER_SELECT = (By.CLASS_NAME, "filter-button")
    WANT_TO_BUY = (By.CLASS_NAME, "tag-text-filters")
    APPLY_FILTER = (By.CLASS_NAME, "button-filter w-button")
    VERIFY_WANT_TO_BUY = (By.CLASS_NAME, "verified-contaier w-container")

    def filter_reely(self):
        self.click(*self.SECONDARY_OPTION)
        self.find_element(*self.SECONDARY_VERIFY)
        self.click(*self.FILTER_SELECT)
        self.click(*self.WANT_TO_BUY)
        self.click(*self.APPLY_FILTER)
        self.verify_text('Want to buy',*self.VERIFY_WANT_TO_BUY)

