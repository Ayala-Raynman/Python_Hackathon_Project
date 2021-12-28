import time

import test_cases.conftest
import utilities.common_ops
import utilities.manage_pages
from extensions.ui_actions import UIActions
from page_objects.web.sign_in_page import Sign_In_Page
from utilities import manage_pages
from utilities import base
from smart_assertions import soft_assert, verify_expectations
from utilities import base
from applitools.selenium import Eyes



class Real_World:

    @staticmethod
    def login(user_name, password):
        UIActions.send_keys(manage_pages.sign_in.find_user_name_elem(), user_name)
        UIActions.send_keys(manage_pages.sign_in.find_password_elem(), password)
        UIActions.click(manage_pages.sign_in.find_loggin_elem())
        balance_text = manage_pages.left_page.find_account_balance_element().text[1:]
        UIActions.click(manage_pages.left_page.find_logout_element())
        return balance_text

    @staticmethod
    def convert_balance_to_integer(balance: str):
        int_balance = int(balance.split('.')[0].replace(",", ""))
        return int_balance

    @staticmethod
    def signup_new_user():
        UIActions.click(manage_pages.sign_in.find_sign_up_button_elem())
        UIActions.click(manage_pages.sign_in.find_sign_up_button_elem())
        UIActions.send_keys(manage_pages.sign_up_page.find_first_name_elem(), string_to_send="jeffjeff")
        UIActions.send_keys(manage_pages.sign_up_page.find_surname_elem(), string_to_send="Kuku")
        UIActions.send_keys(manage_pages.sign_up_page.find_user_name_elem(), string_to_send="jeffjeff123456")
        UIActions.send_keys(manage_pages.sign_up_page.find_password_elem(), string_to_send="jenkins123")
        UIActions.send_keys(manage_pages.sign_up_page.find_confirm_password_elem(), string_to_send="jenkins123")
        UIActions.doubleClick(manage_pages.sign_up_page.find_sign_up_button_elem())

    @staticmethod
    def login_first_after_sign_up():
        UIActions.send_keys(manage_pages.sign_in.find_user_name_elem(), string_to_send="jeffjeff123456")
        UIActions.send_keys(manage_pages.sign_in.find_password_elem(), string_to_send="jenkins123")
        UIActions.click(manage_pages.sign_in.find_loggin_elem())
        try:
            UIActions.click(manage_pages.main_page.find_next_button_in_get_started_page_element())
        except:
            print("user logged in")

    @staticmethod
    def create_bank_account():
        try:
            UIActions.send_keys(manage_pages.main_page.find_bank_name_element(), string_to_send="leumi")
            UIActions.send_keys(manage_pages.main_page.find_routing_number_element(), string_to_send="123456789")
            UIActions.send_keys(manage_pages.main_page.find_account_number_element(), string_to_send="000123456789")
            UIActions.click(manage_pages.main_page.find_submit_button_element())
            UIActions.click(manage_pages.main_page.find_next_button_for_finish())
        except:
            print("user already logged in")

    @staticmethod
    def verify_if_registration_is_successful():
        UIActions.click(manage_pages.main_page.find_my_account_btn_element())
        soft_assert(manage_pages.main_page.find_user_name_label_elem() == "@jeffjeff123456")
        soft_assert(
            manage_pages.user_settings_page.find_first_name_textField_element().get_attribute('value') == "jeffjeff")
        soft_assert(manage_pages.user_settings_page.find_surname_textField_element().get_attribute('value') == "Kuku")
        verify_expectations()

    @staticmethod
    def verify_bank_account_name():
        UIActions.click(manage_pages.main_page.find_bank_accounts_in_side_navbar())
        assert manage_pages.user_settings_page.find_bank_name_element().text == "leumi"

    @staticmethod
    def verify_version_of_web_device():
        eyes = Eyes()
        eyes.api_key = base.api_key_for_applitools
        size = base.driver.get_window_size()
        height = size['height']
        width = size['width']
        print("height is : " + str(height) + " and width is " + str(width))
        eyes.open(base.driver, "Python Hackaton project", "testing the web version of Real World app")
        eyes.check_window("watch in the page in desktop version")
        base.driver.set_window_size(int(width/5), height)
        time.sleep(3)
        size = base.driver.get_window_size()
        height = size['height']
        width = size['width']
        print("height is : " + str(height) + " and width is " + str(width))
        eyes.check_window("watch in the page in mobile version")
        eyes.close()


