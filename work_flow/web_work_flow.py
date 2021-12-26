import test_cases.conftest
import utilities.common_ops
import utilities.manage_pages
from page_objects.web.sign_in_page import Sign_In_Page
from utilities import manage_pages


class Real_World:

    @staticmethod
    def login(user_name,password):
        manage_pages.sign_in.find_user_name_elem().send_keys(user_name)
        manage_pages.sign_in.find_password_elem().send_keys(password)
        manage_pages.sign_in.find_loggin_elem().click()
        return manage_pages.left_page.find_account_balance_element().text[1:]
