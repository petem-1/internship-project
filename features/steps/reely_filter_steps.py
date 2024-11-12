from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open reelly main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(1)

@when('Log in to the page')
def input_text(context):
    context.app.reely_login_page.login_reelly()

@when('Click on “Secondary” option at the left side menu')
def filter_reely(context):
    context.app.reely_filter_page.filter_reely()

@then('Verify the right page opens')
def filter_reely(context):
    context.app.reely_filter_page.filter_reely()

@when('Click on Filters')
def filter_reely(context):
    context.app.reely_filter_page.filter_reely()

@when('Filter the products by “want to buy”')
def filter_reely(context):
    context.app.reely_filter_page.filter_reely()

@when('Click on Apply Filter')
def filter_reely(context):
    context.app.reely_filter_page.filter_reely()

@then('Verify all cards have “Want to buy” tag')
def verify_text(context):
    context.app.reely_filter_page.filter_reely()