from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser:
    def __init__(self, headless=False):
        self.headless = headless
        self.browser = None

    def get_browser(self) -> Chrome:
        if self.headless:
            options = ChromeOptions()
            options.headless = True
            self.browser = Chrome(ChromeDriverManager().install(), chrome_options=options)
            self.browser.set_window_size(1440, 1280)
        else:
            self.browser = Chrome(ChromeDriverManager().install())
            self.browser.maximize_window()

        self.browser.set_page_load_timeout(15)
        return self.browser
