import test_cases.conftest
import utilities.common_ops
import utilities.manage_pages
from extensions.ui_actions import UIActions
from page_objects.web.sign_in_page import Sign_In_Page
from utilities import manage_pages


class Real_World:

    @staticmethod
    def login(user_name,password):
        manage_pages.sign_in.find_user_name_elem().send_keys(user_name)
        manage_pages.sign_in.find_password_elem().send_keys(password)
        manage_pages.sign_in.find_loggin_elem().click()
        balance_text= manage_pages.left_page.find_account_balance_element().text[1:]
        manage_pages.left_page.find_logout_element().click()
        return balance_text

    @staticmethod
    def signup_new_user():
        UIActions.click(manage_pages.sign_in.find_sign_up_button_elem())
        UIActions.click(manage_pages.sign_in.find_sign_up_button_elem())
        manage_pages.sign_up_page.find_first_name_elem().send_keys("JeffJeff")
