from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        text_url = self.browser.current_url
        print(text_url)
        assert 'login' in text_url, 'Login is not in link'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), 'Email field of the Login form is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD),'Password field of the Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM_EMAIL), 'Email field of the Registrate form is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM_PASSWORD), 'Password field of the Registrate form is not presented'
        assert self.is_element_present(*LoginPageLocators.REGISTR_FORM_PASSWORD2), 'Password2 field of the Registrate form is not presented'