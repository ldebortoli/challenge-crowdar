import pytest

from src.tests.base_test import BaseTest
from src.page_objects.main_page import MainPage
from src.page_objects.product_page import ProductPage
from src.page_objects.cart_page import CartPage


@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    yield main_page


@pytest.fixture
def product_page(driver):
    product_page = ProductPage(driver)
    yield product_page


@pytest.fixture
def cart_page(driver):
    cart_page = CartPage(driver)
    yield cart_page


@pytest.mark.ui
@pytest.mark.usefixtures("main_page", "product_page", "cart_page", "credentials")
class TestLogin(BaseTest):

    # Agregar productos al carrito funciona correctamente
    def test_add_a_product_to_the_cart(self, main_page, product_page, cart_page, credentials):
        main_page.login(
            username=credentials["standard_username"],
            password=credentials["standard_password"]
        )

        product_page.click_product_button("Sauce Labs Backpack")
        product_page.go_to_cart()

        assert cart_page.is_product_present("Sauce Labs Backpack")

    # Se pueden remover productos del carrito
    def test_remove_product_from_cart(self, main_page, product_page, cart_page, credentials):
        main_page.login(
            username=credentials["standard_username"],
            password=credentials["standard_password"]
        )

        # Add to cart
        product_page.click_product_button("Sauce Labs Backpack")
        # Remove
        product_page.click_product_button("Sauce Labs Backpack")

        product_page.go_to_cart()

        assert not cart_page.is_product_present("Sauce Labs Backpack")

