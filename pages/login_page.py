from playwright.async_api import Page

from ui_tests import ui_elements


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        _elements = LoginElements()
        self.username_field = self.page.locator(_elements.username_field)
        self.password_field = self.page.locator(_elements.password_field)
        self.login_button = self.page.locator(_elements.login_button)

    def navigate_to_login_page(self):
        self.page.goto(ui_elements.base_url)

    def fill_login_fields(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)

    def perform_valid_login(self):
        self.fill_login_fields(ui_elements.valid_username, ui_elements.valid_password)
        self.login_button.click()


class LoginElements:
    username_field = "#user-name"
    password_field = "#password"
    login_button = ".submit-button"
