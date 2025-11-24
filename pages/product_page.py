from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_TOTAL_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    SUCCESS_MESSAGE_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info strong")

    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_product_name()
        self.should_be_product_price()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*self.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"

    def should_be_product_name(self):
        assert self.is_element_present(*self.PRODUCT_NAME), "Product name is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*self.PRODUCT_PRICE), "Product price is not presented"

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        """Получает название товара со страницы"""
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        """Получает цену товара со страницы"""
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_success_message(self):
        assert self.is_element_present(*self.SUCCESS_MESSAGE), "Success message is not presented"

    def should_be_basket_total_message(self):
        assert self.is_element_present(*self.BASKET_TOTAL_MESSAGE), "Basket total message is not presented"

    def get_success_message_product_name(self):
        """Получает название товара из сообщения об успешном добавлении"""
        return self.browser.find_element(*self.SUCCESS_MESSAGE_PRODUCT_NAME).text

    def get_basket_total(self):
        """Получает общую стоимость корзины из сообщения"""
        return self.browser.find_element(*self.BASKET_TOTAL).text

    def should_be_correct_product_in_basket(self, product_name):
        """Проверяет, что в корзину добавлен правильный товар"""
        success_message_product_name = self.get_success_message_product_name()
        assert product_name == success_message_product_name, \
            f"Product name in success message doesn't match. Expected: {product_name}, Got: {success_message_product_name}"

    def should_be_correct_basket_total(self, product_price):
        """Проверяет, что стоимость корзины соответствует цене товара"""
        basket_total = self.get_basket_total()
        assert product_price == basket_total, \
            f"Basket total doesn't match product price. Expected: {product_price}, Got: {basket_total}"