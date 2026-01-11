from selenium.webdriver.common.by import By

class LoginPage:
    # 1. Locators (The "Map" of the page)
    # We store the HTML IDs here. If they change, we only fix them here.
    USERNAME_FIELD = (By.ID, "user-name")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON =   (By.ID, "login-button")
    ERROR_MESSAGE =  (By.CSS_SELECTOR, "h3[data-test='error']")

    # 2. Constructor (The Setup)
    def __init__(self, browser):
        self.browser = browser

    # 3. Page Actions (What the user can do)
    def load(self):
        self.browser.get("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.browser.find_element(*self.USERNAME_FIELD).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.LOGIN_BUTTON).click()

    # A helper method to do it all at once
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()