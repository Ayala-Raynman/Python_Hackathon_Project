

import pytest

from extensions.verification import verify_equal
from utilities import common_ops
import work_flow.electron_work_flow

@pytest.mark.usefixtures('init_electron')
class Test_Electron:

    def test_01(self):
        actual_text = work_flow.electron_work_flow.ApiDemos.get_text_from_demo_window()
        excpected_text = common_ops.get_data('electronExpectedText')  # "Hello World!"
        verify_equal(actual_text, excpected_text)




