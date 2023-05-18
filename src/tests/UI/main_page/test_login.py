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

    def test_login_standard_user(self, main_page, product_page, credentials):
        main_page.login(
            credentials["standard_username"],
            credentials["standard_password"]
        )

        assert product_page.title() == "Products"
        assert product_page.driver.current_url == "https://www.saucedemo.com/inventory.html"
        # assert False
