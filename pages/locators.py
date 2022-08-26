from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM_EMAIL = (By.CSS_SELECTOR,"input[name='login-username']")
    LOGIN_FORM_PASSWORD =(By.CSS_SELECTOR,"input[name='login-password']")
    REGISTR_FORM_EMAIL =(By.CSS_SELECTOR,"input[name='registration-email']")
    REGISTR_FORM_PASSWORD =(By.CSS_SELECTOR,"input[name='registration-password1']")
    REGISTR_FORM_PASSWORD2 =(By.CSS_SELECTOR,"input[name='registration-password2']")
