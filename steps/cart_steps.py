from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

@given('I am on Target home page')
def step_open_target(context):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.get("https://www.target.com/")
    context.driver.maximize_window()
    time.sleep(3)

@when('I click on the cart icon')
def step_click_cart(context):
    cart_icon = context.driver.find_element(By.XPATH, "//a[contains(@href, '/cart')] | //span[contains(text(), 'Cart')]")
    cart_icon.click()
    time.sleep(4)

@then('I should see "Your cart is empty" message')
def step_verify_empty_cart(context):
    message = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'Your cart is empty')] | //div[contains(text(), 'empty')]")
    assert "empty" in message.text.lower()
    print("✅ Success: Your cart is empty message is shown")
