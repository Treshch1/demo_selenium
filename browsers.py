from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager


class ChromeBrowser:
    def __init__(self, headless=False):
        self.headless = headless
        self.browser = None

    def get_browser(self) -> Chrome:
        if self.headless:
            options = ChromeOptions()
            options.add_argument('--headless')
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            # chrome_prefs = {}
            # options.experimental_options["prefs"] = chrome_prefs
            # chrome_prefs["profile.default_content_settings"] = {"images": 2}
            self.browser = Chrome(options=options)
            self.browser.set_window_size(1440, 1280)
        else:
            self.browser = Chrome()
            self.browser.maximize_window()

        self.browser.set_page_load_timeout(15)
        return self.browser
