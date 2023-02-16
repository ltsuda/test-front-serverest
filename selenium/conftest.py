from dataclasses import dataclass
from typing import Generator

import pytest
from src.consts import URL

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.remote.webdriver import WebDriver

SELENIUM_GRID = "http://localhost:4444/wd/hub"


@dataclass(frozen=True, init=False)
class Browsers:
    CHROME: str = "chrome"
    EDGE: str = "edge"
    FIREFOX: str = "firefox"


def pytest_addoption(parser):
    parser.addoption(
        "--select-browser",
        action="store",
        default=Browsers.CHROME,
        help="Choose which browser to run tests, defaults to 'chrome'",
        choices=(Browsers.CHROME, Browsers.EDGE, Browsers.FIREFOX),
    )
    parser.addoption(
        "--video-on",
        action="store_true",
        default=False,
        help="Enable video recording",
    )


def select_driver(browser, record=False) -> WebDriver:
    match browser:
        case Browsers.CHROME:
            options = ChromeOptions()
            options.set_capability("se:recordVideo", record)
            options.set_capability("se:screenResolution", "1920x1080")
            return webdriver.Remote(command_executor=SELENIUM_GRID, options=options)
        case Browsers.EDGE:
            options = EdgeOptions()
            options.set_capability("se:recordVideo", record)
            options.set_capability("se:screenResolution", "1920x1080")
            return webdriver.Remote(command_executor=SELENIUM_GRID, options=options)
        case Browsers.FIREFOX:
            options = FirefoxOptions()
            options.set_capability("se:recordVideo", record)
            options.set_capability("se:screenResolution", "1920x1080")
            return webdriver.Remote(command_executor=SELENIUM_GRID, options=options)
        case _:
            options = ChromeOptions()
            options.set_capability("se:recordVideo", record)
            options.set_capability("se:screenResolution", "1920x1080")
            return webdriver.Remote(command_executor=SELENIUM_GRID, options=options)


@pytest.fixture(scope="function")
def auth_driver(request) -> Generator[WebDriver, None, None]:
    """Create a webdriver instance per test function, so it doesn't use the same browser session
    for more than one test.
    """

    browser = request.config.getoption("--select-browser")
    record_video = request.config.getoption("--video-on")
    custom_driver: WebDriver = select_driver(browser, record_video)

    custom_driver.maximize_window()
    custom_driver.set_script_timeout(30)
    custom_driver.set_page_load_timeout(30)
    custom_driver.implicitly_wait(0)

    # Login & Authenticate webdriver

    yield custom_driver

    custom_driver.quit()


@pytest.fixture(scope="function")
def driver(request, base_url) -> Generator[WebDriver, None, None]:
    """Create a webdriver instance per test function, so it doesn't use the same browser session
    for more than one test.
    """

    browser = request.config.getoption("--select-browser")
    record_video = request.config.getoption("--video-on")
    custom_driver: WebDriver = select_driver(browser, record_video)

    custom_driver.maximize_window()
    custom_driver.set_script_timeout(30)
    custom_driver.set_page_load_timeout(30)
    custom_driver.implicitly_wait(0)
    custom_driver.get(f"{base_url}{URL.login}")

    yield custom_driver

    custom_driver.quit()


@pytest.fixture(scope="session")
def backend_url():
    """Backend URL fixture to be make requests directly to the backend API

    This needs to be localhost as pytest is outside of the container application

    Returns:
        str: backend URL
    """
    return f"{URL.external_backend}"
