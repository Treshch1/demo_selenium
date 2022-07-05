import pytest

from selenium.common.exceptions import NoSuchWindowException
from urllib3.exceptions import MaxRetryError

from browsers import ChromeBrowser
from page_objects.application import Application


browser_instance = None


def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", default=False)


@pytest.fixture(scope='function')
def browser(request):
    global browser_instance

    def is_valid_browser(_browser):
        try:
            _browser.current_url
            return True
        except (NoSuchWindowException, MaxRetryError):
            return False

    if browser_instance is None or not is_valid_browser(browser_instance):
        headless = True if request.config.getoption('--headless') else False
        browser_instance = ChromeBrowser(headless=headless).get_browser()
    return browser_instance


@pytest.fixture(scope='session', autouse=True)
def stop(request):
    def fin():
        browser_instance.quit()
    request.addfinalizer(fin)
    return browser_instance


@pytest.fixture(scope='function')
def app(browser):
    _app = Application(browser)
    return _app
