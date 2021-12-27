import pytest
from nose.plugins.builtin import cls

import test_cases.conftest
from work_flow.web_work_flow import Real_World
import work_flow.web_work_flow
import utilities.manage_DB
from utilities import manage_DB
from utilities import base


@pytest.mark.usefixtures('init_web')
class Test_Web:
    param_name = "user_name, password,ammount"
    list_users = manage_DB.reade_from_db()

    @pytest.mark.parametrize(base.param_name, base.data_list)
    def test_01(self, user_name, password, amount):
        balance = Real_World.login(user_name, password)
        assert Real_World.convert_balance_to_integer(balance) == amount

    def test_02(self):
        work_flow.web_work_flow.Real_World.signup_new_user()
        work_flow.web_work_flow.Real_World.signup_new_user()
        work_flow.web_work_flow.Real_World.login_first_after_sign_up()
        work_flow.web_work_flow.Real_World.create_bank_account()
        work_flow.web_work_flow.Real_World.verify_if_registration_is_successful()
        work_flow.web_work_flow.Real_World.verify_bank_account_name()

    def test_03(self):
        work_flow.web_work_flow.Real_World.verify_bank_account_name()

    def test_04(self):
        manage_DB.connect()
        result=manage_DB.reade_from_db()
        print(type(result))
        print(result)
        # manage_DB.close_db()
