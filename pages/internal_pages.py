from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from pages.base_page import Page
from pages.locators import ACTIVE_LOCATOR


class SignInPage(Page):
    def fill_form(self, username, password):
        self.driver.find_element_by_name('identity').clear()
        self.driver.find_element_by_name('identity').send_keys(username)
        self.driver.find_element_by_name('password').clear()
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(password)

    def submit(self):
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(Keys.ENTER)
        self.wait.until(expected_conditions.presence_of_element_located((By.NAME, 'status')))
        return DashboardPage(self.driver)

    def sign_in_click(self):
        self.driver.find_element_by_name("submit").click()
        self.wait.until(expected_conditions.presence_of_element_located((By.NAME, 'status')))
        return DashboardPage(self.driver)


class InternalPage(Page):

    def sign_in_click(self):
        sign_in_menu = self.driver.find_element_by_class_name('ow_signin_label')
        sign_in_menu.click()
        return SignInPage(self.driver)


class MainPage(InternalPage):
    pass


class DashboardPage(Page):
    def is_this_page(self):
        print("\n!!!!",self.find_visible_element((By.CSS_SELECTOR, ".ow_responsive_menu .active")).text, "!!!!")
        return self.find_visible_element(*ACTIVE_LOCATOR).text == "DASHBOARD"
