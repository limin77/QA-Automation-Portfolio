import pytest
from tests.pages.login_page import LoginPage

# -----------------------------------------------------------
# 1. THE DATA LIST (The Magazine)
# We list 3 users here. Pytest will run the test once for each.
# -----------------------------------------------------------
USERS_TO_TEST = [
    ("standard_user", "secret_sauce"),
    ("problem_user", "secret_sauce"),           # User with broken images
    ("performance_glitch_user", "secret_sauce") # User that is slow
]

# -----------------------------------------------------------
# 2. THE TEST TRIGGER (The Gun)
# @pytest.mark.parametrize tells Python: "Loop through USERS_TO_TEST"
# -----------------------------------------------------------
@pytest.mark.parametrize("username, password", USERS_TO_TEST)
def test_multiple_valid_logins(driver, username, password):
    
    # Initialize Page Object
    login_page = LoginPage(driver)
    
    # Go to website
    login_page.load()
    
    # Login with the CURRENT data from the list
    login_page.login(username, password)
    
    # Verify we got in
    assert "inventory.html" in driver.current_url

# -----------------------------------------------------------
# 3. NEGATIVE TEST (Separate Logic)
# -----------------------------------------------------------
def test_locked_out_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")
    
    # Verify Error Message (Different logic, so different test function)
    error_msg = driver.find_element(*LoginPage.ERROR_MESSAGE)
    assert "Epic sadface" in error_msg.text