from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CreateWindowsPage:
    def __init__(self, driver):
        self.driver = driver


    def get_window_master_button(self):
        return self.driver.find_element(By.ID, "button-windows")

    def get_window_master_button_by(self):
        return (By.ID, "button-windows")

    def get_new_window_button(self):
        elem: WebElement = self.driver.find_element(By.ID, "new-window")
        #elem.is_displayed()
        return elem

    def get_new_window_button_by(self):
        return (By.ID, "new-window")

    def get_new_window_find_string(self):
        return "new-window"

    def get_new_window_by(self):
        return (By.ID, "new-window")

    def get_toggle(self):
        return self.driver.find_element(By.ID, "new-window-demo-toggle")

    def get_toggle_by(self):
        return (By.ID, "new-window-demo-toggle")

    def click_t(self):
        self.driver.find_element(By.ID, "button-app-sys-information").click()
