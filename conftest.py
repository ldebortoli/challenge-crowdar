import pytest, os

from src.utils.reports import delete_files_in_dir
from src.utils.reports import report_fail_test
from src.utils.browser_setup import browser_selection


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Browser to run the test cases (options: chrome, firefox)"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Set headless mode"
    )
    parser.addoption(
        "--apitesting",
        action="store_true",
        default=False,
        help="Run API tests"
    )


@pytest.fixture
def driver_args(request, scope='session'):
    return {
        "browser": request.config.getoption("--browser"),
        "headless": request.config.getoption("--headless")
    }


@pytest.fixture
def credentials(scope='session'):
    return {
        "standard_username": os.getenv("SAUCEDEMO_STANDARD_USERNAME"),
        "standard_password": os.getenv("SAUCEDEMO_STANDARD_PASSWORD"),

        "locked_username": os.getenv("SAUCEDEMO_LOCKED_USERNAME"),
        "locked_password": os.getenv("SAUCEDEMO_LOCKED_PASSWORD"),

        "problem_username": os.getenv("SAUCEDEMO_PROBLEM_USERNAME"),
        "problem_password": os.getenv("SAUCEDEMO_PROBLEM_PASSWORD"),

        "performance_username": os.getenv("SAUCEDEMO_PERFORMANCE_USERNAME"),
        "performance_password": os.getenv("SAUCEDEMO_PERFORMANCE_PASSWORD")
    }


# Delete old report files
@pytest.fixture(scope='session', autouse=True)
def clean_old_reports(request):
    browser = request.config.getoption("--browser")

    if request.config.option.markexpr == 'api':
        delete_files_in_dir("api", "reports", "html")
    else:
        delete_files_in_dir(browser, "reports", "html")
        delete_files_in_dir(browser, "reports/screenshots", "png")


@pytest.fixture
def driver(driver_args):
    # Set Up driver
    driver = browser_selection(driver_args["browser"])
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    html_plugin = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    report_fail_test(report, item, html_plugin)
