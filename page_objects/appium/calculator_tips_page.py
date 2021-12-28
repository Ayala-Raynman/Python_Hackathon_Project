import allure
from selenium.webdriver.common.by import By


class Calculator_Tips_Page:
    def __init__(self, driver):
        self.driver = driver

    def btn_calc_tips_apps(self):
        return self.driver.find_element(By.XPATH, "(//*[@id='mainGrid']/*/*[@id='icon'])[7]")

    def input_bill(self):
        return self.driver.find_element(By.XPATH, "//*[@id='billInput']")

    def input_tip(self):
        return self.driver.find_element(By.XPATH, "//*[@='tipInput']")

    def input_tip_by(self):
        return (By.XPATH, "//*[@='tipInput']")

    def get_total_payment(self):
        return self.driver.find_element(By.XPATH, "//*[@id='totalCheckResult']")

