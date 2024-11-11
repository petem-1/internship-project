from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By

class ReellyLoginPage(Page):
    EMAIL_FIELD = (By.ID, 'email-2')
    PASSWORD = (By.ID, 'field')
    LOGIN = (By.CSS_SELECTOR, "login-button w-button")


    def login_reelly(self):
        self.input_text('petem801@gmail.com', *self.EMAIL_FIELD)
        self.input_text('Mbison801@', *self.PASSWORD)
        self.click(*self.LOGIN)
        