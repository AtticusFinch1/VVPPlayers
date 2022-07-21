import os
from dotenv import load_dotenv

from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData
import json

class Test_LoginPage(BaseTest):
    load_dotenv()
    def test_valid_login_fan(self):
        self.loginPage=LoginPage(self.driver)
        self.loginPage.valid_login(os.getenv('LOGIN_FAN'), os.getenv('PASSWORD'))
    def test_valid_login_player(self):
        self.loginPage=LoginPage(self.driver)
        self.loginPage.valid_login(os.getenv('LOGIN_PLAYER'), os.getenv('PASSWORD'))