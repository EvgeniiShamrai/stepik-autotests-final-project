import time

import pytest

from pages.product_page import AddProductBasket


@pytest.mark.parametrize('num',
                         [*range(7), pytest.param(7, marks=pytest.mark.xfail(reason='fixing this bug right now')),
                          *range(8, 10)])
def test_guest_can_add_product_to_basket(browser, num):
    url = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    mp = AddProductBasket(browser, url)
    mp.open_site()
    time.sleep(1)
    mp.add_product()
    time.sleep(1)
    mp.solve_quiz_and_get_code()
    time.sleep(2)
    mp.should_be_message_about_addid()
    mp.should_be_total_coast_product()
