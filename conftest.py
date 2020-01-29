import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    base_url = 'http://127.0.0.1/oxwall/'
    driver.get(base_url)
    yield driver
    driver.quit()

@pytest.fixture()
def logged_user(driver):
    username = "admin"
    # Login
    sign_in_menu = driver.find_element_by_class_name('ow_signin_label')
    sign_in_menu.click()
    driver.find_element_by_name('identity').clear()
    driver.find_element_by_name('identity').send_keys(username)
    driver.find_element_by_name('password').clear()
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('pass')
    password_field.send_keys(Keys.ENTER)
    # Wait until login finished
    wait = WebDriverWait(driver, 5)
    wait.until(expected_conditions.presence_of_element_located((By.NAME, 'status')))
    return username
    # TODO: fix Sign out
    # wait.until(
    #     expected_conditions.presence_of_element_located((By.CSS_SELECTOR, f'div.ow_console_right a[href="{base_url}/user/{username}"]')),
    #     message="Can't find User menu"
    # )
    # menu = driver.find_element_by_css_selector('div.ow_console_right a')
    # sign_out = driver.find_element_by_css_selector(f'div.ow_console_right [href="{base_url}/sign-out"]')
    # action = ActionChains(driver)
    # action.move_to_element(menu)
    # action.click(sign_out)
    # action.perform()
