import allure

from extensions.api_Actions import API_Actions
from utilities import base


class Users:
    @staticmethod
    @allure.step("Add user")
    def PostRequest(url, payload):
        response = API_Actions.Post(url, payload)
        base.user_Id += 1
        return response.status_code

    @staticmethod
    @allure.step("Update name")
    def UpdateRequest(url, user_id, name):
        response = API_Actions.Patch(url, user_id, name)
        return response.status_code

    @staticmethod
    @allure.step("Delete user")
    def DeleteRequest(url, user_id):
        response = API_Actions.Delete(url, user_id)
        return response.status_code
