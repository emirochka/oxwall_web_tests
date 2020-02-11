import pytest
from selenium import webdriver

from oxwall_app import Oxwall
from pages.internal_pages import MainPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    base_url = 'http://127.0.0.1:81/oxwall/'
    driver.get(base_url)
    yield driver
    # driver.quit()


@pytest.fixture()
def app(driver):
    return Oxwall(driver)


# @pytest.fixture()
# def logged_user(driver, app):
#     username = "admin"
#     app.login_as(username, "pass")
#     yield username
#     app.logout()

@pytest.fixture()
def logged_user(driver):
    username = "admin"
    password = "pass"

    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    sign_in_page.fill_form(username, password)
    dash_page = sign_in_page.submit()
    yield username
    # dash_page.logout()
