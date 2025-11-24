import pytest
from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    # Теперь тест будет работать для любого товара
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()

    # Получаем актуальные данные товара со страницы
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    print(f"Product name: {product_name}")
    print(f"Product price: {product_price}")

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Проверяем, что сообщения появились
    page.should_be_success_message()
    page.should_be_basket_total_message()

    # Проверяем, что товар и цена корректны (используем полученные данные)
    page.should_be_correct_product_in_basket(product_name)
    page.should_be_correct_basket_total(product_price)

    print("Test passed successfully!")


# Дополнительный тест для другого товара
def test_guest_can_add_different_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    print(f"Product name: {product_name}")
    print(f"Product price: {product_price}")

    page.add_product_to_basket()

    page.should_be_success_message()
    page.should_be_basket_total_message()

    page.should_be_correct_product_in_basket(product_name)
    page.should_be_correct_basket_total(product_price)

    print("Test passed successfully!")


# Параметризованный тест для нескольких товаров
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019",
    "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
])
def test_guest_can_add_multiple_products_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    print(f"Testing product: {product_name}")
    print(f"Product price: {product_price}")

    page.add_product_to_basket()

    page.should_be_success_message()
    page.should_be_basket_total_message()

    page.should_be_correct_product_in_basket(product_name)
    page.should_be_correct_basket_total(product_price)

    print(f"Test passed for: {product_name}")