from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from pages.base_page import Page
from pages.locators import ACTIVE_LOCATOR, SignInPageLocator, DashboardPageLocator


class SignInPage(Page):
    @property
    def username_field(self):
        return self.find_element(SignInPageLocator.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.find_element(SignInPageLocator.PASSWORD_FIELD)

    @property
    def sign_in_button(self):
        return self.find_element(SignInPageLocator.SIGN_IN_BUTTON)

    def fill_form(self, username, password):
        self.username_field.clear()
        self.username_field.send_keys(username)
        self.password_field.clear()
        self.password_field.send_keys(password)

    def submit(self):
        self.password_field.send_keys(Keys.ENTER)
        # TODO: refactor when DashboardPage will be realise
        self.wait.until(expected_conditions.presence_of_element_located(DashboardPageLocator.POST_TEXT_FIELD))
        return DashboardPage(self.driver)

    def sign_in_click(self):
        self.sign_in_button.click()
        # TODO: refactor when DashboardPage will be realise
        self.wait.until(expected_conditions.presence_of_element_located(DashboardPageLocator.POST_TEXT_FIELD))
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
