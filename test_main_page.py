from time import sleep

from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    page_main.open_site()
    sleep(2)
    page_main.go_to_login_link()
    sleep(2)

def test_guest_should_see_login_link(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    page_main.open_site()
    sleep(2)
    page_main.should_be_login_link()
    sleep(2)

def test_word_login_in_url_login_page(browser):
    url='http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    login_page = LoginPage(browser, url)
    page_main.open_site()
    sleep(2)
    page_main.go_to_login_link()
    sleep(2)
    login_page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    login_page = LoginPage(browser, url)
    page_main.open_site()
    sleep(2)
    page_main.go_to_login_link()
    sleep(2)
    login_page.should_be_login_form()

def test_guest_should_see_registr_form(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    page_main = MainPage(browser, url)
    login_page = LoginPage(browser, url)
    page_main.open_site()
    sleep(2)
    page_main.go_to_login_link()
    sleep(2)
    login_page.should_be_register_form()

