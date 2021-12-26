import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

import utilities
import utilities.common_ops
import utilities.manage_pages

driver = None
action = None


@pytest.fixture(scope='class')
def init_web(request):
    platform: str = utilities.common_ops.get_data("BrowserType")
    if platform.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif platform.lower() == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://localhost:3000/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    globals()['driver'] = driver
    request.cls.driver = driver
    utilities.manage_pages.InitPages.init_all_web_pages(driver)

    yield
    driver.quit()

#
# @pytest.fixture(scope='class')
# def init_api(request):



@pytest.fixture(scope='class')
def init_mobile(request):
    driver = None
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
