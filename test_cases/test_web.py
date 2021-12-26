import login as login
import pytest

import test_cases.conftest
import work_flow.web_work_flow


@pytest.mark.usefixtures('init_web')
class Test_Web:

    def test_01(self):
        work_flow.web_work_flow.Real_World.login()
