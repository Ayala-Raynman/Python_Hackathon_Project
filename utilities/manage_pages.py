from page_objects.web.sign_in_page import Sign_In_Page
from page_objects.web.left_page import Left_Page

sign_in = None
left_page = None


class InitPages:

    @staticmethod
    def init_all_web_pages(driver):
        globals()['sign_in'] = Sign_In_Page(driver)
        globals()['left_page'] = Left_Page(driver)
