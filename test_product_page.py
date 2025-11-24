import pytest
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Тест: Гость не должен видеть сообщение об успехе после добавления товара в корзину
    Ожидаемый результат: ПАДАЕТ, потому что сообщение ПОЯВЛЯЕТСЯ после добавления
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()  # Эта проверка должна упасть

def test_guest_cant_see_success_message(browser):
    """
    Тест: Гость не должен видеть сообщение об успехе без добавления товара
    Ожидаемый результат: ПРОХОДИТ, потому что сообщения нет на пустой странице
    """
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()  # Эта проверка должна пройти

def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Тест: Сообщение должно исчезнуть после добавления товара в корзину
    Ожидаемый результат: ПАДАЕТ, потому что сообщение НЕ ИСЧЕЗАЕТ
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_success_message_disappear()  # Эта проверка должна упасть

# После запуска и анализа помечаем падающие тесты как xfail
@pytest.mark.xfail(reason="Сообщение появляется после добавления товара")
def test_guest_cant_see_success_message_after_adding_product_to_basket_xfail(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Сообщение не исчезает после добавления товара")
def test_message_disappeared_after_adding_product_to_basket_xfail(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_success_message_disappear()