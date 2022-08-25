from selenium.webdriver.common.by import By
from time import sleep

def test_guest_can_go_to_login_page(browser):
    url = 'http://selenium1py.pythonanywhere.com/'
    browser.get(url)
    sleep(2)
    browser.implicitly_wait(3)
    login_link=browser.find_element(By.CSS_SELECTOR, '#login_link')
    login_link.click()
    sleep(2)