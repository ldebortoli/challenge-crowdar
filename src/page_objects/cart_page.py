from src.page_objects.base_page import BasePage
from src.locators.cart_page_locators import CartPageLocators


class CartPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def is_product_present(self, product):
        return self.is_present(CartPageLocators.product_in_cart(product))
