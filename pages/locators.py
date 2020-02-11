from selenium.webdriver.common.by import By

ACTIVE_LOCATOR = (By.CSS_SELECTOR, ".ow_responsive_menu .active")


class SignInPageLocator:
    USERNAME_FIELD = (By.NAME, 'identity')
    PASSWORD_FIELD = (By.NAME, 'password')
    SIGN_IN_BUTTON = (By.NAME, 'submit')


class DashboardPageLocator:
    POST_TEXT_FIELD = (By.NAME, 'status')