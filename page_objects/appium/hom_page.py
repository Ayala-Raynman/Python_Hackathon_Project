import allure
from selenium.webdriver.common.by import By


class Home_Page:
    def __init__(self, driver):
        self.driver = driver

    def get_num_sub_apps(self):
        return self.driver.find_elements(By.XPATH, "(//*[@id='mainGrid']/*[./*[@id='icon']])")
