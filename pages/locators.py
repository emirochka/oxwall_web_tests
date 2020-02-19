from selenium.webdriver.common.by import By

ACTIVE_LOCATOR = (By.CSS_SELECTOR, ".ow_responsive_menu .active")


class SignInPageLocator:
    USERNAME_FIELD = (By.NAME, 'identity')
    PASSWORD_FIELD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.NAME, 'submit')


class DashboardPageLocator:
    POST_TEXT_FIELD = (By.NAME, 'status')


class PostLocator:
    POST_TEXT = (By.CLASS_NAME, 'ow_newsfeed_content')
    POST_USER = (By.CSS_SELECTOR, ".ow_newsfeed_string > a")
    POST_TIME = (By.CSS_SELECTOR, "a.create_time.ow_newsfeed_date")
    POST_LIKES_BUTTON = ()
    POST_LIKES_COUNT = ()