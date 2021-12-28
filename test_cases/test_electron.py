import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import page_objects.electron.create_window_page
import utilities.manage_pages
from extensions.verification import verify_equal
from utilities import base, common_ops
import work_flow.electron_work_flow

@pytest.mark.usefixtures('init_electron')
class Test_Electron:

    def test_01(self):
        actual_text = work_flow.electron_work_flow.ApiDemos.get_text_from_demo_window()
        excpected_text = common_ops.get_data('electronExpectedText')  # "Hello World!"
        verify_equal(actual_text, excpected_text)




