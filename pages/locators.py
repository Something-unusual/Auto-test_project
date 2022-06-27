from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")


class ProductPageLocators:
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    ADD_MESSAGE = (By.CSS_SELECTOR, "#messages :first-child .alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#messages :first-child .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "h1 + p")
    CART_TOTAL = (By.CSS_SELECTOR, "#messages :nth-child(3) .alertinner p strong")
