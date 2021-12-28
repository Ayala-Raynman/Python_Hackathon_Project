import unittest
import time

import pytest
from _pytest import mark
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from utilities import base
from work_flow import mobile_work_flow


@pytest.mark.usefixtures('init_mobile')
class Test_appium:
    def test_change_background_color(self):
        actual_background_color = mobile_work_flow.Financial_Calculators.change_background_color()
        print(actual_background_color)

    def test_number_sub_apps(self):
        actual_number_of_sub_apps = mobile_work_flow.Financial_Calculators.get_number_of_app_icons()
        assert actual_number_of_sub_apps == 18

    def test_check_tip_calculation(self):
        bill = 100
        tip = 12
        actual_number_of_total_price = mobile_work_flow.Financial_Calculators.get_total_payment(str(bill), str(tip))
        expected_total_price = (mobile_work_flow.Financial_Calculators.verify_tip(bill, tip))
        print(actual_number_of_total_price)
        print(expected_total_price)
        print(float(actual_number_of_total_price) == expected_total_price)
