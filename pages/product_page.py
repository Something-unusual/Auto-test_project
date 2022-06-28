from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.should_be_add_button()
        self.press_button_to_add_item()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BUTTON), "Add button is not presented"

    def press_button_to_add_item(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def product_name_in_cart_should_be_exact_product_name(self):
        self.should_be_product_name()
        self.should_be_add_message()
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_add_message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_ADD_MESSAGE).text
        assert product_name == product_in_add_message, "Product name in cart is not the exact product added"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def should_be_add_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IN_ADD_MESSAGE), "Add message is not presented"

    def cart_total_should_be_exact_product_price(self):
        self.should_be_product_price()
        self.should_be_cart_total_message()
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        cart_total = self.browser.find_element(*ProductPageLocators.CART_TOTAL).text
        assert product_price == cart_total, "Cart total is not the exact product price"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def should_be_cart_total_message(self):
        assert self.is_element_present(*ProductPageLocators.CART_TOTAL), "Cart total is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is disappeared"
