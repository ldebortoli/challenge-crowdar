from src.page_objects.base_page import BasePage
from src.locators.product_page_locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def title(self):
        return self.find_element(ProductPageLocators.page_title, wait=50).text
