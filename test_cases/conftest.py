import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from appium import webdriver as mb
import utilities
import utilities.common_ops
import utilities.manage_pages
from utilities import base, manage_DB
from utilities.common_ops import get_data

driver = "No Driver"
action = None


@pytest.fixture(scope='class')
def init_web(request):
    platform: str = utilities.common_ops.get_data("BrowserType")
    # platform: str = os.getenv('BrowserType')
    if platform.lower() == 'chrome':
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif platform.lower() == 'firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        raise Exception("worng")
        # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("http://localhost:3000/")
    driver.maximize_window()
    driver.implicitly_wait(10)
    base.driver = driver
    utilities.manage_pages.InitPages.init_all_web_pages(driver)
    manage_DB.reade_from_db()
    yield
    driver.quit()


@pytest.fixture(scope='class')
def init_desktop(request):
    desired_caps = {}
    desired_caps["app"] = get_data("dc_app")
    desired_caps["platformName"] = get_data("dc_platformName")
    desired_caps["deviceName"] = get_data("deviceName")
    driver = webdriver.Remote(get_data("dc_server"), desired_caps)
    globals()['driver'] = driver
    base.driver = driver
    request.cls.driver = driver
    utilities.manage_pages.InitPages.init_desktop_pages(driver)
    yield
    driver.quit()



@pytest.fixture(scope='class')
def init_electron(request):
    options = webdriver.ChromeOptions()
    options.binary_location = utilities.common_ops.get_data('electronAppPath') #electron_app
    edriver = utilities.common_ops.get_data('electronDriverPath')
    driver = webdriver.Chrome(chrome_options=options, executable_path=edriver)

    driver.implicitly_wait(10)
    driver.set_page_load_timeout(10)
    globals()['driver'] = driver
    base.driver = driver
    request.cls.driver = driver
    utilities.manage_pages.InitPages.init_electron_pages(base.driver)

    yield
    driver.quit()

#
# @pytest.fixture(scope='class')
# def init_api(request):


@pytest.fixture(scope='class')
def init_mobile(request):
    base.dc['reportDirectory'] = base.reportDirectory
    base.dc['reportFormat'] = base.reportFormat
    base.dc['testName'] = base.testName
    base.dc['udid'] = 'RF8M90XHJMJ'
    base.dc['appPackage'] = 'com.financial.calculator'
    base.dc['appActivity'] = '.FinancialCalculators'
    base.dc['platformName'] = 'android'
    base.driver = webdriver.Remote('http://localhost:4723/wd/hub', base.dc)
    utilities.manage_pages.InitPages.init_appium_pages(driver)

    yield
    base.driver.quit()


@pytest.fixture(scope='class')
def init_api(request):
    base.api_url = get_data("apiUrl")
