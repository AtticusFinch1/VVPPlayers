import json
import time

import pyautogui
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Pages.Locators import Register_locators
from Config.config import TestData

class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_LOGIN)
        self.driver.maximize_window()
        time.sleep(2)

    def valid_login(self, email, password):
        time.sleep(2)
        user_inputs = self.driver.find_elements(By.CSS_SELECTOR, ".q-field__native")
        user_inputs[0].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Email']").send_keys(
            email)
        time.sleep(2)
        user_inputs[1].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Password']").send_keys(
            password)
        time.sleep(2)
        register_login_button = self.driver.find_element(By.XPATH, "//span[@class='block']")
        register_login_button.click()
        time.sleep(10)








