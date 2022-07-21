import json
import time
import requests
from requests import delete
import pyautogui

from Pages.Locators import Register_locators
from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData
class RegisterPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_REGISTER)
        self.driver.maximize_window()
        time.sleep(5)
    def valid_register_fan(self):
        time.sleep(2)
        self.do_click(Register_locators.name_input)
        time.sleep(2)
        file=open(TestData.AVATARS_PATH)
        content = json.load(file)
        self.do_send_keys(Register_locators.name_input, content["user_details"][0]["first_name"])
        self.do_click(Register_locators.surname_input)
        time.sleep(2)
        self.do_send_keys(Register_locators.surname_input, content["user_details"][0]["last_name"])
        self.do_click(Register_locators.email_input)
        time.sleep(2)
        self.do_send_keys(Register_locators.email_input, content["user_details"][0]["email"])
        time.sleep(2)
        file.close()
        self.do_click(Register_locators.password_input)
        time.sleep(2)
        self.do_send_keys(Register_locators.password_input, content["credentials"][0]["password"])
        self.do_click(Register_locators.confirm_pass_inp)
        time.sleep(2)
        self.do_send_keys(Register_locators.confirm_pass_inp, content["credentials"][0]["pass_confirm"])
        time.sleep(2)
        self.do_click(Register_locators.next_button)
        time.sleep(10)
        BasePage.verify_email(self)
        time.sleep(10)
        BasePage.fill_fan_field(self)
        complete = self.driver.find_element(By.CSS_SELECTOR, ".text-h5")
        return complete.text

    def valid_register_player(self):
        time.sleep(2)
        self.do_click(Register_locators.name_input)
        time.sleep(2)
        file = open(TestData.AVATARS_PATH)
        content = json.load(file)
        self.do_send_keys(Register_locators.name_input, content["user_details"][1]["first_name"])
        self.do_click(Register_locators.surname_input)
        time.sleep(2)
        self.do_send_keys(Register_locators.surname_input, content["user_details"][1]["last_name"])
        self.do_click(Register_locators.email_input)
        time.sleep(2)
        self.do_send_keys(Register_locators.email_input, content["user_details"][1]["email"])
        time.sleep(2)
        file.close()
        self.do_click(Register_locators.password_input)
        time.sleep(2)
        self.do_send_keys(Register_locators.password_input, content["credentials"][0]["password"])
        self.do_click(Register_locators.confirm_pass_inp)
        time.sleep(2)
        self.do_send_keys(Register_locators.confirm_pass_inp, content["credentials"][0]["pass_confirm"])
        time.sleep(2)
        self.do_click(Register_locators.next_button)
        time.sleep(10)
        BasePage.verify_email(self)
        time.sleep(10)
        BasePage.fill_player_field(self)
        BasePage.fill_player_field_details(self)











