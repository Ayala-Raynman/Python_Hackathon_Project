from page_objects.web.sign_in_page import Sign_In_Page

sign_in = None


class InitPages:

    @staticmethod
    def init_all_web_pages(driver):
        globals()['sign_in'] = Sign_In_Page(driver)
