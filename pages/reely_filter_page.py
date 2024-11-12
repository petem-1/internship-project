from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By

class ReellyFilterPage(Page):
    SECONDARY_OPTION = (By.ID, "w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b")
    SECONDARY_VERIFY = (By.ID, "w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d4-7f66df43")
    FILTER_SELECT = (By.CLASS_NAME, ".filter-button")
    WANT_TO_BUY = (By.CLASS_NAME, ".switcher-button.active")
    APPLY_FILTER = (By.CLASS_NAME, ".button-filter.w-button")
    VERIFY_WANT_TO_BUY = (By.CLASS_NAME, "saleTagMLS")

    def filter_reely(self):
        self.click(*self.SECONDARY_OPTION)
        self.find_element(*self.SECONDARY_VERIFY)
        self.click(*self.FILTER_SELECT)
        self.click(*self.WANT_TO_BUY)
        self.click(*self.APPLY_FILTER)
        self.find_elements('Want to buy',*self.VERIFY_WANT_TO_BUY)
    # look up how to do loops
