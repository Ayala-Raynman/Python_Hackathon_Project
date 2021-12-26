import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class Sign_In_Page:
    def __init__(self, driver):
        self.driver = driver

    def find_user_name_elem(self):
        user_name:WebElement=self.driver.find_element(By.ID, "username")
        return user_name

    def find_password_elem(self):
        return self.driver.find_element(By.ID, "password")

    def find_loggin_elem(self):
        return self.driver.find_element(By.XPATH, "//form/button")
