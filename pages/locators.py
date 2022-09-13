from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='login-password']")
    REGISTR_FORM_EMAIL = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTR_FORM_PASSWORD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTR_FORM_PASSWORD2 = (By.CSS_SELECTOR, "input[name='registration-password2']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value='Log In']")
    REGISTR_BUTTON = (By.CSS_SELECTOR, "button[value='Register']")


class ProductPageLocators:
    BUTTON_BASKET = (By.CSS_SELECTOR, '.btn.btn-add-to-basket')
    NAME_PRODUCT = (By.CSS_SELECTOR, '.product_main > h1')
    COST_PRODUCT = (By.CSS_SELECTOR, '.product_main > .price_color')
    NAME_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1)')
    COST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '#messages > div:nth-child(3) > div > p:nth-child(1)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages div:first-child')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class ViewingBasketLocators:
    BUTTON_BASKET = (By.CSS_SELECTOR, "div.pull-right.hidden-xs > span > a.btn-default")


class BasketItemsLocators:
    BASKET_HAS_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
