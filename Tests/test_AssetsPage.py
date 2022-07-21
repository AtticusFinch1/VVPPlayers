import pytest
from Pages.LoginPage import LoginPage
from Tests.test_base import BaseTest
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.AssetsPage import AssetsPage
from selenium.webdriver.common.by import By
import pyautogui
import time
import allure

class Test_Assets(BaseTest):
    @allure.description("OPEN THE PAGE")
    @allure.severity(severity_level="CRITICAL")
    def test_check_items_in_assets(self):
        self.assets_page = AssetsPage(self.driver)


