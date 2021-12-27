from selenium.webdriver.common.by import By


class Calculator_Page:

    def __init__(self, driver):
        self.driver = driver

    def btn_1(self):
        return self.driver.find_element(By.NAME, "One")

    def btn_2(self):
        return self.driver.find_element(By.NAME, "Two")

    def btn_3(self):
        return self.driver.find_element(By.NAME, "Three")

    def btn_4(self):
        return self.driver.find_element(By.NAME, "Four")

    def btn_5(self):
        return self.driver.find_element(By.NAME, "Five")

    def btn_6(self):
        return self.driver.find_element(By.NAME, "Six")

    def btn_7(self):
        return self.driver.find_element(By.NAME, "Seven")

    def btn_8(self):
        return self.driver.find_element(By.NAME, "Eight")

    def btn_9(self):
        return self.driver.find_element(By.NAME, "Nine")

    def btn_0(self):
        return self.driver.find_element(By.NAME, "Zero")

    def btn_C(self):
        return self.driver.find_element(By.NAME, "Clear")

    def btn_plus(self):
        return self.driver.find_element(By.NAME, "Plus")

    def btn_less(self):
        return self.driver.find_element(By.NAME, "Minus")

    def btn_multy(self):
        return self.driver.find_element(By.NAME, "Multiply by")

    def btn_div(self):
        return self.driver.find_element(By.NAME, "Divide by")

    def btn_equal(self):
        return self.driver.find_element(By.NAME, "Equals")

    def btn_result(self):
        return self.driver.find_element(By.XPATH, "//*[@AutomationId='CalculatorResults']")
