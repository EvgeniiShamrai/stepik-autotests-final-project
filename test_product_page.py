import time

import pytest

from pages.product_page import AddProductBasket
from pages.locators import ProductPageLocators

# @pytest.mark.parametrize('num',
#                          [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='fixing this bug right now')),
#                           *range(8, 10)])
# def test_guest_can_add_product_to_basket(browser, num):
#     url = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
#     mp = AddProductBasket(browser, url)
#     mp.open_site()
#     mp.should_not_be_success_message()
#     time.sleep(1)
#     mp.add_product()
#     time.sleep(1)
#     mp.solve_quiz_and_get_code()
#     time.sleep(2)
#     mp.should_be_message_about_addid()
#     mp.should_be_total_coast_product()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    sp = AddProductBasket(browser,url)
    sp.open_site()
    sp.add_product()
    time.sleep(1)
    sp.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    sp = AddProductBasket(browser, url)
    sp.open_site()
    sp.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    sp = AddProductBasket(browser, url)
    sp.open_site()
    sp.add_product()
    sp.should_not_be_success_message_after_add_product()




