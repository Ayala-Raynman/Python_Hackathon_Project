import allure
import pytest
from smart_assertions import verify_expectations

from extensions.verification import verify_equal
from work_flow.web_work_flow import Real_World
import work_flow.web_work_flow
from utilities import manage_DB, manage_pages
from utilities import base
from utilities.common_ops import get_data


@pytest.mark.usefixtures('init_web')
class Test_Web:
    param_name = "user_name, password,ammount"
    list_users = manage_DB.reade_from_db()

    @allure.title("checking balance")
    @allure.description("after taking from sql we will verify if the user has the precise balance")
    @pytest.mark.parametrize(base.param_name, base.data_list)
    def test_01(self, user_name, password, amount):
        balance = Real_World.login(user_name, password)
        verify_equal(Real_World.convert_balance_to_integer(balance), amount)

    @allure.title("verify user details")
    @allure.description("checking if first name,last name and user name are the exact names as the user registered ")
    def test_02(self):
        work_flow.web_work_flow.Real_World.signup_new_user()
        work_flow.web_work_flow.Real_World.login_first_after_sign_up()
        work_flow.web_work_flow.Real_World.create_bank_account()
        work_flow.web_work_flow.Real_World.verify_if_registration_is_successful()
        verify_expectations()

    @allure.title("verify bank details")
    @allure.description("checking if bank account details in the account are the same as bank account details the "
                        "user wrote down the registration")
    def test_03(self):
        work_flow.web_work_flow.Real_World.login_first_after_sign_up()
        work_flow.web_work_flow.Real_World.verify_bank_account_name()
        verify_equal(manage_pages.user_settings_page.find_bank_name_element().text, get_data('bankName'))

    @allure.title("check web version")
    @allure.description("after reducing the web browser window by 80% of the original size we will verify if the "
                        "website has changes its responsiveness by smaller logo")
    def test_04(self):
        work_flow.web_work_flow.Real_World.verify_version_of_web_device()
