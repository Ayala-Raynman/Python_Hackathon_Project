import pytest
from extensions.verification import verify_equal
from utilities import common_ops
import work_flow.electron_work_flow
import allure


@pytest.mark.usefixtures('init_electron')
class Test_Electron:

    @allure.title("Verify text in demo window")
    @allure.description("This test verify that the text in a created demo window is equal to the result we expected")
    def test_01(self):
        actual_text = work_flow.electron_work_flow.ApiDemos.get_text_from_demo_window()
        expected_text = common_ops.get_data('electronExpectedText')
        verify_equal(actual_text, expected_text)



