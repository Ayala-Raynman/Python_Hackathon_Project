import requests
import work_flow.web_work_flow
from utilities import base
from work_flow.api_work_flow import Users


class Test_API:

    def test_01_post(self):
        response_code = Users.PostRequest()
        assert response_code == 201

    def test_02(self):
        response_code = Users.UpdateRequest(base.user_Id,"david david")
        assert response_code == 200

    def test_03(self):
        response_code = Users.DeleteRequest(base.user_Id)
        assert response_code == 200
