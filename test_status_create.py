from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from custom_wait_conditions import presence_of_N_elements_located
import time


def test_status_create():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    base_url = 'http://127.0.0.1/oxwall/'
    wait = WebDriverWait(driver, 5)
    driver.get(base_url)

    # Login
    username = "admin"
    sign_in_menu = driver.find_element_by_class_name('ow_signin_label')
    sign_in_menu.click()
    driver.find_element_by_name('identity').clear()
    driver.find_element_by_name('identity').send_keys(username)
    driver.find_element_by_name('password').clear()
    password_field = driver.find_element_by_name('password')
    password_field.send_keys('pass')
    password_field.send_keys(Keys.ENTER)

    # Wait until login finished
    x = wait.until(expected_conditions.presence_of_element_located((By.NAME, 'status')))

    status_elements = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")

    # Input text in Status field
    driver.find_element_by_name('status').click()
    driver.find_element_by_name('status').send_keys('How are you?!!!!!')
    # Post status
    driver.find_element_by_name('save').click()
    status_elements = wait.until(presence_of_N_elements_located(
        (By.CLASS_NAME, "ow_newsfeed_item"),
        len(status_elements)+1),
        message="Can't find correct count of elements"
    )

    # driver.find_element_by_xpath('//a[contains(@id, "nfa-feed")]/input').send_keys(r'E:\workspace\untitled10_selenium\geoline.png')
    # wait.until(expected_conditions.presence_of_element_located
    #                                ((By.CSS_SELECTOR, f'div.ow_console_right [href="{base_url}/user/{username}"]')))
    #

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
