from utilities import base, manage_pages
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from extensions.ui_actions import UIActions


class Financial_Calculators:
    @staticmethod
    def change_background_color():
        UIActions.click(manage_pages.setting_page.btn_home_screen())
        UIActions.click(manage_pages.setting_page.btn_setting())
        UIActions.click(manage_pages.setting_page.find_background_colors())
        UIActions.click(manage_pages.setting_page.black_background_color())

        current_background_color = Financial_Calculators.get_background_color()
        UIActions.click_safely(manage_pages.setting_page.btn_home_screen(),
                               manage_pages.setting_page.btn_home_screen_by())
        UIActions.click(manage_pages.setting_page.btn_home_screen())
        return current_background_color

    @staticmethod
    def get_background_color():
        chosen_background_color = manage_pages.setting_page.get_current_background_color()
        return chosen_background_color.text

    @staticmethod
    def get_number_of_app_icons():
        number_of_app_icons = manage_pages.home_page.get_num_sub_apps()
        return len(number_of_app_icons)

    @staticmethod
    def get_total_payment(bill, tip):
        UIActions.click(manage_pages.calc_tips_page.btn_calc_tips_apps())
        UIActions.send_keys(manage_pages.calc_tips_page.input_bill(), str(bill))

        WebDriverWait(base.driver, 60).until(
            expected_conditions.presence_of_element_located((manage_pages.calc_tips_page.input_tip_by())))
        UIActions.click(manage_pages.calc_tips_page.input_tip())
        UIActions.send_keys(manage_pages.calc_tips_page.input_tip(), str(tip))
        return manage_pages.calc_tips_page.total_payment().text

    @staticmethod
    def verify_tip(bill, tip):
        return float(float(bill) * (float(tip) + 100) / 100)
