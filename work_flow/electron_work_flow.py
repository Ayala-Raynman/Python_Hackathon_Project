from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import extensions.ui_actions
from extensions.ui_actions import UIActions
import page_objects.electron.create_window_page
from utilities import manage_pages, base


class ApiDemos:
    @staticmethod
    def open_demo_window():
        pass #manage_pages.electron_page.
        #e_page = page_objects.electron.create_window_page.CreateWindowsPage(base.driver)

    @staticmethod
    def switch_to_new_window(handles_before):
        WebDriverWait(base.driver, 5).until(
            lambda driver: len(handles_before) != len(driver.window_handles))
        handles = base.driver.window_handles
        base.driver.switch_to.window(handles[1])

    @staticmethod
    def get_text_from_demo_window():
        e_page = manage_pages.electron_page #page_objects.electron.create_window_page.CreateWindowsPage(base.driver)
        # e_page.click_t()
        # e_page.get_toggle().click()
        if not e_page.get_new_window_button().is_displayed():
            e_page.get_toggle().click()
            WebDriverWait(base.driver, 5).until(EC.element_to_be_clickable(e_page.get_new_window_by()))

        #UIActions.click_safely(e_page.get_new_window_button(), e_page.get_new_window_button_by())
        handles_before = base.driver.window_handles
        #e_page.get_new_window_button().click()
        UIActions.click_safely(e_page.get_new_window_button(),e_page.get_new_window_by())
        # time.sleep(2)
        WebDriverWait(base.driver, 5).until(
            lambda driver: len(handles_before) != len(driver.window_handles))
        handles = base.driver.window_handles
        base.driver.switch_to.window(handles[1])
        #ApiDemos.switch_to_new_window(handles_before)
        actual_text = base.driver.find_element(By.TAG_NAME, 'h2').text
        base.driver.close()
        base.driver.switch_to.window(handles[0])
        return actual_text