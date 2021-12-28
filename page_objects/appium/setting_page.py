import allure
from selenium.webdriver.common.by import By


class Setting_Page:
    def __init__(self, driver):
        self.driver = driver

    def btn_home_screen(self):
        return self.driver.find_element(By.XPATH, "//*[@contentDescription='נווט למעלה']")

    def btn_home_screen_by(self):
        return (By.XPATH, "//*[@contentDescription='נווט למעלה']")

    def btn_setting(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Settings']")

    def find_background_colors(self):
        return self.driver.find_element(By.XPATH,
                                        "//*[@class='android.widget.RelativeLayout' and ./*[@text='Background color']]")

    def black_background_color(self):
        return self.driver.find_element(By.XPATH, "//*[@text='Black']")

    def get_current_background_color(self):
        return self.driver.find_element(By.XPATH, "(//*[@id='listview']/*/*[@id='text2'])[1]")
