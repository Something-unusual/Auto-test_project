from pages.product_page import PageObject


def test_guest_can_add_item_to_cart(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = PageObject(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.add_message_should_contain_product_name()
    page.cart_total_should_be_equal_to_product_price()
