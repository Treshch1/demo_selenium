from page_objects.application import Application
from selenium.webdriver.common.keys import Keys


def test_google_homepage(app: Application):
    app.visit()

    # Assert that input is reset after clicling clear button
    app.homepage.search_input.set_value('Something' + Keys.ENTER)
    assert not app.homepage.search_input.get_value() == 'Something'
    assert app.homepage.clear_input_button.is_displayed()

    # Assert navigation to the list page
    app.homepage.search_input.set_value('Somethingo')
    app.homepage.submit_first_from_suggestions()
    assert app.search_list.navbar.is_displayed()
