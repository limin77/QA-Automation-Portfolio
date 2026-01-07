from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    The Parent Class.
    It contains generic methods that all pages will use.
    """
    def __init__(self, driver):
        self.driver = driver
        # We set a standard wait time of 10 seconds for all pages
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        """
        Smart Locator:
        Waits for the element to be visible before finding it.
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def get_url(self):
        """Returns the current URL of the page."""
        return self.driver.current_url