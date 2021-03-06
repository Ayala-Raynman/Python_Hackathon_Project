import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from extensions.ui_actions import UIActions
from utilities import manage_pages, base


class ApiDemos:

    @staticmethod
    @allure.step("open and navigate to demo window")
    def open_demo_window():
        e_page = manage_pages.electron_page
        if not e_page.get_toggle().is_displayed():
            UIActions.click_safely(e_page.get_window_master_button(), e_page.get_window_master_button_by())
            WebDriverWait(base.driver, 5).until(EC.element_to_be_clickable(e_page.get_toggle_by()))
        if not e_page.get_new_window_button().is_displayed():
            UIActions.click_safely(e_page.get_toggle(), e_page.get_toggle_by())
        handles_before = base.driver.window_handles
        UIActions.click_safely(e_page.get_new_window_button(), e_page.get_new_window_by())
        UIActions.switch_to_new_window(handles_before)

    @staticmethod
    @allure.step("get text of demo window")
    def get_text_from_demo_window():
        original_window_handle = base.driver.current_window_handle
        ApiDemos.open_demo_window()
        actual_text = manage_pages.electron_demo_page.get_demo_window_text()
        base.driver.close()
        base.driver.switch_to.window(original_window_handle)
        return actual_text
