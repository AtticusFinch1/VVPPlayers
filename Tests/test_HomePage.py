import array
import time
import json
import random

import os
from dotenv import load_dotenv

from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Pages.ActionsPage import get_user_video_info, \
                              get_user_id, \
                              get_followers_ids, \
                              new_players_all, \
                              all_videos, \
                              get_filter_data
from Pages.HomePage import HomePage
from Config.config import TestData
from selenium.webdriver.common.by import By

class Test_HomePage(BaseTest):
    load_dotenv()
    def test_notification(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.valid_login(os.getenv('LOGIN_FAN'), os.getenv('PASSWORD'))
        time.sleep(5)
        self.homePage.valid_notification()
        self.loginPage.valid_login(os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        time.sleep(5)
        follower_id = get_user_id(self, os.getenv('LOGIN_FAN'))
        fb_session_cookie = (self.driver.get_cookies())
        fb_cookie = json.dumps(fb_session_cookie[0]["value"])
        followers_list = get_followers_ids(self, fb_cookie)
        print(followers_list)
        print(follower_id)
        assert follower_id in followers_list

    def test_valid_moderation(self):
        self.homePage = HomePage(self.driver)
        self.homePage.valid_moderation()

    def test_video_upload_status(self): # check if new uploaded video is not displayed in other user's accounts
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.valid_login(os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        self.driver.get(TestData.BASE_URL + os.getenv('USERNAME_PLAYER'))
        time.sleep(1)
        self.homePage.video_upload()
        time.sleep(5)
        user_id = get_user_id(self, os.getenv('LOGIN_FAN'))
        time.sleep(5)
        response = get_user_video_info(self, user_id)
        for i in range (response["videos"]["total"]):
            print(response["videos"]["data"][i]["status"])
            assert(response["videos"]["data"][i]["status"] == "approved")

    def test_video_status(self): # check if in all videos only videos with approved status are displayed. Compares number of active videos in allVideos with response total.
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        file = open(TestData.AVATARS_PATH)
        content = json.load(file)
        self.loginPage.valid_login(os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        time.sleep(1)
        self.driver.get(TestData.BASE_URL + "videos/")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        all_videos = self.driver.find_elements(By.CSS_SELECTOR,".fit.flex.flex-center.bg-transparent")
        all_videos_len = (len(all_videos))
        not_active_videos = self.driver.find_elements(By.XPATH,"(//div[@class='video__status absolute-top full-width bg-orange-6 q-py-xs row items-center'])")
        not_active_videos_len = len(not_active_videos)
        diff = all_videos_len - not_active_videos_len
        response = all_videos(self)
        print(diff)
        print(response)
        assert diff == response

    def test_search_profile(self): # Search player by username and compare with last name in search results
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.valid_login(os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        time.sleep(2)
        response = new_players_all(self)
        random_user = random.choice(list(response.items()))
        random_username = random_user[0]
        random_lastname = random_user[1]
        self.homePage.search_profile(random_username)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        try:
            search_name = self.driver.find_elements(By.XPATH,"//span[@class='text-h6 q-mt-md text-weight-medium']")
            search_results = search_name[0].text
            print("random_user, ", random_user, "search_results: ", search_results)
            assert random_lastname in search_results
        except:
            print("Search param is not found.")

    def test_filter_profile(self):
        self.loginPage = LoginPage(self.driver)
        self.homePage = HomePage(self.driver)
        self.loginPage.valid_login(os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))
        time.sleep(2)
        self.driver.get(TestData.BASE_URL + "players/")
        time.sleep(2)
        position = get_filter_data(self)
        time.sleep(2)
        response = len(position)
        time.sleep(2)
        self.homePage.scroll_down(5)
        time.sleep(2)
        new_players_filter = self.driver.find_element(By.XPATH,"//div[contains(@class,'q-page-container')]//a[2]")
        new_players_filter.click()
        time.sleep(2)
        self.homePage.scroll_down(5)
        time.sleep(2)
        all_players_filter = self.driver.find_element(By.XPATH,"//div[@class='filters content row full-width q-pt-none justify-center bg-white']//a[1]")
        all_players_filter.click()
        time.sleep(2)
        self.homePage.scroll_down(5)
        players_count = self.driver.find_elements(By.CSS_SELECTOR,".q-btn.q-btn-item.non-selectable.no-outline.q-btn--standard.q-btn--rectangle.q-btn--rounded.q-btn--actionable.q-focusable.q-hoverable.q-btn--no-uppercase.q-btn--gradient.gradient.q-py-none.q-px-xl.q-my-md")
        print("players count actual", len(players_count))
        print("players count expected", response)
        assert players_count == response



