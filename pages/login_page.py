from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # 1. LOCATORS (Private constants)
    _USERNAME_FIELD = (By.ID, "user-name")
    _PASSWORD_FIELD = (By.ID, "password")
    _LOGIN_BUTTON   = (By.ID, "login-button")

    def __init__(self, driver: WebDriver):
        """
        Initializes the Page Object.
        Args:
            driver (WebDriver): The Selenium WebDriver instance.
        """
        self.driver = driver
        # We set a default Explicit Wait of 10 seconds for this page
        self.wait = WebDriverWait(driver, 10)

    def load(self) -> None:
        """Navigates the browser to the SauceDemo login page."""
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Performs the login action.
        Args:
            username (str): The user's email/username.
            password (str): The user's password.
        """
        # Wait for the username field to be visible before typing (Smart Wait)
        self.wait.until(EC.visibility_of_element_located(self._USERNAME_FIELD)).send_keys(username)
        
        # Find and interact with the rest
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(*self._LOGIN_BUTTON).click()

    def get_url(self) -> str:
        """
        Returns the current page URL for validation.
        Returns:
            str: The URL currently in the browser address bar.
        """
        return self.driver.current_url