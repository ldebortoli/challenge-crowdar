from selenium.webdriver.common.by import By


class MainPageLocators:
    username = By.ID, "user-name"
    password = By.ID, "password"
    login = By.ID, "login-button"
    error_textbox = By.XPATH, "//h3[@data-test=\"error\"]"
