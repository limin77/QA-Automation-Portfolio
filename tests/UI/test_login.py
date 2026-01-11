import pytest
from tests.pages.login_page import LoginPage

# FIXED: We use 'driver' because that is what your conftest.py provides.

def test_standard_user_login(driver):
    # 1. Initialize the Page Object with the 'driver'
    login_page = LoginPage(driver)

    # 2. Use the Page Object
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # 3. Verify
    assert "inventory.html" in driver.current_url

def test_locked_out_user(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    # Verify error message
    error_msg = driver.find_element(*LoginPage.ERROR_MESSAGE)
    assert "Epic sadface" in error_msg.text