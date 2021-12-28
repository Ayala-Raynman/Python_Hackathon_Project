import requests
from utilities.common_ops import get_data

class API_Actions:
    url =get_data("apiUrl")
    headers = {"Content-Type": "application/json"}
    @staticmethod
    def Post():
        payload = {
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }
        response = requests.post(API_Actions.url , json=payload, headers=API_Actions.headers)

        return response

    @staticmethod
    def Delete(user):
        response = requests.delete(API_Actions.url  + str(user))
        return response
    @staticmethod
    def Patch(user,name):
        payload = {"name": name}
        response = requests.patch(API_Actions.url + str(user), json=payload, headers=API_Actions.headers)
        return response
