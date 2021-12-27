from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import utilities.base

# class UIActions:
from utilities import base


class UIActions:
    @staticmethod
    def click(elem: WebElement):
        # WebDriverWait(base.driver, 5).until(EC.element_to_be_clickable(elem))
        base.driver.implicitly_wait(5)
        elem.click()
        # UIActions.click_without_waiting(elem)

    @staticmethod
    def click_without_waiting(elem: WebElement):
        elem.click()

    @staticmethod
    def doubleClick(elem: WebElement):
        action = ActionChains(base.driver)
        action.move_to_element(elem).double_click(elem).perform()

    @staticmethod
    def send_keys(elem: WebElement, string_to_send):
        base.driver.implicitly_wait(5)
        elem.clear()
        elem.send_keys(string_to_send)
