import pytest

driver = None
action = None


@pytest.fixture(scope='class')
def init_web(request):
    driver =None
    globals()['driver'] = driver
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_mobile(request):
    driver =None
    globals()['driver'] = driver

    yield
    driver.quit()


#
# @pytest.mark.usefixtures('init_web')
# class Test_Cases_Web:
#     def test01():
#         .......


#
# @pytest.mark.usefixtures('init_mobile')
# class Test_Cases_Mobile:
#     def test01():