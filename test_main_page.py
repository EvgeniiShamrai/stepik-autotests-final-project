from time import sleep

from pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    page_main.open_site()
    sleep(2)
    page_main.go_to_login_link()
    sleep(2)
