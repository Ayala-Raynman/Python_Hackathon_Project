import os

import allure
import pytest

from extensions.verification import verify_equal
from work_flow.desktop_work_flow import Calculator

@pytest.mark.usefixtures('init_desktop')
class Test_Desktop:
    @allure.title("Verify result of calculator")
    @allure.description("This test verify that the calculation result is equal to the result we expected")
    def test_01_calc(self):
        Calculator.calc_str(os.getenv("Exercise for calculation"))
        verify_equal(Calculator.get_result_number(),int(os.getenv("expected result")))
