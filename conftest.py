import pytest
from selenium import webdriver

from oxwall_app import Oxwall


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    base_url = 'http://127.0.0.1/oxwall/'
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return Oxwall(driver)


@pytest.fixture()
def logged_user(driver, app):
    username = "admin"
    app.login_as(username, "pass")
    yield username
    app.logout()
