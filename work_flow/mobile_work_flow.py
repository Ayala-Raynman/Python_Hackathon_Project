import time

from selenium.webdriver.common.by import By

from utilities import base
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class Financial_Calculators:
    @staticmethod
    def change_background_color():
        base.driver.find_element_by_xpath("xpath=//*[@contentDescription='נווט למעלה']").click()
        base.driver.find_element_by_xpath("xpath=//*[@text='Settings']").click()
        base.driver.find_element_by_xpath(
            "xpath=//*[@class='android.widget.RelativeLayout' and ./*[@text='Background color']]").click()
        base.driver.find_element_by_xpath("xpath=//*[@text='Black']").click()
        current_background_color = Financial_Calculators.get_background_color()
        WebDriverWait(base.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//*[@contentDescription='נווט למעלה']")))
        base.driver.find_element_by_xpath("xpath=//*[@contentDescription='נווט למעלה']").click()
        return current_background_color

    @staticmethod
    def get_background_color():
        chosen_background_color = base.driver.find_element(By.XPATH, "(//*[@id='listview']/*/*[@id='text2'])[1]")
        return chosen_background_color.text

    @staticmethod
    def get_number_of_app_icons():
        number_of_app_icons = base.driver.find_elements(By.XPATH, "(//*[@id='mainGrid']/*[./*[@id='icon']])")
        return len(number_of_app_icons)

    @staticmethod
    def get_total_payment(bill, tip):
        base.driver.find_element(By.XPATH, "(//*[@id='mainGrid']/*/*[@id='icon'])[7]").click()
        base.driver.find_element(By.XPATH, "//*[@id='billInput']").send_keys(str(bill))
        WebDriverWait(base.driver, 60).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='tipInput']")))
        base.driver.find_element(By.XPATH, "//*[@id='tipInput']").click()
        base.driver.find_element(By.XPATH, "//*[@id='tipInput']").send_keys(str(tip))
        return base.driver.find_element(By.XPATH, "//*[@id='totalCheckResult']").text

    @staticmethod
    def verify_tip(bill, tip):
        return float(float(bill)*(float(tip) + 100)/100)

