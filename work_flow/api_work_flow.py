from extensions.api_Actions import API_Actions
from utilities import base


class Users:
    @staticmethod
    def PostRequest():
        response = API_Actions.Post()
        base.user_Id += 1
        return response.status_code

    @staticmethod
    def DeleteRequest(user):
        response = API_Actions.Delete(user)
        return response.status_code

    @staticmethod
    def UpdateRequest(user, name):
        response = API_Actions.Patch(user, name)
        return response.status_code
