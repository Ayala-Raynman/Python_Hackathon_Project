import test_cases.conftest
import utilities.common_ops
import utilities.manage_pages
from page_objects.web.sign_in_page import Sign_In_Page
from utilities import manage_pages


class Real_World:

    @staticmethod
    def login():
        manage_pages.sign_in.find_user_name_elem().send_keys("ayala")
        manage_pages.sign_in.find_password_elem().send_keys("1234")
        manage_pages.sign_in.find_loggin_elem().click()
