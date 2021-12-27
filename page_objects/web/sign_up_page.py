import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class sign_up_page:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("finding first name text field for signup")
    def find_first_name_elem(self):
        return self.driver.find_element(By.ID, "firstName")

    @allure.step("finding surname name text field for signup")
    def find_user_name_elem(self):
        return self.driver.find_element(By.ID, "lastName")

    @allure.step("finding username text field for signup")
    def find_user_name_elem(self):
        return self.driver.find_element(By.ID, "username")

    @allure.step("finding password text field for signup")
    def find_password_elem(self):
        return self.driver.find_element(By.ID, "password")

    @allure.step("finding confirm-password text field for signup")
    def find_password_elem(self):
        return self.driver.find_element(By.ID, "confirm password")

    @allure.step("finding sign up button for signup")
    def find_password_elem(self):
        return self.driver.find_element(By.XPATH, "//*[@data-test='signup-submit']")
