from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import utilities.base

# class UIActions:
from utilities import base


class UIActions:
    @staticmethod
    def click(elem: WebElement):
        # WebDriverWait(base.driver, 5).until(EC.element_to_be_clickable(elem))
        base.driver.implicitly_wait(10)
        elem.click()
        # UIActions.click_without_waiting(elem)

    @staticmethod
    def click_without_waiting(elem: WebElement):
        elem.click()
