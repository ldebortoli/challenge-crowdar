from selenium.webdriver.common.by import By


class CartPageLocators:

    def product_in_cart(product_name):
        return By.XPATH, f"//div[@class=\"cart_item\"]//div[@class=\"inventory_item_name\"][normalize-space(text())=\"{product_name}\"]"
