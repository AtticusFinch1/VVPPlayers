from Tests.test_base import BaseTest
from Pages.RegisterPage import RegisterPage
from Tests.conftest import TestData
from Pages.BasePage import BasePage
import requests

class Test_RegisterPage(BaseTest):
    def test_valid_register_fan(self):
        self.registerPage=RegisterPage(self.driver)
        self.registerPage.valid_register_fan()

    def test_valid_register_player(self):
        self.registerPage=RegisterPage(self.driver)
        self.registerPage.valid_register_player()

