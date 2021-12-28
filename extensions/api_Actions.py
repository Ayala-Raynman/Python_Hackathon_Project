import requests
from utilities.common_ops import get_data


class API_Actions:
    headers = {"Content-Type": "application/json"}
    @staticmethod
    def Post(url, payload):
        response = requests.post(url, json=payload, headers=API_Actions.headers)
        return response

    @staticmethod
    def Delete(url, user):
        response = requests.delete(url + str(user))
        return response

    @staticmethod
    def Patch(url, user, name):
        payload = {"name": name}
        response = requests.patch(url + str(user), json=payload, headers=API_Actions.headers)
        return response
