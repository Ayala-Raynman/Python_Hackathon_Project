import allure
import requests


class API_Actions:
    headers = {"Content-Type": "application/json"}

    @staticmethod
    @allure.step("post request")
    def Post(url, payload):
        response = requests.post(url, json=payload, headers=API_Actions.headers)
        return response

    @staticmethod
    @allure.step("delete request")
    def Delete(url, user):
        response = requests.delete(url + str(user))
        return response

    @staticmethod
    @allure.step("patch request")
    def Patch(url, user, name):
        payload = {"name": name}
        response = requests.patch(url + str(user), json=payload, headers=API_Actions.headers)
        return response
