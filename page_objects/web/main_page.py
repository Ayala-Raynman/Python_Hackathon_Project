import allure
from selenium.webdriver.common.by import By


class main_page:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("finding button in html window")
    def find_popup_element(self):
        return self.driver.find_element(By.XPATH, "//*[@role='dialog']//*[@data-test='user-onboarding-next']")

    @allure.step("find bank name text field")
    def find_bank_name_element(self):
        return self.driver.find_element(By.XPATH, "//*[@id='bankaccount-bankName-input']")

    @allure.step("find routing number text field")
    def find_routing_number_element(self):
        return self.driver.find_element(By.ID, "bankaccount-routingNumber-input")

    @allure.step("find account number text field")
    def find_account_number_element(self):
        return self.driver.find_element(By.ID, "bankaccount-accountNumber-input")

    @allure.step("find submit button for creating bank account")
    def find_submit_button_element(self):
        return self.driver.find_element(By.XPATH, "//*[@role='dialog']//*[@class='MuiGrid-root MuiGrid-container "
                                                  "MuiGrid-spacing-xs-2 MuiGrid-align-items-xs-flex-start']//*["
                                                  "@data-test='bankaccount-submit']")

    @allure.step("find next button for finish registration")
    def find_next_button_for_finish(self):
        return self.driver.find_element(By.XPATH, "//*[@role='dialog']//*[@data-test='user-onboarding-next']")

