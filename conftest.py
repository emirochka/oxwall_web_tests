import pytest
from selenium import webdriver
import json
import os.path

from db.db_connector import OxwallDB
from pages.oxwall_app import Oxwall
from pages.internal_pages import MainPage
from value_object.user import User

PROJECT_DIR = os.path.dirname(__file__)


def pytest_addoption(parser):
    parser.addoption("--config", action="store", default="config.json",
                     help="project config file name")
    # parser.addoption("--browser", action="store", default="Chrome",
    #                  help="project config file name")


@pytest.fixture(scope="session")
def config(request):
    filename = request.config.getoption("--config")
    with open(os.path.join(PROJECT_DIR, filename)) as f:
        return json.load(f)


@pytest.fixture()
def driver(config, selenium, base_url):
    driver = selenium
    driver.implicitly_wait(5)
    driver.maximize_window()
    # base_url = config["web"]["base_url"]
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return Oxwall(driver)


@pytest.fixture(scope="session")
def db(config):
    db = OxwallDB(**config['db'])
    yield db
    db.close()


filename = os.path.join(PROJECT_DIR, "data", "users.json")

with open(filename, encoding="utf8") as f:
    # user_list = json.load(f
    users = [User(**u) for u in json.load(f)]


@pytest.fixture(params=users, ids=[str(u) for u in users])
def user(request, db):
    user = request.param
    if user.username != "admin":
        db.create_user(user)
    yield user
    if user.username != "admin":
        db.delete_user(user)


@pytest.fixture()
def logged_user(driver, config):
    user = User(**config["web"]["user"])
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    sign_in_page.fill_form(user.username, user.password)
    dash_page = sign_in_page.submit()
    yield user
    # dash_page.logout()
