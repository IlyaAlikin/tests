import pytest
import time
from pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_debug_waiting_time_1(browser):
    """Проверяем, ждет ли первый тест 4 секунды"""
    print("\n=== ТЕСТ 1: guest_cant_see_success_message_after_adding_product_to_basket ===")
    start_time = time.time()

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    print("🔍 Перед вызовом should_not_be_success_message...")
    page.should_not_be_success_message()  # Этот метод использует is_not_element_present

    end_time = time.time()
    total_time = end_time - start_time
    print(f"🕒 Общее время выполнения теста 1: {total_time:.2f} секунд")

    # Тест упадет, но нам важно увидеть время ожидания


def test_debug_waiting_time_2(browser):
    """Проверяем, ждет ли второй тест 4 секунды"""
    print("\n=== ТЕСТ 2: guest_cant_see_success_message ===")
    start_time = time.time()

    page = ProductPage(browser, link)
    page.open()

    print("🔍 Перед вызовом should_not_be_success_message...")
    page.should_not_be_success_message()  # Этот метод использует is_not_element_present

    end_time = time.time()
    total_time = end_time - start_time
    print(f"🕒 Общее время выполнения теста 2: {total_time:.2f} секунд")


def test_debug_waiting_time_3(browser):
    """Проверяем, ждет ли третий тест 4 секунды"""
    print("\n=== ТЕСТ 3: message_disappeared_after_adding_product_to_basket ===")
    start_time = time.time()

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    print("🔍 Перед вызовом should_success_message_disappear...")
    page.should_success_message_disappear()  # Этот метод использует is_disappeared

    end_time = time.time()
    total_time = end_time - start_time
    print(f"🕒 Общее время выполнения теста 3: {total_time:.2f} секунд")