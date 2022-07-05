from selenium.webdriver import ActionChains, Keys

from components.text_input import TextInput
from page_objects.base_page import BasePage, Element


class HomePageObject(BasePage):
    URL = 'home'

    search_input = TextInput(input_field=Element('[name="q"]'))
    clear_input_button = Element('span[aria-label="Clear"]')
    suggestion_list = Element('[role="listbox"]')

    def submit_first_from_suggestions(self):
        self.wait(lambda browser: self.suggestion_list.is_displayed())
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.DOWN).send_keys(Keys.ENTER).perform()
