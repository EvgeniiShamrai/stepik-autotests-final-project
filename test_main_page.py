import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/'
        page_main = MainPage(browser, url)
        page_main.open_site()
        page_main.go_to_login_link()

    def test_guest_should_see_login_link(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/'
        page_main = MainPage(browser, url)
        page_main.open_site()
        page_main.should_be_login_link()


def test_word_login_in_url_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    login_page = LoginPage(browser, url)
    page_main.open_site()
    page_main.go_to_login_link()
    login_page.should_be_login_url()


def test_guest_should_see_login_form(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    login_page = LoginPage(browser, url)
    page_main.open_site()
    page_main.go_to_login_link()
    login_page.should_be_login_form()


def test_guest_should_see_registr_form(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    login_page = LoginPage(browser, url)
    page_main.open_site()
    page_main.go_to_login_link()
    login_page.should_be_register_form()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    view_basket = BasketPage(browser, url)
    view_basket.open_site()
    view_basket.go_to_basket()
    view_basket.check_text_empty_basket()
    view_basket.check_basket_items()
