from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class DemoWindowPage:
    def __init__(self, driver):
        self.driver = driver

    def get_demo_window_text_elem(self):
        elem: WebElement = self.driver.find_element(By.TAG_NAME, 'h2')
        return elem

    def get_demo_window_text(self):
        return self.driver.find_element(By.TAG_NAME, 'h2').text

    def set_driver(self, driver):
        self.driver = driver
