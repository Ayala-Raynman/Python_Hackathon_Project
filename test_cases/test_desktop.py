import allure
import pytest
from work_flow.desktop_work_flow import Calculator


@pytest.mark.usefixtures('init_desktop')
class Test_Desktop:
    # משתנים שנקבל בהשך כפרמטרים בהרצה
    expected_str = "4*10/5-3"
    expected_result = 5

    # @allure.title("Verify result of calculator")
    # @allure.description("This test verift that the calculation result is equal to the result we expected")
    def test_01_calc(self):
        Calculator.calc_str(self.expected_str)
        assert Calculator.get_result_number() == self.expected_result
