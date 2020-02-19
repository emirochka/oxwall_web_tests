from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions

from custom_wait_conditions import presence_of_N_elements_located
from pages.base_page import Page
from pages.locators import ACTIVE_LOCATOR, SignInPageLocator, DashboardPageLocator
from pages.page_structure import SignInPageElements

# class SignInPageElements(Page):
#     @property
#     def username_field(self):
#         return self.find_element(SignInPageLocator.USERNAME_FIELD)
#
#     @property
#     def password_field(self):
#         return self.find_element(SignInPageLocator.PASSWORD_FIELD)
#
#     @property
#     def sign_in_button(self):
#         return self.find_element(SignInPageLocator.SIGN_IN_BUTTON)
from pages.post_block import PostBlock


class SignInPage(SignInPageElements):
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
    USER_MENU = (By.CSS_SELECTOR, ".ow_console_items_wrap div:nth-child(5)")
    SIGN_IN_MENU = (By.CLASS_NAME, "ow_signin_label")
    ACTIVE_MENU = (By.CSS_SELECTOR, ".ow_responsive_menu .ow_main_menu .active")
    MAIL_LOCATOR = (By.CLASS_NAME, "ow_mailbox_items_list")
    MAIN_MENU = ()
    DASHBOARD_MENU = ()

    @property
    def sign_in_menu(self):
        return self.find_visible_element(self.SIGN_IN_MENU)

    @property
    def active_menu(self):
        return self.find_element(self.ACTIVE_MENU)

    @property
    def user_menu(self):
        return self.find_element(self.USER_MENU)

    def sign_in_click(self):
        self.sign_in_menu.click()
        return SignInPage(self.driver)



class MainPage(InternalPage):
    pass


class DashboardPage(InternalPage):
    STATUS_BLOCK = (By.XPATH, "//li[contains(@id, 'action-feed')]")
    # ??? STATUS_TEXT = (By.CLASS_NAME, 'ow_newsfeed_content')
    STATUS_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    STATUS_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    NEW_STATUS_FIELD = (By.NAME, "status")
    SEND_BUTTON = (By.NAME, "save")

    @property
    def post_text_field(self):
        return self.find_visible_element(self.NEW_STATUS_FIELD)

    @property
    def send_button(self):
        return self.find_visible_element(self.SEND_BUTTON)

    @property
    def posts(self):
        post_elements = self.find_visible_elements(self.STATUS_BLOCK)
        post_objects = []
        for el in post_elements:
            post_objects.append(PostBlock(el))
        return post_objects
        # return [PostBlock(el) for el in self.find_visible_elements(self.STATUS_BLOCK)]

    def create_post(self, text):
        self.post_text_field.clear()
        self.post_text_field.send_keys(text)
        self.send_button.click()

    def wait_new_post(self, number_of_posts_before):
        self.wait.until(
            presence_of_N_elements_located(self.STATUS_BLOCK, number_of_posts_before + 1),
            message="Can't find correct count of posts"
        )

    def is_this_page(self):
        return self.find_visible_element(ACTIVE_LOCATOR).text == "DASHBOARD"
