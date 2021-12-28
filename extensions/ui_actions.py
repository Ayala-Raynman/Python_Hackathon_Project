import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from utilities import base


class UIActions:
    @staticmethod
    @allure.Step("clicking on an element")
    def click(elem: WebElement):
        # WebDriverWait(base.driver, 5).until(EC.element_to_be_clickable(elem))
        base.driver.implicitly_wait(5)
        elem.click()
        # UIActions.click_without_waiting(elem)

    @staticmethod
    @allure.step("clicking on an element without waiting")
    def click_without_waiting(elem: WebElement):
        elem.click()

    @staticmethod
    @allure.step("clicking on an element with waiting to specific element")
    def click_safely(elem: WebElement, by_obj):
        WebDriverWait(base.driver, 5).until(EC.element_to_be_clickable(by_obj))
        elem.click()

    @staticmethod
    @allure.step("doubleClick on a element")
    def doubleClick(elem: WebElement):
        action = ActionChains(base.driver)
        action.move_to_element(elem).double_click(elem).perform()

    @staticmethod
    @allure.step("send text to input")
    def send_keys(elem: WebElement, string_to_send):
        base.driver.implicitly_wait(5)
        elem.clear()
        elem.send_keys(string_to_send)
