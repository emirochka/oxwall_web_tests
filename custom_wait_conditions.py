from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class presence_of_N_elements_located:
    def __init__(self, locator, count):
        self.locator = locator
        self.count = count

    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) == self.count:
            return elements

# def presence_of_N_elements_located(locator, N):
#     def func(driver):
#         elements = driver.find_elements(*locator)
#         if len(elements) == N:
#             return elements
#     return func


if __name__ == "__main__":
    driver = webdriver.Chrome()
    base_url = "http://demo.oxwall.com"
    driver.get(base_url)

    wait = WebDriverWait(driver, 5)

    els = wait.until(presence_of_N_elements_located((By.CLASS_NAME, "ow_newsfeed_item"), 11),
                     message="Not 11 elements located")

    print(len(els))
