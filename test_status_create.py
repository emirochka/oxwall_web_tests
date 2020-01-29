from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from custom_wait_conditions import presence_of_N_elements_located


def test_status_create(driver, logged_user):
    status_elements = driver.find_elements(By.CLASS_NAME, "ow_newsfeed_item")
    # Input text in Status field
    driver.find_element_by_name('status').click()
    driver.find_element_by_name('status').send_keys('How are you?!!!!!')
    # Post status
    driver.find_element_by_name('save').click()
    # Wait new post appeared
    wait = WebDriverWait(driver, 5)
    status_elements = wait.until(presence_of_N_elements_located(
        (By.CLASS_NAME, "ow_newsfeed_item"),
        len(status_elements)+1),
        message="Can't find correct count of elements"
    )
