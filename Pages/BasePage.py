import json
import time
import requests
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyautogui

from Config.config import TestData
class BasePage(TestData):
    load_dotenv()
    def __init__(self,driver):
        self.driver=driver

    # def _find(self,by_locator):
    #     return self.driver.find_element(by_locator)

    def do_click(self,locator):
        return self.driver.find_element(locator["by"], locator["value"]).click()

    def do_clear(self,locator):
        return self.driver.find_element(locator["by"], locator["value"]).clear()

    def do_send_keys(self,locator,text):
        return self.driver.find_element(locator["by"], locator["value"]).send_keys(text)

    def get_element_text(self,by_locator):
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self,by_locator):
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title

    def do_get_text(self,by_locator):
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute("value")

    def do_hover(self,by_locator):
        actions = ActionChains(self.driver)
        element=WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        actions.move_to_element(element).perform()
    def logout(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR,
                                             '.q-btn__content.text-center.col.items-center.q-anchor--skip.justify-center.row')
        time.sleep(2)
        elements[2].click()
        time.sleep(3)
        user_btns = self.driver.find_elements(By.CSS_SELECTOR, ".q-btn.q-btn-item")
        user_btns[7].click()
        time.sleep(2)
    def verify_email(self):
        api_token = {"api_token": "99eff2ac3f1e64279557b3aeeb207530"}  # take the api token of the email user
        r = requests.get("https://mailtrap.io/api/v1/inboxes/1206778/messages",
                         params=api_token)  # go to current inbox messages by its inbox_id, as we do not have last message_id
        data = r.json()  # convert data to json
        html = data[0]["html_path"]  # to get the endpoint of uri
        # print(html)  # /api/v1/inboxes/1206778/messages/2651900645/body.html
        data_needed = requests.get("https://mailtrap.io" + html, params=api_token)

        soup = BeautifulSoup(data_needed.text, 'html.parser')
        urls = []
        for link in soup.find_all('a'):
            urls.append(link.get('href'))
        # print(urls[1])
        self.driver.get(urls[1])
    def fill_fan_field(self):
        user_inputs = self.driver.find_elements(By.CSS_SELECTOR, ".q-field__native")
        user_inputs[0].click()
        dropdown_options = self.driver.find_elements(By.CSS_SELECTOR, ".q-item-type")
        time.sleep(2)
        dropdown_options[0].click()
        time.sleep(2)
        user_inputs[1].click()
        time.sleep(2)
        file = open(TestData.AVATARS_PATH)
        content = json.load(file)
        self.driver.find_element(By.XPATH,"//input[@aria-label='Username']").send_keys(
            content["user_details"][0]["first_name"])
        time.sleep(1)
        user_inputs[2].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Phone number']").send_keys(
            content["user_details"][0]["phone"])
        time.sleep(1)
        logout_next_button = self.driver.find_elements(By.CSS_SELECTOR, ".q-btn__content")
        logout_next_button[1].click()
        time.sleep(5)
    def fill_player_field(self):
        user_inputs = self.driver.find_elements(By.CSS_SELECTOR, ".q-field__native")
        user_inputs[0].click()
        dropdown_options = self.driver.find_elements(By.CSS_SELECTOR, ".q-item-type")
        time.sleep(1)
        dropdown_options[1].click()
        time.sleep(1)
        user_inputs[1].click()
        time.sleep(1)
        file = open(TestData.AVATARS_PATH)
        content = json.load(file)
        self.driver.find_element(By.XPATH, "//input[@aria-label='Username']").send_keys(
            content["user_details"][1]["first_name"])
        time.sleep(1)
        user_inputs[2].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Phone']").send_keys(
            content["user_details"][0]["phone"])
        time.sleep(3)
        logout_next_button = self.driver.find_elements(By.CSS_SELECTOR, ".q-btn__content")
        logout_next_button[1].click()
        time.sleep(5)
    def fill_player_field_details(self):
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//input[@aria-label='Birth Date']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[contains(text(),'2022')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[contains(text(),'2020')]").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[@class='block'][normalize-space()='1']").click()
        time.sleep(1)
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Close')]").click()
        time.sleep(1)
        player_inputs = self.driver.find_elements(By.CSS_SELECTOR, ".q-field__control-container")
        player_inputs[1].click()
        time.sleep(1)
        dropdown_options = self.driver.find_elements(By.CSS_SELECTOR, ".q-item-type")
        dropdown_options[2].click()
        time.sleep(1)
        player_inputs[2].click()
        time.sleep(1)
        gender_options = self.driver.find_elements(By.CSS_SELECTOR, ".q-item__label")
        gender_options[1].click()
        time.sleep(1)
        file = open(TestData.AVATARS_PATH)
        content = json.load(file)
        player_inputs[3].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Current School / University']").send_keys(
            content["user_details"][1]["current_club"])
        time.sleep(2)
        player_inputs[4].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Height']").send_keys(
            content["user_details"][1]["height"])
        time.sleep(2)
        player_inputs[5].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Weight']").send_keys(
            content["user_details"][1]["weight"])
        time.sleep(2)
        player_inputs[6].click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "(//div[@class='q-item__label'])[1]").click()
        time.sleep(2)
        player_inputs[7].click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//div[@class='q-item__label'])[2]").click()
        time.sleep(2)
        player_inputs[8].click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//div[@class='q-item__label'])[8]").click()
        time.sleep(2)
        player_inputs[9].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Current Club']").send_keys(
            content["user_details"][1]["current_club"])
        time.sleep(1)
        player_inputs[10].click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "(//div[@class='q-item__label'])[8]").click()
        time.sleep(1)
        player_inputs[11].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Province']").send_keys(
            content["user_details"][1]["province"])
        time.sleep(1)
        player_inputs[12].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Address Line']").send_keys(
            content["user_details"][1]["address"])
        time.sleep(1)
        player_inputs[13].click()
        self.driver.find_element(By.XPATH, "//input[@aria-label='Zip Code']").send_keys(
            content["user_details"][1]["weight"])
        register_login_button = self.driver.find_elements(By.CSS_SELECTOR, ".q-btn__content")
        register_login_button[1].click()
        time.sleep(10)
    def send_notification(self):
        time.sleep(2)
        self.driver.get(TestData.BASE_URL + os.getenv("USERNAME_PLAYER"))
        time.sleep(10)
        like_btn = self.driver.find_element(By.CSS_SELECTOR, "div[class='q-page-container'] button:nth-child(1)")
        like_btn.click()
        time.sleep(5)
        follow_btn = self.driver.find_element(By.CSS_SELECTOR, "div[class='q-page-container'] button:nth-child(2)")
        follow_btn.click()
        time.sleep(5)
        profile_btn = self.driver.find_element(By.CSS_SELECTOR, "button[class='q-btn q-btn-item non-selectable no-outline q-btn--flat q-btn--rectangle q-btn--rounded q-btn--actionable q-focusable q-hoverable q-btn--no-uppercase'] span[class='q-btn__content text-center col items-center q-anchor--skip justify-center row']")
        profile_btn.click()
        time.sleep(3)
        logout_btn = self.driver.find_element(By.CSS_SELECTOR, "div[class='q-item q-item-type row no-wrap q-item--clickable q-link cursor-pointer q-focusable q-hoverable']")
        logout_btn.click()
        time.sleep(5)
    def pass_moderation(self):
        self.driver.get("https://localhost/moderator")
        time.sleep(6)
        items_view = self.driver.find_elements(By.CSS_SELECTOR,".q-btn.q-btn-item" )
        items_view[5].click()
        time.sleep(3)
        popup_window = self.driver.find_elements(By.CSS_SELECTOR, ".q-card__section.q-card__section--vert")
        popup_window[4].click()
        pyautogui.scroll(10, x=200, y=600)
        item_approve = self.driver.find_elements(By.CSS_SELECTOR, ".q-btn__content.text-center")
        item_approve[12].click()
        time.sleep(2)
        popup_approve = self.driver.find_elements(By.CSS_SELECTOR, ".q-card__section.q-card__section--vert")
        popup_approve[6].click()
        moderation_ok = self.driver.find_elements(By.CSS_SELECTOR, ".q-btn__content.text-center")
        moderation_ok[14].click()












