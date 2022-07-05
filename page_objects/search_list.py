from page_objects.base_page import BasePage, Element


class SearchListPage(BasePage):
    URL = 'search'

    navbar = Element('#top_nav')
