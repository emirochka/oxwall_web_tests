from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.actions = ActionChains(driver)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, locator):
        el = self.wait.until(EC.presence_of_element_located(locator),
                             message=f"No element located {locator}")
        return el

    def find_visible_element(self, locator):
        el = self.wait.until(EC.visibility_of_element_located(locator),
                             message=f"No visible element located {locator}")
        return el

    def find_visible_elements(self, locator):
        el = self.wait.until(EC.visibility_of_all_elements_located(locator),
                             message=f"Not all elements {locator} visible")
        return el

    def find_clickable_element(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator),
                             message=f"No clickable element located {locator}")
        return el
