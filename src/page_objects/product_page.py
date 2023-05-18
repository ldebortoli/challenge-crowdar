from src.page_objects.base_page import BasePage
from src.locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def title(self):
        return self.find_element(ProductPageLocators.page_title, wait=5).text

    def click_product_button(self, product_name):
        self.find_element(
            ProductPageLocators.product_add_to_cart(product_name),
            wait=5
        ).click()

    def go_to_cart(self):
        self.find_element(ProductPageLocators.cart).click()
