from .base_page import BasePage
from .locators import ProductPageLocators


class PageObject(BasePage):
    def add_product_to_cart(self):
        self.should_be_add_button()
        self.press_button_to_add_item()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def press_button_to_add_item(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def add_message_should_contain_product_name(self):
        self.should_be_product_name()
        self.should_be_add_message()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_message = self.browser.find_element(*ProductPageLocators.ADD_MESSAGE).text
        assert product_name in add_message, f"Expected \"{product_name}\" as a substring of \"{add_message}\""

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_add_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_MESSAGE), "Add message is not presented"

    def cart_total_should_be_equal_to_product_price(self):
        self.should_be_product_price()
        self.should_be_cart_total_message()
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total = self.browser.find_element(*ProductPageLocators.CART_TOTAL).text
        assert product_price == cart_total, "Expected equality of product price and cart total"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def should_be_cart_total_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_TOTAL), "Cart total is not presented"
