from behave import given, when, then
from selenium.webdriver.common.by import By
import time

@given('I am on Target home page')
def step_open_target(context):
    context.driver.get("https://www.target.com/")
    time.sleep(3)

@when('I click on Sign In from header')
def step_click_signin_header(context):
    signin_btn = context.driver.find_element(By.XPATH, "//span[text()='Sign in'] | //button[contains(@aria-label, 'Account')]")
    signin_btn.click()
    time.sleep(2)

@when('I click Sign In from side navigation')
def step_click_signin_side(context):
    side_signin = context.driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')] | //span[text()='Sign in']")
    side_signin.click()
    time.sleep(4)

@then('I should see the Sign In form')
def step_verify_signin_form(context):
    form = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in')] | //input[@type='email']")
    print("✅ Success: Sign In form is visible")
