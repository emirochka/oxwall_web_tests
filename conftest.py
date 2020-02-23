import pytest
from selenium import webdriver
import json
import os.path

from db.db_connector import OxwallDB
from oxwall_app import Oxwall
from pages.internal_pages import MainPage
from value_object.user import User


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    base_url = 'http://127.0.0.1:81/oxwall/'
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture()
def app(driver):
    return Oxwall(driver)


@pytest.fixture(scope="session")
def db():
    db = OxwallDB(host='localhost',
                  user='root',
                  password='mysql',
                  db='oxwa166')
    yield db
    db.close()


PROJECT_DIR = os.path.dirname(__file__)
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
def logged_user(driver):
    user = User(username="admin", password="pass", real_name="Admin")
    main_page = MainPage(driver)
    sign_in_page = main_page.sign_in_click()
    sign_in_page.fill_form(user.username, user.password)
    dash_page = sign_in_page.submit()
    yield user
    # dash_page.logout()
