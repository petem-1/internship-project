from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By


class ReellyFilterPage(Page):
    SECONDARY_OPTION = (By.CSS_SELECTOR, '[href="/secondary-listings"]')
    SECONDARY_VERIFY = (By.CSS_SELECTOR, '[href="/secondary-listings"]')
    FILTER_SELECT = (By.CSS_SELECTOR, "div.filter-button")
    WANT_TO_BUY = (By.CSS_SELECTOR, '[wized="ListingTypeBuy"]')
    APPLY_FILTER = (By.CSS_SELECTOR, "a.button-filter.w-button")
    VERIFY_WANT_TO_BUY = (By.CSS_SELECTOR, 'div[wized="saleTagMLS"]')

    def filter_reely(self):
        sleep(2)

    def click_secondary_option(self):
        self.click(*self.SECONDARY_OPTION)
        sleep(4)

    def verify_secondary_option(self):
        self.find_element(*self.SECONDARY_VERIFY)

    def click_filter_select(self):
        self.click(*self.FILTER_SELECT)

    def click_want_to_buy(self):
        self.click(*self.WANT_TO_BUY)
        sleep(4)

    def click_apply_filter(self):
        # Calls the updated click method
        self.click(*self.APPLY_FILTER)
        sleep(7)

    def verify_want_to_buy(self):
        # Locate all elements with the "Want to buy" tag
        elements = self.find_elements(*self.VERIFY_WANT_TO_BUY)

        # Verify each element's text
        all_have_tag = all(element.text.strip() == "Want to buy" for element in elements)

        # Assert that all elements contain the "Want to buy" text
        assert all_have_tag, "Not all cards have the 'Want to buy' tag"
