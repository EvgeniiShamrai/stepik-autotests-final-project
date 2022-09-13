from pages.base_page import BasePage
from pages.locators import BasketItemsLocators

class BasketPage(BasePage):
    def check_basket_items(self):
        assert self.is_not_element_present(*BasketItemsLocators.BASKET_HAS_ITEMS,5), "The basket is not empty"

    def check_text_empty_basket(self):
        text_basket = self.browser.find_element(*BasketItemsLocators.TEXT_BASKET_IS_EMPTY).text
        assert text_basket == "Your basket is empty. Continue shopping", "The basket is not empty"
