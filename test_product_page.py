from pages.product_page import PageObject
import pytest

product_base_link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{offer_number}" for offer_number in range(10)]


@pytest.mark.parametrize('promo_url', [urls[0], urls[1], urls[2], urls[3], urls[4], urls[5], urls[6],
                                       pytest.param(urls[7], marks=pytest.mark.xfail), urls[8], urls[9]])
def test_guest_can_add_product_to_cart(browser, promo_url):
    link = promo_url
    page = PageObject(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.product_name_in_cart_should_be_exact_product_name()
    page.cart_total_should_be_exact_product_price()
