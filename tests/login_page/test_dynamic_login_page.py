
def test_valid_login(page_without_login):
    page_without_login.login.perform_valid_login()
    assert page_without_login.home_page.menu_burger
