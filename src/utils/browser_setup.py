from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def browser_selection(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
    elif browser == "firefox":
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )
    elif browser == "edge":
        driver = None
    elif browser == "opera":
        driver = None
    elif browser == "brave":
        driver = None
    elif browser == "chromium":
        driver = None
    return driver
