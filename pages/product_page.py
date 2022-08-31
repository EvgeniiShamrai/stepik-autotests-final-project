from time import sleep

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class AddProductBasket(BasePage):
    def add_product(self):
        button_add = self.browser.find_element(*ProductPageLocators.BUTTON_BASKET)
        button_add.click()

    def should_be_message_about_addid(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "Product name is not presented"
        assert self.is_element_present(
            *ProductPageLocators.NAME_PRODUCT_IN_MESSAGE), 'Message about adding is not presented'
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_message = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_MESSAGE).text
        assert name_product in name_product_message, 'The name of the product added to the cart does not match' \
                                                     ' the name of the product in the successful addition message'

    def should_be_total_coast_product(self):
        assert self.is_element_present(*ProductPageLocators.COST_PRODUCT), 'Product price is not presented'
        assert self.is_element_present(
            *ProductPageLocators.COST_PRODUCT_IN_BASKET), 'Message basket total is not presented'
        coast_product = (self.browser.find_element(*ProductPageLocators.COST_PRODUCT).text.split('£')[1])
        coast_basket = (self.browser.find_element(*ProductPageLocators.COST_PRODUCT_IN_BASKET).text.split('£')[1])
        assert coast_product == coast_basket, 'The price of the product does not match the price in the basket'
