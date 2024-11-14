from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.by import By


class ReellyFilterPage(Page):
    SECONDARY_OPTION = (By.CSS_SELECTOR, '[href="/secondary-listings"]')
    SECONDARY_VERIFY = (By.CSS_SELECTOR, '[href="/secondary-listings"]')
    FILTER_SELECT = (By.CSS_SELECTOR, "div.filter-button")
    WANT_TO_BUY = (By.XPATH, "//div[@class='tag-text-filters' and text()='Want to buy']")
    # (By.CSS_SELECTOR, '[wized="ListingTypeBuy"]')
    APPLY_FILTER = (By.CSS_SELECTOR, "a.button-filter.w-button")
    VERIFY_WANT_TO_BUY = (By.CSS_SELECTOR, 'div[wized="saleTagMLS"]')

    # def filter_reely(self):
    #     sleep(2)

    def click_secondary_option(self):
        self.wait_to_be_clickable_click(*self.SECONDARY_OPTION)
        sleep(4)

    def verify_secondary_option(self):
        self.find_element(*self.SECONDARY_VERIFY)
        sleep(2)

    def click_filter_select(self):
        self.wait_to_be_clickable_click(*self.FILTER_SELECT)
        sleep(2)

    def click_want_to_buy(self):
        self.wait_to_be_clickable_click(*self.WANT_TO_BUY)
        sleep(2)

    def click_apply_filter(self):
        element = self.wait.until(EC.element_to_be_clickable(self.APPLY_FILTER))
        sleep(2)
        ActionChains(self.driver).move_to_element(element).click().perform()
        sleep(3)

    # def verify_want_to_buy(self):
    #     # Locate all elements with the "Want to buy" tag
    #     elements = self.find_elements(*self.VERIFY_WANT_TO_BUY)
    #
    #     # Print each element's text to see what's being captured
    #     for element in elements:
    #         print(f"Element text: '{element.text.strip()}'")
    #
    #     # Verify each element's text
    #     all_have_tag = all(element.text.strip() == "Want to buy" for element in elements)
    #
    #     # Assert that all elements contain the "Want to buy" text
    #     assert all_have_tag, "Not all cards have the 'Want to buy' tag"

    def verify_want_to_buy(self):
        # Locate all elements with the "Want to buy" tag
        elements = self.find_elements(*self.VERIFY_WANT_TO_BUY)
        sleep(2)

    # Print each element's text to see what's being captured
        for element in elements:
            print(f"Element text: '{element.text.strip()}'")

            # Verify each element's text
            all_have_tag = all(element.text.strip() == "Want to buy" for element in elements)

            # Assert that all elements contain the "Want to buy" text
            assert all_have_tag, "Not all cards have the 'Want to buy' tag"