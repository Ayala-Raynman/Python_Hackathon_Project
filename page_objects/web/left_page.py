import allure
from selenium.webdriver.common.by import By


class Left_Page:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("find a user account balance")
    def find_account_balance_element(self):
        return self.driver.find_element(By.XPATH, "//*[@data-test='sidenav-user-balance']")

    @allure.step("find logout button")
    def find_logout_element(self):
        return self.driver.find_element(By.XPATH, "//*[@data-test='sidenav-signout']/div/span")


    @allure.step("find user settings to locate the user name details")
    def find_my_account_btn_element(self):
        return self.driver.find_element(By.XPATH, "//*[text() = 'My Account']")
