from pages.base_page import Page
from pages.locators import SignInPageLocator


class SignInPageElements(Page):
    @property
    def username_field(self):
        return self.find_element(SignInPageLocator.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.find_element(SignInPageLocator.PASSWORD_FIELD)

    @property
    def sign_in_button(self):
        return self.find_element(SignInPageLocator.SIGN_IN_BUTTON)
