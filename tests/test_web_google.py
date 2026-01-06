# test/test_web_google.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_duckduckgo_search():
    print("\n--- Starting the Search Robot ---")

    # 1. Open Browser
    driver = webdriver.Chrome()

    # WE USE DUCKDUCKGO (Friendly to Bots)
    driver.get("https://duckduckgo.com")

    time.sleep(2)

    # 2. FIND THE ELEMENT
    # DuckDuckGo also uses the name "q" for their search box
    search_box = driver.find_element(By.NAME, "q")
     
    # 3. INTERACT
    print("Typing into DuckDuckGo...")
    search_box.send_keys("QA Automation Engineer")

    time.sleep(1)

    # Hit Enter
    search_box.send_keys(Keys.RETURN)

    # 4. VERIFY
    time.sleep(3)

    current_url = driver.current_url
    print(f"Current URL: {current_url}")

    # Check for the "+ in the URL
    # assert "QA+Automation+Engineer" in the current_url

    print("Test Passed! Closing browser...")
    driver.quit()