from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome in Incognito
chrome_options = Options()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)

try:
    # 1. Open Target
    driver.get("https://www.target.com/")
    print("✅ Opened Target.com")
    time.sleep(3)

    # 2. Click Account button
    account_btn = driver.find_element(By.XPATH, "//span[text()='Account' or contains(@aria-label, 'Account')]")
    account_btn.click()
    print("✅ Clicked Account button")
    time.sleep(2)

    # 3. Click Sign In
    signin_btn = driver.find_element(By.XPATH, "//span[text()='Sign in'] | //a[contains(text(), 'Sign in')]")
    signin_btn.click()
    print("✅ Clicked Sign In")
    time.sleep(4)

    # 4. Verify Sign In page
    header = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in')]")
    print(f"✅ Found header: {header.text}")

    print("\n🎉 HW2 Test Case Completed Successfully!")

except Exception as e:
    print(f"❌ Error occurred: {e}")

finally:
    time.sleep(3)
    driver.quit()
