import pytest
from pages.product_page import ProductPage


# Тест для поиска бага в промо-акциях
@pytest.mark.parametrize('promo_offer', [
    "offer0", "offer1", "offer2", "offer3", "offer4",
    "offer5", "offer6", "offer7", "offer8", "offer9"
])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_offer}"
    page = ProductPage(browser, link)
    page.open()

    # Получаем актуальные данные товара со страницы
    product_name = page.get_product_name()
    product_price = page.get_product_price()

    print(f"\nTesting promo: {promo_offer}")
    print(f"Product: {product_name}")
    print(f"Price: {product_price}")
    print(f"URL: {link}")

    # Добавляем товар в корзину
    page.add_product_to_basket()

    # Проверяем, что сообщения появились
    page.should_be_success_message()
    page.should_be_basket_total_message()

    # Проверяем, что товар и цена корректны
    page.should_be_correct_product_in_basket(product_name)
    page.should_be_correct_basket_total(product_price)

    print(f"✅ Promo {promo_offer} passed successfully!")


# Альтернативный вариант с явным указанием ссылок
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket_with_links(browser, link):
    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    print(f"\nTesting URL: {link}")
    print(f"Product: {product_name}")
    print(f"Price: {product_price}")

    page.add_product_to_basket()

    page.should_be_success_message()
    page.should_be_basket_total_message()

    page.should_be_correct_product_in_basket(product_name)
    page.should_be_correct_basket_total(product_price)

    print(f"✅ Test passed for: {link}")