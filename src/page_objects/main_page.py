from src.page_objects.base_page import BasePage
from src.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.find_element(MainPageLocators.username).send_keys(username)
        self.find_element(MainPageLocators.password).send_keys(password)
        self.find_element(MainPageLocators.login).click()
