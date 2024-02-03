import os

import pytest
from playwright.sync_api import sync_playwright

from ui_tests.pages.pages import Pages


@pytest.fixture()
def playwright_setup(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        page.close()
        context.close()
        browser.close()


@pytest.fixture()
def page_without_login(playwright_setup):
    pages = Pages(playwright_setup)
    pages.login.navigate_to_login_page()
    return pages


@pytest.fixture()
def page_after_login(page_without_login):
    pages = page_without_login
    pages.login.perform_valid_login()
    return pages
