import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage

def test_login_success():
    print("\n--- Starting POM Login Test ---")
    
    # 1. SETUP: Configure Chrome for Cloud/Linux
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")             # <--- CRITICAL FOR GITHUB
    chrome_options.add_argument("--disable-dev-shm-usage")  # <--- CRITICAL FOR GITHUB
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Pass the options to the driver
    driver = webdriver.Chrome(options=chrome_options)
    
    # 2. INIT
    login_page = LoginPage(driver)
    
    # 3. ACTION
    print("Loading Page...")
    login_page.load()
    
    print("Logging In...")
    login_page.login("standard_user", "secret_sauce")
    
    # 4. ASSERT
    current_url = login_page.get_url()
    if "inventory" in current_url:
        print("✅ PASS: Login Successful")
        assert True
    else:
        print(f"❌ FAIL: Still on {current_url}")
        assert False

    driver.quit()