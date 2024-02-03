from playwright.async_api import Page


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        _elements = HomePageElements()
        self.menu_burger = self.page.locator(_elements.menu_burger)


class HomePageElements:
    menu_burger = "#react-burger-menu-btn"
