import json
import os
import time
import random

import pyautogui
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.LoginPage import LoginPage
from Pages.RegisterPage import RegisterPage
from Pages.ActionsPage import get_filter_data
import requests
from collections import Counter, defaultdict

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL_LOGIN)
        self.driver.maximize_window()
        time.sleep(2)
    def valid_notification(self):
        BasePage.send_notification(self)

    def valid_moderation(self):
        file = open(TestData.AVATARS_PATH)
        content = json.load(file)
        self.registerPage = RegisterPage(self.driver)
        self.registerPage.valid_register_player()
        BasePage.logout(self)
        time.sleep(4)
        self.loginPage = LoginPage(self.driver)
        self.loginPage.valid_login_player(content["moderators"][0]["email"], content["moderators"][0]["password"])
        time.sleep(2)
        BasePage.pass_moderation(self)
    def video_upload(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        upload_btn = self.driver.find_element(By.CSS_SELECTOR,".q-btn.q-btn-item.non-selectable.no-outline.q-btn--outline.q-btn--rectangle.text-primary.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-ml-auto")
        upload_btn.click()
        time.sleep(1)
        browse_btn = self.driver.find_element(By.XPATH,"//span[@class='text-h6 text-primary cursor-pointer all-pointer-events']")
        browse_btn.click()
        time.sleep(2)
        pyautogui.typewrite(self.FILE_PATH, interval=0.15)
        pyautogui.press('enter')
        time.sleep(3)
        description_input = self.driver.find_element(By.XPATH, "//textarea[@aria-label='Description']")
        description_input.click()
        time.sleep(1)
        description_input.send_keys("Test uploading video description")
        time.sleep(1)
        publish_btn = self.driver.find_element(By.CSS_SELECTOR,"button[class='q-btn q-btn-item non-selectable no-outline q-btn--standard q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase q-ml-auto'] span[class='block']")
        publish_btn.click()
        time.sleep(2)
        self.driver.refresh()

    def search_profile(self, param):
        search_input = self.driver.find_element(By.XPATH,"//input[@aria-label='Search for players']")
        search_input.click()
        time.sleep(1)
        search_input.send_keys(param)
        time.sleep(1)
        search_input.send_keys(Keys.UP)
        time.sleep(1)
        search_input.send_keys(Keys.RETURN)
    def filter_profile_gender(self): # clicks on a random player position and returns position name
        filter_btn = self.driver.find_element(By.XPATH,"//button[@class='q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle q-btn--actionable "
                                                       "q-focusable q-hoverable q-btn--no-uppercase full-height no-margin']//span[@class='q-btn__content text-center "
                                                       "col items-center q-anchor--skip justify-center row']")
        filter_btn.click()
        time.sleep(2)
        gender_selector = self.driver.find_element(By.XPATH, "(//div[@class='q-field__inner relative-position col self-stretch'])[4]")
        gender_selector.click()
        time.sleep(1)
        gender_male = self.driver.find_element(By.XPATH,"//span[normalize-space()='Male']")
        gender_female = self.driver.find_element(By.XPATH,"//span[normalize-space()='Female']")
        gender_male.click()
        time.sleep(1)
        apply_filter = self.driver.find_element(By.XPATH,"//button[@class='q-btn q-btn-item non-selectable no-outline q-btn--standard q-btn--rectangle bg-primary text-white q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase']//span[@class='q-btn__content text-center col items-center q-anchor--skip justify-center row']")
        apply_filter.click()
        data_all = get_filter_data(self)
        print(len(data_all))
        print(data_all)
        gender_counter = Counter(token["gender"] for token in data_all)
        gender_counter_male = (gender_counter["male"])
        gender_counter_female = (gender_counter["female"])
        #unique_users = list({v["id"]:v for v in data_all}.values())
        return gender_counter_male

    def scroll_down(self, n):
        for i in range(0,n):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)

    def switch_position(self, position):
        if position == "Centre Back":
            return "centre_back"
        elif position == "Full Back":
            return "full_back"
        elif position == "Right Full Back":
            return "right_full_back"
        elif position == "Left Full Back":
            return "left_fool_back"
        elif position == "Winger":
            return "winger"
        elif position == "Right Winger":
            return "right_winger"
        elif position == "Left Winger":
            return "left_winger"
        elif position == "Central Midfielder":
            return "central_midfielder"
        elif position == "Defensive Midfielder":
            return "defensive_midfielder"
        elif position == "Attacking Midfielder":
            return "attacking_midfielder"
        elif position == "Wide Midfielder":
            return "wide_midfielder"
        elif position == "Wide Right Midfielder":
            return "wide_right_midfielder"
        elif position == "Wide Left Midfielder":
            return "wide_left_midfielder"
        elif position == "Striker":
            return
        elif position == "Centre Forward":
            return "centre_forward"
        elif position == "Second Striker":
            return "second_striker"
        elif position == "Right Forward":
            return "right_forward"
        elif position == "Left Forward":
            return "left_forward"
        return position







