from selenium.webdriver.common.by import By


class ProductPageLocators:
    page_title = By.CLASS_NAME, "title"
    cart = By.ID, "shopping_cart_container"

    def product_add_to_cart(product_name):
        return By.XPATH, f"//div[@class=\"inventory_item\"]//div[@class=\"inventory_item_name\"][normalize-space(text())=\"{product_name}\"]/parent::a/parent::div/parent::div//button"
