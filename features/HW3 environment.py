from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def before_all(context):
    """Setup browser before all tests"""
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()

def after_all(context):
    """Close browser after all tests"""
    context.driver.quit()
