import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.select import Select
from Config.config import TestData
import undetected_chromedriver.v2 as uc
@pytest.fixture(params=['chrome'],scope='class')
def init_driver(request):
    if request.param=="chrome":
        caps = webdriver.DesiredCapabilities.CHROME.copy()
        caps['acceptInsecureCerts'] = True
        web_driver=webdriver.Chrome(service=TestData.s, desired_capabilities=caps)
        request.cls.driver=web_driver
        yield
    # web_driver = webdriver.Remote(
    #     command_executor='http://127.0.0.1:4443/wd/hub',
    #     desired_capabilities=DesiredCapabilities.CHROME
    # )
    # web_driver.get("https://localhost/login")
    # request.cls.driver = web_driver
    # yield