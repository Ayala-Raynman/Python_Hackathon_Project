import allure

from extensions.ui_actions import UIActions
from test_cases import conftest
from utilities import manage_pages


class Calculator:
    @staticmethod
    @allure.step("Check each member in the string to see if it is a number or a character")
    def calc_str(exercise):
        for i in exercise:
            print(i)
            if i.isdigit():
                Calculator.numbers_buttns(i)
            else:
                Calculator.operator_buttons(i)
        UIActions.click(manage_pages.calc_page.btn_equal())

    @staticmethod
    @allure.step("Clicking on number type organs")
    def numbers_buttns(digit):
        print(conftest.driver)
        if digit == "1":
            UIActions.click(manage_pages.calc_page.btn_1())
        elif digit == "2":
            UIActions.click(manage_pages.calc_page.btn_2())
        elif digit == "3":
            UIActions.click(manage_pages.calc_page.btn_3())
        elif digit == "4":
            UIActions.click(manage_pages.calc_page.btn_4())
        elif digit == "5":
            UIActions.click(manage_pages.calc_page.btn_5())
        elif digit == "6":
            UIActions.click(manage_pages.calc_page.btn_6())
        elif digit == "7":
            UIActions.click(manage_pages.calc_page.btn_7())
        elif digit == "8":
            UIActions.click(manage_pages.calc_page.btn_8())
        elif digit == "9":
            UIActions.click(manage_pages.calc_page.btn_9())
        else:
            UIActions.click(manage_pages.calc_page.btn_0())

    @staticmethod
    @allure.step("Click on character type organs")
    def operator_buttons(digit):
        if digit == "+":
            UIActions.click(manage_pages.calc_page.btn_plus())
        elif digit == "-":
            UIActions.click(manage_pages.calc_page.btn_less())
        elif digit == "*":
            UIActions.click(manage_pages.calc_page.btn_multy())
        elif digit == "/":
            UIActions.click(manage_pages.calc_page.btn_div())
        else:
            print("Unsupported operator")

    @staticmethod
    @allure.step("Returns the result of the calculation")
    def get_result_number():
        str_display = manage_pages.calc_page.btn_result().get_attribute("Name")
        int_display = int(str_display.replace("Display is", "").strip())
        return int_display
