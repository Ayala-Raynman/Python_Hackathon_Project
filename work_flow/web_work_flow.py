import time

import allure

import test_cases.conftest
import utilities.common_ops
import utilities.manage_pages
from extensions.ui_actions import UIActions
from page_objects.web.sign_in_page import Sign_In_Page
from utilities import manage_pages
from utilities.common_ops import get_data
from smart_assertions import soft_assert, verify_expectations
from utilities import base
from applitools.selenium import Eyes


class Real_World:

    @staticmethod
    @allure.step("logging in")
    def login(user_name, password):
        UIActions.send_keys(manage_pages.sign_in.find_user_name_elem(), user_name)
        UIActions.send_keys(manage_pages.sign_in.find_password_elem(), password)
        UIActions.click(manage_pages.sign_in.find_loggin_elem())
        balance_text = manage_pages.left_page.find_account_balance_element().text[1:]
        UIActions.click(manage_pages.left_page.find_logout_element())
        return balance_text

    @staticmethod
    @allure.step("converting balance to integer")
    def convert_balance_to_integer(balance: str):
        int_balance = int(balance.split('.')[0].replace(",", ""))
        return int_balance

    @staticmethod
    @allure.step("signing up new user")
    def signup_new_user():
        UIActions.click(manage_pages.sign_in.find_sign_up_button_elem())
        UIActions.click(manage_pages.sign_in.find_sign_up_button_elem())
        UIActions.send_keys(manage_pages.sign_up_page.find_first_name_elem(), string_to_send=get_data('firstName'))
        UIActions.send_keys(manage_pages.sign_up_page.find_surname_elem(), string_to_send=get_data('lastName'))
        UIActions.send_keys(manage_pages.sign_up_page.find_user_name_elem(), string_to_send=get_data('userName'))
        UIActions.send_keys(manage_pages.sign_up_page.find_password_elem(), string_to_send=get_data('password'))
        UIActions.send_keys(manage_pages.sign_up_page.find_confirm_password_elem(),
                            string_to_send=get_data('reconfirmPassword'))
        UIActions.doubleClick(manage_pages.sign_up_page.find_sign_up_button_elem())

    @staticmethod
    @allure.step("making a log in after sign up")
    def login_first_after_sign_up():
        UIActions.send_keys(manage_pages.sign_in.find_user_name_elem(), string_to_send=get_data('userName'))
        UIActions.send_keys(manage_pages.sign_in.find_password_elem(), string_to_send=get_data('password'))
        UIActions.click(manage_pages.sign_in.find_loggin_elem())
        try:
            UIActions.click(manage_pages.main_page.find_next_button_in_get_started_page_element())
        except:
            print("user logged in")

    @staticmethod
    @allure.step("creating a bank account")
    def create_bank_account():
        try:
            UIActions.send_keys(manage_pages.main_page.find_bank_name_element(), string_to_send=get_data('bankName'))
            UIActions.send_keys(manage_pages.main_page.find_routing_number_element(),
                                string_to_send=get_data('routingNumber'))
            UIActions.send_keys(manage_pages.main_page.find_account_number_element(),
                                string_to_send=get_data('accountNumber'))
            UIActions.click(manage_pages.main_page.find_submit_button_element())
            UIActions.click(manage_pages.main_page.find_next_button_for_finish())
        except:
            print("user already logged in")

    @staticmethod
    @allure.step("verifying registration")
    def verify_if_registration_is_successful():
        UIActions.click(manage_pages.main_page.find_my_account_btn_element())
        soft_assert(manage_pages.main_page.find_user_name_label_elem() == "@" + get_data('userName'))
        soft_assert(
            manage_pages.user_settings_page.find_first_name_textField_element().get_attribute('value') == get_data('firstName'))
        soft_assert(manage_pages.user_settings_page.find_surname_textField_element().get_attribute('value') == get_data('lastName'))
        UIActions.click(manage_pages.left_page.find_logout_element())

    @staticmethod
    @allure.step("verifying bank account name")
    def verify_bank_account_name():
        UIActions.click(manage_pages.main_page.find_bank_accounts_in_side_navbar())

    @staticmethod
    @allure.step("verifying version of device")
    def verify_version_of_web_device():
        eyes = Eyes()
        eyes.api_key = base.api_key_for_applitools
        size = base.driver.get_window_size()
        height = size['height']
        width = size['width']
        eyes.open(base.driver, "Python Hackaton project", "testing the web version of Real World app")
        eyes.check_window("watch in the page in desktop version")
        base.driver.set_window_size(int(width / 5), height)
        time.sleep(3)
        eyes.check_window("watch in the page in mobile version")
        eyes.close()
