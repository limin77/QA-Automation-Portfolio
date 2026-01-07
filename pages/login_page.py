# pages/login_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # ---  1. LOCATORS (The 'Ingredients') ---
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "h3[data-test='error']")

    # --- 2. ACTIONS (The 'The Recipes') ---
    def load(self):
        """Opens the SauceDemo login page"""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        """Performs the full login action"""
        self.find(self.USERNAME_FIELD).send_keys(username)
        self.find(self.PASSWORD_FIELD).send_keys(password)
        self.find(self.LOGIN_BUTTON).click()

    def get_error_message(self):
        """Returns the error text if login fails"""
        return self.find(self.ERROR_MESSAGE).text
