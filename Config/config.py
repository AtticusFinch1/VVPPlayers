import os
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv


class TestData:
    load_dotenv()
    s = Service(os.getenv('CHROMEDRIVER'))
    BASE_URL = (os.getenv('BASE_URL'))
    BASE_URL_REGISTER = (os.getenv('BASE_URL_REGISTER'))
    BASE_URL_LOGIN = (os.getenv('BASE_URL_LOGIN'))
    AVATARS_PATH = (os.getenv('AVATARS_PATH'))
    FILE_PATH = (os.getenv('FILE_PATH'))


