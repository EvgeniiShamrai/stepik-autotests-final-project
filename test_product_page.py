import time

import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import AddProductBasket


@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
        lp = LoginPage(browser, url)
        lp.open_site()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        lp.register_new_user(email, password)
        time.sleep(4)
        lp.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        mp = AddProductBasket(browser, url)
        mp.open_site()
        mp.should_not_be_success_message()
        mp.add_product()
        mp.should_be_message_about_addid()
        mp.should_be_total_coast_product()

    def test_user_cant_see_success_message(self, browser):
        url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        sp = AddProductBasket(browser, url)
        sp.open_site()
        sp.should_not_be_success_message()




@pytest.mark.need_review
@pytest.mark.parametrize('num', [0, 1, 2, 3, 4, 5, 6,  pytest.param(7, marks=pytest.mark.xfail(reason="fixing this bug right now")), 8, 9])
def test_guest_can_add_product_to_basket(browser, num):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    sp = AddProductBasket(browser, url)
    sp.open_site()
    sp.add_product()
    sp.solve_quiz_and_get_code()
    sp.should_be_message_about_addid()
    sp.should_be_total_coast_product()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    sp = AddProductBasket(browser, url)
    sp.open_site()
    sp.add_product()
    time.sleep(1)
    sp.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    sp = AddProductBasket(browser, url)
    sp.open_site()
    sp.add_product()
    sp.should_not_be_success_message_after_add_product()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddProductBasket(browser, link)
    page.open_site()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = AddProductBasket(browser, link)
    page.open_site()
    page.go_to_login_link()

@pytest.mark.need_review
@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    view_basket = BasketPage(browser, url)
    view_basket.open_site()
    view_basket.go_to_basket()
    view_basket.check_text_empty_basket()
    view_basket.check_basket_items()
