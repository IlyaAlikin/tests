import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProductPage:

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, user_auth):
        """
        Тест: зарегистрированный пользователь может добавить товар в корзину
        """
        # Переходим на страницу товара
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()

        # Получаем название товара и цену
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()

        # Добавляем товар в корзину
        product_page.add_to_basket()

        # Проверяем сообщения о добавлении в корзину
        product_page.should_be_success_message()
        product_page.should_be_correct_product_name_in_message(product_name)
        product_page.should_be_basket_total_message()
        product_page.should_be_correct_price_in_message(product_price)

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self, browser):
        """
        Тест: гость может добавить товар в корзину
        """
        # Переходим на страницу товара
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()

        # Получаем название товара и цену
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()

        # Добавляем товар в корзину
        product_page.add_to_basket()

        # Проверяем сообщения о добавлении в корзину
        product_page.should_be_success_message()
        product_page.should_be_correct_product_name_in_message(product_name)
        product_page.should_be_basket_total_message()
        product_page.should_be_correct_price_in_message(product_price)

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        """
        Тест: гость не видит товаров в корзине, открытой со страницы товара
        """
        # Переходим на страницу товара
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()

        # Переходим в корзину
        product_page.go_to_basket_page()

        # Проверяем, что корзина пуста
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty()
        basket_page.should_have_empty_basket_message()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        """
        Тест: гость может перейти на страницу логина со страницы товара
        """
        # Переходим на страницу товара
        product_page = ProductPage(browser, "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        product_page.open()

        # Переходим на страницу логина
        product_page.go_to_login_page()

        # Проверяем, что находимся на странице логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


class ProductPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def get_product_name(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main h1").text

    def get_product_price(self):
        return self.browser.find_element(By.CSS_SELECTOR, ".product_main .price_color").text

    def add_to_basket(self):
        add_button = self.browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
        add_button.click()

    def should_be_success_message(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )

    def should_be_correct_product_name_in_message(self, product_name):
        success_message = self.browser.find_element(By.CSS_SELECTOR, ".alert-success:first-child")
        assert product_name in success_message.text, \
            f"Название товара '{product_name}' не найдено в сообщении: '{success_message.text}'"

    def should_be_basket_total_message(self):
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-info"))
        )

    def should_be_correct_price_in_message(self, product_price):
        basket_message = self.browser.find_element(By.CSS_SELECTOR, ".alert-info")
        assert product_price in basket_message.text, \
            f"Цена товара '{product_price}' не найдена в сообщении: '{basket_message.text}'"

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(By.CSS_SELECTOR, ".btn-group a.btn-default")
        basket_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()


class BasketPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def should_be_empty(self):
        # Проверяем, что нет товаров в корзине
        basket_items = self.browser.find_elements(By.CSS_SELECTOR, ".basket-items")
        assert len(basket_items) == 0, "Корзина должна быть пустой, но найдены товары"

    def should_have_empty_basket_message(self):
        # Проверяем сообщение о пустой корзине
        empty_message = self.browser.find_element(By.CSS_SELECTOR, "#content_inner p")
        assert "Your basket is empty" in empty_message.text or \
               "Ваша корзина пуста" in empty_message.text, \
            "Не найдено сообщение о пустой корзине"


class LoginPage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL не содержит 'login'"

    def should_be_login_form(self):
        assert self._is_element_present(By.CSS_SELECTOR, "#login_form"), "Форма логина не найдена"

    def should_be_register_form(self):
        assert self._is_element_present(By.CSS_SELECTOR, "#register_form"), "Форма регистрации не найдена"

    def _is_element_present(self, by, selector):
        return len(self.browser.find_elements(by, selector)) > 0


# Фикстуры для pytest
@pytest.fixture
def user_auth(browser):
    """
    Фикстура для авторизации пользователя
    """
    # Реализация авторизации пользователя
    login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/accounts/login/")
    login_page.open()

    # Заполняем форму логина (замените на реальные данные)
    email_field = browser.find_element(By.CSS_SELECTOR, "#id_login-username")
    email_field.send_keys("test@example.com")

    password_field = browser.find_element(By.CSS_SELECTOR, "#id_login-password")
    password_field.send_keys("testpassword123")

    login_button = browser.find_element(By.CSS_SELECTOR, "[name='login_submit']")
    login_button.click()