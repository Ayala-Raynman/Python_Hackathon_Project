import allure
from selenium.webdriver.common.by import By


class main_page:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("finding next button in get started window")
    def find_next_button_in_get_started_page_element(self):
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
        return self.driver.find_element(By.XPATH, "//*[@role='presentation']//*[@data-test='bankaccount-submit']")

    @allure.step("find DONE button for finish registration")
    def find_next_button_for_finish(self):
        return self.driver.find_element(By.XPATH, "//*[@role='dialog']//*[@data-test='user-onboarding-next']")

    @allure.step("find My Accounts button for User Settings page")
    def find_my_account_btn_element(self):
        return self.driver.find_element(By.XPATH, "//*[text()='My Account']")

    @allure.step("find label text username text and return it")
    def find_user_name_label_elem(self):
        return self.driver.find_element(By.XPATH, "//*[@data-test='sidenav-username']").text

    @allure.step("find Bank accounts in the user side-navbar")
    def find_bank_accounts_in_side_navbar(self):
        return self.driver.find_element(By.XPATH, "//*[@data-test='sidenav-bankaccounts']")








