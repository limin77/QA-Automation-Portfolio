# tests/test_login_negative.py
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_locked_out_user():
    print("\n--- Starting Negative Login Test ---")
    
    # 1. Open Browser
    driver = webdriver.Chrome()
    driver.get("https://saucedemo.com/")
    time.sleep(2)

    # 2. FIND LOGIN ELEMENTS (Best practice: By.ID)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password"). send_keys("secret_sauce")

    # 3. CLICK LOGIN
    print("Attempting to login as Locked Out User...")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2) # wait for the red box to appear

    # FIND THE ERROR MESSAGE
    # We use CSS_SELECTOR because this element has no ID, but it has 'data-test="error"'
    error_box = driver.find_element(By.CSS_SELECTOR, "[data-test='error']")
    # Extract bthe text from the box
    actual_error_text = error_box.text
    print(f"Error Message Found: {actual_error_text}")

    # 5. VERIFY
    # Check if the text matches exactly what we expect
    expected_error = "Epic sadface: Sorry, this user has been locked out."

    assert expected_error == actual_error_text

    print("✅ TEST PASSED: The system correctly blocked the user!")
    driver.quit()