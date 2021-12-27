from page_objects.web.sign_in_page import Sign_In_Page
from page_objects.web.main_page import main_page
from page_objects.web.user_settings_page import user_settings_page
from page_objects.web.sign_up_page import sign_up_page
from page_objects.web.left_page import Left_Page
from page_objects.desktop.calculator_page import Calculator_Page

sign_in = None
left_page = None
calc_page=None


class InitPages:

    @staticmethod
    def init_all_web_pages(driver):
        globals()['sign_in'] = Sign_In_Page(driver)
        globals()['main_page'] = main_page(driver)
        globals()['user_settings_page'] = user_settings_page(driver)
        globals()['sign_up_page'] = sign_up_page(driver)


        globals()['left_page'] = Left_Page(driver)

    @staticmethod
    def init_desktop_pages(driver):
        globals()['calc_page']=Calculator_Page(driver)
