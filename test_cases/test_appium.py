import allure
import pytest
from extensions.verification import verify_equal
from utilities.common_ops import get_data
from work_flow import mobile_work_flow


@pytest.mark.usefixtures('init_mobile')
class Test_appium:
    @allure.title("Verify change background color")
    @allure.description("This test verify the background color change")
    def test_01_change_background_color(self):
        actual_background_color = mobile_work_flow.Financial_Calculators.change_background_color()
        expected_color = get_data("background_color")
        verify_equal(actual_background_color, expected_color)

    @allure.title("Verify sub-applications")
    @allure.description("This test verify the nun of  sub-applications")
    def test_02_number_sub_apps(self):
        actual_number_of_sub_apps = mobile_work_flow.Financial_Calculators.get_number_of_app_icons()
        expected_sub_app = get_data("sub_app")
        verify_equal(actual_number_of_sub_apps, expected_sub_app)

    @allure.title("Verify tip calculation application")
    @allure.description("This test verify  tip calculation app")
    def test_03_check_tip_calculation(self):
        bill = 100
        tip = 12
        actual_number_of_total_price = mobile_work_flow.Financial_Calculators.get_total_payment(str(bill), str(tip))
        expected_total_price = (mobile_work_flow.Financial_Calculators.verify_tip(bill, tip))
        verify_equal(float(actual_number_of_total_price), expected_total_price)
