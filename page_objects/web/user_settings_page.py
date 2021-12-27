import allure
from selenium.webdriver.common.by import By


class user_settings_page:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("find surname text field under user settings")
    def find_surname_textField_element(self):
        return self.driver.find_element(By.ID, "user-settings-lastName-input")

    @allure.step("find first name text field under user settings")
    def find_first_name_textField_element(self):
        return self.driver.find_element(By.ID, "user-settings-firstName-input")
