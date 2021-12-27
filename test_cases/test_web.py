import pytest

import test_cases.conftest
import work_flow.web_work_flow


@pytest.mark.usefixtures('init_web')
class Test_Web:

    def test_01(self):
        balance = work_flow.web_work_flow.Real_World.login("Katharina_Bernier", "s3cret")
        assert balance == '1,681.37'

    def test_02(self):
        work_flow.web_work_flow.Real_World.signup_new_user()
