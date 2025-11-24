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

    def add_product_to_basket(self):
        add_button = self.browser.find_element(*self.ADD_TO_BASKET_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*self.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*self.PRODUCT_PRICE).text

    def should_be_success_message(self):
        assert self.is_element_present(*self.SUCCESS_MESSAGE), "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*self.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_disappear(self):
        assert self.is_disappeared(*self.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def get_success_message_product_name(self):
        return self.browser.find_element(*self.SUCCESS_MESSAGE_PRODUCT_NAME).text

    def get_basket_total(self):
        return self.browser.find_element(*self.BASKET_TOTAL).text

    def should_be_correct_product_in_basket(self, product_name):
        success_message_product_name = self.get_success_message_product_name()
        assert product_name == success_message_product_name, \
            f"Product name in success message doesn't match. Expected: {product_name}, Got: {success_message_product_name}"

    def should_be_correct_basket_total(self, product_price):
        basket_total = self.get_basket_total()
        assert product_price == basket_total, \
            f"Basket total doesn't match product price. Expected: {product_price}, Got: {basket_total}"