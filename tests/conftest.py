import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# --- EXISTING FIXTURE (We keep this) ---
@pytest.fixture
def sample_data():
    return [100, 200, 50]

# --- NEW DRIVER FIXTURE (Add this) ---
@pytest.fixture
def driver():
    print("\n[Fixture] Setting up the browser...")
    
    # Configure Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Initialize Driver
    my_driver = webdriver.Chrome(options=chrome_options)
    
    # Yield creates the driver and pauses here for the test to run
    yield my_driver
    
    # Teardown happens after the test finishes
    print("\n[Fixture] Closing the browser...")
    my_driver.quit()