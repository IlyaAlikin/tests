import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('link',
                         ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    # Получаем название товара и цену до добавления в корзину
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    # Добавляем товар в корзину (внутри этого метода решается quiz)
    page.add_product_to_basket()

    # Проверяем сообщения после добавления в корзину
    page.should_be_success_message()
    page.should_be_basket_total_message()

    # Проверяем, что название товара в сообщении совпадает с добавленным товаром
    success_message_product_name = page.get_success_message_product_name()
    assert product_name == success_message_product_name, \
        f"Product name in success message doesn't match. Expected: {product_name}, Got: {success_message_product_name}"

    # Проверяем, что стоимость корзины совпадает с ценой товара
    basket_total = page.get_basket_total()
    assert product_price == basket_total, \
        f"Basket total doesn't match product price. Expected: {product_price}, Got: {basket_total}"


if __name__ == "__main__":
    pytest.main()