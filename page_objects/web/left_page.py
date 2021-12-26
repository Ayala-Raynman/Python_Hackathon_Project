import allure
from selenium.webdriver.common.by import By


class main_page:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("find a user account balance")
    def find_account_balance(self):
        return self.driver.find_element(By.XPATH, "//*[@data-test='sidenav-user-balance']")

    @allure.step("find logout button")
    def find_logout(self):
        return self.driver.find_element(By.XPATH, "//*[@data-test='sidenav-signout']/div/span")
