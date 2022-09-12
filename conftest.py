import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Choose browser: chrome or firefox')
    parser.addoption('--language', action='store', default='ru', help='Choose language: ru or en')


# Фикстура для определения веб драйвра и после отработки тестов драйвер закрывается
@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == 'chrome':
        options = Options()
        # чтобы указать язык браузера с помощью WebDriver, используйте класс Options и метод add_experimental_option
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print('\n start browser Chrome..')
        browser = webdriver.Chrome(options=options)
        # чтобы указать язык браузера с помощью WebDriver Firefox, используйте экземпляр класса webdriver.FirefoxProfile() и метод set_preference
    elif browser_name == 'firefox':
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', user_language)
        browser = webdriver.Firefox(firefox_profile=profile)
        print('\n start browser Firefox..')
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\n quit browser..')
    browser.quit()
