from ui_tests.pages.home_page import HomePage
from ui_tests.pages.login_page import LoginPage


class Pages:
    def __init__(self, page):
        self.login = LoginPage(page)
        self.home_page = HomePage(page)
