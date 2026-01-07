# tests/test_login.py
import pytest
from selenium import webdriver
from pages.login_page import LoginPage # <--- We impoert the Menu here!

def test_login_success():
    print("\n--- Starting POM Login Test ---")

    # 1. SETUP: Open the Browser
    driver = webdriver.Chrome()

    # 2. INIT: Give the driver to our Page Object
    login_page = LoginPage(driver)

    # 3. Action: Use the simple methods we created
    print("Loading Page...")
    login_page.load()

    print("Logging In...")
    login_page.login("standard_user", "secret_sauce")

    # 4. ASSERT: Verify we are on the inventory page
    # (We check the URL to confrim success)
    current_url = login_page.get_url()
    if "inventory" in current_url:
        print("✅ PASS: Login Successful (Redirected to Inventory)")
        assert True
    else:
        print(f"❌ FAIL: Still on {current_url}")
        assert False

    # 5. TEARDOWN: Close the browser
    driver.quit()
