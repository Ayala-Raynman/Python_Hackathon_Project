import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import utilities.common_ops

driver = None
action = None


@pytest.fixture(scope='class')
def init_web(request):
    driver =None
    platform: str = utilities.common_ops.get_data("BrowserType")
    if platform.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif platform.lower() == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
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