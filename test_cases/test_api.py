import json
import allure
import pytest
from utilities import base
from utilities.common_ops import get_data
from work_flow.api_work_flow import Users
from extensions.verification import verify_equal

@pytest.mark.usefixtures('init_api')
class Test_API:
    @allure.title("Create new user")
    @allure.description("This test for create  a new user and add to the list of users")
    def test_01_post(self):
        payload = json.loads(get_data("newUser"))
        response_code = Users.PostRequest(base.api_url, payload)
        verify_equal(response_code,201)

    @allure.title("Update")
    @allure.description("update name for user")
    def test_02(self):
        response_code = Users.UpdateRequest(base.api_url,base.user_Id, get_data("userName"))
        verify_equal(response_code, 200)

    @allure.title("Delete")
    @allure.description("delete user by id from the list of users")
    def test_03(self):
        response_code = Users.DeleteRequest(base.api_url,base.user_Id)
        verify_equal(response_code,200)
