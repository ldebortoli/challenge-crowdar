import pytest

from src.tests.base_test import BaseTest
from src.page_objects.main_page import MainPage
from src.page_objects.product_page import ProductPage


@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    yield main_page


@pytest.fixture
def product_page(driver):
    product_page = ProductPage(driver)
    yield product_page


@pytest.mark.ui
@pytest.mark.usefixtures("main_page", "product_page", "credentials")
class TestLogin(BaseTest):

    # Inicio de sesión válido con usuario standard
    def test_login_standard_user(self, main_page, product_page, credentials):
        main_page.login(
            username=credentials["standard_username"],
            password=credentials["standard_password"]
        )

        assert product_page.title() == "Products"
        assert product_page.driver.current_url == "https://www.saucedemo.com/inventory.html"
        assert False

    # Inicio de sesión con contraseña inválida
    def test_standard_user_wrong_password(self, main_page, credentials):
        main_page.login(
            username=credentials["standard_username"],
            password="Invalid password"
        )

        assert main_page.get_error_text() == "Epic sadface: Username and password do not match any user in this service"
        assert main_page.driver.current_url == "https://www.saucedemo.com/"
