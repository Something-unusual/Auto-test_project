from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import faker

product_base_link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{offer_number}" for offer_number in range(10)]


@pytest.mark.authorized_users
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = product_base_link
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        fake_email = faker.Faker().email()
        fake_password = faker.Faker().password()
        page.register_new_user(fake_email, fake_password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = product_base_link
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = product_base_link
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.product_name_in_basket_should_be_exact_product_name()
        page.basket_total_should_be_exact_product_price()


def test_guest_cant_see_success_message(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('promo_url', [urls[0], urls[1], urls[2], urls[3], urls[4], urls[5], urls[6],
                                       pytest.param(urls[7], marks=pytest.mark.xfail), urls[8], urls[9]])
def test_guest_can_add_product_to_basket(browser, promo_url):
    link = promo_url
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_in_basket_should_be_exact_product_name()
    page.basket_total_should_be_exact_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = product_base_link
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_disappear_of_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_no_products_message()
    page.should_be_empty_basket_message()
