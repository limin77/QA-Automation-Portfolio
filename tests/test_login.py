# tests/test.login.py
# UPGRADE VERSION: Uses WebDriverWait instead of time.sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # The Watchdog
from selenium.webdriver.support import expected_conditions as EC # The Rules

def test_valid_login_smart():
    print("\n--- Starting Smart Login Test ---")

    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    # SETUP THE WATCHDOG
    # "Iwill wait up to 10 seconds for elements to appear."
    wait = WebDriverWait(driver, 10)

    # 1. Smart find (Wait until visible)
    # This replaces the old driver.find_element...
    user_field = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    pass_field = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "login-button")

    # 2 INTERACT
    print("Typing credentials...")
    user_field.send_keys("standard_user")
    pass_field.send_keys("secret_sauce")

    print("Clicking Login...")
    login_btn.click()

    # 3. SMART VERIFY (Wait for URL change)
    # This replaces time.sleep(2)
    wait.until(EC.url_contains("inventory"))

    print(f"URL Verified: {driver.current_url}")
    print("✅ Smart Login Successful!")

    driver.quit()