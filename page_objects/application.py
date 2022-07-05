from selenium.webdriver.firefox.webdriver import WebDriver

from page_objects.base_page import BasePage
from page_objects.homepage import HomePageObject
from page_objects.search_list import SearchListPage


class Application(BasePage):
    URL = ''

    def __init__(self, browser: WebDriver):
        super().__init__(browser)
        self.homepage = HomePageObject(browser)
        self.search_list = SearchListPage(browser)
